---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/overview/
title: Image Builder overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:00:35.670717+00:00
---

# Image Builder overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Image Builder overview Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

Image Builder is a declarative operating system (OS) image customization tool that runs within your Google Cloud project using Cloud Build. It automates the process of building, customizing, and validating OS images to help verify that they boot correctly and follow your configuration requirements before you publish them for production workloads.

## Key benefits

By automating the lifecycle of custom OS images inside Google Cloud, Image Builder helps you manage infrastructure and validate configuration requirements. Image Builder provides the following features for your custom OS image builds:

  * **Automate OS image creation** : Create and maintain custom OS images using declarative YAML recipes and automated Cloud Build workflows, without the need for custom scripting or external tools. Because Image Builder runs within Cloud Build, you can use [Cloud Build triggers](https://docs.cloud.google.com/build/docs/triggers) to automatically launch image builds on repository events (such as a Git push or tag), set up recurring schedules (for example, weekly builds for security patches), or respond to Pub/Sub messages (to trigger builds programmatically from external workflows or webhooks).
  * **Validate images before publishing** : Verify images before publishing them. Google-provided checks validate that intermediate images boot, support Secure Boot (when applicable), load required network drivers, and run a healthy guest agent.
  * **Trace script execution** : Track the code that runs during your build pipeline. Image Builder automatically records the cryptographic SHA-256 hash of your inline customization scripts inside the build logs to maintain an audit trail.
  * **Pay only for resources used** : The Image Builder service is available at no additional charge. You incur costs only for the underlying compute, storage, and build resources consumed while your pipelines run.



## How Image Builder works

Image Builder runs inside your Google Cloud project by using a Cloud Build orchestrator container. The image build process consists of the following phases:

  1. Validation and preparation: The orchestrator container checks YAML syntax and verifies that all required APIs are enabled and that target Identity and Access Management (IAM) security permissions are active.
  2. Workspace and disk preparation: The orchestrator container archives the Cloud Build workspace directory (`/workspace`) containing your source code and configurations into a compressed tar file (`.tar.gz`) and uploads this tar file to the Cloud Storage workdir bucket specified in your build configuration. The orchestrator container then uses a statically-compiled customization provisioner file system to create a temporary Compute Engine image, which defines the secondary data disk attached to your worker VM.
  3. Worker VM execution: The orchestrator container launches an ephemeral worker VM instance by using the specified source image as the boot disk and attaches the secondary data disk containing the customization provisioner. The worker VM's hardware properties, VPC network, subnetwork, and external IP assignment—either an ephemeral public IP or no external IP—are determined by the `infrastructureConfig` settings in your `imagebuilder.yaml` file.
  4. Customization: A startup script mounts the data disk and starts the customization provisioner on the worker VM. The provisioner downloads the workspace archive and applies your declared customizations, such as running shell scripts, copying files, or compiling drivers. It also performs a security sanitization pass to clean SSH keys, unique machine IDs, and log histories. It then shuts down the instance.
  5. Validation (testing): The orchestrator container creates a temporary test OS image from the customized boot disk and provisions temporary test VMs using the network and infrastructure configuration in your `imagebuilder.yaml` file to run the following system-defined validation checks: 
     * Intel IDPF driver verification: Verifies that supported instances load the Intel Infrastructure Data Path Function (`idpf`) network driver rather than generic display or fallback drivers.
     * Networking and guest agent verification: Confirms the guest agent service is active, at least one non-loopback network interface is up, and names conform to conventions (`eth*` or `en*`).
     * Secure Boot verification: Ensures that UEFI Secure Boot is active and that the system enforces guest kernel verification.
     * Suspend or resume verification: Suspends the test VM by using the Compute Engine API and verifies that network connectivity is recovered post-resume without a system reboot.
  6. Release: If all validation checks pass, the orchestrator container prepares the final image: 
     * If Artifact Registry is configured: The orchestrator container exports the customized boot disk as a tar file to an Artifact Registry generic repository and creates the final production Compute Engine image using the Artifact Registry URI as its source.
     * If Artifact Registry is not configured: The orchestrator container creates the Compute Engine image directly in your project using the customized boot disk.

**Note:** System validation tests run by default, but you can disable them by configuring `skipSystemTests: true` in your `imagebuilder.yaml` file.

## Pricing and quota considerations

The Image Builder service is available at no extra cost. However, Google Cloud charges for standard resources provisioned during the build, test, and release phases:

  * **Compute Engine** : charges for worker VMs, test VMs, and attached Persistent Disks.
  * **Cloud Build** : charges for orchestrator container runtime minutes.
  * **Cloud Storage** : charges for workspace archives, log exports, and intermediate assets.
  * **Artifact Registry** : charges for storing exported image tar files, if configured.
  * **Custom images** : charges for storing intermediate test, debug, and production images.



For detailed information about resource costs, refer to the pricing documentation for [Compute Engine](https://docs.cloud.google.com/compute/pricing), [Cloud Build](https://docs.cloud.google.com/build/pricing), [Cloud Storage](https://docs.cloud.google.com/storage/pricing), [Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing), and [custom image storage](https://docs.cloud.google.com/compute/disks-image-pricing#custom-image-storage).

**Note:** Image Builder automatically attaches the following free license to all custom OS images that you create: https://www.googleapis.com/compute/v1/projects/image-builder-official/global/licenses/image-builder. For more information about license types, see [About licenses](https://docs.cloud.google.com/compute/docs/licenses/about).

### Quota requirements

Ensure your project has sufficient Compute Engine CPU and Persistent Disk quotas in the zone where you run your builds. Insufficient quota in the target zone causes the pipeline to fail during VM provisioning.

## What's next

  * [Prepare your environment for Image Builder](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites).
  * [Create and manage pipelines using the console](https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline-console).
  * [Create and manage pipelines programmatically](https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
