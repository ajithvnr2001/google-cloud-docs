---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema/
title: Image customization file \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:04:04.979241+00:00
---

# Image customization file  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Image customization file Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

This document describes the structure and parameters of the customization recipe file, `imagebuilder.yaml`, that you use to define the base OS image, hardware configurations, release destinations, and customization actions for your Image Builder pipeline.

## Schema overview

The customization configuration uses the API version `imagebuilder.gcp.com/v1` and the resource kind `OSImageCustomization`.

A standard recipe file has the following structure:
    
    
    apiVersion: imagebuilder.gcp.com/v1
    kind: OSImageCustomization
    metadata:
      # Recipe metadata and identifying details
      name: CONFIG_NAME
      description: DESCRIPTION
    infrastructureConfig:
      # VM machine type, zone, and network settings
      machineType: MACHINE_TYPE
      zone: ZONE
      network: projects/PROJECT_ID/global/networks/NETWORK_NAME
      subnetwork: projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
      externalIP: ephemeral
      acceleratorType: ACCELERATOR_TYPE
      acceleratorCount: ACCELERATOR_COUNT
      debug: DEBUG_BOOLEAN
      instanceDurationHours: DURATION_HOURS
      reservations:
        - RESERVATION_NAME
      validationConcurrency: VALIDATION_CONCURRENCY
    source:
      # Base source image profile
      imageFamily: projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY
      # Alternatively, use a direct image version URI:
      # imagePath: projects/IMAGE_PROJECT/global/images/IMAGE_NAME
    destinations:
      # Output OS image release targets
      - diskImage:
          name: IMAGE_NAME
          project: PROJECT_ID
          family: IMAGE_FAMILY
          description: DESCRIPTION
          licenses:
            - projects/PROJECT_ID/global/licenses/LICENSE_NAME
          labels:
            env: production
          signatureDatabaseFile: SIGNATURE_DB_PATH
          storageLocations:
            - STORAGE_LOCATION
    spec:
      config:
        # Build options and validation test flags
        skipSystemTests: false
      steps:
        # Customization actions (Shell, FileCopy, UpdateKernelCommandLine, InstallGPU)
        - name: STEP_NAME
          action: ACTION_TYPE
          inputs:
            # Action-specific input parameters

## Metadata

Provides identifying details for this custom build template:
    
    
    metadata:
      name: CONFIG_NAME
      description: DESCRIPTION

  * `name` (string, Required): The identifier for this configuration.
  * `description` (string, Optional): A description of the build's purpose.



## Infrastructure configuration

Specifies the hardware and network properties of temporary virtual machine instances that Image Builder creates during build and validation tasks:
    
    
    infrastructureConfig:
      machineType: MACHINE_TYPE
      zone: ZONE
      network: projects/PROJECT_ID/global/networks/NETWORK_NAME
      subnetwork: projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
      externalIP: ephemeral
      acceleratorType: ACCELERATOR_TYPE
      acceleratorCount: ACCELERATOR_COUNT
      debug: DEBUG_BOOLEAN
      instanceDurationHours: DURATION_HOURS
      reservations:
        - RESERVATION_NAME
      validationConcurrency: VALIDATION_CONCURRENCY

  * `machineType` (string, Required): The Compute Engine machine type to use for the worker and test VMs. Make sure that the machine type matches the architecture of the source image that you specify in `imageFamily` or `imagePath`. For example, use `e2-standard-4` for x86 images and `c4a-standard-4` for Arm images. Bare-metal machine types are not supported.
  * `zone` (string, Required): The zone where the worker and test VMs run, such as `us-central1-a`.
  * `network` (string, Optional): The VPC network to attach to the worker and validation test VMs, such as `projects/<var>PROJECT_ID</var>/global/networks/<var>NETWORK_NAME</var>` or `default`. If omitted, Image Builder uses the default network.
  * `subnetwork` (string, Optional): The VPC subnetwork to attach to the worker and validation test VMs, such as `projects/<var>PROJECT_ID</var>/regions/<var>REGION</var>/subnetworks/<var>SUBNET_NAME</var>`.
  * `externalIP` (string, Optional): Specifies the external IP address allocation for the worker and validation test VMs. Allowed values: 
    * `ephemeral` (default): Allocates a public ephemeral IPv4 address from a shared pool.
    * `none`: Creates VMs with no external IP address, which uses private VPC networking only. When set to `none`, ensure that your VPC subnetwork has Private Google Access or Cloud NAT enabled so that the VMs can access required Google Cloud services and package repositories.
  * `acceleratorType` (string, Optional): The GPU accelerator type to attach to the worker VM, such as `nvidia-tesla-t4` or `nvidia-l4`.
  * `acceleratorCount` (number, Optional): The number of GPU accelerators to attach to the worker VM.
  * `debug` (boolean, Optional): If you set `debug` to `true`, Image Builder preserves the worker VM whether customization completes or fails so you can inspect or troubleshoot the active instance using SSH. Defaults to `false`.
  * `instanceDurationHours` (number, Optional): Limits the worker VM runtime. The time limit begins when customization completes or encounters a script error, allowing you to connect to the active VM during interactive debugging sessions. Capped at a maximum of `2.0` hours.
  * `reservations` (array of strings, Optional): Capacity reservation resource names (such as `test-reservation` in the same project) to consume when Image Builder creates VMs.
  * `validationConcurrency` (number, Optional): Specifies the maximum number of validation tests to run in parallel on the temporary validation test compute instance. The allowed values include the following: 
    * `0` or omitted (default): Image Builder auto-detects the concurrency based on the machine type and accelerator configuration and sets it as follows: 
      * `1` (sequential) for bare-metal machine types or configurations with GPU accelerators attached, which helps prevent exceeding quota limits or resource exhaustion.
      * `4` (parallel) for all other machine types.
    * `1`: Runs validation tests sequentially. If your project has limited quota for the specified `machineType`, then setting concurrency to `1` can be helpful because it prevents multiple compute instances from being started at the same time.
    * `2` or greater: Runs the specified number of validation tests in parallel. If you have sufficient capacity or reservations, increasing concurrency can reduce overall execution time for validation tests.



