---
url: https://docs.cloud.google.com/workstations/docs/known-issues/
title: Known issues \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:46.916959+00:00
---

# Known issues  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

This page describes known issues that you might encounter while using Cloud Workstations.

## Unable to start workstation due to Compute Engine resource shortages

If Compute Engine is experiencing resource shortages (stockouts) of the machine type specified in your workstation configuration, you might be unable to start your workstation. To address this issue, try one of the following strategies:

  1. **Recommended** : Specify additional machine types in your configuration with the [boost mode](https://docs.cloud.google.com/workstations/docs/boost-workstation) feature and configure [automatic failover](https://docs.cloud.google.com/workstations/docs/boost-workstation#automatic-failover).
  2. Change the machine type in your workstation configuration to a machine type that has available capacity in your region.
  3. [Reserve capacity](https://docs.cloud.google.com/workstations/docs/reserve-capacity) for your selected machine type. Cloud Workstations automatically consumes reservations, or you can configure the service to consume a specific reservation.



## Workbench failed to connect to server

This error indicates the editor is unable to establish a WebSocket connection to the base editor. This is usually due to an intermediary proxy or network configuration blocking WebSocket traffic, or blocking traffic to `*.cloudworkstations.dev` domains.

If you aren't sure how to resolve the traffic issue, contact your network administrator.

## Connecting to a stopped workstation

If you are unable to connect to a stopped workstation, review your workstation cluster settings. For Cloud Workstations to automatically restart a stopped workstation when you connect, your workstation cluster must be configured to use the default Google Cloud console launcher. For more information, see [Automatically restart stopped workstations](https://docs.cloud.google.com/workstations/docs/automatically-restart-stopped-workstations).

## Disabling the Cloud Workstations API doesn't delete Cloud Workstations resources

Disabling the Cloud Workstations API doesn't delete Cloud Workstations resources. To avoid being billed, you must delete the underlying Cloud Workstations resources.

## Environment variables set on the workstation configuration are not set in SSH sessions

Environment variable set at the workstation configuration or workstation level are not set in the SSH sessions by default, and instead require the use of a [custom image](https://docs.cloud.google.com/workstations/docs/customize-container-images#container_image_that_sets_container_environment_variables_in_ssh_sessions).

## IntelliJ IDEA-based IDEs

The following features of the IntelliJ IDEA-based IDEs extension are not available, due to [limitations on JetBrains Gateway](https://youtrack.jetbrains.com/issue/CWM-838/Editor-like-synchronization-for-consoles):

  * Debug on Kubernetes
  * Debug a locally running Cloud Run service



## Google Cloud CLI can't find my command

If the `gcloud` CLI can't find your command, update to the current version:
    
    
    gcloud components update
    

Also, make sure that you use current Cloud Workstations `gcloud` CLI syntax. For help, see [`gcloud workstations --help`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations). As noted in the `gcloud` CLI [release levels](https://docs.cloud.google.com/sdk/gcloud#release_levels), alpha and beta commands may change without notice.

## Switching from Regional Persistent Disk to Hyperdisk

It is not possible to switch a workstation configuration from Regional Persistent Disk to Hyperdisk after the workstation configuration is created. To switch a workstation's backing home disk, you must create a new configuration using Hyperdisk and then manually [clone the workstation](https://docs.cloud.google.com/workstations/docs/clone-workstation) to the new configuration.

## APT repository GPG key expiration or rotation errors

When you run `apt-get update` or install packages inside a workstation container, you might encounter GPG key errors, such as `KEYEXPIRED` or `NO_PUBKEY` _KEY_ID_. This occurs when an upstream third-party repository owner (such as Yarn, NodeSource, or Microsoft) updates or rotates their signing key out-of-band.

To update the preinstalled APT repository keys in your container, run the key refresh script:
    
    
    sudo /google/scripts/refresh-preinstalled-apt-keys.sh
    

You can also run this script directly in your custom `Dockerfile` before running `apt-get update` or `apt-get install`. For more information, see [Update preconfigured Secure APT keys](https://docs.cloud.google.com/workstations/docs/customize-container-images#update_preconfigured_secure_apt_keys).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
