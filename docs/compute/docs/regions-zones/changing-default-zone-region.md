---
url: https://docs.cloud.google.com/compute/docs/regions-zones/changing-default-zone-region/
title: Changing the default region or zone \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:25.137875+00:00
---

# Changing the default region or zone  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/regions-zones/changing-default-zone-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Changing the default region or zone Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set a default [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones) for your Google Cloud console [project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

When you make a request to Compute Engine, you might be required to provide a region or a zone depending on the specific requirements of your request. Any request involving [regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) resources requires that you supply a region name, and any request involving [zonal](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) resources requires that you supply a zone name. For example, you must specify a region when you create a static external IP address, and you must specify a zone when you create a Compute Engine instance. For a complete list of regions and zones, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

For more information about global, regional, and zonal Compute Engine resources, see [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

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




## How a default region and zone affect your project

The default region and zone settings affect only client tools, such as the Google Cloud CLI and the Google Cloud console. When you use these tools to construct your requests, the tools help you manage resources by automatically selecting the default region and zone.

When you use the Google Cloud console to create regional or zonal resources like addresses and instances, Compute Engine sets the region and zone fields for you. You can accept the pre-populated values or explicitly change one or both of the values.

When you use the gcloud CLI, omit setting the `--region` and `--zone` flags to use the default region and zone properties for the new project.

You can always change the default region and zone settings in the metadata server, override the default region and zone locally for the gcloud CLI, or override the settings manually for each request by using either the gcloud CLI or the Google Cloud console.

## Looking up the default region or zone

The metadata server contains metadata information about a project, including the project ID and project name. You can query the metadata server to get and use information about the project.

If you specify a default region and zone for your project, then Compute Engine sets these values in the [metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) for your project.

Default regions and zones are set by using the following values:

  * `google-compute-default-region`
  * `google-compute-default-zone`



To see what your default region and zone settings are, run the following [`gcloud`](https://docs.cloud.google.com/compute/docs/gcloud-compute) command, replacing `PROJECT_ID` with your project ID:
    
    
    gcloud compute project-info describe --project PROJECT_ID
    

Look for the default region and zone metadata values in the response. If the `google-compute-default-region` and `google-compute-default-zone` keys and values are missing from the response, that means no default region or zone is set.

## Changing the default region or zone

There are no restrictions on which regions or zones you can set for your default properties. For example, it is possible to set a default zone that is outside of your default region. Check the default region and zone settings when creating and managing your resources.

###  Console 

To change your default region or zone, follow these steps:

  1. In the Google Cloud console, go to the **Settings** page.

[Go to Settings](https://console.cloud.google.com/compute/settings)

  2. From the **Region** drop-down menu, select a default region.

  3. From the **Zone** drop-down menu, select a default zone.

  4. Click **Save**.




###  gcloud 

You can change the default region and zone by making a request to the [metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) server. For example:
    
    
    gcloud compute project-info add-metadata \
        --metadata google-compute-default-region=europe-west1,google-compute-default-zone=europe-west1-b
    

After you update the default metadata by using any method, run the `gcloud init` command to reinitialize your `default` configuration. The gcloud CLI refreshes the default region and zone settings only after you run the `gcloud init` command.

For more information about using the gcloud CLI options to set default regions and zones, see [Set default properties](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-properties).

## What's next

  * Learn more about [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * Learn more about [global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
