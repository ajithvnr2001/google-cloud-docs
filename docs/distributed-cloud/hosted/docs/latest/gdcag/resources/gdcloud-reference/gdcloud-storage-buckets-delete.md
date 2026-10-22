---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-buckets-delete/
title: gdcloud storage buckets delete \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:10.430262+00:00
---

# gdcloud storage buckets delete  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-buckets-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud storage buckets delete Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud storage buckets delete - Delete storage buckets.

## SYNOPSIS
    
    
    gdcloud storage buckets delete BUCKET_NAME [ BUCKET_NAME ...]
        [--location=LOCATION]
        [--location-type=LOCATION_TYPE]
        [--project=PROJECT_ID]
        [--format=FORMAT]
        [--log-http] [flags]
    

## DESCRIPTION

Delete one or more storage buckets.

### EXAMPLES
    
    
    The following command deletes a zonal bucket named my-bucket under the default project:
    
        gdcloud storage buckets delete my-bucket --location=zone1 --location-type=SingleZone
    
    The following command deletes two zonal buckets, one named my-bucket and a second bucket named my-other-bucket:
    
        gdcloud storage buckets delete my-bucket my-other-bucket --location=zone1 --location-type=SingleZone
    
    The following command deletes a zonal bucket under a project with ID my-project-id:
    
        gdcloud storage buckets delete my-bucket --location=zone1 --location-type=SingleZone --project=my-project-id
    
    The following command deletes a dual-zone bucket named my-dz-bucket under the default project:
    
        gdcloud storage buckets delete my-dz-bucket --location=zone1,zone2 --location-type=AsyncDualZone
    
    The following command deletes two dual-zone buckets, one named my-dz-bucket and a second bucket named my-other-dz-bucket:
    
        gdcloud storage buckets delete my-dz-bucket my-other-dz-bucket --location=zone1,zone2 --location-type=AsyncDualZone
    
    The following command deletes a dual-zone bucket under a project with ID my-project-id:
    
        gdcloud storage buckets delete my-dz-bucket --location=zone1,zone2 --location-type=AsyncDualZone --project=my-project-id
    

### OPTIONAL FLAGS
    
    
          --location string        Comma-separated list of zones where the storage buckets are available. If unset, will use current zone as the location
          --location-type string   Bucket location configuration type. Available options are: [AsyncDualZone, SyncDualZone, SingleZone]. (default "singlezone")
          --log-http               Log all HTTP server requests and responses to stderr.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
