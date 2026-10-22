---
url: https://docs.cloud.google.com/developer-device-platform/device-run/android-executable/
title: Developer Device Platform Device Run for Android Executables \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:30.707650+00:00
---

# Developer Device Platform Device Run for Android Executables  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/device-run/android-executable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Developer Device Platform Device Run for Android Executables Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to run a standalone Android executable using the `gcloud beta device-run` CLI and find your results in Google Cloud console. It assumes you have a Google Cloud account and project.

If you are migrating from [Firebase Test Lab](https://firebase.google.com/docs/test-lab) to Developer Device Platform, see our [migration guide](https://docs.cloud.google.com/developer-device-platform/device-run/migrate), [command and flag translation](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation), and [migration skill](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/migration-skill) for AI agents.

To use this Google Cloud CLI, you will need to provide your Google Cloud project ID. See [`gcloud beta device-run`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run) for a summary of commands.

## Before you begin

These steps assume that you have already:

  1. Created a Google Cloud project.
  2. Set up Developer Device Platform following the [Quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart).
  3. Authenticated with `gcloud` in the terminal.
  4. Reviewed the [Device Run overview](https://docs.cloud.google.com/developer-device-platform/device-run) for general information.
  5. Prepared a standalone Android executable (such as a compiled C++ binary, benchmark runner, or shell script).



## Step 1. Configure your executable run

**Tip:** To view all available options for the `submit` commands, run `gcloud beta device-run sessions submit android-executable --help`.

### Options for Android executables

  * _Multiple devices_ : To run the same executable across multiple devices, provide the `--device` flag with multiple device IDs separated by commas, such as `--device shiba-34,tokay-36`, or with multiple `--device` flags, each specifying a distinct device ID (for example, `--device shiba-34 --device tokay-36`).
  * _Push files to device_ : Push additional files (such as ML model weights, test inputs, or `.so` shared libraries) to the device before execution using `--other-files-to-push=SOURCE=DEST,...`. `SOURCE` supports both local paths and Cloud Storage (`gs://...`) paths, and `DEST` is the destination path on the device.
  * _Pull files from device_ : Pull generated files or directories from the device after execution completes using `--paths-to-pull=DEVICE_PATH,...`.
  * _Custom Cloud Storage bucket_ : Specify an existing Cloud Storage bucket name (without a `gs://` scheme or path) using `--bucket-name=`. If you don't specify a bucket, the Google Cloud CLI uses or creates a default bucket named `PROJECT_ID-devicerun`.
  * _Flaky test retries_ : Set the maximum number of attempts per job or shard to handle flakiness: `--flaky-test-attempts=3` (defaults to `1` attempt).
  * _Device environment and diagnostics_ : Configure device orientation (`--orientation=portrait` or `landscape`), locale (`--locale=en-US`), mock GPS location (`--coordinates=LATITUDE,LONGITUDE`), screen video recording (`--video=always` or `on-failure`), `dumpsys` collection (`--dumpsys=always` or `on-failure`), or `bugreport` collection (`--bugreport=always` or `on-failure`).
  * _Labels_ : Attach user-defined key-value labels to the session using `--labels=KEY=VALUE,...`.
  * _Executable arguments_ : Pass command-line arguments to the executable using `--executable-args=ARG,...` as a comma-separated list or by repeating the flag. Each element becomes one argument, so rewrite space-separated command lines in comma-separated form (for example, `--executable-args="--input=a.file,--threads=4"`). To pass an argument that itself contains a comma, prefix the value with `^SEP^` to specify a different separator (for example, `--executable-args="^;^--shape=1,224,224,3;--threads=4"`).
  * _Environment variables_ : Set environment variables for the executable process on the device using `--executable-env-vars=KEY=VALUE,...` (for example, `--executable-env-vars=LD_LIBRARY_PATH=/data/local/tmp/lib`).
  * _Executable timeout_ : Limit the execution duration of the executable: `--executable-timeout=10m` (valid range is `1m` to `3h` and defaults to `5m`, excluding device preparation and cleanup time).



### Synchronous and asynchronous runs

By default, the submit command is **blocking (synchronous)**. It will wait for the executable to complete and print a summary table of the results.

To submit the session and return immediately after uploading files to Cloud Storage, add the `--async` flag:
    
    
    gcloud beta device-run sessions submit android-executable \
      --device shiba-35 \
      --executable ./MY_EXECUTABLE \
      --async
    

This returns a session ID immediately. You can then wait for it using the `sessions wait` command:
    
    
    gcloud beta device-run sessions wait SESSION_ID
    

The command will block until the job is completed.

### Multiple devices

To run the same executable across multiple devices, provide the `--device` flag with multiple device IDs separated by commas or with multiple `--device` flags, each specifying a distinct device ID.
    
    
    gcloud beta device-run sessions submit android-executable \
      --device shiba-34,tokay-36 \
      --executable ./MY_EXECUTABLE
    

Or:
    
    
    gcloud beta device-run sessions submit android-executable \
      --device shiba-34 \
      --device tokay-36 \
      --executable ./MY_EXECUTABLE
    

### Executable timeout

Limit the duration of your executable run:
    
    
    gcloud beta device-run sessions submit android-executable \
      --device shiba-35 \
      --executable ./MY_EXECUTABLE \
      --executable-timeout=10m
    

The valid range is `1m` to `3h` for runs and defaults to `5m`.

## Step 2. Choose devices

Using the `device-run` CLI, Android executables can be run across available physical and virtual devices. To view the complete list of available devices, visit either the interactive [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog#available-devices) or run:
    
    
    gcloud beta device-run devices list
    

Example output:
    
    
    ID        MAKE    NAME     MODEL FORM      OS_VERSION CAPACITY  AVAILABILITY  PRODUCTS
    tegu-35   Google  Pixel 9a tegu  PHYSICAL  35         MEDIUM    LOW           Automation, Streaming
    tokay-34  Google  Pixel 9  tokay PHYSICAL  34         HIGH      HIGH          Automation, Streaming
    

See the [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog#filter-devices) to learn how to filter this list. To target a specific device for your execution, use its corresponding ID (for example, `tegu-35`) in the submit command.

## Step 3. Run your executable

Submit a standalone Android executable.

To run a standalone executable (such as a compiled C++ binary, on-device machine learning benchmark runner like LiteRT, or shell script) directly on an Android device without packaging it into an APK, use the [`sessions submit android-executable`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run/sessions/submit/android-executable) command.

These flags are required for Android executables:

  * _Device_ : Specify a device using `--device`: `--device shiba-35`
  * _Executable_ : Specify the local or Cloud Storage path to the executable using `--executable`: `--executable /path/to/my_executable`



To run your executable, issue a command resembling the following, using your own device IDs and executable path:
    
    
    gcloud beta device-run sessions submit android-executable \
      --device shiba-34 \
      --executable /path/to/my_executable \
      --executable-args="--input=/data/local/tmp/file.name,--threads=4" \
      --other-files-to-push=/path/to/model.tflite=/data/local/tmp/model.tflite \
      --paths-to-pull=/data/local/tmp/output
    

The job's result report folder can be found at a Cloud Storage path such as `gs://BUCKET_NAME/automation/sessions/SESSION_ID/`. See the command output for the link, resembling: `https://console.cloud.google.com/storage/browser/BUCKET_NAME/automation/sessions/SESSION_ID/`.

## Step 4. Explore and manage your executable run

For both async and sync mode of the `sessions submit android-executable` command, you can use the `sessions describe` command to query the job status during the execution, or get the result after it is completed:
    
    
    gcloud beta device-run sessions describe SESSION_ID
    

The output summarizes the execution results and links to the results in Google Cloud console. For example:
    
    
    Session SESSION_ID finished with result [FAILED].
    Result files are stored at [https://console.cloud.google.com/storage/browser/BUCKET_NAME/automation/sessions/SESSION_ID/].
    JOB NAME  EXECUTION NAME  EXECUTION RESULT
    job-000 all FAILED: 2 test cases failed, 5 passed
    

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

Next up, [run an Android instrumentation test](https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument) or [find and analyze logs](https://docs.cloud.google.com/developer-device-platform/device-run/find-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
