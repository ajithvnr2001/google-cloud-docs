---
url: https://docs.cloud.google.com/developer-device-platform/device-run/migrate/migration-skill/
title: Migrate from Firebase Test Lab and Flank to Developer Device Platform with AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:27.439619+00:00
---

# Migrate from Firebase Test Lab and Flank to Developer Device Platform with AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/device-run/migrate/migration-skill/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Migrate from Firebase Test Lab and Flank to Developer Device Platform with AI Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This skill assists with translating legacy test run configurations and workflows (from Flank or `gcloud firebase test`) to the modern, resource-oriented `gcloud beta device-run` CLI surface (and `gcloud alpha device-run` for submitting iOS XCTest sessions).

## Command & Resource Structure Mapping

The Device Run CLI organizes commands by resource: `devices`, `software-versions`, and `sessions`:

### 1\. Device Catalog (`devices`)

  * **List Devices** : 
    * _Legacy_ : `gcloud firebase test android/ios models list`
    * _New_ : `gcloud beta device-run devices list [--filter="..."]`
    * _Example_ : `gcloud beta device-run devices list --filter="platform:android"`
  * **Describe Device** : 
    * _Legacy_ : `gcloud firebase test android/ios models describe {MODEL}`
    * _New_ : `gcloud beta device-run devices describe {DEVICE}`
    * _Example_ : `gcloud beta device-run devices describe redfin-30`
  * **Check Device Capacities & Fleet Availability**: 
    * _Legacy_ : `gcloud firebase test android/ios list-device-capacities`
    * _New_ : Embedded directly on the Device resource (`availability.capacity` and `availability.available`). Inspect using `gcloud beta device-run devices describe {DEVICE}` or filter directly with `gcloud beta device-run devices list --filter="availability.capacity=CAPACITY_HIGH"`.



### 2\. Software Versions (`software-versions`)

  * **List Supported Software Versions (Xcode & Android Test Orchestrator)**: 
    * _Legacy_ : `gcloud firebase test ios xcode-versions list`
    * _New_ : `gcloud beta device-run software-versions list`
  * **Describe Software Version** : 
    * _New_ : `gcloud beta device-run software-versions describe {SOFTWARE_VERSION}`
    * _Example_ : `gcloud beta device-run software-versions describe xcode-16-4`



### 3\. Automation Sessions (`sessions`)

  * **Submit Android Instrumentation** : 
    * _Legacy_ : `gcloud firebase test android run --type=instrumentation ...`
    * _New_ : `gcloud beta device-run sessions submit instrumentation ...`
  * **Submit iOS XCTest** : 
    * _Legacy_ : `gcloud firebase test ios run --type=xctest ...`
    * _New_ : `gcloud alpha device-run sessions submit xctest ...`
  * **Wait for Session Completion** : 
    * _Legacy_ : Synchronous CLI blocking only
    * _New_ : `gcloud beta device-run sessions wait {SESSION}`
  * **Describe / Inspect Session** : 
    * _Legacy_ : View web link in Firebase Console / Cloud Tool Results
    * _New_ : `gcloud beta device-run sessions describe {SESSION} [--full]`
  * **List Past Sessions** : 
    * _Legacy_ : View matrix history in web console
    * _New_ : `gcloud beta device-run sessions list`
  * **Cancel Session** : 
    * _Legacy_ : Web console only (no CLI command)
    * _New_ : `gcloud beta device-run sessions cancel {SESSION}`



* * *

## Flag Mapping Reference Table

The following table maps parameters from legacy Firebase Test Lab and Flank to their supported equivalents in `gcloud beta device-run`:

