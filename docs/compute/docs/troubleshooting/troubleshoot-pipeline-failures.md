---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-pipeline-failures/
title: Troubleshoot pipeline failures \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:51.264958+00:00
---

# Troubleshoot pipeline failures  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-pipeline-failures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot pipeline failures Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage).  If your Image Builder pipeline fails during the customization phase, review the log files, configure the interactive debug flag on your worker VM, or analyze intermediate debug images to identify compile-time or script errors. 

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



## Review logging channels

Image Builder writes logs to multiple locations to help you diagnose failures at different levels of the stack:

  * **Cloud Build orchestrator logs** : Displays the high-level builder steps in the Cloud Build Console. If a step fails, a link to the corresponding Cloud Storage workdir directory is printed.
  * **Customization VM agent logs** : The customization agent captures the standard output (`stdout`) and standard error (`stderr`) of your customization steps. The orchestrator polls these records and streams them directly into the Cloud Build trace logs. If the logs are truncated or you need to inspect them in full, go to the folder matching your build ID in the `_GCS_WORKDIR` bucket.
  * **Serial console logs** : If the guest OS fails to boot, the customization agent can't start. In these cases, look at the serial console logs. The orchestrator streams the worker VM's serial port output directly to your Cloud Storage workdir bucket. A link to the serial log file is printed at the end of the failing Cloud Build trace.
  * **Guest OS journal logs** : For detailed system-level troubleshooting on Linux, the customization agent uploads a full system `journal` log copy to your Cloud Storage workdir bucket at the end of the run.



## Resolve script failures using the debug flag

By default, if a customization step fails, Image Builder terminates execution and deletes the worker VM immediately to control costs.

To debug scripts interactively, you can enable the `debug` flag. This keeps the VM active, allowing you to connect directly to the active guest system by using SSH.

### Enable the debug flag

In your [`imagebuilder.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema) file, set `debug: true` under the `infrastructureConfig` block:
    
    
    infrastructureConfig:
      machineType: e2-standard-4
      zone: us-central1-a
      # Enable interactive debugging
      debug: true
      instanceDurationHours: 1.5

### Trigger the build and wait for failure

Submit your build using standard methods. If the pipeline encounters a script error, the following occurs:

  1. The orchestrator pauses the build execution.
  2. Image Builder does not delete the worker VM. It remains running in your project.
  3. The VM remains active for the time specified in the `instanceDurationHours` property before automatic termination.



### Connect to the worker VM to debug

Look at the Cloud Build console output to retrieve the name of the active worker VM instance. Open a terminal and connect to the worker VM by using [`gcloud compute ssh`](https://docs.cloud.google.com/compute/docs/connect/standard-ssh):
    
    
    gcloud compute ssh WORKER_VM_NAME \
        --zone=BUILD_ZONE \
        --project=PROJECT_ID
    

If your `imagebuilder.yaml` file configures `externalIP: none`, which results in no external IP address, include the `--tunnel-through-iap` flag to connect by using [Identity-Aware Proxy (IAP) TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding):
    
    
    gcloud compute ssh WORKER_VM_NAME \
        --zone=BUILD_ZONE \
        --project=PROJECT_ID \
        --tunnel-through-iap
    

Once connected, you can run commands in real time, inspect target files, analyze running processes, review installer history logs, and test script modifications directly on the disk.

## Analyze intermediate debug images

As an alternative to keeping the worker VM active with the `debug` flag, you can analyze the disk state by using the auto-generated debug image:

  1. Whenever a build fails with `debug: false` (the default), the orchestrator exports the partially customized boot disk as a Compute Engine image.
  2. The debug image is named using the pattern `image-builder-debug-image-BUILD_ID` and is assigned to the `image-builder-debug-images` image family.
  3. To inspect the file system, create a temporary VM instance using this debug image as the boot disk:
         
         gcloud compute instances create temp-debug-vm \
             --image-family=image-builder-debug-images \
             --zone=ZONE \
             --project=PROJECT_ID
         

  4. Connect to the `temp-debug-vm` instance to inspect the disk and isolate why the customization failed.




## Resolve Cloud Build timeouts

If an Image Builder pipeline run takes longer than expected, then the Cloud Build job stops and fails with a `TIMEOUT` status.

Build times can vary and are typically longer for larger machine types, so set the timeout to allow more time for the build to complete. If not set, the default Cloud Build timeout is 1 hour (`3600s`).

To configure a longer timeout, set the `timeout` field at the root level of your [`cloudbuild.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema) file:
    
    
    options:
      automapSubstitutions: true
      requestedVerifyOption: VERIFIED
      substitutionOption: ALLOW_LOOSE
      dynamicSubstitutions: true
      logging: CLOUD_LOGGING_ONLY
    
    # Increase the overall build timeout (for example, 2 hours)
    timeout: '7200s'

After updating the timeout value, re-run the build and verify that the Image Builder pipeline is able to execute to completion.

For more information about the `timeout` parameter, see `timeout` in the Cloud Build documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
