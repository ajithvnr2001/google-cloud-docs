---
url: https://docs.cloud.google.com/location-finder/docs/quickstart/
title: Quickstart: Enable Cloud Location Finder and run a query \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:31.125689+00:00
---

# Quickstart: Enable Cloud Location Finder and run a query  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/location-finder/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Cloud Location Finder ](https://docs.cloud.google.com/location-finder/docs)
  * [ Guides ](https://docs.cloud.google.com/location-finder/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Enable Cloud Location Finder and run a query

This page shows you how to enable Cloud Location Finder using the Google Cloud CLI and find cloud locations by proximity, jurisdiction, and carbon footprint. You can find locations using HTTP requests or Google Cloud CLI commands.

## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.
  2. To [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI, run the following command: 
         
         gcloud init
         

If you've already installed Google Cloud CLI previously, make sure you have the latest available version by running `gcloud components update`.

  3. Enable the Cloud Location Finder API: 
         
         gcloud services enable cloudlocationfinder.googleapis.com  --project PROJECT
         

  4. Add the `cloudlocationfinder.viewer` role: 
         
         gcloud projects add-iam-policy-binding PROJECT \
             --member USER_IDENTIFIER \
             --role roles/cloudlocationfinder.viewer
         

     * Replace PROJECT with your project ID.
     * Replace USER_IDENTIFIER with the identifier for your user account. For example, user:myemail@example.com.
  5. If you plan to find Google Distributed Cloud connected locations using Cloud Location Finder, [enable the GDC Hardware Management API](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/order#hardware-api-enable) and add the `gdchardwaremanagement.reader` role: 
         
         gcloud projects add-iam-policy-binding PROJECT \
             --member USER_IDENTIFIER \
             --role roles/gdchardwaremanagement.reader
         




## Explore common Cloud Location Finder queries

Cloud Location Finder lets you query the cloud location repository to identify nearby cloud locations based on proximity, territory code, or Google carbon free energy (CFE%) consumption. The following sections provide common examples of how to interact with the Cloud Location Finder repository.

Cloud Location Finder uses [gRPC Transcoding syntax](https://google.aip.dev/127).

  * Replace PROJECT with your project ID.
  * Replace CLOUD_REGION with the source cloud region to find the closest location to, including the cloud provider prefix. For example, `gcp-us-central1` or `aws-us-east-1`.
  * Replace CLOUD_PROVIDER with the cloud provider to find the closest location to. For example, `AWS` or `GCP`.



### Find the nearest cloud zone

Use this query to identify the nearest Google Cloud zone to a cloud location using proximity data for a cloud provider that you specify.

### HTTP
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "X-Goog-User-Project: PROJECT" \
        -G "https://cloudlocationfinder.googleapis.com/v1/projects/PROJECT/locations/global/cloudLocations:search" \
        --data-urlencode "source_cloud_location=projects/PROJECT/locations/global/cloudLocations/CLOUD_REGION" \
        --data-urlencode "query=cloud_provider=CLOUD_PROVIDER_CLOUD_PROVIDER AND cloud_location_type=CLOUD_LOCATION_TYPE_ZONE" \
        --data-urlencode "page_size=1"
    

### gcloud
    
    
    gcloud cloudlocationfinder cloud-locations search \
        --source-cloud-location=CLOUD_REGION \
        --query="cloud_provider=CLOUD_PROVIDER_CLOUD_PROVIDER AND cloud_location_type=CLOUD_LOCATION_TYPE_ZONE" \
        --limit=1
    

### Find all Google Distributed Cloud connected zones in a region

Use this query to list Distributed Cloud connected zones within a specific region.

### HTTP
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "X-Goog-User-Project: PROJECT" \
        -G "https://cloudlocationfinder.googleapis.com/v1/projects/PROJECT/locations/global/cloudLocations" \
        --data-urlencode 'filter=containing_cloud_location="projects/PROJECT/locations/global/cloudLocations/CLOUD_REGION" AND cloud_provider=CLOUD_PROVIDER_GCP AND cloud_location_type=CLOUD_LOCATION_TYPE_GDCC_ZONE'
    

### gcloud
    
    
    gcloud cloudlocationfinder cloud-locations list \
        --filter='cloud_provider=CLOUD_PROVIDER_GCP AND cloud_location_type=CLOUD_LOCATION_TYPE_GDCC_ZONE AND containing_cloud_location="projects/PROJECT/locations/global/cloudLocations/CLOUD_REGION"'
    

### Find regions within a specific territory

Use this query to identify regions within a specific territory, or jurisdiction, using a territory code that you provide.

### HTTP
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "X-Goog-User-Project: PROJECT" \
        -G "https://cloudlocationfinder.googleapis.com/v1/projects/PROJECT/locations/global/cloudLocations:search" \
        --data-urlencode "source_cloud_location=projects/PROJECT/locations/global/cloudLocations/CLOUD_REGION" \
        --data-urlencode 'query=cloud_provider=CLOUD_PROVIDER_CLOUD_PROVIDER AND cloud_location_type=CLOUD_LOCATION_TYPE_REGION AND territory_code="TERRITORY_CODE"' \
        --data-urlencode "page_size=1"
    

### gcloud
    
    
    gcloud cloudlocationfinder cloud-locations search \
        --source-cloud-location=CLOUD_REGION \
        --query="cloud_provider=CLOUD_PROVIDER_CLOUD_PROVIDER AND cloud_location_type=CLOUD_LOCATION_TYPE_REGION AND territory_code=\"TERRITORY_CODE\"" \
        --limit=1
    

### List cloud locations that minimize carbon footprint

Use this query to identify regions with the lowest carbon footprint based on [Carbon free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon%22%3ECFE%20consumption).

**Note:** CFE data is available for only Google Cloud locations.

### HTTP
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "X-Goog-User-Project: PROJECT" \
        -G "https://cloudlocationfinder.googleapis.com/v1/projects/PROJECT/locations/global/cloudLocations" \
        --data-urlencode "filter=cloud_provider=CLOUD_PROVIDER_CLOUD_PROVIDER AND cloud_location_type=CLOUD_LOCATION_TYPE_REGION" \
        --data-urlencode "page_size=5"
    

### gcloud
    
    
    gcloud cloudlocationfinder cloud-locations list \
        --filter="cloud_provider=CLOUD_PROVIDER_CLOUD_PROVIDER AND cloud_location_type=CLOUD_LOCATION_TYPE_REGION" \
        --limit=5
    

## What's next

  * Review [supported locations](https://docs.cloud.google.com/location-finder/docs/overview#supported-locations)
  * Learn about the [location search query syntax](https://docs.cloud.google.com/location-finder/docs/syntax)
  * Check out the [API reference](https://docs.cloud.google.com/location-finder/docs/reference/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
