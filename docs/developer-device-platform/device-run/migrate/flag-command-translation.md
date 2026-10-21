---
url: https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation/
title: Firebase Test Lab to Developer Device Platform Command and Flag Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:45.701059+00:00
---

# Firebase Test Lab to Developer Device Platform Command and Flag Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Firebase Test Lab to Developer Device Platform Command and Flag Translation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Developer Device Platform (DDP)** replaces the legacy _Firebase Test Lab_ console and Test Lab CLI workflows with a unified, high-performance, and secure Google Cloud-first testing CLI: `gcloud beta device-run`

This guide provides command-line translations and mappings of flags from Test Lab (or Flank) to DDP. Use this guidance to migrate your tests manually. See [Migrate from Firebase Test Lab to Developer Device Platform](https://docs.cloud.google.com/developer-device-platform/device-run/migrate) for automation tools, benefits, key differences and migration tips.

## Sharding migration

DDP modernizes sharding configurations by natively replacing both Flank's complex Cloud Storage-based smart sharding and Test Lab's uniform sharding.

### Uniform Sharding

  * Set `--sharding-option=uniform`.
  * Set `--uniform-sharding-count={count}` (1-20 for physical, 1-200 for virtual).

  * **Legacy Firebase Test Lab** : `--num-uniform-shards {N}`

  * **DDP CLI** : `--sharding-option=uniform --uniform-sharding-count={N}`




### Smart Sharding

  * Set `--sharding-option=smart`.
  * Set `--smart-sharding-target-duration={duration}` (e.g. `2m`, `10m`, `1h`; valid range: `2m` to `1h`).
  * Set `--smart-sharding-record-name={record_name}` (points to the YAML tracking record inside `--bucket-name` under `automation/smart-sharding/`).
  * Set `--smart-sharding-max-shard-count={max_count}` (optional maximum limit: 0-20 for physical, 0-200 for virtual).



Using historical 30-day timing metadata:

  * **Legacy Flank** :
        
        max-test-shards: 10
        shard-time: 120
        smart-flank-gcs-path: gs://my-bucket/smart-sharding/timing-record.yaml
        

  * **DDP CLI** :
        
        --sharding-option=smart \
        --smart-sharding-max-shard-count=10 \
        --smart-sharding-target-duration=2m \
        --smart-sharding-record-name=timing-record \
        --bucket-name=my-bucket
        

**Note:** Specify `--smart-sharding-record-name` as the YAML base name (excluding the file extension).



## Declarative YAML configuration (`--flags-file`)

For complex configurations or teams that prefer maintaining version-controlled files instead of long terminal commands, `gcloud` provides a universal `--flags-file` argument preprocessor (see `$ gcloud topic flags-file`):

### Android
    
    
    gcloud beta device-run sessions submit instrumentation --flags-file=device-run-flags.yaml
    

### iOS
    
    
    gcloud alpha device-run sessions submit xctest --flags-file=device-run-flags.yaml
    

**Note:** **Why keys require`--`:** `gcloud` injects YAML keys directly into the CLI parser as command-line flags. Every key in the YAML file must be prefixed with `--` (e.g. `--device:`, `--apps:`). Without `--`, `gcloud` rejects them as unrecognized positional arguments.

Here is an example demonstrating a multi-valued list and dictionary flags:

### Android
    
    
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
    

### iOS
    
    
    # device-run-flags.yaml
    --device:
    
        -   iphonese3-18-4
        -   iphone16pro-18-3
    --test: MyTests.zip
    --additional-apps:
        -   helper-app.ipa
    --xcode-version: '16.4'
    --xctest-timeout: 15m
    --other-files-to-push:
      /local/path/test-config.json: com.example.app:/Documents/test-config.json
    --paths-to-pull:
        -   com.example.app:/Documents/screenshots
    --labels:
      env: staging
      team: mobile-qa
    

## End-to-end command translation examples

See these standard and complex translations for concrete examples.

### Example: Run a standard Instrumentation test

**Legacy Firebase CLI:**
    
    
    gcloud firebase test android run \
      --app=app-debug.apk \
      --test=app-debug-androidTest.apk \
      --device model=shiba,version=36 \
      --timeout=5m \
      --num-flaky-test-attempts=2 \
      --directories-to-pull=/sdcard/screenshots \
      --environment-variables key=value
    

**DDP CLI translation:**
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device=shiba-36 \
      --apps=app-debug.apk \
      --test=app-debug-androidTest.apk \
      --instrumentation-timeout=5m \
      --flaky-test-attempts=3 \
      --paths-to-pull=/sdcard/screenshots \
      --additional-test-options key=value
    

**Note:** Firebase Test Lab retry limit (`R=2`) is translated to total execution attempts (`A=3`) in DDP.

### Example: Migrate a complex flank YAML configuration

**Legacy Flank configuration:**
    
    
    app: app-debug.apk
    test: app-debug-androidTest.apk
    device:
      -   model: shiba
        version: 36
    shard-time: 120
    smart-flank-gcs-path: gs://my-bucket/smart-sharding/timing-record.yaml
    

**DDP CLI translation:**
    
    
    gcloud beta device-run sessions submit instrumentation \
      --device=shiba-36 \
      --apps=app-debug.apk \
      --test=app-debug-androidTest.apk \
      --bucket-name=my-bucket \
      --sharding-option=smart \
      --smart-sharding-target-duration=2m \
      --smart-sharding-record-name=timing-record
    

## Post-execution and result retrieval

Since DDP does not launch with a graphical web UI (like the legacy Firebase Console), developers must manage, describe, and inspect results directly using the CLI or programmatic REST APIs:
    
    
    # 1. List active and completed test sessions
    gcloud beta device-run sessions list
    
    # 2. Get a summary and direct Cloud Storage bucket link of a session's results
    gcloud beta device-run sessions describe session-number
    
    # 3. Get detailed metadata and print full results
    gcloud beta device-run sessions describe session-number --full
    
    # 4. Cancel a running session (replaces console cancellation)
    gcloud beta device-run sessions cancel session-number
    

## Flag mapping reference

Here is the flag mapping for migrating test configurations from Flank or `gcloud firebase test android/ios run` to the new DDP `gcloud beta device-run sessions submit instrumentation` and `gcloud alpha device-run sessions submit xctest` commands.

**Tip:** Append `--help` to any `gcloud` command to see detailed usage information.

### Core parameters and assets

Legacy Parameter (Test Lab / Flank) | Target DDP Parameter | Format / Conversion Logic  
---|---|---  
`--app` | `--apps` | **List**. If multiple application APKs/AABs are supplied, pass them all to `--apps` in the order to be installed on the device. Path can be local or in Cloud Storage (`gs://...`).  
`--test` | `--test` | REQUIRED **String**. Path to the test APK containing Instrumentation tests, either local or in Cloud Storage.  
`--client-details` | `--labels` | **Dictionary** of `key=value` pairs to attach to the test session.  
  
### Device configuration and targeting

Legacy Parameter (Test Lab / Flank) | Target DDP Parameter | Format / Conversion Logic  
---|---|---  
`--device model={M},version={V}` | `--device={M}-{V}` | REQUIRED **String** that maps model and OS version to a single `--device` ID string. DDP's `--device` flag accepts multiple device IDs separated by commas (ex. `--device=shiba-34,tokay-36`) or multiple `--device` flags, each specifying a distinct device ID (ex. `--device=shiba-34 --device=tokay-36`).  
`--device locale={L}` | `--locale={L}` | **String**. Maps device locale to top-level `--locale` flag (`language-region`, ex. `--locale=en-US`) to switch the device to before running the test.  
`--device orientation={O}` | `--orientation={O}` | **String**. Maps device orientation to top-level `--orientation` flag (`portrait` or `landscape`).  
_N/A_ | `--coordinates` | **String**. Mocks device GPS location coordinates (ex. `--coordinates=37.4220,-122.0841`).  
  
### Execution control and flakiness

Legacy Parameter (Test Lab / Flank) | Target DDP Parameter | Format / Conversion Logic  
---|---|---  
`--num-flaky-test-attempts {R}` | `--flaky-test-attempts {A}` | **Integer**. The maximum number of execution attempts per test shard. Convert retry count _R_ to total attempts _A_ limit: _A_ = _R_ +1 (defaults to 1).  
_N/A_ | `--flaky-test-parallel-retry` | **Boolean**. Whether to retry test failures in parallel (defaults to `false` for sequential execution).  
_N/A_ | `--flaky-test-retry-level` | **String**. Defines whether to retry at the `shard` or individual `test` level (defaults to `shard`).  
`--async` | `--async` | **Boolean**. Maps 1:1. Command executes synchronously by default. Pass this to return to the terminal immediately. Exits immediately after file upload and prints operation and session IDs.  
  
### Test runner and targets

Legacy Parameter (Test Lab / Flank) | Target DDP Parameter | Format / Conversion Logic  
---|---|---  
`--environment-variables` | `--additional-test-options` | **Dictionary** of options passed to the Instrumentation test runner. Formats supported in `--test-targets` are not allowed here.  
`--test-targets` | `--test-targets` | **Dictionary** of test targets or target filters to run. Each target must be fully qualified with the package name or class name supporting keys such as `package`, `notPackage`, `class`, `notClass`, `annotation`, `notAnnotation`, and `size`. Formats `testfile` or `notTestfile` are not supported.  
`--use-orchestrator` | `--orchestrator-version` | Whether to use Android Test Orchestrator. Takes `auto` (default orchestrator) or specific version string (ex. `1.6`). Available versions can be queried using `gcloud beta device-run software-versions list`.  
`--test-runner-class` | `--test-runner-class` | **String**. The fully-qualified Instrumentation test runner class (ex. `com.foo.MyRunner`) to use. If not specified, a default runner class is determined by examining the application's manifest.  
`--directories-to-pull` | `--paths-to-pull` | **List**. Directories to download from the device after test run.  
`--other-files` | `--other-files-to-push` | **Dictionary**. Comma-separated `SOURCE=DEST` list of auxiliary files to push to the device prior to test run.  
  
### Output and storage

Legacy Parameter (Test Lab / Flank) | Target DDP Parameter | Format / Conversion Logic  
---|---|---  
`--results-bucket` | `--bucket-name` | **String**. Cloud Storage bucket where test artifacts, including local input files, test output files, and smart sharding timing records, are uploaded (defaults to `gs://[PROJECT_ID]-devicerun` if not specified).  
`--results-dir` | _Managed automatically_ | **Unsupported**. Sub-paths are automatically organized in Cloud Storage under `automation/sessions/{session_id}/`.  
  
### Sharding configuration

Legacy Parameter (Test Lab / Flank) | Target DDP Parameter | Format / Conversion Logic  
---|---|---  
`--num-uniform-shards {N}` | `--sharding-option=uniform --uniform-sharding-count={N}` | **String** and **Integer**. Combined flag configuration both activates uniform sharding strategy and sets max shard count (valid count range: 1-20 physical, 1-200 virtual).  
Flank `--max-test-shards {N}` | `--sharding-option=smart --smart-sharding-max-shard-count={N}` | **String** and **Integer**. Combined flag configuration both activates smart sharding strategy and sets max shard count (valid count range: 0-20 physical, 0-200 virtual).  
Flank `--shard-time {S}` | `--sharding-option=smart --smart-sharding-target-duration={S}` | REQUIRED **String**. Activates smart sharding with target execution time (ex. `2m`, `10m`, `1h`). Valid range: `2m` to `1h`.  
Flank `--smart-flank-gcs-path` | `--smart-sharding-record-name={name} --bucket-name={bucket}` | REQUIRED **String**. Name of the sharding record YAML (excluding file extension) inside `--bucket-name` under `smart-sharding/` in Cloud Storage.  
  
### Android-specific flags

Use this table to map legacy `gcloud firebase test android run` flags to their new `device-run` equivalents:

Legacy Parameter (`firebase android`) | Target DDP Parameter | Format / Conversion Logic  
---|---|---  
`--additional-apks` | `--apps` | **List**. Merge additional list values directly into the main `--apps` list.  
_N/A_ | `--bugreport` | **String**. Collect a full `bugreport` from the device (values: `always`, `on-failure`).  
_N/A_ | `--dumpsys` | **String**. Collect system state using `dumpsys` (values: `always`, `on-failure`).  
`--timeout` | `--instrumentation-timeout` | **Duration** (ex. `10m`, `20s`, `1h`). Valid range: `1m` to `3h` (defaults to `5m`).  
`--record-video` | `--video` | **String**. When to record video of the device screen during the test run.Valid values are `always` or `on-failure`.  
  
### iOS-specific flags

Use this table to map legacy `gcloud firebase test ios run` flags to their new `device-run` equivalents:

Legacy Parameter (`firebase ios`) | Target DDP Parameter | Format / Conversion Logic  
---|---|---  
`--test` | `--test` | Path to built XCTest zip.  
`--device model={M},version={V}` | `--device={M}-{V}` | Target device ID string.  
`--device locale={L}` | `--locale={L}` | Target locale string (`language-region`, ex. `--locale=en-US`).  
`--timeout` | `--xctest-timeout` | Duration (e.g. `5m`). Range: `1m` to `1h`.  
`--xcode-version` | `--xcode-version` | Catalog ID or version string of Xcode to use (ex. `xcode-16-4` or `16.4`). Available versions can be queried using `gcloud beta device-run software-versions list`.  
`--results-bucket` | `--bucket-name` | Custom destination GCS bucket.  
`--async` | `--async` | Synchronous by default, pass to exit immediately.  
`--other-files` | `--other-files-to-push` | Dictionary in `SOURCE=BUNDLE_ID:DEST` format.  
`--directories-to-pull` | `--paths-to-pull` | List in `BUNDLE_ID:DEVICE_PATH` format.  
`--additional-ipas` | `--additional-apps` | List of helper IPAs to install prior to test.  
`--xctestrun-file` | `--xctestrun-file` | Path to custom `.xctestrun` plist.  
`--num-flaky-test-attempts` | `--flaky-test-attempts` | Integer count of retry attempts (e.g. `3`).  
`--client-details` | `--labels` | Key-value pairs (`KEY=VALUE`).  
  
## Feedback and questions

[Contact us](https://docs.cloud.google.com/developer-device-platform/quickstart#contact-us) to file bugs and feature requests or join our discussion forum.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
