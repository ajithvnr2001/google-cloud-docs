---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-buckets-create/
title: gdcloud storage buckets create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:19:32.709166+00:00
---

# gdcloud storage buckets create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-buckets-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud storage buckets create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud storage buckets create - Create new storage buckets.

## SYNOPSIS
    
    
    gdcloud storage buckets create [ BUCKET_NAME ...]
        --bucket-file=BUCKET_FILE |
        [--location=LOCATION]
        [--location-type=LOCATION_TYPE]
        ( [--description=DESCRIPTION]
        [--storage-class=STORAGE_CLASS]
        [--project=PROJECT_ID]
        [--api-version=VERSION]
        [--labels=key1=value1,key2=value2 | --labels-file=LABELS_FILE]
        [--annotations=value1,key2=value2 | --annotations-file=ANNOTATIONS_FILE]
        [--finalizers=value1,value2]
        [--enable-locking-policy]
        [--retention-days=RETENTION_DAYS]
        [--enable-cors-policy=bool]
        [--cors-file=CORS_FILE] )
        [--enable-life-cycle-policy=bool]
        [--life-cycle-rules-file=LIFE_CYCLE_RULES_FILE] )
        [--format=FORMAT]
        [--log-http] [flags]
    

## DESCRIPTION

Create buckets for storing objects.

### EXAMPLES
    
    
    The following command creates a zonal bucket named "my-bucket" in the default project:
    
        gdcloud storage buckets create my-bucket --location=zone1 --location-type=SingleZone
    
    The following command creates two zonal buckets, one named "my-bucket" and a second bucket named "my-other-bucket":
    
        gdcloud storage buckets create my-bucket my-other-bucket --location=zone1 --location-type=SingleZone
    
    The following command creates a zonal bucket with the Standard storage class in a project with ID my-project-id:
    
        gdcloud storage buckets create my-bucket --storage-class=Standard --project=my-project-id --location=zone1 --location-type=SingleZone
    
    The following command creates a zonal bucket from a file containing YAML configuration for the bucket. Flags other than --bucket-file are ignored when creating a bucket:
    
        gdcloud storage buckets create --bucket-file=BUCKET_FILE --location=zone1 --location-type=SingleZone
    
    The following command creates two dual-zone buckets, one named "my-dual-zone-bucket" and a second bucket named "my-other-dual-zone-bucket":
    
        gdcloud storage buckets create my-dual-zone-bucket my-other-dual-zone-bucket --location=zone1,zone2 --location-type=AsyncDualZone
    
    The following command creates a dual-zone bucket from a file containing YAML configuration for the bucket. Flags other than --bucket-file are ignored when creating a bucket:
    
        gdcloud storage buckets create --bucket-file=BUCKET_FILE --location=zone1,zone2 --location-type=AsyncDualZone
    

### OPTIONAL FLAGS
    
    
          --annotations stringToString     Comma-separated list of key-value pairs for annotations. (default [])
          --annotations-file string        Path to a file containing YAML configuration for annotations.
          --api-version string             API version for the bucket (default is the newest API version).
          --bucket-file string             Path to a file containing YAML configuration for a bucket custom resource.
                                           If set, the gdcloud CLI creates the bucket from the YAML configuration and ignores the other flags that define the bucket API field.
          --cors-rules-file string         Path to a file containing YAML configuration for the CORS policy detail. It must contain an array of CORS rules.
          --description string             String description of bucket contents.
          --enable-cors-policy             If set, the custom policy defined in CORS_FILE takes effect.
                                           Otherwise, CORS_FILE is ignored even if it has been set.
                                           (default is false).
          --enable-life-cycle-policy       If set, the custom policy defined in LIFE_CYCLE_RULES_FILE takes effect.
                                           Otherwise, LIFE_CYCLE_RULES_FILE is ignored even if it has been set.
                                           (default is false).
          --enable-locking-policy          Locking policy that must be enabled when creating the bucket and cannot be disabled afterwards.
                                           If unset, object locking and versioning is disabled and cannot be enabled.
                                           The locking policy does not have a default amount of retention days.
                                           Use the --retention-days flag to set the retention days.
          --finalizers strings             Comma-separated list of strings for finalizers.
          --labels stringToString          Comma-separated list of key-value pairs for labels. (default [])
          --labels-file string             Path to a file containing YAML configuration for labels.
          --life-cycle-rules-file string   Path to a file containing YAML configuration for the life cycle policy detail. It must contain an array of life cycle rules.
          --location string                Comma-separated list of zones where the storage buckets are available. If unset, will use current zone as the location
          --location-type string           Bucket location configuration type. Available options are: [AsyncDualZone, SyncDualZone, SingleZone]. (default "singlezone")
          --log-http                       Log all HTTP server requests and responses to stderr.
          --retention-days int32           Minimum number of days as an integer that each version of every object will be retained.
                                           If set, the locking policy controlled by the --enable-locking-policy flag is enabled by default.
          --storage-class string           Storage class of the bucket. The available value is "Standard". (default "Standard")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
