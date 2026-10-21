---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/device-run/sessions/submit/android-executable/
title: gcloud alpha device-run sessions submit android-executable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:31.960213+00:00
---

# gcloud alpha device-run sessions submit android-executable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/device-run/sessions/submit/android-executable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha device-run sessions submit android-executable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha device-run sessions submit android-executable - submit a Device Run session with an Android executable job 
SYNOPSIS
    

`gcloud alpha device-run sessions submit android-executable` `--device`=[`DEVICE`,…] `--executable`=`EXECUTABLE_PATH` [`--async`] [`--bucket-name`=`BUCKET_NAME`] [`--bugreport`=`BUGREPORT`] [`--coordinates`=`LATITUDE`,`LONGITUDE`] [`--dumpsys`=`DUMPSYS`] [`--executable-args`=[`ARG`,…]] [`--executable-env-vars`=[`KEY`=`VALUE`,…]] [`--executable-timeout`=`EXECUTABLE_TIMEOUT`] [`--flaky-test-attempts`=`FLAKY_TEST_ATTEMPTS`] [`--labels`=[`KEY`=`VALUE`,…]] [`--locale`=`LOCALE`] [`--location`=`LOCATION`] [`--orientation`=`ORIENTATION`] [`--other-files-to-push`=[`SOURCE`=`DEST`,…]] [`--paths-to-pull`=[`DEVICE_PATH`,…]] [`--video`=`VIDEO`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Submit a Device Run session with an Android executable job. 
EXAMPLES
     To submit an Android executable session on a device with ID `my-device-id`, run: 
    
    
    gcloud alpha device-run sessions submit android-executable --device=my-device-id --executable=gs://my-bucket/my_executable --executable-args="--flag1=value1,--flag2=value2" --bucket-name=my-bucket

To submit an Android executable session asynchronously without waiting for it to complete, run: 
    
    
    gcloud alpha device-run sessions submit android-executable --device=my-device-id --executable=gs://my-bucket/my_executable --bucket-name=my-bucket --async

REQUIRED FLAGS
    

`--device`=[`DEVICE`,…]
     Id of the device type to run the executable on. Can be repeated to specify multiple device types. A job will be created for each specified device type. 
`--executable`=`EXECUTABLE_PATH`
     The path to the Android executable to run. Supports both Google Cloud Storage (`gs://…`) paths and local filesystem paths. Any local file will be uploaded to Google Cloud Storage prior to execution. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bucket-name`=`BUCKET_NAME`
     The name of a Google Cloud Storage bucket to store artifacts, including local input files and output files. If not specified, a default bucket named `gs://[PROJECT_ID]-devicerun` will be used or created. 

A bucket named explicitly with this flag must already exist; only the default bucket is created automatically. This flag accepts a bucket name only, without a `gs://` scheme or a path. 

Logcat collection is enabled by default for every job, so each execution directory always contains a `logcat.txt` file with the device-wide Android system log. This is different from `output.log`, which only captures the standard output and standard error written by your own executable. 

The Google Cloud Storage bucket layout will be structured as follows: 

  * gs://{bucket-name}/automation/ 
    * inputs/ 
      * 2026-05-29_10:13.026220_JZTM/ 
        * my_executable 
        * … 
    * sessions/ 
      * my-session-id1/ 
        * job-000/ 
          * execution-000/ 
            * logcat.txt 
            * output.log 
            * … 


`--bugreport`=`BUGREPORT`
     Specify when to collect bugreport from the device. `BUGREPORT` must be one of: `always`, `on-failure`. 
`--coordinates`=`LATITUDE`,`LONGITUDE`
     Specify the mock location coordinates (latitude and longitude) to set on the device before running the test. The format is latitude,longitude (e.g., 37.4220,-122.0841). Latitude must be in the range [-90.0, 90.0] and longitude must be in the range [-180.0, 180.0]. 
`--dumpsys`=`DUMPSYS`
     Specify when to collect dumpsys logs from the device. `DUMPSYS` must be one of: `always`, `on-failure`. 
`--executable-args`=[`ARG`,…]
     Arguments to pass to the executable when executing on the device. Can be specified as a comma-separated list or by repeating the flag. Each element becomes one argument, so a space-separated command line must be rewritten in comma-separated form, for example `--executable-args="--input=a.tflite,--threads=4"`. To pass an argument that itself contains a comma, prefix the value with `^SEP^` to choose a different separator, for example `--executable-args="^;^--shape=1,224,224,3;--threads=4"`. 
`--executable-env-vars`=[`KEY`=`VALUE`,…]
     A dictionary of environment variables to set for the executable process on the device. 
`--executable-timeout`=`EXECUTABLE_TIMEOUT`
     Specify the maximum duration allowed for the executable to run (e.g., `10m`, `15m`, `1h`). The valid range is `1m` to `3h`. If not specified, defaults to `5m`. It does not include any time necessary to prepare and clean up the target device. 
`--flaky-test-attempts`=`FLAKY_TEST_ATTEMPTS`
     Specify the maximum number of execution attempts per job to handle flakiness. If not specified, defaults to 1. 
`--labels`=[`KEY`=`VALUE`,…]
     A dictionary of user-defined key-value labels to attach to the session. 
`--locale`=`LOCALE`
     Locale code to set on the device for the execution. 
Location resource - Location to submit session. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
    * The default is `global` with a fully specified name; 
      * provide the argument `--project` on the command line; 
        * set the property `core/project`. 


`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line; 
    * The default is `global`. 


`--orientation`=`ORIENTATION`
     Orientation of the device for the execution. `ORIENTATION` must be one of: `portrait`, `landscape`. 
`--other-files-to-push`=[`SOURCE`=`DEST`,…]
     A dictionary of additional files to be pushed to the device before running the executable. The key is the source path of the file (supports both Google Cloud Storage and local paths; local files will be uploaded to Google Cloud Storage prior to execution), and the value is the destination path on the device. 
`--paths-to-pull`=[`DEVICE_PATH`,…]
     A list of file or directory paths to pull from the device following execution completion. 
`--video`=`VIDEO`
     Specify when to record video of the device screen during the run. Accepted values are `always` or `on-failure`. `VIDEO` must be one of: `always`, `on-failure`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta device-run sessions submit android-executable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run/sessions/submit/android-executable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
