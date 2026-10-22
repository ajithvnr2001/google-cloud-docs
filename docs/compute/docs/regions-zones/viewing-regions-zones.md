---
url: https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones/
title: View available regions and zones \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:37.278028+00:00
---

# View available regions and zones  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View available regions and zones Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view a list of available regions and zones and how to get information about a specific region.

To learn more about regions and zones, read the [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) documentation.

To learn more about global, regional, and zonal Compute Engine resources, read the [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources) documentation.

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




### Required roles

To get the permissions that you need to view available regions and zones, ask your administrator to grant you the [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View a list of available zones

A zone is a deployment area within a region. Some regions have specialized zones that provide significant capacity for high-demand accelerators (GPUs and TPUs). These specialized zones are called _AI zones_ , which are ideal for AI and ML workloads.

To view a list of available zones, including the AI zones, use one of the following options:

###  Console 

View a list of zones on the **Zones** page in the Google Cloud console.

[Go to Zones](https://console.cloud.google.com/compute/zones)

###  gcloud 

Using the Google Cloud CLI, run the [`gcloud compute zones list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list):
    
    
    gcloud compute zones list

###  REST 

Make a `GET` request to the [`zones.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zones/list) method to get a list of zones for a project. Replace `PROJECT_ID` with your [PROJECT_ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    
    
    https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones

### View a list of zones that support accelerators (GPUs and TPUs)

To view a list of zones that support accelerators (GPUs and TPUs), use one of the following methods:

  * To find AI zones that provide significant capacity for accelerators, search for AI zones.
  * To find all zones that support a specific accelerator, search by accelerator type.
  * To find all zones that support a specific machine type with an accelerator, search by machine type.



#### Search for AI zones

**Important:** When AI zone visibility is turned off, your Google Cloud project's visibility of AI zones is restricted. To view AI zones, [turn on AI zone visibility](https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones#turn_on_ai_zones).

If you want to run AI and ML workloads, then consider using AI zones. You can identify an AI zone by the string `ai` in its name. For example, `us-central1-ai1a` is an AI zone in the `us-central1` region, with `us-central1-a` as its parent zone. To learn more, see [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).

The Google Cloud console lists AI zones together with other zones, grouped by regions. To view a list of available AI zones, use the gcloud CLI or REST API.

###  Console 

In the Google Cloud console, the **Zones** page lists the AI zones in a region where these zones are supported. You can identify an AI zone by the string `AI` in its name—for example, `us-central1` region lists `Zone AI1A`.

[Go to Zones](https://console.cloud.google.com/compute/zones)

###  gcloud 

Use the [`gcloud compute zones list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list) and filter zones containing the string `ai`:
    
    
    gcloud compute zones list \
        --filter="name~'-ai'"
    

###  REST 

Make a `GET` request to the [`zones.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zones/list) method. To match zones containing `ai` in their name, use the `filter` query parameter with the regular expression `name eq '.*-ai.*'`.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones?filter=name%20eq%20'.*-ai.*'
    

Replace `PROJECT_ID` with your [PROJECT_ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

#### Search by accelerator type

Searching by an accelerator type returns all zones, including AI zones, where that accelerator is supported.

###  gcloud 

To search by accelerator type, use the [`gcloud compute accelerator-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/accelerator-types/list) with the `--filter` flag.

For example, to find all zones with a specific accelerator like an NVIDIA B200 GPU or a Cloud TPU v6e (Trillium), run one of the following commands:

  * NVIDIA B200
        
        gcloud compute accelerator-types list \
              --filter="name=nvidia-b200" \
              --format="value(zone)"
        

  * Cloud TPU v6e (Trillium)
        
        gcloud compute accelerator-types list \
              --filter="name=ct6e" \
              --format="value(zone)"
        




Replace the accelerator type in the example with the accelerator type by which you want to search.

###  REST 

To search by accelerator type, send a `GET` request to the [`acceleratorTypes.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/acceleratorTypes/aggregatedList) with the `filter` parameter.

For example, to find all zones with a specific accelerator like an NVIDIA B200 GPU or a Cloud TPU v6e (Trillium), run one of the following commands:

  * NVIDIA B200 
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/acceleratorTypes?filter=name=nvidia-b200
        

  * Cloud TPU v6e (Trillium) 
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/acceleratorTypes?filter=name=ct6e
        




Replace the accelerator type in the example with the accelerator type by which you want to search.

#### Search by machine type

Searching by a machine type returns all zones, including AI zones, where that machine type is supported.

###  gcloud 

To search by machine type, use the [`gcloud compute machine-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-types/list) with the `--filter` flag.

For example, to find all zones with a specific machine type like `a4-highgpu-8g` A4 machine type or a `ct6e-standard-4t` Cloud TPU v6e (Trillium) machine type, run one of the following commands:

  * `a4-highgpu-8g` A4 machine type
        
        gcloud compute machine-types list \
              --filter="name=a4-highgpu-8g" \
              --format="value(zone)"
        

  * `ct6e-standard-4t` Cloud TPU v6e (Trillium) machine type
        
        gcloud compute machine-types list \
              --filter="name=ct6e-standard-4t" \
              --format="value(zone)"
        




Replace the machine type in the example with the machine type by which you want to search.

###  REST 

To search by machine type, make a `GET` request to the [`machineTypes.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/machineTypes/aggregatedList) with the `filter` parameter.

For example, to find all zones with a specific machine type like `a4-highgpu-8g` A4 machine type or a `ct6e-standard-4t` Cloud TPU v6e (Trillium) machine type, run one of the following commands:

  * `a4-highgpu-8g` A4 machine type
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/machineTypes?filter=name=a4-highgpu-8g
        

  * `ct6e-standard-4t` Cloud TPU v6e (Trillium) machine type
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/machineTypes?filter=name=ct6e-standard-4t
        




Replace `PROJECT_ID` with your Project ID and the machine type with the machine type by which you want to search.

### Exclude AI zones from lists

If you have access to AI zones, but don't want to see them in your zone listings, use filters to exclude them. This might be the case if you're using services that AI zones don't support, or if you have an existing automation that depends on the list of zones. You can identify AI zones by the `-ai` suffix in their names.

###  gcloud 

To exclude AI zones from the list of available zones, use the [`gcloud compute zones list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list) and filter zones containing the string `-ai`:
    
    
    gcloud compute zones list --filter 'name !~ ".*-ai.*"'
    

To filter out AI zones when listing machine types, use the [`gcloud compute machine-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-types/list) and filter zones containing the string `-ai`:
    
    
    gcloud compute machine-types list --filter 'zone !~ ".*-ai.*"'
    

###  REST 

To exclude AI zones from API results, use the `name ne ".*-ai.*"` regular expression within the filter query parameter. When adding this filter into a URL, you must encode the filter query parameter as `filter=name%20ne%20%22.%2A-ai.%2A%22`.
    
    
    https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones?filter=name%20ne%20%22.%2A-ai.%2A%22
    

Replace `PROJECT_ID` with your [PROJECT_ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

###  Terraform 

To exclude AI zones from the list of available zones, create a local function as in the following example:
    
    
    # Fetch zones from API
    data "google_compute_zones" "available" {
      project = var.my_project_id
      region  = var.my_region
      status  = "UP"
    }
    
    locals {
      # Filter the list in Terraform
      non_ai_zones = [
        for zone in data.google_compute_zones.available.names : zone
        if !strcontains(zone, "-ai")
      ]
    }
    
    # Example usage
    output "standard_gce_zones" {
      description = "List of zones, excluding AI/ML zones."
      value       = locals.non_ai_zones
    }
    

## View a list of available regions

###  Console 

You can view the available regions on the **Zones** page in the Google Cloud console.

[Go to Zones](https://console.cloud.google.com/compute/zones)

###  gcloud 

Using the Google Cloud CLI, run the [`gcloud compute regions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list):
    
    
    gcloud compute regions list

The command lists all available regions and provides information such as quotas and the status of the region itself.

For example:
    
    
    gcloud compute regions list
    NAME             CPUS   DISKS_GB     ADDRESSES  RESERVED_ADDRESSES  STATUS
    asia-east1       0/24   0/10240           0/23       0/7                 UP
    asia-northeast1  0/24   0/10240           0/23       0/7                 UP
    asia-southeast1  0/24   0/10240           0/23       0/7                 UP
    europe-west1     0/24   0/10240           2/23       0/7                 UP
    us-central1      0/24   0/10240           0/23       0/7                 UP
    us-east1         0/24   0/10240           0/23       0/7                 UP
    us-west1         0/24   0/10240           0/23       0/7                 UP
    

###  REST 

Make a `GET` request to the [`regions.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regions/list) method to get a list of regions. Replace `PROJECT_ID` with your [PROJECT_ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    
    
    https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions

## View information about a region

###  Console 

You can view information about regions on the **Zones** page in the Google Cloud console.

[Go to Zones](https://console.cloud.google.com/compute/zones)

###  gcloud 

To get information about a single region, run the [`gcloud compute regions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/describe), where `REGION` is the name of the region you want to get more information about:
    
    
    gcloud compute regions describe REGION

A response would be similar to the following:
    
    
    creationTimestamp: '2013-09-06T17:54:12.193-07:00'
    description: us-central1
    id: '5778272079688511892'
    kind: compute#region
    name: us-central1
    quotas:
    - limit: 24.0
        metric: CPUS
        usage: 5.0
    - limit: 5120.0
        metric: DISKS_TOTAL_GB
        usage: 650.0
    - limit: 7.0
        metric: STATIC_ADDRESSES
        usage: 4.0
    - limit: 23.0
        metric: IN_USE_ADDRESSES
        usage: 5.0
    - limit: 1024.0
        metric: SSD_TOTAL_GB
        usage: 0.0
    selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
    status: UP
    zones:
    - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a
    - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-b
    - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-c
    - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-f
    

###  REST 

Make a `GET` request to the [`regions.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regions/get) method to get information about a region. Replace `PROJECT_ID` with your [PROJECT_ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) and `REGION` with the region you want more information about.
    
    
    https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION

## What's next

  * Learn more about [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones)
  * Learn about [Changing the default region or zone](https://docs.cloud.google.com/compute/docs/regions-zones/changing-default-zone-region)
  * Learn more about [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
