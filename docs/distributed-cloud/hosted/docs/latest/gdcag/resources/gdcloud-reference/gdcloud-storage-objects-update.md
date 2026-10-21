---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-objects-update/
title: gdcloud storage objects update \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:39:53.515603+00:00
---

# gdcloud storage objects update  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-objects-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud storage objects update Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud storage objects update - Update object storage objects.

## SYNOPSIS
    
    
    gdcloud storage objects update [URL ...]
        [--continue-on-error, -c]
        [--recursive, -r]
        [--cache-control=CACHE_CONTROL]
        [--content-disposition=CONTENT_DISPOSITION]
        [--content-encoding=CONTENT_ENCODING]
        [--content-language=CONTENT_LANGUAGE]
        [--content-md5=MD5_DIGEST]
        [--content-type=CONTENT_TYPE]
        [--custom-metadata=[CUSTOM_METADATA,...]]
        [--clear-custom-metadata]
        [--remove-custom-metadata=[CUSTOM_METADATA,...]]
        [--update-custom-metadata=[CUSTOM_METADATA,...]]
        [--format=FORMAT]
        [--log-http]
        [--verbosity=VERBOSITY] [flags]
    

### EXAMPLES
    
    
    The following command sets an object's custom-metadata:
    
        gdcloud storage objects update s3://my-bucket/my-object --custom-metadata=key1=value1,key2=value2
    
    The following command updates an object's custom-metadata:
    
        gdcloud storage objects update s3://my-bucket/my-object --update-custom-metadata=key1=value1,key2=value2
    

### OPTIONAL FLAGS
    
    
          --cache-control string                    How caches should handle requests and responses.
          --clear-custom-metadata                   Clear all custom metadata on objects. When used with --preserve-posix,
                                                    POSIX attributes are still stored in custom metadata.
          --content-disposition string              How content should be displayed.
          --content-encoding string                 How content is encoded (e.g. gzip).
          --content-language string                 Content's language (e.g. "en" signifies "English").
          --content-md5 string                      Manually specified MD5 hash digest for the contents of an uploaded
                                                    file. This flag cannot be used when uploading multiple files.
          --content-type string                     Type of data contained in the object (e.g. text/html).
      -c, --continue-on-error                       If any operations are unsuccessful, the command will exit with a non-zero
                                                    exit status after completing the remaining operations. This flag takes
                                                    effect only in sequential execution mode (i.e. processor and thread count
                                                    are set to 1). Parallelism is default.
          --custom-metadata stringToString          Set custom metadata on objects. When used with --preserve-posix, POSIX
                                                    attributes are also stored in custom metadata. (default [])
          --log-http                                Log all HTTP server requests and responses to stderr.
      -r, --recursive                               Recursively copy the contents of any directories that match the source
                                                    path expression.
          --remove-custom-metadata stringArray      Remove individual custom metadata keys from objects. This flag can be
                                                    used with --update-custom-metadata. When used with --preserve-posix,
                                                    POSIX attributes specified by this flag are not preserved.
          --update-custom-metadata stringToString   Add or set individual custom metadata key-value pairs on objects.
                                                    Existing custom metadata not specified with this flag is not changed.   This
                                                    flag can be used with --remove-custom-metadata. When keys overlap with
                                                    those provided by --preserve-posix, values specified by this flag are used. (default [])
          --verbosity string                        Override the default verbosity for this command. VERBOSITY must be one of:
                                                    debug, info, warning, error, critical, none. (default "warning")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
