---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-validation-tests/
title: Troubleshoot validation tests \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:17:17.076153+00:00
---

# Troubleshoot validation tests  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-validation-tests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot validation tests Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage).  To verify that custom VM images boot correctly and meet configuration requirements, Image Builder executes automated validation tests on a temporary test VM. If one of these tests fails, the pipeline stops and Image Builder does not publish the final image. 

## Before you begin

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




## Overview

If the customization steps complete successfully, the orchestrator exports the VM boot disk as a temporary test image (named `image-builder-test-image-BUILD_ID` in the `image-builder-test-images` family).

The orchestrator boots a test VM from this image and runs a suite of system tests. Image Builder outputs the test outcomes in a standard JUnit XML format directly to the Cloud Build logs.

## Troubleshoot specific validation tests

Review the common failures and diagnostic steps for each validation test:

### Intel IDPF driver verification

This test verifies that supported VM instances load the high-performance Intel Infrastructure Data Path Function (`idpf`) driver on physical network interfaces.

  * **Failure Condition** : The VM fails validation if it reverts to a generic network adapter package or if the guest kernel lacks the active `idpf` driver module.
  * **Resolution** : 
    * Ensure your base operating system has a kernel version compatible with IDPF.
    * Confirm that standard network utilities are not stripping or block-listing the driver.
    * For custom kernel builds, verify that `CONFIG_IDPF` is configured.



### Networking and guest agent verification

This test asserts that the instance has working guest communications and standardized network interface configurations.

  * **Failure Condition** : The test fails under any of the following conditions: 
    * The guest agent service manager `SubState` does not show a `running` status.
    * No non-loopback network interface is online.
    * Interface names don't match expected standard patterns (for example, `eth*` or `en*`).
  * **Resolution** :

    * Verify that the guest agent is installed and configured to start at boot:
          
          systemctl is-active google-guest-agent
          

    * Ensure your network configurations (such as netplan or ifupdown templates) don't disable primary virtual interfaces.




### Secure Boot verification

This test asserts that UEFI Secure Boot is active and that the system enforces guest OS kernel signature validation on the image.

  * **Failure Condition** : The test fails if Compute Engine UEFI variables report `SecureBoot` is not `1` or `SetupMode` is not `0`.
  * **Resolution** :

    * Confirm your image includes valid signature keys.
    * In your [`imagebuilder.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema) file, verify that `guestOsFeatures` contains `UEFI_COMPATIBLE` under your destinations block:
          
          destinations:
            - diskImage:
                guestOsFeatures:
                  - UEFI_COMPATIBLE
          




### Suspend or resume verification

This test suspends the test VM using the Compute Engine API and asserts that after VM execution resumes, connectivity is restored without triggering a full guest reboot.

  * **Failure Condition** : The test fails if the instance reboots on wake, hangs during suspension, or fails to recover network pings.
  * **Resolution** : 
    * Verify that ACPI services and power policies on the guest operating system are enabled and configured to respond to ACPI events.
    * Inspect guest system logs (`/var/log/syslog` or `/var/log/messages`) to check if custom daemons block system sleep requests.



## Skip validation tests

Although we recommend that you validate production images, you can skip validation tests during testing by setting `skipSystemTests: true` under the `spec.config` block in your `imagebuilder.yaml` file:
    
    
    spec:
      config:
        skipSystemTests: true
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