Test Type  | Feature Group  | Legacy Parameter (firebase / Flank) | Target Parameter (`device-run`)  | Format / Conversion Logic   
---|---|---|---|---  
Common (Android & iOS)  | Core parameters and assets | Flank `--project` | `--project` | Standard Google Cloud global flag (`--project=PROJECT_ID`) or active Google Cloud CLI configuration.  
Common (Android & iOS)  | Core parameters and assets | `--client-details` | `--labels` | **Dictionary** of key=value pairs.   
Common (Android & iOS)  | Device configuration and targeting  | `--device model={M},version={V}` | `--device={M}-{V}` | Maps model and OS version to `--device` ID string. Accepts a comma-separated list of multiple devices in a single flag (ex. `--device=mediumphone-arm-32,shiba-36`).  
Common (Android & iOS)  | Execution control and flakiness  | `--async` | `--async` | Maps 1:1. Command stays synchronous by default, pass this to return immediately. Monitor or await with `gcloud beta device-run sessions wait <SESSION_ID>`.  
Common (Android & iOS)  | Execution control and flakiness | `--num-flaky-test-attempts {R}` | `--flaky-test-attempts {A}` | **Integer**. Convert retry count $R$ to total attempts limit: $A = R + 1$ (defaults to 1).  
Common (Android & iOS)  | Execution control and flakiness | N/A  | `--flaky-test-parallel-retry` | **Boolean**. Whether to retry test failures in parallel (defaults to sequential).  
Common (Android & iOS)  | Execution control and flakiness | N/A  | `--flaky-test-retry-level` | **String**. Retry level: `shard` or `test` (defaults to `shard`).   
Common (Android & iOS)  | Output and storage  | `--results-bucket` | `--bucket-name` | Bucket where test output artifacts are uploaded (defaults to `gs://[PROJECT_ID]-devicerun`).  
Common (Android & iOS)  | Output and storage  | `--results-dir` | _Managed automatically_ | Setting custom subdirectories is not supported; all test artifacts are automatically organized under `automation/sessions/{session_id}/` within the bucket specified by `--bucket-name`.  
Common (Android & iOS) | Output and storage | `--record-video` | `--video` | Valid values: `always` or `on-failure`.   
Common (Android & iOS) | Output and storage | `--directories-to-pull` | `--paths-to-pull` | **List** of paths to pull from the device after run.  
Common Android  | Core parameters and assets | `--app` | `--apps` | **List**. If multiple application APKs/AABs are supplied, pass them all to `--apps`.  
Common Android  | Core parameters and assets | `--additional-apks` | `--apps` | **List**. Merge additional list values directly into the main `--apps` list.   
Common Android  | Core parameters and assets | `--obb-files` | `--other-files-to-push` | **Dictionary** in `SOURCE=DEST` format. Push OBB files directly to device path (`/sdcard/Android/obb/{package_name}/`).  
Common Android  | Core parameters and assets | `--other-files` | `--other-files-to-push` | **Dictionary** in `SOURCE=DEST` format.   
Common Android  | Device configuration and targeting | `--device locale={L}` | `--locale={L}` | Maps device locale to top-level `--locale` flag (`language-region`, ex. `--locale=en-US`).  
Common Android  | Device configuration and targeting | `--device orientation={O}` | `--orientation={O}` | Maps device orientation to top-level `--orientation` flag (`portrait` or `landscape`).  
Common Android  | Device configuration and targeting | N/A  | `--coordinates` | Mock location coordinates (`latitude,longitude`, ex., `37.4220,-122.0841`).  
Common Android  | Execution control and flakiness | `--grant-permissions` | Automated Default  | **Automated**. Runtime permissions are granted automatically by default (equivalent to `--grant-permissions=all`).|  
Common Android  | Output and storage | N/A  | `--dumpsys` | Collect dumpsys from device (`always` or `on-failure`).  
Common Android  | Output and storage | N/A  | `--bugreport` | Collect bugreport from device (`always` or `on-failure`).  
Android Instrumentation  | Core parameters and assets | `--type=instrumentation` | `sessions submit instrumentation` | Sub-command structure determines test type instead of a `--type` flag.   
Android Instrumentation  | Core parameters and assets | `--test` | `--test` | Path to the binary file containing instrumentation tests.   
Android Instrumentation  | Execution control and flakiness | `--timeout` | `--instrumentation-timeout` | **Duration** (ex., `10m`, `20s`, `1h`). Valid range: `1m` to `3h` (defaults to `5m`).  
Android Instrumentation  | Execution control and flakiness | `--num-uniform-shards {N}` | `--sharding-option=uniform`  
`--uniform-sharding-count={N}` | Flag configuration activates uniform sharding strategy (valid count range: 1-20 physical, 1-200 virtual).  
Android Instrumentation  | Execution control and flakiness | Flank `--shard-time {S}` | `--sharding-option=smart`  
`--smart-sharding-target-duration={S}` | Activates smart sharding with target execution time (ex. `2m`, `10m`, `1h`). Valid range: `2m` to `1h`.  
Android Instrumentation  | Execution control and flakiness  | Flank `--smart-flank-gcs-path` | `--smart-sharding-record-name={name}`  
`--bucket-name={bucket}` | Name of the sharding record YAML (exclude extension) inside `--bucket-name` under `automation/smart-sharding/`.  
Android Instrumentation  | Execution control and flakiness | Flank `--max-test-shards {N}` | `--smart-sharding-max-shard-count={N}` | Maps to a max shard bound when smart sharding is enabled (0-20 physical, 0-200 virtual).  
Android Instrumentation | Test runner and targets | `--test-runner-class` | `--test-runner-class` | Fully-qualified runner class.   
Android Instrumentation  | Test runner and targets  | `--test-targets` | `--test-targets` | **Dictionary** supporting keys like `package`, `notPackage`, `class`, `notClass`, `annotation`, `notAnnotation`, and `size`. Formats like `testfile` or `notTestfile` won't be supported.  
Android Instrumentation | Test runner and targets | `--use-orchestrator` | `--orchestrator-version` | Takes `auto` (default orchestrator) or specific version string (ex., `1.6`).  
Android Instrumentation  | Test runner and targets  | `--environment-variables` | `--additional-test-options` | **Dictionary** of options passed to the test runner. Formats supported in `--test-targets` are not allowed here.  
Common iOS  | Core parameters and assets | `--additional-ipas` | `--additional-apps` | **List** of `.ipa` files to install on the device before the test run.   
Common iOS  | Core parameters and assets | `--other-files` | `--other-files-to-push` | **Dictionary** in `SOURCE=BUNDLE_ID:DEVICE_PATH` format.   
Common iOS  | Device configuration and targeting | `--device locale={L}` | `--locale={L}` | Maps device locale to top-level `--locale` flag (`language-region`, ex. `--locale=en-US`).  
Common iOS  | Output and storage  | `--directories-to-pull` | `--paths-to-pull` | List of files or directories to pull after test in format `BUNDLE_ID:DEVICE_PATH`.  
iOS XCTest only  | Core parameters and assets | `--type=xctest` | `sessions submit xctest` | Sub-command structure determines test type instead of a `--type` flag (uses `gcloud alpha`).  
iOS XCTest only  | Core parameters and assets | `--test` | `--test` | The path to the ZIP file containing the iOS app and XCTest files.   
iOS XCTest only  | Execution control and flakiness | `--timeout` | `--xctest-timeout` | Maximum duration allowed for the XCTest run (valid range: `1m` to `1h`, defaults to `5m`).  
iOS XCTest only  | Test runner and targets | `--xctestrun-file` | `--xctestrun-file` | The path to the custom .xctestrun file.   
iOS XCTest only  | Test runner and targets  | `--xcode-version` | `--xcode-version` | Catalog ID or version string of Xcode to use (ex. `xcode-16-4` or `16.4`). Query using `software-versions list`.  
  
