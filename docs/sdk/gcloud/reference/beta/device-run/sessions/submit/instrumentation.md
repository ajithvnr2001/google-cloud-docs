---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run/sessions/submit/instrumentation/
title: gcloud beta device-run sessions submit instrumentation \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:33.139878+00:00
---

# gcloud beta device-run sessions submit instrumentation  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run/sessions/submit/instrumentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta device-run sessions submit instrumentation Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta device-run sessions submit instrumentation - submit a Device Run session with an instrumentation job 
SYNOPSIS
    

`gcloud beta device-run sessions submit instrumentation` `--device`=[`DEVICE`,…] `--test`=`TEST_PATH` [`--additional-test-options`=[`KEY`=`VALUE`,…]] [`--apps`=[`APP_PATH`,…]] [`--async`] [`--bucket-name`=`BUCKET_NAME`] [`--bugreport`=`BUGREPORT`] [`--coordinates`=`LATITUDE`,`LONGITUDE`] [`--dumpsys`=`DUMPSYS`] [`--flaky-test-attempts`=`FLAKY_TEST_ATTEMPTS`] [`--[no-]flaky-test-parallel-retry`] [`--flaky-test-retry-level`=`FLAKY_TEST_RETRY_LEVEL`] [`--instrumentation-timeout`=`INSTRUMENTATION_TIMEOUT`] [`--labels`=[`KEY`=`VALUE`,…]] [`--locale`=`LOCALE`] [`--location`=`LOCATION`] [`--orchestrator-version`=`ORCHESTRATOR_VERSION`] [`--orientation`=`ORIENTATION`] [`--other-files-to-push`=[`SOURCE`=`DEST`,…]] [`--paths-to-pull`=[`DEVICE_PATH`,…]] [`--sharding-option`=`SHARDING_OPTION`] [`--smart-sharding-max-shard-count`=`SMART_SHARDING_MAX_SHARD_COUNT`] [`--smart-sharding-record-name`=`SMART_SHARDING_RECORD_NAME`] [`--smart-sharding-target-duration`=`SMART_SHARDING_TARGET_DURATION`] [`--test-runner-class`=`TEST_RUNNER_CLASS`] [`--test-targets`=[`KEY`=`VALUE`,…]] [`--uniform-sharding-count`=`UNIFORM_SHARDING_COUNT`] [`--video`=`VIDEO`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Submit a Device Run session with an instrumentation job. 
EXAMPLES
     To submit an instrumentation session in location `us-central1` on a device with ID `my-device-id`, run: 
    
    
    gcloud beta device-run sessions submit instrumentation --location=us-central1 --device=my-device-id --apps=gs://my-bucket/app.apk --test=gs://my-bucket/test.apk --bucket-name=my-bucket

To submit an instrumentation session asynchronously without waiting for it to complete, run: 
    
    
    gcloud beta device-run sessions submit instrumentation --location=us-central1 --device=my-device-id --apps=gs://my-bucket/app.apk --test=gs://my-bucket/test.apk --bucket-name=my-bucket --async

REQUIRED FLAGS
    

`--device`=[`DEVICE`,…]
     Id of the device type to run the test on. Can be repeated to specify multiple device types. A job will be created for each specified device type. 
`--test`=`TEST_PATH`
     The path to the APK file containing instrumentation tests. Supports both Google Cloud Storage (`gs://…`) paths and local filesystem paths. Any local file will be uploaded to Google Cloud Storage prior to test execution. 
OPTIONAL FLAGS
    

`--additional-test-options`=[`KEY`=`VALUE`,…]
     A dictionary of additional options to pass to the instrumentation test. Formats supported in test_targets are not allowed to be used here. 
`--apps`=[`APP_PATH`,…]
     A list of application binary files (.apk, .aab, or .apks) to install before running the test. The order of the applications in the list determines their installation order on the device. Supports both Google Cloud Storage (`gs://…`) paths and local filesystem paths. Any local file will be uploaded to Google Cloud Storage prior to test execution. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bucket-name`=`BUCKET_NAME`
     The name of a Google Cloud Storage bucket to store test artifacts, including local input files, test output files, and smart sharding timing records. If not specified, a default bucket named `gs://[PROJECT_ID]-devicerun` will be used or created. 

The Google Cloud Storage bucket layout will be structured as follows: 

  * gs://{bucket-name}/automation/ 
    * inputs/ 
      * 2026-05-29_10:13.026220_JZTM/ 
        * app-debug.apk 
        * app-debug-androidTest.apk 
    * sessions/ 
      * my-session-id1/ 
        * job-000/ 
          * execution-000/ 
            * junit.xml 
            * … 
          * execution-001/ 
            * junit.xml 
            * … 
          * merged_junit.xml 
      * my-session-id2/ 
        * … 
    * smart-sharding/ 
      * sharding-record-A.yaml 
      * sharding-record-B.yaml 


`--bugreport`=`BUGREPORT`
     Specify when to collect bugreport from the device. Accepted values are `always` or `on-failure`. `BUGREPORT` must be one of: `always`, `on-failure`. 
`--coordinates`=`LATITUDE`,`LONGITUDE`
     Specify the mock location coordinates (latitude and longitude) to set on the device before running the test. The format is latitude,longitude (e.g., 37.4220,-122.0841). Latitude must be in the range [-90.0, 90.0] and longitude must be in the range [-180.0, 180.0]. 
`--dumpsys`=`DUMPSYS`
     Specify when to collect dumpsys from the device. Accepted values are `always` or `on-failure`. `DUMPSYS` must be one of: `always`, `on-failure`. 
`--flaky-test-attempts`=`FLAKY_TEST_ATTEMPTS`
     Specify the maximum number of execution attempts per test shard to handle flakiness or infrastructure errors. If not specified, defaults to 1. 
`--[no-]flaky-test-parallel-retry`
     Whether to retry the test failures in parallel. By default, the test is retried sequentially. If true, when the initial attempt fails, (flaky-test-attempts - 1) attempts will be triggered at the same time to run in parallel. Use `--flaky-test-parallel-retry` to enable and `--no-flaky-test-parallel-retry` to disable. 
`--flaky-test-retry-level`=`FLAKY_TEST_RETRY_LEVEL`
     Specify the level to retry the test failures. By default, the test is retried at the shard level. Accepted values are `shard` or `test`. `FLAKY_TEST_RETRY_LEVEL` must be one of: `shard`, `test`. 
`--instrumentation-timeout`=`INSTRUMENTATION_TIMEOUT`
     Specify the maximum duration allowed for the instrumentation test run (e.g., `10m`, `20s`, `1h`). The valid range is `1m` to `3h`. If not specified, defaults to `5m`. 
`--labels`=[`KEY`=`VALUE`,…]
     A dictionary of user-defined key-value labels to attach to the session. 
`--locale`=`LOCALE`
     Specify the locale (language and region) to switch the device to before running the test. The format is `language-region`, e.g., `en-US` or `zh-CN`. The typical language value is a two- or three-letter language code as defined in ISO 639. The typical region value is a two-letter ISO 3166 code or a three-digit UN M.49 area code. 
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


`--orchestrator-version`=`ORCHESTRATOR_VERSION`
     Specify the version of the Android Test Orchestrator to use during test execution. If not specified, no orchestrator is used. Available versions can be found in the catalog, queryable with the command `gcloud device-run software-versions list`. If set to `auto`, the system-default orchestrator version is used. 
`--orientation`=`ORIENTATION`
     Specify the orientation to set the device to before running the test. Accepted values are `portrait` or `landscape`. `ORIENTATION` must be one of: `portrait`, `landscape`. 
`--other-files-to-push`=[`SOURCE`=`DEST`,…]
     A dictionary of additional files to be pushed to the device before running the test. The key is the source path of the file (supports both Google Cloud Storage and local paths; local files will be uploaded to Google Cloud Storage prior to test execution), and the value is the destination path on the device. 
`--paths-to-pull`=[`DEVICE_PATH`,…]
     A list of file or directory paths to pull from the device following test completion. 
`--sharding-option`=`SHARDING_OPTION`
     Specify the sharding strategy to partition the test execution across multiple device allocations. Accepted values are `uniform` or `smart`. `SHARDING_OPTION` must be one of: `uniform`, `smart`. 
`--smart-sharding-max-shard-count`=`SMART_SHARDING_MAX_SHARD_COUNT`
     Specify the maximum number of shards to create for smart sharding. If unset or set to 0, system-defined max limits are used. The valid range is `0` to `20` for physical devices and `0` to `200` for virtual devices. 
`--smart-sharding-record-name`=`SMART_SHARDING_RECORD_NAME`
     Specify the name of the smart sharding record file, excluding the file extension. Required when `--sharding-option=smart`. This file is located in the Google Cloud Storage bucket specified by `--bucket-name` under the `smart-sharding/` directory with a `.yaml` extension. If the file does not exist, it will be created automatically; otherwise, its contents will be updated upon session completion. 
`--smart-sharding-target-duration`=`SMART_SHARDING_TARGET_DURATION`
     Specify the targeted execution time (e.g., `2m`, `10m`, `1h`) per shard for smart sharding. The valid range is `2m` to `1h`. Required when `--sharding-option=smart`. 
`--test-runner-class`=`TEST_RUNNER_CLASS`
     The instrumentation test runner class to use. If not specified, a default runner class will be determined by examining the application's manifest. 
`--test-targets`=[`KEY`=`VALUE`,…]
     A list of test targets or target filters to run. Each target must be fully qualified with the package name or class name, in one of these formats: 

  * `package package_name`
    * `notPackage com.package.to.skip`
      * `class package_name.class_name`
        * `class package_name.class_name#method_name`
        * `notClass com.foo.ClassToSkip`
        * `notClass com.foo.ClassName#testMethodToSkip`
        * `annotation com.foo.AnnotationToRun`
        * `notAnnotation com.foo.AnnotationToSkip`
        * `size [small|medium|large]`

Formats like `testfile` or `notTestfile` won't be supported. If empty, all targets in the module will be run. 



`--uniform-sharding-count`=`UNIFORM_SHARDING_COUNT`
     Specify the total number of shards to create for uniform sharding. Required when `--sharding-option=uniform`. The valid range is `1` to `20` for physical devices and `1` to `200` for virtual devices. 
`--video`=`VIDEO`
     Specify when to record video of the device screen during the test run. Accepted values are `always` or `on-failure`. `VIDEO` must be one of: `always`, `on-failure`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha device-run sessions submit instrumentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/device-run/sessions/submit/instrumentation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
