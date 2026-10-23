---
url: https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument/
title: Developer Device Platform Device Run for Android Instrumentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:49.772851+00:00
---

# Developer Device Platform Device Run for Android Instrumentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Developer Device Platform Device Run for Android Instrumentation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to run an Android instrumentation test using the `gcloud beta device-run` CLI and find your results in Google Cloud console. It assumes you have a Google Cloud account and project.

If you are migrating from [Firebase Test Lab](https://firebase.google.com/docs/test-lab) to Developer Device Platform, see our [migration guide](https://docs.cloud.google.com/developer-device-platform/migrate), [command and flag translation](https://docs.cloud.google.com/developer-device-platform/migrate/flag-command-translation), and [migration skill](https://docs.cloud.google.com/developer-device-platform/migrate/migration-skill) for AI agents.

To use this Google Cloud CLI, you will need to provide your Google Cloud project ID. See [`gcloud beta device-run`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run) for a summary of commands.

## Before you begin

These steps assume that you have already:

  1. Created a Google Cloud project.
  2. Set up Developer Device Platform following the [Quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart).
  3. Authenticated with `gcloud` in the terminal.
  4. Reviewed the [Device Run overview](https://docs.cloud.google.com/developer-device-platform/device-run) for general information.
  5. [Built an instrumented test](https://developer.android.com/training/testing/instrumented-tests) for Android.



## Step 1. Configure your test run

**Tip:** To view all available options for the `submit` commands, run `gcloud beta device-run sessions submit instrumentation --help`.

### Options for Android instrumentation tests

  * _Multiple devices_ : To run the same test across multiple devices, provide the `--device` flag with multiple device IDs separated by commas, such as `--device shiba-34,tokay-36`, or with multiple `--device` flags, each specifying a distinct device ID (for example, `--device shiba-34 --device tokay-36`).
  * _Push files to device_ : Push additional files (such as ML model weights, test inputs, or `.so` shared libraries) to the device before execution using `--other-files-to-push=SOURCE=DEST,...`. `SOURCE` supports both local paths and Cloud Storage (`gs://...`) paths, and `DEST` is the destination path on the device.
  * _Pull files from device_ : Pull generated files or directories from the device after execution completes using `--paths-to-pull=DEVICE_PATH,...`.
  * _Custom Cloud Storage bucket_ : Specify an existing Cloud Storage bucket name (without a `gs://` scheme or path) using `--bucket-name=`. If you don't specify a bucket, the Google Cloud CLI uses or creates a default bucket named `PROJECT_ID-devicerun`.
  * _Flaky test retries_ : Set the maximum number of attempts per job or shard to handle flakiness: `--flaky-test-attempts=3` (defaults to `1` attempt).
  * _Device environment and diagnostics_ : Configure device orientation (`--orientation=portrait` or `landscape`), locale (`--locale=en-US`), mock GPS location (`--coordinates=LATITUDE,LONGITUDE`), screen video recording (`--video=always` or `on-failure`), `dumpsys` collection (`--dumpsys=always` or `on-failure`), or `bugreport` collection (`--bugreport=always` or `on-failure`).
  * _Labels_ : Attach user-defined key-value labels to the session using `--labels=KEY=VALUE,...`.
  * _Additional apps_ : You can optionally specify one or more APKs, AABs, or APKS files to install prior to running your tests using the `--apps=path1,path2,...,path_n` flag. The order you specify is the order in which these apps are installed.
  * _Test timeout_ : Limit the execution duration: `--instrumentation-timeout=10m` (valid range is `1m` to `3h` and defaults to `5m`).



### Synchronous and asynchronous runs

By default, the submit command is **blocking (synchronous)**. It will wait for the test to complete and print a summary table of the results.

To submit the session and return immediately after uploading files to Cloud Storage, add the `--async` flag:
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device shiba-35 \
      --test ./ANDROID_TESTS.apk \
      --async
    

This returns a session ID immediately. You can then wait for it using the `sessions wait` command:
    
    
    gcloud beta device-run sessions wait SESSION_ID
    

The command will block until the job is completed.

### Multiple devices

To run the same test across multiple devices, provide the `--device` flag with multiple device IDs separated by commas or with multiple `--device` flags, each specifying a distinct device ID:
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device shiba-34,tokay-36 \
      --test ./ANDROID_TESTS.apk
    

Or:
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device shiba-34 \
      --device tokay-36 \
      --test ./ANDROID_TESTS.apk
    

### Test timeout

Limit the execution duration of your test:
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device shiba-35 \
      --test ./ANDROID_TESTS.apk \
      --instrumentation-timeout=10m
    

The valid range is `1m` to `3h` and defaults to `5m`.

### Software versions

Discover and use available software packages and versions of [AndroidX Test Orchestrator](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#use-android) and inspect their lifecycles, supported versions, and metadata before configuring test runs.

First, list all available software packages and their versions:
    
    
    gcloud beta device-run software-versions list
    

Receiving output resembling:
    
    
    ID                                NAME                              SOFTWARE_TYPE               VERSION  STATE   IS_DEFAULT
    androidx-test-orchestrator-1-4-1  AndroidX Test Orchestrator 1.4.1  ANDROIDX_TEST_ORCHESTRATOR  1.4.1    ACTIVE  True
    androidx-test-orchestrator-1-6-1  AndroidX Test Orchestrator 1.6.1  ANDROIDX_TEST_ORCHESTRATOR  1.6.1    ACTIVE
    xcode-16-4                        Xcode 16.4                        XCODE                       16.4     ACTIVE
    xcode-26-2                        Xcode 26.2                        XCODE                       26.2     ACTIVE  True
    

Then describe a specific package _using its exact resource ID_ from the list:
    
    
    gcloud beta device-run software-versions describe androidx-test-orchestrator-1-4-1
    

Receiving output resembling:
    
    
    id: androidx-test-orchestrator-1-4-1
    isDefault: true
    lifecycle:
      state: ACTIVE
    name: AndroidX Test Orchestrator 1.4.1
    softwareType: ANDROIDX_TEST_ORCHESTRATOR
    version: 1.4.1
    

Now that you know which software versions are available, you can use them in your test runs with the `--orchestrator-version` flag, like so:
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device shiba-35 \
      --test ./ANDROID_TESTS.apk \
      --orchestrator-version=1.4.1
    

### Enable Orchestrator

Developer Device Platform supports [Android Test Orchestrator](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#use-android), which lets you run each of your app's tests within its own invocation of `Instrumentation`.

When you use Orchestrator, you:

  * _Avoid shared state_. Each test runs in its own `Instrumentation` instance. So if your tests share app state, most of that shared state is removed from your device's CPU or memory after each test. To remove all shared state from your device's CPU and memory after each test, include the `clearPackageData` setting like so: `--additional-test-options clearPackageData=true`

  * _Isolate crashes_. If one test crashes, it takes down only its own instance of `Instrumentation`. This means your other tests still run and provide complete test results.




Android Test Orchestrator is off by default in Developer Device Platform. To both enable the Orchestrator and specify its version to use during test execution, pass the version you selected to the `--orchestrator-version=ORCHESTRATOR_VERSION` flag in your `sessions submit instrumentation` command, like so:
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device shiba-35 \
      --test ./ANDROID_TESTS.apk \
      --orchestrator-version=1.4.1
    

Set the flag to `auto` to use the system-default Orchestrator version.

**Note:** Since each Orchestrator test runs its own `Instrumentation` instance, the increased run times might grow your quota usage or billed time and cause you to exceed your devices' timeout limits. You may need to increase your instrumentation timeout setting with the `--instrumentation-timeout` flag accordingly.

## Step 2. Choose devices

Using the `device-run` CLI, Android tests can be run across available physical and virtual devices. To view the complete list of available devices, visit either the interactive [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog#available-devices) or run:
    
    
    gcloud beta device-run devices list
    

Example output:
    
    
    ID        MAKE    NAME     MODEL FORM      OS_VERSION CAPACITY  AVAILABILITY  PRODUCTS
    tegu-35   Google  Pixel 9a tegu  PHYSICAL  35         MEDIUM    LOW           Automation, Streaming
    tokay-34  Google  Pixel 9  tokay PHYSICAL  34         HIGH      HIGH          Automation, Streaming
    

See the [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog#filter-devices) to learn how to filter this list. To target a specific device for your execution, use its corresponding ID (for example, `tegu-35`) in the submit command.

## Step 3. Run your test

Submit an Android instrumentation test APK.

These flags are required for Android instrumentation tests:

  * _Device_ : Specify a device using `--device`: `--device shiba-35`
  * _Test_ : Specify the test APK using `--test`: `--test /path/to/test.apk`



To run your instrumentation test, issue a [`sessions submit instrumentation`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run/sessions/submit/instrumentation) command resembling the following, using your own device IDs and test path:
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device shiba-34 \
      --apps /path/to/app.apk \
      --test /path/to/test.apk
    

The job's result report folder can be found at a Cloud Storage path such as `gs://BUCKET_NAME/automation/sessions/SESSION_ID/`. See the command output for the link, resembling: `https://console.cloud.google.com/storage/browser/BUCKET_NAME/automation/sessions/SESSION_ID/`.

## Step 4. Use sharding

To include Developer Device Platform instrumentation tests in a Continuous Integration and Continuous Delivery (CI/CD) workflow, you should consider sharding your tests. Test sharding divides a set of instrumentation tests into sub-groups (shards) that run separately in isolation. Developer Device Platform automatically runs each shard in parallel using multiple devices, and completes the entire set of tests in less time.

**Caution:** Sharding tests may cost more. Although test sharding reduces the time it takes for all your tests to run, the overhead of starting your app on each shard may increase individual device times.

### Step 4.1. Choosing sharding option

If your jobs have only a small numbers of test cases, or the total execution time of all test cases is not long, it is not necessary to use sharding. If you have a large number of test cases, or the total execution time of all their test cases is long, consider using sharding.

Developer Device Platform supports both smart and uniform sharding. When deciding how to shard your tests, consider the following options:

  * If all test cases will take a similar amount of time, use uniform sharding by dividing all test cases into `n` shards.

  * When the execution time of different test cases varies greatly, use smart sharding. Developer Device Platform uses historical test execution time to create different shards and attempts to complete all shards in a similar duration.


**Note:** The number of shards is configurable, so when Developer Device Platform runs many shards in parallel, test runs could be bottlenecked at the availability of devices. For this reason, we recommend the number of devices specified in the `--device` flag be less than or equal to the number of shards.

### Uniform sharding

To shard your tests with uniform sharding, include the `--sharding-option=uniform` and `--uniform-sharding-count=` flags in the `sessions submit instrumentation` command like so:
    
    
    gcloud beta device-run sessions submit instrumentation \
        --test path/to/test.apk \
     --device shiba-34,tokay-36 \
        --sharding-option=uniform \
        --uniform-sharding-count=2
    

You should see output indicating `Job status: 2 running`. The service creates two jobs, one for each device. Because the inputs to both jobs are identical, the service centralizes validation, performing them only once.

Your will see the two jobs listed separately in the final output of the command when complete:
    
    
    JOB NAME  EXECUTION NAME  EXECUTION RESULT
    job-000   execution-000   PASSED
    job-001   execution-000   PASSED
    

### Smart sharding

To shard your tests with smart sharding, include the `--sharding-option=smart`, `--smart-sharding-max-shard-count=`, `--smart-sharding-target-duration=` (in minutes or 1h), and `--smart-sharding-record-name=` flags in the `sessions submit instrumentation` command like so:
    
    
    gcloud beta device-run sessions submit instrumentation \
        --test path/to/test.apk \
        --device shiba-34,shiba-35,tokay-36 \
        --sharding-option=smart \
        --smart-sharding-max-shard-count=3 \
        --smart-sharding-target-duration=5m \
        --smart-sharding-record-name=test.yaml
    

You should see final output indicating three jobs ran:
    
    
    Session [session-3cd0564a] finished with result [ERROR].
    JOB NAME  EXECUTION NAME  EXECUTION RESULT
    job-000   execution-000   PASSED
    job-001   execution-000   PASSED
    job-002   execution-000   PASSED
    

Here is a summary of the smart sharding flags used here:

  * `--smart-sharding-max-shard-count=SMART_SHARDING_MAX_SHARD_COUNT` \- Specify the maximum number of shards to create for smart sharding. If unset or set to 0, system-defined max limits are used. The valid range is 0 to 20 for physical devices and 0 to 200 for virtual devices.

  * `--smart-sharding-target-duration=SMART_SHARDING_TARGET_DURATION` \- Specify the targeted execution time (e.g., 2m, 10m, 1h) per shard for smart sharding. The valid range is 2m to 1h. Required when `--sharding-option=smart`.

  * `--smart-sharding-record-name=SMART_SHARDING_RECORD_NAME` \- Specify the name of the smart sharding record file, excluding the file extension. Required when --sharding-option=smart. This YAML file is located in the Google Cloud Storage bucket specified by `--bucket-name` under the `smart-sharding/` directory. If the file does not exist, it will be created automatically; otherwise, its contents will be updated upon session completion.




## Step 5. Explore and manage your test run

For both async and sync mode of the `sessions submit instrumentation` command, you can use the `sessions describe` command to query the job status during the execution, or get the result after it is completed:
    
    
    gcloud beta device-run sessions describe SESSION_ID
    

The output summarizes test results and links to the results in Google Cloud console. For example:
    
    
    Session SESSION_ID finished with result [FAILED].
    Result files are stored at [https://console.cloud.google.com/storage/browser/BUCKET_NAME/automation/sessions/SESSION_ID/].
    JOB NAME  EXECUTION NAME  EXECUTION RESULT
    job-000   all             FAILED: 2 test cases failed, 5 passed
    

Use the following command to list all your running and completed sessions:
    
    
    gcloud beta device-run sessions list
    

Receive output containing the list of sessions in your project, resembling:
    
    
    SESSION_ID                                    START_TIME                STATE
    session-4825e153                              2026-07-28T16:38:43.155Z  DONE
    session-813ca602                              2026-07-28T22:40:32.415Z  DONE
    session-67cd0570                              2026-07-16T08:25:55.474Z  DONE
    session-17cc299c                              2026-07-14T14:31:33.649Z  DONE
    session-911d0763                              2026-07-09T00:39:02.051Z  DONE
    session-4e943fea                              2026-07-15T23:08:32.252Z  DONE
    session-0132e458                              2026-08-20T18:33:19.751Z  DONE
    session-1077f07b                              2026-07-28T22:35:43.848Z  DONE
    session-71b054c6                              2026-07-15T01:15:41.643Z  DONE
    session-4f8b2e45                              2026-08-06T23:11:56.161Z  DONE
    

The `sessions` list command supports all [standard Google Cloud CLI flag options](https://docs.cloud.google.com/sdk/gcloud/reference/functions/list). For example:
    
    
    gcloud beta device-run sessions list --limit 5
    

Which results in results resembling:
    
    
    SESSION_ID                            START_TIME                STATE
    session-4825e153                      2026-07-28T16:38:43.155Z  DONE
    session-813ca602                      2026-07-28T22:40:32.415Z  DONE
    93ec2df2-d5bf-4c36-b7f7-c2a4fb0dc3ce  2026-07-03T05:10:58.015Z  DONE
    session-67cd0570                      2026-07-16T08:25:55.474Z  DONE
    session-17cc299c                      2026-07-14T14:31:33.649Z  DONE
    

Or to find all running sessions, run:
    
    
    gcloud beta device-run sessions list --filter RUNNING
    

Assuming you have running sessions, you will see results resembling:
    
    
    SESSION_ID        START_TIME  STATE
    session-d7ff8b81              RUNNING
    

Else, you will receive `Listed 0 items.`

To cancel a running session, run this command with your session ID:
    
    
    gcloud beta device-run sessions cancel SESSION_ID
    

The command returns immediately, as the session is only marked to be cancelled. Cancellation happens asynchronously in the backend.

If the session is already finished, only the current status is printed. Requesting cancellation for a finished session is not an error.

## What's next

Next up, [run an Android executable](https://docs.cloud.google.com/developer-device-platform/device-run/android-executable) or [find and analyze logs](https://docs.cloud.google.com/developer-device-platform/device-run/find-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
