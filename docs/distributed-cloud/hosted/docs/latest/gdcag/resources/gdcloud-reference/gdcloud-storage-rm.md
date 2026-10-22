---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-rm/
title: gdcloud storage rm \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:19:55.313414+00:00
---

# gdcloud storage rm  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-rm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud storage rm Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud storage rm - Delete objects in a bucket.

## SYNOPSIS
    
    
    gdcloud storage rm [URLS ...]
        [--all-versions]
        [--continue-on-error]
        [--recursive] [flags]
    

### EXAMPLES
    
    
    The following command deletes a single object named 'my-object' from the bucket 'my-bucket':
    
        gdcloud storage rm s3://my-bucket/my-object
    
    The following command deletes all objects and folders within the bucket 'my-bucket'. This is required when deleting a bucket's entire contents.
    Note: For versioned buckets, this command only creates delete markers for the live versions. Previous versions remain. To permanently delete all versions, use --all-versions.
    
        gdcloud storage rm --recursive s3://my-bucket
    
    The following command permanently deletes all objects and all their historical versions in 'my-bucket':
    
        gdcloud storage rm --all-versions --recursive s3://my-bucket
    
    The following command deletes all objects and subfolders within the folder 'my-folder':
    
        gdcloud storage rm --recursive s3://my-bucket/my-folder/
    
    The following command deletes all objects directly inside 'my-folder', but does NOT delete objects in subfolders:
    
        gdcloud storage rm s3://my-bucket/my-folder/*
    
    The following command deletes all objects directly inside 'my-folder', and objects in all subfolders inside 'my-folder':
    
        gdcloud storage rm --recursive s3://my-bucket/my-folder/*
    
    The following command deletes all historical versions of all objects directly inside 'my-folder', and of objects in  all subfolders inside 'my-folder':
    
        gdcloud storage rm --recursive --all-versions s3://my-bucket/my-folder/*
    
    The following command deletes all objects and subfolders inside 'my-folder' (equivalent to --recursive on the folder):
    
        gdcloud storage rm s3://my-bucket/my-folder/**
    
    The following command deletes all historical versions of 'my-object', permanently removing it. Use this if the bucket has versioning enabled:
    
        gdcloud storage rm --all-versions s3://my-bucket/my-object
    
    The following command deletes a specific version of 'my-object' using its version ID:
    
        gdcloud storage rm s3://my-bucket/my-object#VERSION_ID
    
    The following command attempts to delete multiple objects. If one deletion fails (e.g., due to permissions), it proceeds to delete the others instead of stopping immediately:
    
        gdcloud storage rm --continue-on-error s3://my-bucket/obj1 s3://my-bucket/obj2
    

### OPTIONAL FLAGS
    
    
          --all-versions        Delete all versions of an object.
          --continue-on-error   If any operations are unsuccessful, the command will exit with a non-zero exit status after completing the remaining operations.
          --recursive           Recursively delete the contents of buckets or directories that match the path expression. When this option is used together with a non-recursive wildcard path (e.g. 'bucket/*'), this option takes precedence and recursively deletes contents or directories matching the wildcard path
          --verbosity string    Override the default verbosity for this command. VERBOSITY must be one of: debug, info, warning, error, none. (default "info")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
