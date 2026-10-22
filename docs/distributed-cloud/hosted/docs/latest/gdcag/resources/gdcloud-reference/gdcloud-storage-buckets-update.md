---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-buckets-update/
title: gdcloud storage buckets update \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:46.887035+00:00
---

# gdcloud storage buckets update  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-buckets-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud storage buckets update Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud storage buckets update - Update storage buckets.

## SYNOPSIS
    
    
    gdcloud storage buckets update [ BUCKET_NAME ...]
        [--location=location]
        [--location-type]
        --bucket-file=BUCKET_FILE |
        ( [--description=description]
        [--project=project-id]
        [--labels=key1=value1,key2=value2] | [--labels-file=LABELS_FILE] | [--update-labels=key1=value1,key2=value2]
        [--annotations=key1=value1,key2=value2] | [--annotations-file=ANNOTATIONS_FILE] | [--update-annotations=key1=value1,key2=value2]
        [--finalizers=value1,value2] | [--update-finalizers=value1,value2]
        [--retention-days=value]
        [--enable-cors-policy=bool]
        [--cors-rules-file=CORS_RULES_FILE]
        [--enable-life-cycle-policy=bool]
        [--life-cycle-rules-file=LIFE_CYCLE_RULES_FILE ]) [flags]
    

## DESCRIPTION

Update buckets for storing objects.

### EXAMPLES
    
    
    The following command updates a zonal bucket named my-zonal-bucket:
    
        gdcloud storage buckets update my-zonal-bucket \
            --retention-days=120 \
            --enable-cors-policy=true \
            --cors-rules-file=corsRulesFilePath \
            --enable-life-cycle-policy=true \
            --life-cycle-rules-file=lifeCycleRulesFilePath \
            --location=zone1 \
            --location-type=SingleZone
    
    The following command updates a dual-zone bucket named my-dual-zone-bucket:
    
        gdcloud storage buckets update my-dual-zone-bucket \
            --retention-days=120 \
            --enable-cors-policy=true \
            --cors-rules-file=corsRulesFilePath \
            --enable-life-cycle-policy=true \
            --life-cycle-rules-file=lifeCycleRulesFilePath \
            --location=zone1,zone2 \
            --location-type=AsyncDualZone
    
    The following command updates a zonal bucket from a file containing YAML configuration for the bucket:
    
        gdcloud storage buckets update --bucket-file=BUCKET_FILE --location=zone1 --location-type=SingleZone
    
    The following command updates a dual-zone bucket from a file containing YAML configuration for the bucket:
    
        gdcloud storage buckets update --bucket-file=BUCKET_FILE --location=zone1,zone2 --location-type=AsyncDualZone
    

### OPTIONAL FLAGS
    
    
          --annotations stringToString          Comma-separated list of key-value pairs for annotations. Existing annotations not specified with this flag will be deleted. (default [])
          --annotations-file string             Path to a file containing YAML configuration for annotations. Existing annotations not specified with this flag will be deleted.
          --bucket-file string                  Path to a file containing YAML configuration for a bucket custom resource.
                                                If set, the gdcloud CLI updates the bucket from the YAML configuration and ignores the other flags that define the bucket API field.
          --cors-rules-file string              Path to a file containing YAML configuration for the CORS policy detail. It must contain an array of CORS rules.
          --description string                  String description of bucket contents.
          --enable-cors-policy                  If set, the custom policy defined in CORS_FILE takes effect.
                                                Otherwise, CORS_FILE is ignored even if it has been set.
                                                (default is false).
          --enable-life-cycle-policy            If set, the custom policy defined in LIFE_CYCLE_RULES_FILE takes effect.
                                                Otherwise, LIFE_CYCLE_RULES_FILE is ignored even if it has been set.
                                                (default is false).
          --finalizers strings                  Comma-separated list of strings for finalizers. Existing finalizers not specified with this flag will be deleted.
          --labels stringToString               Comma-separated list of key-value pairs for labels. Existing labels not specified with this flag will be deleted. (default [])
          --labels-file string                  Path to a file containing YAML configuration for labels. Existing labels not specified with this flag will be deleted.
          --life-cycle-rules-file string        Path to a file containing YAML configuration for the life cycle policy detail. It must contain an array of life cycle rules.
          --location string                     Comma-separated list of zones where the storage buckets are available. If unset, will use current zone as the location
          --location-type string                Bucket location configuration type. Available options are: [AsyncDualZone, SyncDualZone, SingleZone]. (default "singlezone")
          --log-http                            Log all HTTP server requests and responses to stderr.
          --retention-days int32                Minimum number of days as an integer that each version of every object will be retained.
          --update-annotations stringToString   Comma-separated list of key-value pairs for annotations to add or set. Existing annotations not specified with this flag are not changed. (default [])
          --update-finalizers strings           Comma-separated list of strings for finalizers to add or set. Existing finalizers not specified with this flag are not changed.
          --update-labels stringToString        Comma-separated list of key-value pairs for labels to add or set. Existing labels not specified with this flag are not changed. (default [])
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
