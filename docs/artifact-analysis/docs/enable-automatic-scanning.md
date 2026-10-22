---
url: https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning/
title: Enable or disable automatic scanning \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:21.667735+00:00
---

# Enable or disable automatic scanning  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Enable or disable automatic scanning Stay organized with collections  Save and categorize content based on your preferences. 

This document tells you how to enable and disable automatic scanning.

Artifact Analysis provides automated vulnerability scanning for container images in Artifact Registry through the Container Scanning API. Platform administrators and application developers can use the scan results to identify and mitigate risks to their software supply chain.

By default, Artifact Analysis scans all supported package types in your project when you enable the Container Scanning API. To lower costs and reduce noise in scanning findings, you can disable scanning on individual repositories. For more information, see Control scanning settings for an individual repository.

See the [Pricing page](https://cloud.google.com/artifact-analysis/pricing#vulnz) for pricing information.

## Limitations

Scanning isn't supported in Artifact Registry virtual repositories.

## Enable the Container Scanning API

**Important:** When you enable the Artifact Analysis API, Artifact Analysis automatically begins scanning each new image as they are pushed to Artifact Registry repositories in your project. However, scanning is disabled by default for packages pushed to Artifact Registry repositories. To enable scanning in a repository, see [Control scanning settings for an individual repository](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning#disable-repo).

You can enable the Container Scanning API for an existing project, or create a new project and then enable the API. Enabling the Container Scanning API also enables the Container Analysis API for metadata storage and retrieval.

To enable vulnerability scanning for your project in Artifact Registry, complete the following steps:

In the Google Cloud console, open the **Enable access to API** page:

[ Enable the Container Scanning API ](https://console.cloud.google.com/apis/enableflow?apiid=containerscanning.googleapis.com)

## Control scanning settings for an individual repository

This section explains how to control the scanning settings for individual repositories. This feature is only supported in Artifact Registry.

By default, enabling the Container Scanning API activates scanning for all images you push to standard and remote Docker repositories in Artifact Registry. The following repository formats also support automatic scanning; however, scanning is disabled by default and must be enabled manually:

  * Maven
  * Npm
  * Python



Scanning with Artifact Analysis provides comprehensive information about potential threats to your software supply chain. You can also disable scanning on individual repositories if needed.

You can disable scanning on repositories to:

  * Manage your scanning costs within a project. You don't need to turn off scanning for an entire project, or create a new project to isolate repositories.
  * Reduce the number of vulnerability findings you receive. You can focus on remediating vulnerabilities in specific repositories.



To change scanning settings for existing Artifact Registry repositories, do the following:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the repository and click **Edit Repository**.

  3. **Enable** or **disable** vulnerability scanning.

  4. Click **Save**.




###  gcloud 

To disable scanning on the repository:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT-ID \
        --location=LOCATION \
        --disable-vulnerability-scanning
    

To allow scanning on the repository:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT-ID \
        --location=LOCATION \
        --allow-vulnerability-scanning
    

Where:

  * REPOSITORY: The name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults) repository, then you can omit this flag to use the default.
  * PROJECT-ID: The Google Cloud project ID. If this flag is omitted, then the current or default project is used.
  * LOCATION: Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults) location, then you can omit this flag to use the default.



To configure scanning settings for a new Artifact Registry repository, see [Create standard repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) or [Create remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo).

## Disable the Container Scanning API

This section explains how to disable vulnerability scanning for your project in Artifact Registry.

When you disable the Container Scanning API, scanning stops for all repositories in your project. Scanning settings for individual repositories are preserved. If you previously disabled scanning on some repositories, and later re-enable the API for your project, those repositories will remain excluded from scanning.

To update scanning settings for individual repositories, see [Update repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/update-repo-settings).

### Console

  1. Open the **Settings** page for Artifact Registry:

[Open the Settings page](https://console.cloud.google.com/artifacts/settings)

  2. In the **Vulnerability Scanning** section, click **Disable**.




### gcloud

Run the following command:
    
    
    gcloud services disable containerscanning.googleapis.com
    

## Extend your monitoring time window

Artifact Analysis continuously monitors the vulnerability metadata for scanned images in Artifact Registry. The default time window for continuous monitoring is 30 days. After this period your images are stale and the vulnerability scanning results are no longer updated.

To extend the monitoring window, you must pull or push the image within the 30-day period. We recommend creating a scheduled task to re-push containers that don't require frequent updating, for example, your Istio and proxy images.

## What's next

  * [Get started with automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/quickstart-scanning-os-automatically).
  * [Understand container scanning concepts](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