* * *

## Actionable Translation Guidance

Follow these guidelines to translate Firebase Test Lab and Flank configurations to device-run:

### 1\. Device Specifications

In `gcloud beta device-run`, `--device` accepts a comma-separated list of model and version ID strings. Unlike Firebase which required one `--device` flag per device, device-run allows specifying multiple devices in one flag. Device locale, orientation, and mock coordinates are specified using separate top-level flags:

  * ❌ `--device model=MediumPhone.arm,version=32,locale=en,orientation=portrait`
  * ✅ `--device=mediumphone-arm-32 --locale=en-US --orientation=portrait`



### 2\. Dictionaries and Lists

Convert comma-separated flags into lists (`--apps`, `--paths-to-pull`) or key-value dictionaries (`--other-files-to-push`, `--additional-test-options`):

  * ❌ `--other-files /sdcard/file1.txt=local/file1.txt,/sdcard/file2.txt=local/file2.txt`
  * ✅ `--other-files-to-push local/file1.txt=/sdcard/file1.txt,local/file2.txt=/sdcard/file2.txt`



### 3\. Sharding Strategies

  * **Uniform Sharding** : 
    * Set `--sharding-option=uniform`.
    * Set `--uniform-sharding-count={count}` (1-20 for physical, 1-200 for virtual).
  * **Smart Sharding** : 
    * Set `--sharding-option=smart`.
    * Set `--smart-sharding-target-duration={duration}` (ex. `2m`, `10m`, `1h`; valid range: `2m` to `1h`).
    * Set `--smart-sharding-record-name={record_name}` (points to the YAML tracking record inside `--bucket-name` under `automation/smart-sharding/`).
    * Set `--smart-sharding-max-shard-count={max_count}` (optional maximum limit: 0-20 for physical, 0-200 for virtual).



### 4\. Asynchronous Execution

  * **Async & Waiting**: When `--async` is specified, the CLI returns immediately with the created session ID. You can wait for session completion in CI/CD workflows using: `gcloud beta device-run sessions wait <SESSION_ID>`



### 5\. Declarative YAML Configuration (`--flags-file`)

For complex configurations or teams that prefer maintaining version-controlled files instead of long terminal commands, `gcloud` provides a universal `--flags-file` argument preprocessor (see `$ gcloud topic flags-file`):
    
    
    gcloud beta device-run sessions submit instrumentation --flags-file=device-run-flags.yaml
    

