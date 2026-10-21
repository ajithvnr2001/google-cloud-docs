---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download/
title: Download the gdcloud CLI \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:36:12.908679+00:00
---

# Download the gdcloud CLI  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Download the gdcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to download the gdcloud CLI in your Google Distributed Cloud (GDC) air-gapped environment. GDC offers multiple gdcloud CLI bundle options for various use cases, such as:

  * **Platform** : Select the operating system (OS) and architecture that correspond with your local environment.
  * **GDC version** : Select the binary version of the gdcloud CLI, which corresponds with GDC patch versions. We recommend using the latest version available, but you can download archived versions for specific use cases.
  * **Type** : Select the binary type based on your needs. The `Full` bundle type is the comprehensive gdcloud CLI command bundle that includes all supported commands for the chosen platform. The `Lite` bundle type includes a subset of the gdcloud CLI commands from the `Full` bundle to provide a smaller bundle download size.



The available gdcloud CLI bundles give you flexibility to run the CLI as you prefer. For more information, see [Available gdcloud CLI bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview#cli-support).

This document is for all audience groups that work on GDC that must use a dedicated command-line interface tool for their air-gapped hardware and software workflows. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

  * Confirm that you have network access to an active GDC environment and know your GDC console URL (hostname). Unlike the Google Cloud CLI, the gdcloud CLI isn't publicly available for download; you download the bundle directly from your GDC console. Contact your Infrastructure Operator or Platform Administrator if you don't have this URL.

  * [Configure an organization network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-network-policy) to allow traffic from a specific CIDR outside the organization to the artifact registry. Use service `all` in the `OrganizationNetworkPolicy` resource configuration.




## Download the gdcloud CLI

Download the gdcloud CLI bundle to your system from the GDC console:

  1. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in) and access the GDC **Welcome** page.

  2. Navigate to the **Connect with CLI** section.

![Use the GDC console to download the CLI bundle.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/resources/images/download-button.png)

  3. Click **Download CLI Bundle**.

  4. Choose the supported platform of interest.

![Download the CLI bundle](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/resources/images/download-cli-bundle.png)

  5. Choose the type and version that corresponds with the platform you selected.

  6. Click **Download** to download the gdcloud CLI bundle to your local environment. Alternatively, you can select **Copy Bundle URL** to copy the download URL if you prefer initiating the download from the command-line.




## Extract the gdcloud CLI bundle

Extract the contents of the downloaded gdcloud CLI bundle to any location on your file system.

To replace an existing installation, remove the existing `google-distributed-cloud-hosted-cli` directory and extract the archive to the same location.

  * Extract the bundle:
        
        tar -xf BUNDLE_PATH/CLI_TAR_FILE
        

Replace the following:

    * `BUNDLE_PATH`: the path of the gdcloud CLI bundle. The default path is `~/Downloads`, unless the bundle download path was intentionally changed.
    * `CLI_TAR_FILE`: the name of the gdcloud CLI tar file you downloaded, such as `gdcloud_cli_windows_amd64.tar.gz`.



## What's next

  * [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in)
  * [gdcloud CLI reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud)
  * [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
