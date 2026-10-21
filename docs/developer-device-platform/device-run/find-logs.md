---
url: https://docs.cloud.google.com/developer-device-platform/device-run/find-logs/
title: Find your Developer Device Platform test results \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:46.409312+00:00
---

# Find your Developer Device Platform test results  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/device-run/find-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Find your Developer Device Platform test results Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to find the results of tests and executables triggered following the [Developer Device Platform Device Run](https://docs.cloud.google.com/developer-device-platform/device-run) guide.

## Before you begin

These steps assume that you have already created a Google Cloud project, completed the setup steps in the Developer Device Platform [Quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart) guide, and authenticated with `gcloud` in the terminal.

**Note:** The BUCKET_NAME on this page refers to either your custom Cloud Storage bucket included with the `--bucket-name=` flag or the default `PROJECT_ID-devicerun` bucket created for you when using [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run).

## At the command line

See a basic summary of your test or executable result with this command and your session ID:
    
    
    gcloud beta device-run sessions describe SESSION_ID
    

Which returns results resembling:
    
    
    Session SESSION_ID finished with result [FAILED].
    Result files are stored at [https://console.cloud.google.com/storage/browser/BUCKET_NAME/automation/sessions/SESSION_ID/].
    JOB NAME  EXECUTION NAME  EXECUTION RESULT
    job-000   all             FAILED: 2 test cases failed, 5 passed
    job-001   all             PASS
    

For each device type ID you specified with the `--device` flag, one job is generated in the session. The job index will follow the order of your device IDs. Test failures are expected and should be investigated and resolved through iterative improvements and runs.

To get additional details about a session, append `--full` to the previously run `describe` command like so:
    
    
    gcloud beta device-run sessions describe SESSION_ID --full
    

Which returns results resembling:

### Android instrumentation
    
    
    name: projects/PROJECT_ID/locations/global/sessions/session-370961e1
    sessionConfig:
      displayName: instrumentation-session
      jobConfigs:
    
        -   action:
          androidInstrumentationTest:
            testInstallable:
              files:
            -   gcsInputFile:
                  path: gs://BUCKET_NAME/automation/inputs/2026-07-30_11:28.31915956_8514/app_name_test.apk
        allocationConfig:
          deviceConfigs:
        -   actions:
            -   androidInstallPackages:
                installables:
                -   files:
                    -   gcsInputFile:
                      path: gs://BUCKET_NAME/automation/inputs/2026-07-30_11:28.31915956_8514/app_name.apk
            -   androidLogcat: {}
            requirement:
              deviceId: pa3q-35
        displayName: job-000
      outputDirectoryConfig:
        gcsOutputDirectory:
          path: gs://BUCKET_NAME/automation/sessions
    sessionReport:
      endTime: '2026-07-30T03:30:05.838Z'
      id: 6587313f-fdf7-418a-a9b9-b6fa98dff838
      jobReports:
        -   displayName: job-000
        endTime: '2026-07-30T03:30:04.601Z'
        executionReports:
            -   displayName: all
          endTime: '2026-07-30T03:30:02.151Z'
          id: 29b167dd-dde9-4ea9-b2cd-738049083fc9
          outputFiles:
                -   gcsOutputFile:
              path: gs://PROJECT_ID-devicerun/automation/sessions/session-370961e1/job-000/execution-000/logcat.txt
                -   gcsOutputFile:
              path: gs://PROJECT_ID-devicerun/automation/sessions/session-370961e1/job-000/execution-000/instrument.log
                -   gcsOutputFile:
              path: gs://PROJECT_ID-devicerun/automation/sessions/session-370961e1/job-000/execution-000/junit.xml
          result:
            cause:
              summary:
                message: One or more test assertions or test methods failed. Inspect the
                  test runner logs and structured test results for details.
                reason: TEST_CASE_FAILURE
                type: CUSTOMER
            resultType: FAILED
          startTime: '2026-07-30T03:29:32.769Z'
          status:
            progressMessages:
                    -   2 test cases failed, 5 passed
            statusType: DONE
        id: 7974e37a-2928-4aaf-abba-3a8b6bae853b
        result:
          cause:
            summary:
              message: Job has one or more failed tests. See execution reports for details.
              reason: JOB_HAS_FAILED_TESTS
          resultType: FAILED
        startTime: '2026-07-30T03:28:53.756Z'
        status:
          statusType: DONE
      result:
        cause:
          summary:
            message: Session has one or more failed jobs. See job reports for details.
            reason: SESSION_HAS_FAILED_JOBS
        resultType: FAILED
      startTime: '2026-07-30T03:28:52.702Z'
      status:
        statusType: DONE
    

### Android executable
    
    
    name: projects/PROJECT_ID/locations/global/sessions/session-8a41c2b0
    sessionConfig:
      displayName: android-executable-session
      jobConfigs:
    
        -   action:
          androidNativeBinary:
            androidNativeBinary:
              gcsInputFile:
                path: gs://BUCKET_NAME/automation/inputs/2026-07-30_11:28.31915956_8514/my_executable
            args:
            -   --example_flag=/data/local/tmp/example_value
            -   --threads=4
        allocationConfig:
          deviceConfigs:
        -   actions:
            -   androidLogcat: {}
            -   androidPushFiles:
                fileConfigs:
                -   destinationPath: /data/local/tmp/model.tflite
                    sourceFile:
                      gcsInputFile:
                        path: gs://BUCKET_NAME/automation/inputs/2026-07-30_11:28.31915956_8514/model.tflite
            requirement:
              deviceId: shiba-34
        displayName: job-000
      outputDirectoryConfig:
        gcsOutputDirectory:
          path: gs://BUCKET_NAME/automation/sessions
    sessionReport:
      endTime: '2026-07-30T03:30:05.838Z'
      id: 4b9120ec-fdf7-418a-a9b9-b6fa98dff838
      jobReports:
        -   displayName: job-000
        endTime: '2026-07-30T03:30:04.601Z'
        executionReports:
            -   displayName: execution-000
          endTime: '2026-07-30T03:30:02.151Z'
          id: 19a267dd-dde9-4ea9-b2cd-738049083fc9
          outputFiles:
                -   gcsOutputFile:
              path: gs://PROJECT_ID-devicerun/automation/sessions/session-8a41c2b0/job-000/execution-000/logcat.txt
                -   gcsOutputFile:
              path: gs://PROJECT_ID-devicerun/automation/sessions/session-8a41c2b0/job-000/execution-000/output.log
          result:
            resultType: PASSED
          startTime: '2026-07-30T03:29:32.769Z'
          status:
            statusType: DONE
        id: 8874e37a-2928-4aaf-abba-3a8b6bae853b
        result:
          resultType: PASSED
        startTime: '2026-07-30T03:28:53.756Z'
        status:
          statusType: DONE
      result:
        resultType: PASSED
      startTime: '2026-07-30T03:28:52.702Z'
      status:
        statusType: DONE
    

### iOS XCTest

Here is the actual sanitized output of `gcloud beta device-run sessions describe SESSION_ID --full` from a live iOS XCTest run with all flags enabled:
    
    
    name: projects/PROJECT_ID/locations/global/sessions/session-4b941167-5629-4abb-a8a1-a9814bf16847
    sessionConfig:
      displayName: xctest-session
      jobConfigs:
    
        -   action:
          iosXcTest:
            testsZip:
              gcsInputFile:
                path: gs://BUCKET_NAME/automation/inputs/2026-10-09_11:33.01234567_ABCD/MyTests.zip
        allocationConfig:
          deviceConfigs:
            -   actions:
                -   iosInstallPackages:
                ipas:
                    -   gcsInputFile:
                    path: gs://BUCKET_NAME/automation/inputs/2026-10-09_11:33.01234567_ABCD/AdditionalApp.ipa
            requirement:
              deviceId: iphonese3-18-4
        displayName: job-000
      outputDirectoryConfig:
        gcsOutputDirectory:
          path: gs://BUCKET_NAME/automation/sessions
    

In this output, find pulled files for the App Under Test at `.../artifacts/output.txt` (without `com.example.app/Documents/`).

## In web browser

For full details, load the URL to the bucket containing your test results from the test output. It should resemble: `https://console.cloud.google.com/storage/browser/BUCKET_NAME/automation/sessions/SESSION_ID/`

Sessions appear in the following path format in storage: `gs://BUCKET_NAME/automation/sessions/SESSION_ID/job-000/EXECUTION_ID/`

### Navigating

To browse for your logs in the Google Cloud console web interface, follow these steps:

  1. In a browser, append your project name as used in the `gcloud config set project` command to the URL `https://console.cloud.google.com/?project=` and load the page.
  2. Expand the menu at top left.
  3. Find _Cloud Storage_.
  4. From the storage menu, select **Buckets**.
  5. In the first column, click the name of your project.
  6. Click **Automation**.
  7. Click **Sessions**.
  8. In the _Filter_ field, paste the session ID from your latest test run (see the test output).
  9. Click the resulting session name.
  10. Select **job-** * to view `junit.xml` (for Android instrumentation and iOS XCTest runs), which contains merged result details across all executions and test cases in the job.
  11. Open **execution-** * (or **execution-*-rerun-** * when flaky test retries are configured with `--flaky-test-attempts`) for a breakdown of each individual execution or shard. Depending on your session type and configured flags, this folder can contain numerous artifacts, depending on your session type and configured flags. See Understand the results for more details.
  12. Visit the public and authenticated URLs to understand the results.



### File structure

Explore the log files in your Cloud Storage bucket to understand more about your session execution. The file structure resembles:

### Android instrumentation
    
    
    -   gs://BUCKET_NAME/automation
        -   inputs/
            -   2026-05-29_10:13.026220_JZTM
                -   app.apk
                -   test.apk
        -   sessions/
            -   SESSION_ID
                -   job-000/
                    -   junit.xml
                    -   execution-000/
                        -   artifacts/
                            -   sdcard/
                                -   output.txt
                        -   bugreport.zip
                        -   dumpsys.txt
                        -   instrument.log
                        -   junit.xml
                        -   logcat.txt
                        -   video.mp4
                    -   execution-001/
                        -   instrument.log
                        -   junit.xml
                        -   logcat.txt
                        -   video.mp4
                -   job-001/
            -   SESSION_ID
    

### Android executable
    
    
    -   gs://BUCKET_NAME/automation
        -   inputs/
            -   2026-05-29_10:13.026220_JZTM
                -   my_executable
                -   model.tflite
        -   sessions/
            -   SESSION_ID
                -   job-000/
                    -   execution-000/
                        -   artifacts/
                            -   data/
                                -   local/
                                    -   tmp/
                                        -   results.json
                        -   bugreport.zip
                        -   dumpsys.txt
                        -   logcat.txt
                        -   output.log
                        -   video.mp4
                -   job-001/
            -   SESSION_ID
    

### iOS XCTest
    
    
    -   gs://BUCKET_NAME/
        -   automation/
            -   inputs/
                -   2026-10-09_11:33.01234567_ABCD/
                    -   AdditionalApp.ipa
                    -   MyTests.zip
                    -   data.txt
            -   sessions/
                -   SESSION_ID/
                    -   job-000/
                        -   execution-000/
                            -   artifacts/
                                -   output.txt
                            -   junit.xml
                            -   system.log
    

In this output, understand the pulled path under `artifacts/`. For `--paths-to-pull=com.example.app:/Documents/output.txt`, when pulling from the App Under Test (AUT), the service strips `/Documents` and places the file directly at `artifacts/output.txt` (not `artifacts/com.example.app/Documents/output.txt`). If pulled from an additional app (`--additional-apps`), it is placed at `artifacts/<bundle_id>-genfiles/output.txt`.

## Understand the results

For Android instrumentation and iOS XCTest runs, the `junit.xml` files generated in your output are standard JUnit XML files. An execution-level `junit.xml` is written to each `execution-*` directory, and a merged `junit.xml` is written to each `job-*` directory. These files contain the per-test-method results, letting you review the specific pass or fail status, execution time, and error traces for each individual test method. You can readily integrate and parse these files with most Continuous Integration and Continuous Delivery (CI/CD) systems and test reporting tools.

In addition to structured test results, each `execution-*` directory contains platform-specific logs and artifacts:

  * **Android instrumentation runs** include `instrument.log` for raw instrumentation runner output and `logcat.txt` for the device-wide Android system log. When enabled with `--bugreport`, `--dumpsys`, or `--video`, the execution directory also includes `bugreport.zip`, `dumpsys.txt`, and screen video recordings.
  * **Android executable runs** include `output.log`, which captures the standard output (`stdout`) and standard error (`stderr`) written by your executable, and [`logcat.txt`](https://developer.android.com/tools/logcat) (collected by default for every Android job), which captures the device-wide Android system log, along with any optional `--bugreport`, `--dumpsys`, or `--video` artifacts.
  * **iOS XCTest runs** include `system.log` (collected by default for every iOS XCTest job), which captures the raw iOS device syslog, and any `.ips` diagnostic crash reports if a process crashed during the test execution.
  * **Pulled device files** specified with `--paths-to-pull` are stored under the `artifacts/` subfolder of the execution directory. 
    * For Android runs, pulled files preserve their device path under `artifacts/` (for example, `artifacts/sdcard/output.txt` or `artifacts/data/local/tmp/results.json`).
    * For iOS XCTest runs, files pulled from an app data container using `--paths-to-pull=BUNDLE_ID:DEVICE_PATH` are organized by bundle ID under `artifacts/`: 
      * If `com.example.app` is the App Under Test, it is saved directly at `artifacts/output.txt`.
      * If `com.example.app` is an additional app (`--additional-apps`), it is saved at `artifacts/com.example.app-genfiles/output.txt`.



## Supporting documentation

  * [Fundamentals of testing Android apps](https://developer.android.com/training/testing/fundamentals)
  * [Build instrumented tests](https://developer.android.com/training/testing/instrumented-tests)
  * [XCTest documentation](https://developer.apple.com/documentation/xctest)
  * [About Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets)



## What's next

Next up, try our Developer Device Platform [Device Streaming API](https://docs.cloud.google.com/device-streaming/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