> !NOTE **Why keys require`--`:** `gcloud` injects YAML keys directly into the CLI parser as command-line flags. Every key in the YAML file must be prefixed with `--` (ex. `--device:`, `--apps:`). Without `--`, `gcloud` rejects them as unrecognized positional arguments.

Here is an example demonstrating multi-valued list and dictionary flags:
    
    
    # device-run-flags.yaml
    --device:
      -   mediumphone-arm-32
      -   shiba-36
    --apps:
      -   app-debug.apk
      -   test-helper.apk
    --test: app-debug-androidTest.apk
    --bucket-name: my-bucket
    --sharding-option: smart
    --smart-sharding-target-duration: 2m
    --smart-sharding-record-name: timing-record
    --paths-to-pull:
      -   /sdcard/screenshots
      -   /sdcard/coverage.ec
    --additional-test-options:
      coverage: "true"
      clearPackageData: "true"
    

* * *

## Example translations

Use these examples to translate your existing Firebase Test Lab and Flank configurations to device-run.

### Firebase Test Lab to device-run

`firebase cmd`:
    
    
    gcloud firebase test android run \
      --app=app-debug.apk \
      --test=app-debug-androidTest.apk \
      --device model=shiba,version=36 \
      --timeout=5m \
      --num-flaky-test-attempts=2 \
      --directories-to-pull=/sdcard/screenshots \
      --environment-variables coverage=true
    

Translates to:
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device=shiba-36 \
      --apps=app-debug.apk \
      --test=app-debug-androidTest.apk \
      --instrumentation-timeout=5m \
      --flaky-test-attempts=3 \
      --paths-to-pull=/sdcard/screenshots \
      --additional-test-options coverage=true
    

### Flank Configurations to device-run

`flank options` (`flank.yml`):
    
    
    gcloud:
      app: app-debug.apk
      test: app-debug-androidTest.apk
      device:
        -   model: mediumphone-arm
          version: 32
      shard-time: 120
      smart-flank-gcs-path: gs://my-bucket/automation/smart-sharding/timing-record.yaml
    

Translates to:

#### Option 1: Direct CLI Invocation (Recommended)

Translate directly into the modern CLI command:
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device=mediumphone-arm-32 \
      --apps=app-debug.apk \
      --test=app-debug-androidTest.apk \
      --bucket-name=my-bucket \
      --sharding-option=smart \
      --smart-sharding-target-duration=2m \
      --smart-sharding-record-name=timing-record
    

#### Option 2: Declarative YAML Flags File (`--flags-file`)

If you prefer maintaining configurations in a version-controlled YAML file rather than shell script strings, use `gcloud`'s built-in `--flags-file` feature:
    
    
    # device-run-flags.yaml
    # Note: gcloud requires keys to start with '--'
    --device:
      -   mediumphone-arm-32
    --apps:
      -   app-debug.apk
    --test: app-debug-androidTest.apk
    --bucket-name: my-bucket
    --sharding-option: smart
    --smart-sharding-target-duration: 2m
    --smart-sharding-record-name: timing-record
    

Submit with CLI:
    
    
    gcloud beta device-run sessions submit instrumentation --flags-file=device-run-flags.yaml
    

_(You can append or override flags on the command line as well, such as adding`--async`)._

### Device Catalog Discovery

`listing & inspecting devices`:
    
    
    # List all available Android devices
    gcloud beta device-run devices list --filter="platform:android"
    
    # Filter devices with high fleet capacity (replaces legacy list-device-capacities)
    gcloud beta device-run devices list --filter="availability.capacity=CAPACITY_HIGH"
    
    # Describe a specific device (OS versions, form factors, orientation, locales, capacity)
    gcloud beta device-run devices describe redfin-30
    

### End-to-End Session Lifecycle in CI/CD

`submitting, waiting, and inspecting sessions`:
    
    
    # 1. Submit asynchronously and capture session ID
    SESSION_ID=$(gcloud beta device-run sessions submit instrumentation \
      --apps=app-debug.apk \
      --test=app-debug-androidTest.apk \
      --device=mediumphone-arm-32 \
      --async \
      --format="value(name)")
    
    # 2. Wait for session completion in CI/CD pipeline
    gcloud beta device-run sessions wait "$SESSION_ID"
    
    # 3. Describe session summary (or pass --full for complete details)
    gcloud beta device-run sessions describe "$SESSION_ID"
    
    # 4. Cancel a running session if aborted
    gcloud beta device-run sessions cancel "$SESSION_ID"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
