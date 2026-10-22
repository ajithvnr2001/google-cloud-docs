---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-storage-rm/
title: gdcloud storage rm \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:58.692745+00:00
---

# gdcloud storage rm  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-storage-rm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud storage rm Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud storage rm - Delete objects and buckets.

## SYNOPSIS
    
    
    gdcloud storage rm [URLS ...]
        [--all-versions]
        [--continue-on-error]
        [--recursive]
        [--format=FORMAT]
        [--log-http]
        [--verbosity=VERBOSITY] [flags]
    

### EXAMPLES
    
    
    The following command deletes an object named my-object from
    the bucket my-bucket:
    
        gdcloud storage rm s3://my-bucket/my-object
    
    The following command deletes all objects directly within the directory
    my-dir, but no objects within subdirectories:
    
        gdcloud storage rm s3://my-bucket/my-dir/*
    
    The following command deletes all objects and subdirectories within the
    directory my-dir:
    
        gdcloud storage rm s3://my-bucket/my-dir/**
    
    Note that for buckets that contain versioned objects, the previous
    command only affects live versions. Use the --recursive flag instead to
    delete all versions.
    
    The following command deletes all versions of all resources in my-bucket
    and then deletes the bucket.
    
        gdcloud storage rm --recursive s3://my-bucket/
    
    The following command deletes all text files in the top-level of my-bucket,
    but not text files in subdirectories:
    
        gdcloud storage rm --recursive s3://my-bucket/*.txt
    

### OPTIONAL FLAGS
    
    
          --all-versions        Delete all versions of an object.
          --continue-on-error   If any operations are unsuccessful, the command will exit with a non-zero
                                exit status after completing the remaining operations. This flag takes
                                effect only in sequential execution mode (i.e. processor and thread count
                                are set to 1). Parallelism is default.
          --log-http            Log all HTTP server requests and responses to stderr.
          --recursive           Recursively delete the contents of buckets or directories that match
                                the path expression. If the path is set to a bucket, the bucket is also
                                deleted. This option implies the --all-versions option. If you want to
                                delete only live object versions, use the ** wildcard instead.
          --verbosity string    Override the default verbosity for this command. VERBOSITY must be one of:
                                debug, info, warning, error, critical, none. (default "warning")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