## Source image

Identifies the base operating system image that Image Builder uses to launch the worker VM. You must specify one of the following options:

To specify a standard image family:
    
    
    source:
      imageFamily: projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY

To specify a direct image version URI:
    
    
    source:
      imagePath: projects/IMAGE_PROJECT/global/images/IMAGE_NAME

  * `imageFamily` (string): The path to a standard image family group, such as `projects/ubuntu-os-cloud/global/images/family/ubuntu-2204-lts`.
  * `imagePath` (string): The direct resource URI to a specific Compute Engine image version, such as `projects/cos-cloud/global/images/cos-105-17412-226-28`.



## Destinations

Defines where and how to release the compiled custom OS image. This property contains a list of release destination objects under `diskImage`:
    
    
    destinations:
      - diskImage:
          name: IMAGE_NAME
          project: PROJECT_ID
          family: IMAGE_FAMILY
          description: DESCRIPTION
          licenses:
            - projects/PROJECT_ID/global/licenses/LICENSE_NAME
          labels:
            env: production
          signatureDatabaseFile: SIGNATURE_DB_PATH
          storageLocations:
            - STORAGE_LOCATION

  * `name` (string, Required): The base name prefix assigned to the final Compute Engine image resource. Image Builder automatically appends the unique build ID to this prefix and truncates the final image name to 63 characters.
  * `family` (string, Optional): The image family to apply to the newly generated image.
  * `project` (string, Required): The Google Cloud project where Image Builder writes the output image.
  * `description` (string, Optional): Description text attached to the generated image metadata.
  * `licenses` (array of strings, Optional): Resource paths of specific software licenses applied to this image.
  * `labels` (map, Optional): Tagging metadata key-value pairs, such as `env: production`.
  * `signatureDatabaseFile` (string, Optional): Resource path to a secure boot signature database file.
  * `storageLocations` (array of strings, Optional): Target storage region or multi-region, such as `us-central1` or `us`, where Compute Engine stores the final disk blocks. Note: Although this property is formatted as a list, you can specify only a single location per image destination.



## Specification configuration

Applies general execution options:
    
    
    spec:
      config:
        skipSystemTests: false

  * `skipSystemTests` (boolean, Optional): Toggles whether the test VM evaluates boot conditions, networking, and UEFI structures. Defaults to `false`.



## Specification steps

Specifies a list of step objects that Image Builder runs in order on the worker VM. For complete input parameter schemas and usage examples for each step type, see [Supported customization actions](https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions).

All customization step objects share the following common properties:
    
    
    spec:
      steps:
        - name: STEP_NAME
          action: ACTION_TYPE
          inputs:
            # Action-specific input parameters

  * `name` (string, Required): User-defined name for this customization step.
  * `action` (string, Required): The helper action to invoke. Supported actions: 
    * [`Shell`](https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions#shell): Executes terminal scripts in the VM.
    * [`FileCopy`](https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions#filecopy): Transfers assets from Cloud Storage buckets or workspaces.
    * [`UpdateKernelCommandLine`](https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions#updatekernelcommandline): Updates boot parameters.
    * [`InstallGPU`](https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions#installgpu): Registers NVIDIA GPU drivers.
  * `inputs` (object, Required): The key-value properties required by the selected action. For complete parameter references and examples, see [Supported customization actions](https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions).



The following snippet shows an example step using the `Shell` action:
    
    
    spec:
      steps:
        - name: setup-environment
          action: Shell
          inputs:
            inlineScript: |
              #!/usr/bin/env bash
              echo "Running customization..."

## What's next

  * Explore detailed input schemas, parameter references, and usage examples for customization steps in [Supported customization actions](https://docs.cloud.google.com/compute/docs/images/image-builder/supported-customization-actions).
  * Learn how to configure pipeline orchestration settings in the [Cloud Build configuration file schema](https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema).
  * Follow the step-by-step tutorial to [Create an Image Builder pipeline](https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
