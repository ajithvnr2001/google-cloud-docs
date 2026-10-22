---
url: https://docs.cloud.google.com/developer-device-platform/troubleshooting/
title: Developer Device Platform Troubleshooting & FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:03.955606+00:00
---

# Developer Device Platform Troubleshooting & FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Resources ](https://docs.cloud.google.com/developer-device-platform/resources)



Send feedback 

#  Developer Device Platform Troubleshooting & FAQ Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides troubleshooting help and answers to frequently asked questions about running tests with Developer Device Platform. If you can't find what you're looking for or need additional help, [contact us](https://docs.cloud.google.com/developer-device-platform/quickstart#contact-us).

## Troubleshooting

#### What resources do you have for migrating from Firebase Test Lab to Developer Device Platform?

If you are migrating from [Firebase Test Lab](https://firebase.google.com/docs/test-lab) to Developer Device Platform, see our [migration guide](https://docs.cloud.google.com/developer-device-platform/device-run/migrate), [command and flag translation](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation), and [migration skill](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/migration-skill) for AI agents.

#### Why is my test taking so long to run?

When you select a device with a high capacity level in the Developer Device Platform catalog, tests may start faster. When a device has low capacity, tests might take longer to run. If the number of tests invoked is much larger than the capacity of the selected devices, tests can take longer to finish.

Tests running on any device-capacity level may take longer due to the following factors: 

  * Traffic, which affects device availability and test speed.
  * Device or infrastructure failures, which can happen at any time. To check if there is a reported infrastructure for Developer Device Platform, see the [Google Cloud Personalized Service Health](https://status.cloud.google.com/) dashboard.



To learn more about device capacity in the Developer Device Platform, see the [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog).

#### Why am I receiving inconclusive test results?

Inconclusive test outcomes commonly occur either because of canceled test runs or infrastructure errors. In addition to `PASSED` and `FAILED`, Developer Device Platform may return `ERROR`, `TIMED_OUT` and `CANCELLED`.

Infrastructure errors are caused by internal Developer Device Platform issues, like network errors or unexpected device behaviors. Developer Device Platform internally retries test runs that produce infrastructure errors multiple times before reporting an inconclusive outcome.

To determine the cause of the error, follow these steps:

  1. Check for known outages in the [Google Cloud Service Health](https://status.cloud.google.com/) dashboard.
  2. Retry the test in Developer Device Platform to verify that it is reproducible.

**Note:** Developer Device Platform does not charge you for infrastructure errors.
  3. Try running the test on a different device or device type, if applicable. See the [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog) for more information.




#### Why did sharding make my tests run longer?

Sharding can cause your tests to run longer when the number of shards you specified exceeds the number of devices available for use in Developer Device Platform. To avoid this situation, limit your device count to your shard count. For more information about choosing a different device, see the [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog).

#### Why is it taking a long time for my test to start?

When you submit a test request, your app is first validated, re-signed, etc. in preparation for running tests on a device. Normally, this process completes in less than a few seconds, but it can be affected by factors like the size of your app.

After your app is prepared, test executions are scheduled and remain in a queue until a device is ready to run it.

**Note:** The time your test spends waiting for an available device does not count toward your billing time.

#### Why is it taking a long time for my test to finish?

After the test execution is finished, test artifacts are downloaded from the device, processed, and uploaded to Cloud Storage. The duration of this step can be affected by the amount and size of the artifacts.

#### Why does `sessions.batchGet` return an HTML `400 Bad Request` error?

When you call the [`sessions.batchGet`](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/batchGet) REST method with many session names, you might receive a `400 Bad Request` response as an HTML page, instead of a JSON error, with the message "Your client has issued a malformed or illegal request."

This error means that the request URL is too long. In a `GET` request, each session name is sent as a `names` query parameter, and Google Cloud APIs limit request URLs to about 16 KB, which is roughly 150 session names. The request is rejected before it reaches Device Run.

To retrieve up to 500 sessions in one call, send a `POST` request to the same URL with the `X-HTTP-Method-Override: GET` header, and pass the session names in the request body:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      -H "X-HTTP-Method-Override: GET" \
      -H "Content-Type: application/json" \
      -d '{"names": ["projects/PROJECT_ID/locations/LOCATION/sessions/SESSION_ID_1",
                     "projects/PROJECT_ID/locations/LOCATION/sessions/SESSION_ID_2"]}' \
      "https://devicerun.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/sessions:batchGet"
    

The request is processed exactly like the equivalent `GET` request, with the same permissions, validation, and response. You can also pass the parameters as a form-encoded (`application/x-www-form-urlencoded`) body, or split the session names into smaller batches. Client libraries and gRPC clients send requests in the message body, so this limit doesn't affect them. For more information, see [Long request URLs](https://docs.cloud.google.com/apis/docs/http#long_request_urls).

  


### Android-specific troubleshooting

#### App not returning data and can't locate screenshots

Test execution artifacts (such as screenshots and log files) are stored in Cloud Storage and directly rendered into the Google Cloud console. Check that you have assigned project-level roles.

Also note, Developer Device Platform has a dedicated [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) that uses its own credentials rather than yours to:

  * Read and write to Cloud Storage buckets and objects
  * Download Cloud Storage input files to the internal system
  * Upload files from the internal system to the Cloud Storage output bucket



It is possible you have access to a Cloud Storage bucket and file, but that bucket is owned by a different Google Cloud project than the one used in DDP. Therefore, the Developer Device Platform service account does not have access to it.

You could also have additional access controls on individual buckets. See [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run) for how to include files with your tests and [Share Storage](https://docs.cloud.google.com/developer-device-platform/device-run/share-storage) for how to grant Developer Device Platform access to external buckets.

#### Why am I receiving partial or missing instrumentation test case results?

When you run instrumentation tests, you might see total test cases are less than expected. This is often caused by Developer Device Platform being incapable of parsing the logcat for test case start or end markers that are usually generated by [AndroidJUnitRunner](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner).

The following are common causes of this issue:

Issue description | Possible resolution  
---|---  
Test case did not run because of a timeout. If the total duration of the tests is longer than a timeout you specified or longer than a max timeout, Developer Device Platform cancels the rest of the test cases.  | 

  * Increase the instrumentation timeout for the test, using [`--instrumentation-timeout`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run/sessions/submit/instrumentation#--instrumentation-timeout), to make sure all tests can complete. 
  * Shard the tests if you did not already do so, so that each shard runs a subset of the tests and completes in a shorter period of time. 
  * If you already enabled sharding, increase the number of shards.

  
The test case failed to complete because it exited prematurely or got stuck. The test case may exit prematurely because of an uncaught exception or assertion error. Test cases can get stuck in an infinite loop or might be unable to proceed, for example, if the app does not show the correct view and the test case can't perform the action on the UI.  |  Check the video and the `logcat` to investigate where the test stopped.   
A custom test runner (including extending AndroidJUnitRunner) crashed unexpectedly or wrote unexpected test case start or end markers to `logcat`.  | Check your test runner code.  
Excessive logs were written to `logcat`, which overwhelmed the buffer or crashed the `logcat` process.  |  Reduce writes to `logcat`.   
The app under test crashed.  |  Debug your app.   
  
  


* * *

## Frequently asked questions (FAQ)

#### Where can I find information on Developer Device Platform pricing?

See [Pricing and billing questions](https://docs.cloud.google.com/developer-device-platform/pricing) for details.

#### Where can I find device details, like resolution, etc.?

Detailed device information is available through the API and can be accessed from the Developer Device Platform CLI with the [`device-run devices describe <device-id>`](https://docs.cloud.google.com/developer-device-platform/device-catalog#describe-devices) command:
    
    
    gcloud beta device-run devices describe DEVICE_ID
    

#### How do I find out if the traffic reaching my backend is coming from Developer Device Platform?

From your backend, you can determine if traffic is coming from Developer Device Platform-hosted test devices by checking the source IP address against our [IP ranges](https://docs.cloud.google.com/developer-device-platform/resources/ip-blocks).

#### Does Developer Device Platform work with VPC-SC?

Developer Device Platform does not work with VPC-SC, which blocks the copying of apps and other test artifacts between Developer Device Platform's internal storage and users' results buckets.

#### How do I reduce flaky tests in Developer Device Platform?

To detect flaky behavior in your tests, we recommend using the `--flaky-test-attempts` option. Deflake reruns are billed or counted toward your daily quota the same as normal test executions.

Keep the following in mind:

  * DDP will by default run the retry in sequence to save cost. Users need to set `--flaky-test-parallel-retry` to run in parallel.
  * The `--flaky-test-retry-level` flag defines whether to retry at the `shard` or individual `test` level and defaults to `shard`. Set it to `test` to reduce the retry test size and duration.

**Note:** Infrastructure errors are independent from the deflake feature and don't trigger deflake reruns.

  


### iOS-specific FAQ

#### Does Developer Device Platform support Appium, Flutter/FlutterDriver, ReactNative/Jest, or Cucumber?

While some of these items are on our roadmap, we're unable to provide commitment to supporting these testing and app development platforms.

#### Why is my iOS test missing videos in the results?

Support for videos in the results is planned for iOS 18 or later.

  


### Android-specific FAQ

#### Does Developer Device Platform support wearable devices?

Yes! Developer Device Platform supports Google Pixel Watch. You can now run tests on your standalone Wear OS app on Google Pixel Watches. To learn more about Developer Device Platform devices, see the [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog).

#### Does Developer Device Platform support the latest Google devices?

Yes! Developer Device Platform supports the Google Pixel Tablet and Google Pixel Fold. You can run your tests on your standalone physical devices. To learn more about devices available in Developer Device Platform, see the [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog).

#### Does Developer Device Platform support Appium, Flutter/FlutterDriver, ReactNative/Jest, or Cucumber?

While some of these items are on our roadmap, we're unable to provide commitment to supporting these testing and app development platforms. However, if you built your app with a framework that supports Espresso (for example, Flutter), you can write an instrumentation test using [Espresso](https://developer.android.com/training/testing/espresso) and then run the test in Developer Device Platform.

#### Does Developer Device Platform support testing obfuscated apps, for example, with ProGuard or R8)?

Developer Device Platform does not explicitly support obfuscation or deobfuscation. While the app will likely run, any obfuscated app data, like stack traces, will appear as obfuscated in the logs.

#### Can I use my foldable device in different foldable states and postures while testing on Developer Device Platform? 

Yes! You can test your foldable device in [foldable states and postures](https://developer.android.com/guide/topics/large-screens/learn-about-foldables#foldable_postures).

Foldable devices can be in various folded states, such as [`FLAT`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#FLAT\(\)) (fully open) or [`HALF_OPENED`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#HALF_OPENED\(\)) (between fully open and completely closed).

Postures, on the other hand, consist of specific device orientation and foldable state. For example, tabletop posture, which is a `HALF_OPENED` state in horizontal orientation, or book posture, which is a `HALF_OPENED` state in vertical orientation.

If you are running instrumentation tests, you can use the [Jetpack WindowManager](https://developer.android.com/jetpack/androidx/releases/window) library and follow [testing your app on foldables](https://developer.android.com/guide/topics/large-screens/test-apps-on-foldables) documentation to test on different states and postures.

Alternatively, available states are device-specific and can be interacted with using the `adb shell command cmd device_state`.

  * To list the current state, run `adb shell cmd device_state state`.
  * To set or override the current state, run `adb shell cmd device_state state <IDENTIFIER>`.
  * To reset the state, run `adb shell cmd device_state state reset`.
  * To check available states, run the `adb shell cmd device_state print-states` command on the foldable device.



###  Google Pixel Fold (model ID `felix`)
    
    
    $ adb shell cmd device_state print-states
    Supported states: [
          DeviceState{identifier=0, name='CLOSED', app_accessible=true},
          DeviceState{identifier=1, name='HALF_OPENED', app_accessible=true},
          DeviceState{identifier=2, name='OPENED', app_accessible=true},
          DeviceState{identifier=3, name='REAR_DISPLAY_STATE', app_accessible=true},
    ]
    

###  Samsung Galaxy Z Fold4 (model ID `q4q`)
    
    
    $ adb shell cmd device_state print-states
    Supported states: [
          DeviceState{identifier=0, name='CLOSE', app_accessible=true},
          DeviceState{identifier=1, name='TENT', app_accessible=true},
          DeviceState{identifier=2, name='HALF_FOLDED', app_accessible=true},
          DeviceState{identifier=3, name='OPEN', app_accessible=true},
    ]
    

#### Can I try out Developer Device Platform if I don't have an app?

Unlike other Developer Device Platform products, you don't need to add a Developer Device Platform SDK in order to use Developer Device Platform. If you don't already have an app, you can download an APK online or build an app and a test APK from one of the samples in the [AndroidX GitHub repository](https://github.com/android/testing-samples). Note that an instrumentation test requires both an app and a test APK that are built from source code. For more information, read about [Instrumented tests](https://developer.android.com/studio/test/index.html).

To learn more about Developer Device Platform features, see the [DDP product overview](https://docs.cloud.google.com/developer-device-platform/overview).

#### What devices are best for screenshot-diff testing?

_Screenshot-diff testing_ is where test assertions are based on comparing screen images obtained while running a test to golden images representing expected behavior. Such tests may be more brittle on some device types than others. We recommend targeting Arm (`*.arm`) emulator devices for these kinds of tests. Arm emulator devices use images that are very similar or identical to Android Studio generic emulators.

We also recommend that you investigate test libraries that can help make screenshot tests more robust in the presence of expected changes.

#### Does Developer Device Platform update virtual devices?

Yes! Virtual devices are updated when the following changes are made:

  1. Updates to existing images
  2. Deprecation of earlier API levels
  3. New Android API levels are added



#### How do I enable coverage reports?

To enable coverage reports, add `coverage=true` to the [`additional-test-options` field](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run/sessions/submit/instrumentation#--additional-test-options). If you're using Android Test Orchestrator, you must provide a directory path to store the coverage results:
    
    
    --additional-test-options coverage=true,coverageFilePath=/sdcard/Download/
    

If you're not using Orchestrator, you can specify a file path:
    
    
    --additional-test-options coverage=true,coverageFile=/sdcard/Download/coverage.ec
    

#### How do I sign in to a Wear app without a phone?

If your app normally requires a phone for login, you can create a build variant that skips login and uses a token embedded in your test build, or read from files on disk typically pushed using the `--other-files-to-push` flag.

  


* * *

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
