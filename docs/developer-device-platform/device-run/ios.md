---
url: https://docs.cloud.google.com/developer-device-platform/device-run/ios/
title: Developer Device Platform Device Run for iOS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:46.361727+00:00
---

# Developer Device Platform Device Run for iOS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/device-run/ios/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Developer Device Platform Device Run for iOS Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to run an iOS XCTest using the `gcloud alpha device-run` CLI and find your results in the Google Cloud console. It assumes you have a Google Cloud account and project.

If you are migrating from [Firebase Test Lab](https://firebase.google.com/docs/test-lab) to Developer Device Platform, see our [migration guide](https://docs.cloud.google.com/developer-device-platform/device-run/migrate), [command and flag translation](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation), and [migration skill](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/migration-skill) for AI agents.

To use the `device-run` CLI, you will need to provide your Google Cloud project ID. See [`gcloud alpha device-run`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/device-run) for a summary of commands.

## Before you begin

These steps assume that you have already:

  1. Created a Google Cloud project.
  2. Set up Developer Device Platform following the [Quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart).
  3. Authenticated with `gcloud` in the terminal.
  4. Reviewed the [Device Run overview](https://docs.cloud.google.com/developer-device-platform/device-run) for general information.
  5. Compiled your tests and packaged them into a ZIP.



## Step 1. Configure your test run

**Tip:** To view all available options for the `submit xctest` command, run `gcloud alpha device-run sessions submit xctest --help`.

You can customize your test execution using the following optional flags (although at least one instance of the `--device` flag is required):

  * _Multiple devices_ : Specify the `--device` flag multiple times to run the same test on multiple devices concurrently: `--device iphonese3-18-4 --device iphonese3-26-3` or `--device iphonese3-18-4,iphonese3-26-3`
  * _Additional apps_ : Install one or more additional `.ipa` packages before launching the test using `--additional-apps`: `--additional-apps=/path/to/AdditionalApp.ipa`
  * _Custom`.xctestrun` file_: Pass a custom configuration file with `--xctestrun-file`: `--xctestrun-file=/path/to/CustomTests.xctestrun`
  * _Apple Xcode versions_: Directly access by CLI supported Xcode versions with the `--xcode-version` flag, for example: `--xcode-version=xcode-16-4`
  * _Test timeout_ : Limit the execution duration: `--xctest-timeout=10m` (Valid range is `1m` to `1h` and defaults to `5m`).
  * _Labels_ : Attach user-defined metadata to the session: `--labels=env=staging,owner=my-team`
  * _Locale_ : Set the device locale: `--locale=en-US`
  * _Push files to device_ : Push files to the app data container before test execution: `--other-files-to-push=/tmp/data.txt=com.example.app:/Documents/data.txt`
  * _Pull files from device_ : Pull files from the app data container after test execution: `--paths-to-pull=com.example.app:/Documents/output.txt`
  * _Flaky test retries_ : Set the maximum number of attempts to rerun flaky tests: `--flaky-test-attempts=3` (Defaults to 1 attempt).
  * _Custom Cloud Storage bucket_ : Specify a custom Cloud Storage bucket for inputs and outputs: `--bucket-name=my-custom-bucket` (Defaults to `PROJECT_ID-devicerun`).
  * Because uploading large ZIP or IPA files can be time-consuming, you can directly reference your files using their Cloud Storage `gs://` paths to save upload time.



### Synchronous and asynchronous runs

By default, the submit command is **blocking (synchronous)**. It will wait for the test to complete and print a summary table of the results.

To submit the session and return immediately after uploading files to Cloud Storage, add the `--async` flag:
    
    
    gcloud alpha device-run sessions submit xctest \
      --device iphonese3-18-4 \
      --test ./IOS_TESTS.zip \
      --async
    

This returns a session ID immediately. You can then wait for it using the `sessions wait` command:
    
    
    gcloud alpha device-run sessions wait SESSION_ID
    

The command will block until the job is completed.

### Multiple devices

To run the same test across multiple devices, provide the `--device` flag with multiple device IDs separated by commas or with multiple `--device` flags, each specifying a distinct device ID.

### Separated by commas
    
    
    gcloud alpha device-run sessions submit xctest \
      --device iphonese3-18-4,iphonese3-26-3 \
      --test ./IOS_TESTS.zip
    

### Multiple flags
    
    
    gcloud alpha device-run sessions submit xctest \
      --device iphonese3-18-4 \
      --device iphonese3-26-3 \
      --test ./IOS_TESTS.zip
    

### Test timeout

Limit the execution duration of your test:
    
    
    gcloud alpha device-run sessions submit xctest \
      --device iphonese3-18-4 \
      --test ./IOS_TESTS.zip \
      --xctest-timeout=10m
    

The valid range is `1m` to `1h` and defaults to `5m`.

### Software versions

Discover and use available software packages and versions of [Apple Xcode](https://developer.apple.com/xcode/) and inspect their lifecycles, supported versions, and metadata before configuring test runs.

First, list all available software packages and their versions:
    
    
    gcloud alpha device-run software-versions list
    

Receiving output resembling:
    
    
    ID                                NAME                              SOFTWARE_TYPE               VERSION  STATE   IS_DEFAULT
    androidx-test-orchestrator-1-4-1  AndroidX Test Orchestrator 1.4.1  ANDROIDX_TEST_ORCHESTRATOR  1.4.1    ACTIVE  True
    androidx-test-orchestrator-1-6-1  AndroidX Test Orchestrator 1.6.1  ANDROIDX_TEST_ORCHESTRATOR  1.6.1    ACTIVE
    xcode-16-4                        Xcode 16.4                        XCODE                       16.4     ACTIVE
    xcode-26-2                        Xcode 26.2                        XCODE                       26.2     ACTIVE  True
    

Then describe a specific package _using its exact resource ID_ from the list:
    
    
    gcloud alpha device-run software-versions describe xcode-16-4
    

Receiving output resembling:
    
    
    id: xcode-16-4
    lifecycle:
      state: ACTIVE
    name: Xcode 16.4
    softwareType: XCODE
    supportedIosVersions:
    
    -   '15.0'
    -   '15.1'
    -   '15.2'
    -   '15.4'
    -   '15.7'
    -   '16.0'
    -   '16.1'
    -   '16.2'
    -   '16.3'
    -   '16.5'
    -   '16.6'
    -   '18.0'
    -   '18.3'
    -   '18.4'
    version: '16.4'
    

Now that you know which software versions are available, you can use them in your test runs with the `--xcode-version` flag, like so:
    
    
    gcloud alpha device-run sessions submit xctest \
      --device iphonese3-18-4 \
      --test ./IOS_TESTS.zip \
      --xcode-version=16.4
    

## Step 2. Choose device types

Using the `device-run` CLI, iOS tests can be executed across available physical devices. To view the complete list of available devices visit either the interactive [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog#available-devices) or run:
    
    
    gcloud alpha device-run devices list
    

Example output:
    
    
    ID                MAKE   NAME           MODEL        HARDWARE_TYPE  OS_VERSION  CAPACITY  AVAILABILITY  PRODUCTS
    iphonese3-18-4    Apple  iPhone SE 3             iphonese3    PHYSICAL       18.4        NONE      NONE          Automation
    iphonese3-26-3    Apple  iPhone SE 3             iphonese3    PHYSICAL       26.3        NONE      NONE          Automation
    

See the [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog#filter-devices) to learn how to filter this list. To target a specific device for your test execution, use its corresponding ID (ex. `iphonese3-18-4`) in the submit command.

## Step 3. Prepare and package your XCTest

Before running your tests, you must compile them, ensure they are signed, verify the code signatures, and package the resulting artifacts into a ZIP file containing your `.xctestrun` configuration and the application test bundles.

**Tip:** **Migrating from Firebase Test Lab?** Device Run accepts the same test package as Firebase Test Lab: the `Debug-iphoneos/` directory and the `.xctestrun` file from `Build/Products`, as described in Run an XCTest. If you already have a build and packaging pipeline for Firebase Test Lab, you can reuse it unchanged and pass the resulting `.zip` to `--test`. For the rest of the migration, see the iOS section of [Flag and command translation](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation#ios-flags).

### 1\. Build your tests for physical iOS devices

Open your project in Xcode and build your app and test targets for testing:

  1. Ensure that code signing is configured correctly in Xcode (specifying a valid provisioning profile and developer identity) for both the app target and the test runner target.
  2. Build for testing using Xcode (_Product > Build For > Testing_) or with `xcodebuild`.

For a workspace:
         
         xcodebuild build-for-testing \
           -workspace YourProject.xcworkspace \
           -scheme YourScheme \
           -derivedDataPath ./build \
           -destination "generic/platform=iOS"
         

For a standalone project:
         
         xcodebuild build-for-testing \
           -project YourProject.xcodeproj \
           -scheme YourScheme \
           -derivedDataPath ./build \
           -destination "generic/platform=iOS"
         




This generates the build products under: `./build/Build/Products`

**Note:** You don't need to register the Device Run device UDIDs in your Apple Developer account. Developer Device Platform re-signs your application and test bundles with a lab provisioning profile before installing them on the physical device, so a valid local development certificate and provisioning profile is all that is required to complete the build and packaging steps.

### 2\. Verify build products and signatures

After building, verify that the application, runner, and `.xctestrun` manifest were generated under `./build/Build/Products/`. If signed locally, you can verify bundle signatures using `codesign`:

  1. Verify the app bundle:
         
         codesign --verify --deep --verbose ./build/Build/Products/Debug-iphoneos/YourApp.app
         

Expected output: `YourApp.app: valid on disk`

  2. If running an XCUITest, also verify the test runner bundle:
         
         codesign --verify --deep --verbose ./build/Build/Products/Debug-iphoneos/YourApp-Runner.app
         

Expected output: `YourApp-Runner.app: valid on disk`


**Note:** A separate `YourApp-Runner.app` bundle is produced only for UI test (XCUITest) targets. Application-hosted unit tests are embedded in the host app instead, and are covered by the verification of `YourApp.app`.

### 3\. Create the ZIP archive

Compress both the `Debug-iphoneos` directory and the `.xctestrun` file located in the build output products folder into a single ZIP archive.

**Caution:** The Debug-iphoneos/ directory and the .xctestrun file must reside directly at the root of the ZIP archive. Do NOT zip the outer Products/ or build/ folder.

Run the following command from the build products directory:
    
    
    cd ./build/Build/Products
    zip -r MyTests.zip Debug-iphoneos *.xctestrun
    

This creates the packaged `MyTests.zip` that is ready to be used with the `--test` flag.

## Step 4. Run your XCTest

Note these flags are required:

  * _Device_ : Specify a device using `--device`: `--device iphonese3-18-4`
  * _Test_ : Specify the test zip file using `--test`: `--test ./MyTests.zip`



To run your XCTest, use the `gcloud alpha device-run sessions submit xctest` command. You must provide the test zip file (`MyTests.zip`) compiled in the previous step.

To run a basic test session:
    
    
    gcloud alpha device-run sessions submit xctest \
      --device iphonese3-18-4 \
      --test ./MyTests.zip
    

When execution begins, the CLI displays the created Session ID and the Cloud Storage destination where results will be stored:
    
    
    Creating session [session-ee78b0ed] in location [global].
    Result files will be stored at [https://console.cloud.google.com/storage/browser/BUCKET_NAME/automation/sessions/session-ee78b0ed/].
    
    Waiting for session [session-ee78b0ed] to complete....
    

## Step 5. Explore and manage your test run

You can track active runs and manage historic sessions using these commands:

  * _Describe session_ : Query the live progress or final results of a session: `gcloud alpha device-run sessions describe SESSION_ID` Add `--full` to view complete details including device allocations, execution IDs, and Cloud Storage artifact paths.
  * _List sessions_ : View your recent runs: `gcloud alpha device-run sessions list --limit=10`
  * _Cancel session_ : Stop a running test session: `gcloud alpha device-run sessions cancel SESSION_ID`
  * _Cancel operation_ : Stop a pending or active operation: `gcloud alpha device-run operations cancel OPERATION_ID`



## What's next

Next up, [find and analyze logs](https://docs.cloud.google.com/developer-device-platform/device-run/find-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
