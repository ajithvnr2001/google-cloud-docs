---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/device-run/sessions/submit/xctest/
title: gcloud alpha device-run sessions submit xctest \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:31.486261+00:00
---

# gcloud alpha device-run sessions submit xctest  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/device-run/sessions/submit/xctest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha device-run sessions submit xctest Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha device-run sessions submit xctest - submit a Device Run session with an iOS XCTest job 
SYNOPSIS
    

`gcloud alpha device-run sessions submit xctest` `--device`=[`DEVICE`,…] `--test`=`TEST_PATH` [`--additional-apps`=[`APP_PATH`,…]] [`--async`] [`--bucket-name`=`BUCKET_NAME`] [`--flaky-test-attempts`=`FLAKY_TEST_ATTEMPTS`] [`--labels`=[`KEY`=`VALUE`,…]] [`--locale`=`LOCALE`] [`--location`=`LOCATION`] [`--other-files-to-push`=[`SOURCE`=`BUNDLE_ID`:`DEST`,…]] [`--paths-to-pull`=[`BUNDLE_ID`:`DEVICE_PATH`,…]] [`--xcode-version`=`XCODE_VERSION`] [`--xctest-timeout`=`XCTEST_TIMEOUT`] [`--xctestrun-file`=`XCTESTRUN_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Submit a Device Run session with an iOS XCTest job. 
EXAMPLES
     To submit an XCTest session on an iPhone 16 Pro, run: 
    
    
    gcloud alpha device-run sessions submit xctest --device=iphone16pro-18-3 --test=gs://my-bucket/SmokeTests.zip --bucket-name=my-bucket

To submit an XCTest session asynchronously without waiting for it to complete, run: 
    
    
    gcloud alpha device-run sessions submit xctest --device=iphone16pro-18-3 --test=gs://my-bucket/SmokeTests.zip --bucket-name=my-bucket --async

REQUIRED FLAGS
    

`--device`=[`DEVICE`,…]
     Id of the device type to run the test on. Can be repeated to specify multiple device types. A job will be created for each specified device type. 
`--test`=`TEST_PATH`
     The path to the .zip file containing the iOS app and XCTest files. Supports both Google Cloud Storage (`gs://…`) paths and local filesystem paths. Any local file will be uploaded to Google Cloud Storage prior to test execution. 
OPTIONAL FLAGS
    

`--additional-apps`=[`APP_PATH`,…]
     A list of additional application binary files (.ipa) to install before running the test. The order of the applications in the list determines their installation order on the device. Supports both Google Cloud Storage (`gs://…`) paths and local filesystem paths. Any local file will be uploaded to Google Cloud Storage prior to test execution. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bucket-name`=`BUCKET_NAME`
     The name of a Google Cloud Storage bucket to store test artifacts, including local input files and test output files. If not specified, a default bucket named `gs://[PROJECT_ID]-devicerun` will be used or created. 
`--flaky-test-attempts`=`FLAKY_TEST_ATTEMPTS`
     Specify the maximum number of execution attempts per job to handle flakiness. If not specified, defaults to 1. 
`--labels`=[`KEY`=`VALUE`,…]
     A dictionary of user-defined key-value labels to attach to the session. 
`--locale`=`LOCALE`
     Specify the locale (language and region) to switch the iOS application to before running the test. The format is `language-region`, e.g., `en-US` or `zh-CN`. The typical language value is a two- or three-letter language code as defined in ISO 639. The typical region value is a two-letter ISO 3166 code or a three-digit UN M.49 area code. 
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


`--other-files-to-push`=[`SOURCE`=`BUNDLE_ID`:`DEST`,…]
     A dictionary of additional files to be pushed to the device before running the test. The key is the source path of the file (supports both Google Cloud Storage and local paths; local files will be uploaded to Google Cloud Storage prior to test execution), and the value is the destination path in the format BUNDLE_ID:DEVICE_PATH. 
`--paths-to-pull`=[`BUNDLE_ID`:`DEVICE_PATH`,…]
     A list of file or directory paths to pull from the device following test completion, in the format BUNDLE_ID:DEVICE_PATH. 
`--xcode-version`=`XCODE_VERSION`
     The catalog ID or version string of the Xcode version to use for the test run (e.g. `xcode-16-4` or `16.4`). If not specified, a system default Xcode version is used. Available versions can be queried using `gcloud device-run catalog software-versions list`. 
`--xctest-timeout`=`XCTEST_TIMEOUT`
     Specify the maximum duration allowed for the XCTest run (e.g., `10m`, `15m`, `1h`). The valid range is `1m` to `1h`. If not specified, defaults to `5m`. It does not include any time necessary to prepare and clean up the target device. 
`--xctestrun-file`=`XCTESTRUN_FILE`
     The path to the custom .xctestrun file. Supports both Google Cloud Storage (`gs://…`) paths and local filesystem paths. Any local file will be uploaded to Google Cloud Storage prior to test execution. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
