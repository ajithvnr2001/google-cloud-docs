---
url: https://docs.cloud.google.com/developer-device-platform/device-run/
title: Developer Device Platform Device Run Overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:55:35.339890+00:00
---

# Developer Device Platform Device Run Overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/device-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Developer Device Platform Device Run Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Welcome to Developer Device Platform Device Run, which lets you run tests and executables on physical and virtual Android devices and physical iOS devices in the cloud. This page summarizes capabilities and describes commonalities between running [Android instrumentation tests](https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument), [Android executables](https://docs.cloud.google.com/developer-device-platform/device-run/android-executable), and [iOS XCTest](https://docs.cloud.google.com/developer-device-platform/device-run/ios) tests.

If you are migrating from [Firebase Test Lab](https://firebase.google.com/docs/test-lab) to Developer Device Platform, see our [migration guide](https://docs.cloud.google.com/developer-device-platform/device-run/migrate), [command and flag translation](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation), and [migration skill](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/migration-skill) for AI agents.

To use this Google Cloud CLI, you will need to provide your Google Cloud project ID. For a summary of commands, see: [`gcloud beta device-run`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run)

**Tip:** Append `--help` to any `gcloud` command to see detailed usage information.

## Key capabilities

Developer Device Platform Device Run is a Google Cloud service that lets you execute automated test suites across physical and virtual mobile devices. Built for modern Continuous Integration and Continuous Delivery (CI/CD) workflows, Device Run offers command-line control through the Google Cloud CLI (`gcloud beta device-run`), allowing teams to run, manage, and scale test suites on dedicated hardware and virtual environments.

### 1\. Cross-platform automated testing

  * _Android and iOS support_ : Device Run supports built-in test frameworks, including _Android Instrumentation tests_ (`.apk`), **Android executables** (compiled binaries), and _iOS XCTests_ (`.ipa` or `.zip`).
  * _Flexible device targeting_ : Target specific physical or virtual devices listed in the [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-run/device-catalog) using OS and model identifiers (e.g., Pixel or iPhone models) via the `--device` flag.
  * _Multi-device parallel execution_ : Execute identical test suites concurrently across multiple devices by specifying comma-separated device IDs or supplying multiple `--device` flags.



### 2\. Flexible execution modes and controls

  * _Synchronous and asynchronous submissions_ : Test runs operate synchronously by default, displaying a summary upon completion. Adding the `--async` flag returns a session ID immediately for non-blocking execution, which can be monitored later using `gcloud beta device-run sessions wait`.
  * _Custom execution timeouts_ *: Configure execution duration limits with `--instrumentation-timeout` or `--xctest-timeout`.
  * _Flaky test retries_ : Set maximum retry attempts for flaky test executions using the `--flaky-test-attempts` flag.



### 3\. Software version and dependency management

  * _Configurable test environments_ *: Discover, inspect, and select specific software environment versions — such as _AndroidX Test Orchestrator_ and _Apple Xcode_ — prior to initiating test runs.
  * _Version discovery_ : Use `gcloud beta device-run software-versions list` and `describe` commands to view active software packages, supported OS versions, and default runtime specifications.



### 4\. Storage and artifact management

  * _Cloud Storage integration_ : Test inputs (APKs, IPAs, supporting apps) and output artifacts (logs, test reports) are stored in Cloud Storage.
  * _Bucket flexibility_ : Automatically defaults to a project bucket named `PROJECT_ID-devicerun` or routes to a custom bucket specified via the `--bucket-name` flag. You are in complete control of this bucket and will need to manually remove its contents when no longer needed or otherwise configure automated lifecycle management on the bucket. See [About object deletion](https://docs.cloud.google.com/storage/docs/object-deletion-overview) for instructions.
  * _Direct cloud paths_ : Reference existing `gs://` paths directly for large files to eliminate upload overhead.



### 5\. Advanced Android testing features

  * _Android Test Orchestrator_ : Isolate test execution by running each test in its own `Instrumentation` instance to prevent shared app state and isolate application crashes.
  * _Test Sharding_ : 
    * _Uniform Sharding_ : Evenly splits test cases across a specified number of shards (`--sharding-option=uniform`).
    * _Smart Sharding_ : Uses historical test execution data to balance test cases dynamically across shards, targeting a specific total execution duration (`--sharding-option=smart`).



### 6\. Session management and diagnostics

  * _Full session control_ : List, describe, filter, or cancel active or historic test runs using `sessions list`, `sessions describe`, and `sessions cancel`.
  * _Early input validation_ : Performs automatic validation on submitted test binaries and configuration artifacts, surfacing explicit error details and root causes (such as target package mismatches) when errors occur.



## Core settings

### Required flags

Note these flags are required:

  * _Device_ : Specify a device using `--device`: `--device shiba-35` or `--device iphonese3-18-4`
  * _Test_ or _executable_ : Specify the test package using `--test` (`--test /path/to/test.apk` or `--test /path/to/MyTests.zip`) for test runs, or specify the executable binary or script using `--executable` (`--executable /path/to/my_executable`) for Android executable runs.



The following configuration options are common across Device Run sessions.

### Input and output Cloud Storage paths

  * _Custom Cloud Storage bucket_ : You can specify a custom Cloud Storage bucket for inputs and outputs: `--bucket-name=my-custom-bucket` If you don't specify a Cloud Storage bucket using the `--bucket-name=` flag, the Google Cloud CLI will use a default bucket named `PROJECT_ID-devicerun`.
  * _Input files_ : When you specify a local path with the `--test`, `--executable`, `--apps`, `--additional-apps`, `--other-files-to-push`, or `--xctestrun-file` flags, the Google Cloud CLI automatically copies it to your Cloud Storage bucket under `gs://BUCKET_NAME/automation/inputs/DATE_TIME_FOUR_CHARS_SUFFIX/` each time you execute the command, where `BUCKET_NAME` defaults to `PROJECT_ID-devicerun`.
  * _Cloud paths_ : Because uploading large files can be time-consuming, you can directly reference them using their Cloud Storage `gs://` paths to save upload time.
  * _Result files_ : Output artifacts are uploaded to your Cloud Storage bucket under `gs://BUCKET_NAME/automation/sessions/session-[SESSION_ID]/`.



### Input validation

Developer Device Platform attempts to validate your inputs, including artifacts, and returns an `ERROR` rather than `PASSED` or `FAILED` when encountering erroneous input:
    
    
    Session [session-94b57778] finished with result [ERROR].
    JOB NAME  EXECUTION NAME  EXECUTION RESULT
    job-000   execution-000   ERROR
    

Now append `--full` to the `sessions describe` command to see more details about the session:
    
    
    gcloud beta device-run sessions describe --full session-94b57778
    

Which results in output resembling:
    
    
    name: projects/user-test1/locations/global/sessions/session-94b57778
    sessionConfig:
      displayName: instrumentation-session
      jobConfigs:
      -   action:
          androidInstrumentationTest:
            testInstallable:
              files:
              -   gcsInputFile:
                  path: gs://user-test1-devicerun/automation/inputs/2026-09-16_18:55.17372947_EECF/my-test.apk
        allocationConfig:
          deviceConfigs:
          -   actions:
            -   androidLogcat: {}
            requirement:
              deviceId: mediumphone-arm-34
        displayName: job-000
      outputDirectoryConfig:
        gcsOutputDirectory:
          path: gs://user-test1-devicerun/automation/sessions
    sessionReport:
      endTime: '2026-09-16T18:55:49.721Z'
      id: ed681f23-669b-4464-8a93-b28456e58136
      jobReports:
      -   displayName: job-000
        endTime: '2026-09-16T18:55:45.839Z'
        executionReports:
        -   displayName: execution-000
          endTime: '2026-09-16T18:55:46.694Z'
          id: ce370173-af94-4dd7-acc6-0863e4d2e9ec
          result:
            cause:
              summary:
                message: The instrumentation target package does not match any of the
                  installable packages.
                reason: INSTRUMENTATION_TARGET_MISMATCH
                type: CUSTOMER
            resultType: ERROR
          startTime: '1970-01-01T00:00:00Z'
          status:
            statusType: PENDING
        id: 953b5106-3c20-40f0-aceb-18af89cd1b83
        result:
          cause:
            summary:
              message: The instrumentation target package does not match any of the installable
                packages.
              reason: INSTRUMENTATION_TARGET_MISMATCH
              type: CUSTOMER
          resultType: ERROR
        startTime: '2026-09-16T18:55:31.651Z'
        status:
          statusType: DONE
      result:
        resultType: ERROR
      startTime: '2026-09-16T18:55:24.442Z'
      status:
        statusType: DONE
    

## What's next

[Run an Android instrumentation test](https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument), an [Android executable](https://docs.cloud.google.com/developer-device-platform/device-run/android-executable) or an [iOS XCTest](https://docs.cloud.google.com/developer-device-platform/device-run/ios) with Developer Device Platform.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
