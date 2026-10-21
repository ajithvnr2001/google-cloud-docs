---
url: https://docs.cloud.google.com/sdk/gcloud/reference/storage/intelligence-configs/enable/
title: gcloud storage intelligence-configs enable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:08.977985+00:00
---

# gcloud storage intelligence-configs enable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/storage/intelligence-configs/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud storage intelligence-configs enable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud storage intelligence-configs enable - enables storage intelligence 
SYNOPSIS
    

`gcloud storage intelligence-configs enable` (`--organization`=`ORGANIZATION` | `--project`=`PROJECT` | `--sub-folder`=`SUB_FOLDER`) [`--trial-edition` `--exclude-bucket-id-regexes`=[`EXCLUDE_BUCKET_ID_REGEXES`,…] | `--include-bucket-id-regexes`=[`INCLUDE_BUCKET_ID_REGEXES`,…] `--exclude-locations`=[`EXCLUDE_LOCATIONS`,…] | `--include-locations`=[`INCLUDE_LOCATIONS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Enable storage intelligence plan for the organization, sub-folder or project along with filters. The command sets `STANDARD` edition by default if no other edition flags like ``--trial-edition`` are specified. 
EXAMPLES
     To remove buckets from the storage intelligence plan, Use the following command with ``\--exclude-bucket-id-regexes`` flag. to specify list of bucket id regexes., 
    
    
    gcloud storage intelligence-configs enable --organization=my-org --exclude-bucket-id-regexes="my-bucket-.*"

To apply location based filters in the storage intelligence plan, Use ``\--include-locations`` or ``\--exclude-locations`` flags to specify allowed list of locations or excluded list of locations. The following command updates storage intelligence plan of sub-folder `123456` with the specified list of included locations., 
    
    
    gcloud storage intelligence-configs enable --sub-folder=123456 --include-locations="us-east1","us-west1"

The following command enables storage intelligence with Trial edition for the given project, 
    
    
    gcloud storage intelligence-configs enable --project=my-project --trial-edition

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--organization`=`ORGANIZATION`
     Specifies organization id for the storage intelligence config. 
`--project`=`PROJECT`
     Specifies project for the storage intelligence config. 
`--sub-folder`=`SUB_FOLDER`
     Specifies sub-folder id for the storage intelligence config. 
SETTINGS FLAGS
    

`--trial-edition`
     Enables Storage Intelligence for TRIAL edition. 
At most one of these can be specified: 

`--exclude-bucket-id-regexes`=[`EXCLUDE_BUCKET_ID_REGEXES`,…]
     Sets filter for bucket id regexes to exclude. Accepts list of bucket id regexes in comma separated format. If the regex contains special characters that may have a specific meaning in the shell, escape them using backslashes(\\). To clear bucket id regexes list, provide flag with an empty list. e.g `--exclude-bucket-id-regexes=""` or `--exclude-bucket-id-regexes=` . 
`--include-bucket-id-regexes`=[`INCLUDE_BUCKET_ID_REGEXES`,…]
     Sets filter for bucket id regexes to include. Accepts list of bucket id regexes in comma separated format. If the regex contains special characters that may have a specific meaning in the shell, escape them using backslashes(\\). To clear bucket id regexes list, provide flag with empty list. e.g `--include-bucket-id-regexes=""` or `--include-bucket-id-regexes=` . 
At most one of these can be specified: 

`--exclude-locations`=[`EXCLUDE_LOCATIONS`,…]
     Comma separated list of [locations](https://cloud.google.com/storage/docs/locations#available-locations) to exclude in storage intelligence filter. To clear excluded locations, provide flag with empty list. e.g `--exclude-locations=""` or `--exclude-locations=` . 
`--include-locations`=[`INCLUDE_LOCATIONS`,…]
     Comma separated list of [locations](https://cloud.google.com/storage/docs/locations#available-locations) to include in storage intelligence filter. To clear included locations, provide flag with empty list. e.g `--include-locations=""` or `--include-locations=` . 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha storage intelligence-configs enable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/intelligence-configs/enable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
