---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions
title: REST Resource: projects.locations.sessions \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:09:14.269640+00:00
---

# REST Resource: projects.locations.sessions  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  REST Resource: projects.locations.sessions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Session
    * JSON representation
  * SessionConfig
    * JSON representation
  * JobConfig
    * JSON representation
  * JobSettings
    * JSON representation
  * RetrySettings
    * JSON representation
  * FlakyTestRetryStrategy
    * JSON representation
  * TestReductionMode
  * JobAction
    * JSON representation
  * AndroidInstrumentationTest
    * JSON representation
  * UniformSharding
    * JSON representation
  * SmartSharding
    * JSON representation
  * InputFile
    * JSON representation
  * GcsPath
    * JSON representation
  * AndroidInstallable
    * JSON representation
  * AndroidNativeBinary
    * JSON representation
  * IosXcTest
    * JSON representation
  * AllocationConfig
    * JSON representation
  * DeviceConfig
    * JSON representation
  * DeviceRequirement
    * JSON representation
  * DeviceAction
    * JSON representation
  * AndroidOrientationDeviceAction
    * JSON representation
  * AndroidLogcatDeviceAction
  * AndroidSwitchLocaleDeviceAction
    * JSON representation
  * AndroidRecordVideoDeviceAction
    * JSON representation
  * AndroidPushFilesDeviceAction
    * JSON representation
  * FileConfig
    * JSON representation
  * AndroidPullFilesDeviceAction
    * JSON representation
  * AndroidInstallPackagesDeviceAction
    * JSON representation
  * AndroidBugreportDeviceAction
    * JSON representation
  * AndroidDumpsysDeviceAction
    * JSON representation
  * AndroidMockLocationDeviceAction
    * JSON representation
  * LatLng
    * JSON representation
  * IosPushFilesDeviceAction
    * JSON representation
  * FileConfig
    * JSON representation
  * IosPullFilesDeviceAction
    * JSON representation
  * PathConfig
    * JSON representation
  * IosInstallPackagesDeviceAction
    * JSON representation
  * IosRecordVideoDeviceAction
    * JSON representation
  * IosAppPrivacyReportDeviceAction
  * IosSwitchLocaleDeviceAction
    * JSON representation
  * SessionNotificationConfig
    * JSON representation
  * SessionOutputFileDirectoryConfig
    * JSON representation
  * SessionReport
    * JSON representation
  * JobReport
    * JSON representation
  * ExecutionReport
    * JSON representation
  * Status
    * JSON representation
  * StatusType
  * Result
    * JSON representation
  * ResultType
  * ResultCause
    * JSON representation
  * IssueSummary
    * JSON representation
  * IssueType
  * Warning
    * JSON representation
  * OutputFile
    * JSON representation
  * Methods



## Resource: Session

A session resource in the AutomationSession API.

At a high level, `Session` describes the configuration of one or multiple jobs, the state transitions it goes through, and the results.

JSON representation  
---  
      
    
    {
      "name": string,
      "sessionConfig": {
        object ([SessionConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SessionConfig))
      },
      "sessionReport": {
        object ([SessionReport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SessionReport))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the session. Format: `projects/{project}/locations/{location}/sessions/{session}`.  
`sessionConfig` |  `object (`[SessionConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SessionConfig)`)` Required. Configuration used to create the session.  
`sessionReport` |  `object (`[SessionReport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SessionReport)`)` Output only. The runtime information and result report of the session.  
  
## SessionConfig

SessionConfig is used to create a session.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "jobConfigs": [
        {
          object ([JobConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#JobConfig))
        }
      ],
      "notificationConfig": {
        object ([SessionNotificationConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SessionNotificationConfig))
      },
      "outputDirectoryConfig": {
        object ([SessionOutputFileDirectoryConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SessionOutputFileDirectoryConfig))
      }
    }  
  
Fields  
---  
`displayName` |  `string` Optional. User-settable, human-readable name for the session.Maximum size is 63 bytes when encoded as UTF-8. If set, must match regex: `^[A-Za-z0-9][A-Za-z0-9-_ ]*$`.  
`jobConfigs[]` |  `object (`[JobConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#JobConfig)`)` Required. Configs of the jobs in the session.  
`notificationConfig` |  `object (`[SessionNotificationConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SessionNotificationConfig)`)` Optional. Notification config for the session.  
`outputDirectoryConfig` |  `object (`[SessionOutputFileDirectoryConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SessionOutputFileDirectoryConfig)`)` Required. Output file directory config for the session.  
  
## JobConfig

The configuration of a job.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "settings": {
        object ([JobSettings](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#JobSettings))
      },
      "action": {
        object ([JobAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#JobAction))
      },
      "allocationConfig": {
        object ([AllocationConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AllocationConfig))
      },
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`displayName` |  `string` Optional. User-settable, human-readable name for the job.If set, it must be unique within the session. If not set, the display name will default to `job-<index>`, where `<index>` is the 0-based index of the job in the session formatted as three digits (ex. job-000, job-001, ...).Maximum size is 63 bytes when encoded as UTF-8. If set, must match regex: `^[A-Za-z0-9][A-Za-z0-9-_ ]*$`.  
`settings` |  `object (`[JobSettings](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#JobSettings)`)` Optional. Job settings.  
`action` |  `object (`[JobAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#JobAction)`)` Required. Job action.  
`allocationConfig` |  `object (`[AllocationConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AllocationConfig)`)` Required. Allocation config.  
`labels` |  `map (key: string, value: string)` Optional. User-defined metadata for tracking or categorization. These labels do not affect job execution and are surfaced in the JobReport.Limits:

  * Maximum number of entries: 16.
  * Maximum key size: 32 bytes (UTF-8).
  * Maximum value size: 1024 bytes (UTF-8).

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## JobSettings

Job settings to control the job execution.

JSON representation  
---  
      
    
    {
      "retrySettings": {
        object ([RetrySettings](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#RetrySettings))
      }
    }  
  
Fields  
---  
`retrySettings` |  `object (`[RetrySettings](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#RetrySettings)`)` Optional. The retry settings of the job.  
  
## RetrySettings

Retry settings.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "flakyTestRetryStrategy": {
        object ([FlakyTestRetryStrategy](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#FlakyTestRetryStrategy))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The retry strategy of the job. If not set, the default retry strategy is flaky_test_retry_strategy. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`flakyTestRetryStrategy` |  `object (`[FlakyTestRetryStrategy](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#FlakyTestRetryStrategy)`)` Optional. The default retry strategy. Allows an Execution to retry on test failures and infrastructure errors.  
End of mutually exclusive fields.  
  
## FlakyTestRetryStrategy

Default retry strategy. It will retry on test failures for up to flakyTestAttempts (including the initial run). It also retries on infra issues for up to 2 attempts (including the initial run). So in total, an execution can run up to flakyTestAttempts * 2 times in the worst case.

JSON representation  
---  
      
    
    {
      "flakyTestAttempts": integer,
      "parallelRetry": boolean,
      "testReductionMode": enum ([TestReductionMode](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#TestReductionMode))
    }  
  
Fields  
---  
`flakyTestAttempts` |  `integer` Required. The total attempts for flaky tests, including the initial run. Default value: 1 (no retry). Range: [1, 5].  
`parallelRetry` |  `boolean` Optional. Whether to retry the test failures in parallel. By default, the test is retried sequentially. If true, when the initial attempt fails, (flakyTestAttempts - 1) attempts will be triggered at the same time to run in parallel.  
`testReductionMode` |  `enum (`[TestReductionMode](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#TestReductionMode)`)` Optional. The mode of test reduction for retry. If the test runner doesn't support the specified test reduction mode, the request will be rejected with an `INVALID_ARGUMENT` error.  
  
## TestReductionMode

Determines how the test cases are reduced for retry.

Enums  
---  
`TEST_REDUCTION_MODE_UNSPECIFIED` | The test reduction mode is unspecified. Will default to `NO_REDUCTION`.  
`NO_REDUCTION` | Runs the same set of test cases of the previous attempt.  
`REDUCE_TO_FAILED_TEST_CASES` | Only runs the failed test cases of the previous attempt.For Android Instrumentation tests, this reduction mode only works when the tests in the test APK use one of the following test runners:

  * `androidx.test.ext.junit.runners.AndroidJUnit4`
  * `org.junit.runners.JUnit4` \- `com.google.testing.junit.testparameterinjector.TestParameterInjector`
  * `org.junit.runners.Parameterized`

Otherwise, its behavior will fall back to `NO_REDUCTION`.  
  
## JobAction

The action to be performed in a job.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "androidInstrumentationTest": {
        object ([AndroidInstrumentationTest](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstrumentationTest))
      },
      "androidNativeBinary": {
        object ([AndroidNativeBinary](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidNativeBinary))
      },
      "iosXcTest": {
        object ([IosXcTest](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosXcTest))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The specific job action to perform. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`androidInstrumentationTest` |  `object (`[AndroidInstrumentationTest](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstrumentationTest)`)` Android instrumentation test.  
`androidNativeBinary` |  `object (`[AndroidNativeBinary](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidNativeBinary)`)` Android native binary execution.  
`iosXcTest` |  `object (`[IosXcTest](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosXcTest)`)` iOS XCTest.  
End of mutually exclusive fields.  
  
## AndroidInstrumentationTest

The configuration of an Android instrumentation test.

See <https://developer.android.com/training/testing/instrumented-tests> for more information on Android instrumentation tests.

JSON representation  
---  
      
    
    {
      "testInstallable": {
        object ([AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable))
      },
      "testRunnerClass": string,
      "testTargets": [
        string
      ],
      "enableCodeCoverage": boolean,
      "additionalTestOptions": {
        string: string,
        ...
      },
      "orchestratorVersion": string,
      "instrumentationTimeout": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "uniformSharding": {
        object ([UniformSharding](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#UniformSharding))
      },
      "smartSharding": {
        object ([SmartSharding](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SmartSharding))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`testInstallable` |  `object (`[AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable)`)` Required. The test package to install and run the test.  
`testRunnerClass` |  `string` Optional. Full class name of the test runner class.The class must be `androidx.test.runner.AndroidJUnitRunner` or a subclass of it.The default value is determined by examining the application's manifest. If multiple instrumentations are found, the first one in the manifest will be used.  
`testTargets[]` |  `string` Optional. A list of test targets or target filters to run.Each target must be fully qualified with the package name or class name, in one of these formats:

  * `package package_name`
  * `notPackage com.package.to.skip`
  * `class package_name.class_name`
  * `class package_name.class_name#methodName`
  * `notClass com.foo.ClassToSkip`
  * `notClass com.foo.ClassName#testMethodToSkip`
  * `annotation com.foo.AnnotationToRun`
  * `notAnnotation com.foo.AnnotationToSkip`
  * `size [small|medium|large]`

Formats like `testfile` or `notTestfile` won't be supported.If empty, all targets in the module will be run.Limits:

  * Maximum number of entries: 1024.

  
`enableCodeCoverage` |  `boolean` Optional. Whether to enable code coverage collection for the test.A coverage file `coverage.ec` will be uploaded to the results folder. For this to work, your classes have to be instrumented offline (build time) by EMMA/JaCoCo.  
`additionalTestOptions` |  `map (key: string, value: string)` Optional. Additional test options to pass to the test runner.Passed to `am instrument` command as `-e` options, which will be passed to the instrumentation test runner using its `onCreate()` method.Formats supported in testTargets are not allowed to be used here.Limits:

  * Maximum number of entries: 32.
  * Maximum key size: 64 bytes (UTF-8).
  * Maximum value size: 1024 bytes (UTF-8).

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`orchestratorVersion` |  `string` Optional. The version of the Android Test Orchestrator to use for the test.The available orchestrator versions can be retrieved from the catalog service. If set to "auto", the default orchestrator is used. If not set, no orchestrator is used.  
`instrumentationTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout of the instrumentation test. Default value: 5 min. Range: [1 min, 3 hours].A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
The sharding option of the test. If not set, no sharding will be performed and the test will be run as a single shard. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`uniformSharding` |  `object (`[UniformSharding](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#UniformSharding)`)` Optional. Uniform sharding strategy to split the job into multiple shards with equal number of test methods.  
`smartSharding` |  `object (`[SmartSharding](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#SmartSharding)`)` Optional. Smart sharding strategy to split the job into multiple shards based on the test methods and their execution time.  
End of mutually exclusive fields.  
  
## UniformSharding

Uniformly shards test cases given a total number of shards.

It will be translated to `-e numShard` and `-e shardIndex` AndroidJUnitRunner arguments. With uniform sharding enabled, specifying either of these sharding arguments via `environment_variables` is invalid.

Based on the sharding mechanism AndroidJUnitRunner uses, there is no guarantee that test cases will be distributed uniformly across all shards.

JSON representation  
---  
      
    
    {
      "shardCount": integer
    }  
  
Fields  
---  
`shardCount` |  `integer` Required. The total number of shards to create. This must always be a positive number that is no greater than the total number of test cases.Limits:

  * For physical devices, the number of shards must be <= 20.
  * For virtual devices, the number of shards must be <= 200.

  
  
## SmartSharding

The smart sharding strategy to split the job into multiple shards based on the test methods and their recorded execution time.

JSON representation  
---  
      
    
    {
      "targetedShardDuration": string,
      "timingRecord": {
        object ([InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile))
      },
      "maxShardCount": integer
    }  
  
Fields  
---  
`targetedShardDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The targeted duration of each shard.Limits:

  * Must be at least 2 minutes.
  * Must be at most 3 hours.

Shard duration is not guaranteed because smart sharding uses test case history and default durations which may not be accurate. Durations are calculated based on the following inputs:

  * Timing records from previous runs of the same test case.
  * For new test cases, the average duration of other known test cases.
  * A system-chosen, default duration if there are no previous timing records available.

Because the actual shard duration can exceed the targeted shard duration, we recommend that you set the targeted value at least 5 minutes less than the maximum allowed instrumentation timeout. This approach avoids cancelling the shard before all tests can finish.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timingRecord` |  `object (`[InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile)`)` Required. The timing record file to use for smart sharding.If the file does not exist, smart sharding will use default test time (30s) for each test method to shard the job into multiple shards.This file will be overwritten with the latest timing record after the job is completed.  
`maxShardCount` |  `integer` Optional. The maximum number of shards to create. If unset or less than 1, system-defined max limits are used. This limit takes precedence if the targetedShardDuration cannot be satisfied.Limits:

  * For physical devices, the number of shards must be <= 20.
  * For virtual devices, the number of shards must be <= 200.

  
  
## InputFile

Input file.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsInputFile": {
        object ([GcsPath](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#GcsPath))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsInputFile` |  `object (`[GcsPath](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#GcsPath)`)` An input file in Google Cloud Storage.  
End of mutually exclusive fields.  
  
## GcsPath

A path to a file or directory in Google Cloud Storage.

JSON representation  
---  
      
    
    {
      "path": string
    }  
  
Fields  
---  
`path` |  `string` Required. The Google Cloud Storage path of the file or directory. Format: `gs://<bucket_name>/<object_path>`.  
  
## AndroidInstallable

An Android Installable represents the file(s) for installing an Android package on a device.

This can be an APK, an Android App Bundle (AAB), or an APK Set.

JSON representation  
---  
      
    
    {
      "files": [
        {
          object ([InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile))
        }
      ]
    }  
  
Fields  
---  
`files[]` |  `object (`[InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile)`)` Required. Files that make up the package.Supported formats are distinguished by their file extension:

  * APK: One or more files with extension `.apk`.
  * App Bundle: A single file with extension `.aab`.
  * APK Set: A single file with extension `.apks`.

  
  
## AndroidNativeBinary

The configuration of an Android native binary execution.

JSON representation  
---  
      
    
    {
      "androidNativeBinary": {
        object ([InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile))
      },
      "executionTimeout": string,
      "args": [
        string
      ],
      "envVars": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`androidNativeBinary` |  `object (`[InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile)`)` Required. The file path of the Android native binary.  
`executionTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout of the execution. Default value: 5 min. Range: [1 min, 3 hours].A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`args[]` |  `string` Optional. Arguments for running the binary file. The flags will be appended to the command line that invokes the binary.Limits:

  * Maximum number of entries: 64
  * Maximum entry size: 1024 bytes (UTF-8)

  
`envVars` |  `map (key: string, value: string)` Optional. A map of environment variables to set for the binary process. The keys are the variable names and the values are the variable values.Limits:

  * Maximum number of entries: 32
  * Maximum key size: 64 bytes (UTF-8)
  * Key regex: `[a-zA-Z_][a-zA-Z0-9_]*`
  * Maximum value size: 1024 bytes (UTF-8)

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## IosXcTest

The configuration of an iOS XCTest.

JSON representation  
---  
      
    
    {
      "testsZip": {
        object ([InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile))
      },
      "xctestrun": {
        object ([InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile))
      },
      "xcodeVersion": string,
      "xcTestTimeout": string
    }  
  
Fields  
---  
`testsZip` |  `object (`[InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile)`)` Required. The .zip containing the .xctestrun file and the contents of the DerivedData/Build/Products directory.  
`xctestrun` |  `object (`[InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile)`)` Optional. An .xctestrun file that will override the .xctestrun file in the tests zip.  
`xcodeVersion` |  `string` Optional. The Xcode version that should be used for the test.If not set, a system-default Xcode version is used. The available Xcode versions can be retrieved from the catalog service.  
`xcTestTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout of the test. Default value: 5 min. Range: [1 min, 3 hours].A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## AllocationConfig

Allocation config.

JSON representation  
---  
      
    
    {
      "deviceConfigs": [
        {
          object ([DeviceConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#DeviceConfig))
        }
      ]
    }  
  
Fields  
---  
`deviceConfigs[]` |  `object (`[DeviceConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#DeviceConfig)`)` Required. At least one device config is required. If more than one device config is required, the multiple devices are allocated to each shard of the OmniLab job to run multi-device-interaction tests.  
  
## DeviceConfig

The configuration of a run on a device.

JSON representation  
---  
      
    
    {
      "requirement": {
        object ([DeviceRequirement](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#DeviceRequirement))
      },
      "actions": [
        {
          object ([DeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#DeviceAction))
        }
      ]
    }  
  
Fields  
---  
`requirement` |  `object (`[DeviceRequirement](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#DeviceRequirement)`)` Required. The requirement of the device.  
`actions[]` |  `object (`[DeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#DeviceAction)`)` Optional. The actions to be performed on the device. Actions will be executed in the order they are specified in the list.Each action type can at most have 1 instance in the list.  
  
## DeviceRequirement

The requirement of a device.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "deviceId": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The specific device requirement. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`deviceId` |  `string` The device ID of a device in the catalog.The device ID is the last part of a device's resource name.  
End of mutually exclusive fields.  
  
## DeviceAction

The action to be performed on a device.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "androidOrientation": {
        object ([AndroidOrientationDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidOrientationDeviceAction))
      },
      "androidLogcat": {
        object ([AndroidLogcatDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidLogcatDeviceAction))
      },
      "androidSwitchLocale": {
        object ([AndroidSwitchLocaleDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidSwitchLocaleDeviceAction))
      },
      "androidRecordVideo": {
        object ([AndroidRecordVideoDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidRecordVideoDeviceAction))
      },
      "androidPushFiles": {
        object ([AndroidPushFilesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidPushFilesDeviceAction))
      },
      "androidPullFiles": {
        object ([AndroidPullFilesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidPullFilesDeviceAction))
      },
      "androidInstallPackages": {
        object ([AndroidInstallPackagesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallPackagesDeviceAction))
      },
      "androidBugreport": {
        object ([AndroidBugreportDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidBugreportDeviceAction))
      },
      "androidDumpsys": {
        object ([AndroidDumpsysDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidDumpsysDeviceAction))
      },
      "androidMockLocation": {
        object ([AndroidMockLocationDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidMockLocationDeviceAction))
      },
      "iosPushFiles": {
        object ([IosPushFilesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosPushFilesDeviceAction))
      },
      "iosPullFiles": {
        object ([IosPullFilesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosPullFilesDeviceAction))
      },
      "iosInstallPackages": {
        object ([IosInstallPackagesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosInstallPackagesDeviceAction))
      },
      "iosRecordVideo": {
        object ([IosRecordVideoDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosRecordVideoDeviceAction))
      },
      "iosAppPrivacyReport": {
        object ([IosAppPrivacyReportDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosAppPrivacyReportDeviceAction))
      },
      "iosSwitchLocale": {
        object ([IosSwitchLocaleDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosSwitchLocaleDeviceAction))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The specific device action to perform. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`androidOrientation` |  `object (`[AndroidOrientationDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidOrientationDeviceAction)`)` Sets the orientation of the device.  
`androidLogcat` |  `object (`[AndroidLogcatDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidLogcatDeviceAction)`)` Collects logcat output from the device.  
`androidSwitchLocale` |  `object (`[AndroidSwitchLocaleDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidSwitchLocaleDeviceAction)`)` Switches the locale (language and region) of the device.  
`androidRecordVideo` |  `object (`[AndroidRecordVideoDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidRecordVideoDeviceAction)`)` Records a video of the device screen during the run.  
`androidPushFiles` |  `object (`[AndroidPushFilesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidPushFilesDeviceAction)`)` Pushes files to the device at the beginning of the run.  
`androidPullFiles` |  `object (`[AndroidPullFilesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidPullFilesDeviceAction)`)` Pulls directories and files from the device at the end of the run.  
`androidInstallPackages` |  `object (`[AndroidInstallPackagesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallPackagesDeviceAction)`)` Installs Android packages on the device.  
`androidBugreport` |  `object (`[AndroidBugreportDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidBugreportDeviceAction)`)` Captures a bugreport from the device unless the test result is pass.  
`androidDumpsys` |  `object (`[AndroidDumpsysDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidDumpsysDeviceAction)`)` Captures a dumpsys from the device.  
`androidMockLocation` |  `object (`[AndroidMockLocationDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidMockLocationDeviceAction)`)` Mocks the location of the device.  
`iosPushFiles` |  `object (`[IosPushFilesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosPushFilesDeviceAction)`)` Pushes files to the iOS device sandbox at the beginning of the run.  
`iosPullFiles` |  `object (`[IosPullFilesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosPullFilesDeviceAction)`)` Pulls directories and files from the iOS device sandbox at the end of the run.  
`iosInstallPackages` |  `object (`[IosInstallPackagesDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosInstallPackagesDeviceAction)`)` Installs additional iOS packages on the device.  
`iosRecordVideo` |  `object (`[IosRecordVideoDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosRecordVideoDeviceAction)`)` Records a video of the iOS device screen during the run.  
`iosAppPrivacyReport` |  `object (`[IosAppPrivacyReportDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosAppPrivacyReportDeviceAction)`)` Collects the exported iOS App Privacy Report during the run.  
`iosSwitchLocale` |  `object (`[IosSwitchLocaleDeviceAction](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IosSwitchLocaleDeviceAction)`)` Switches the locale (language and region) of the iOS application.  
End of mutually exclusive fields.  
  
## AndroidOrientationDeviceAction

Sets the orientation of the device.

JSON representation  
---  
      
    
    {
      "orientation": string
    }  
  
Fields  
---  
`orientation` |  `string` Required. The orientation to set the device to.One of `portrait` or `landscape`.  
  
## AndroidLogcatDeviceAction

This type has no fields.

Collects logcat output from the device.

The output will be written to a file named `logcat.txt` in the execution output directory.

## AndroidSwitchLocaleDeviceAction

Switches the locale (language and region) of the device.

JSON representation  
---  
      
    
    {
      "localeCode": string
    }  
  
Fields  
---  
`localeCode` |  `string` Required. The locale (language and region) to switch the device to.The format is `language-region`, ex. "en-US", "zh-CN", etc. The typical language value is a two or three-letter language code as defined in ISO639. The typical region value is a two-letter ISO 3166 code or a three-digit UN M.49 area code.  
  
## AndroidRecordVideoDeviceAction

Records a video of the device screen during the run.

The video will be written to a file named `video.mp4` in the execution output directory.

JSON representation  
---  
      
    
    {
      "discardOnPass": boolean
    }  
  
Fields  
---  
`discardOnPass` |  `boolean` Optional. Whether to discard and not upload the recording when the test passes. Default is false.  
  
## AndroidPushFilesDeviceAction

Pushes files to the device at the beginning of the run.

Files are overwritten if a file with the same path already exists on the device, if device permissions allow.

JSON representation  
---  
      
    
    {
      "fileConfigs": [
        {
          object ([FileConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#FileConfig))
        }
      ]
    }  
  
Fields  
---  
`fileConfigs[]` |  `object (`[FileConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#FileConfig)`)` Required. Configs of pushing files to the device.Limits:

  * A maximum of 50 files are allowed.

  
  
## FileConfig

The configuration of pushing a file to the device.

JSON representation  
---  
      
    
    {
      "sourceFile": {
        object ([InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile))
      },
      "destinationPath": string
    }  
  
Fields  
---  
`sourceFile` |  `object (`[InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile)`)` Required. The file to be pushed to the device.  
`destinationPath` |  `string` Required. The destination path on the device.  
  
## AndroidPullFilesDeviceAction

Pulls directories and files from the device at the end of the run.

Files will be copied to the '/artifacts' directory, with the absolute path structure preserved.

Note that:

  1. A clean device is provided for the run.
  2. Any existing files in the output directory may be overwritten.
  3. Pulling files is best effort. Will skip files if they don't exist on the device.

JSON representation  
---  
      
    
    {
      "paths": [
        string
      ]
    }  
  
Fields  
---  
`paths[]` |  `string` Required. Absolute directory or file paths to pull from the device.Limits:

  * A maximum of 10 paths are allowed.

  
  
## AndroidInstallPackagesDeviceAction

Installs Android packages on the device.

At least one installable is specified when using this device action.

Limits:

  * A maximum of 20 installables in total are allowed.
  * A maximum of 100 files are allowed in total across all installables.

JSON representation  
---  
      
    
    {
      "installables": [
        {
          object ([AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable))
        }
      ],
      "preTargetAppInstallables": [
        {
          object ([AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable))
        }
      ],
      "targetApp": {
        object ([AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable))
      },
      "postTargetAppInstallables": [
        {
          object ([AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable))
        }
      ]
    }  
  
Fields  
---  
`installables[]  
**(deprecated)**` |  `object (`[AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable)`)` This item is deprecated!Optional. Deprecated: use `preTargetAppInstallables`, `targetApp` and `postTargetAppInstallables` instead.The Android packages to install on the device. The installation will be performed in the order specified, before the installables of all other fields.  
`preTargetAppInstallables[]` |  `object (`[AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable)`)` Optional. The Android packages to install on the device before `targetApp` (if specified) is installed.The installation will be performed in the order specified.  
`targetApp` |  `object (`[AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable)`)` Optional. The primary Android package to install, serving as the target package for subsequent actions and as the installation ordering anchor.Whether this package is treated as the application under test depends on the job action:

  * Actions that require an explicit target package (such as performance metrics collection, or accessibility scans) use this package to identify the application to inspect or drive.
  * Actions that discover or manage targets independently (such as Android instrumentation tests, where target packages are defined in the test runner manifest) treat this field primarily as an installation order anchor between pre- and post-installables.

Optional. If omitted, all packages in `preTargetAppInstallables` and `postTargetAppInstallables` are installed without a designated target package.  
`postTargetAppInstallables[]` |  `object (`[AndroidInstallable](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#AndroidInstallable)`)` Optional. The Android packages to install on the device after `targetApp` (if specified) is installed.The installation will be performed in the order specified.  
  
## AndroidBugreportDeviceAction

Captures a bugreport from the device.

The output will be written to a file named `bugreport.zip` in the execution output directory.

JSON representation  
---  
      
    
    {
      "collectOnPass": boolean
    }  
  
Fields  
---  
`collectOnPass` |  `boolean` Optional. Whether to deliver the bugreport when the test passes. If false, the bugreport is skipped on pass to save time (default behavior). If true, the bugreport is always delivered.  
  
## AndroidDumpsysDeviceAction

Captures dumpsys output from the device.

The output will be written to a file named `dumpsys.log` in the execution output directory.

JSON representation  
---  
      
    
    {
      "collectOnPass": boolean
    }  
  
Fields  
---  
`collectOnPass` |  `boolean` Optional. Whether to deliver the dumpsys when the test passes. If false, the dumpsys is skipped on pass to save time (default behavior). If true, the dumpsys is always delivered.  
  
## AndroidMockLocationDeviceAction

Mocks the location of the Android device.

JSON representation  
---  
      
    
    {
      "location": {
        object ([LatLng](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#LatLng))
      }
    }  
  
Fields  
---  
`location` |  `object (`[LatLng](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#LatLng)`)` Required. The mock location to set on the device.  
  
## LatLng

An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the [ WGS84 standard](https://en.wikipedia.org/wiki/World_Geodetic_System#1984_version). Values must be within normalized ranges.

JSON representation  
---  
      
    
    {
      "latitude": number,
      "longitude": number
    }  
  
Fields  
---  
`latitude` |  `number` The latitude in degrees. It must be in the range [-90.0, +90.0].  
`longitude` |  `number` The longitude in degrees. It must be in the range [-180.0, +180.0].  
  
## IosPushFilesDeviceAction

Pushes files to the iOS device sandbox at the beginning of the run.

JSON representation  
---  
      
    
    {
      "fileConfigs": [
        {
          object ([FileConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#FileConfig_1))
        }
      ]
    }  
  
Fields  
---  
`fileConfigs[]` |  `object (`[FileConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#FileConfig_1)`)` Required. Configs of pushing files to the device.Limits: - A maximum of 50 files are allowed.  
  
## FileConfig

The configuration of pushing a file to the iOS device.

JSON representation  
---  
      
    
    {
      "sourceFile": {
        object ([InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile))
      },
      "bundleId": string,
      "destinationPath": string
    }  
  
Fields  
---  
`sourceFile` |  `object (`[InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile)`)` Required. The file to be pushed.  
`bundleId` |  `string` Required. The bundle ID of the application sandbox.  
`destinationPath` |  `string` Required. The destination path relative to the app sandbox, ex. "/Documents/file.txt".  
  
## IosPullFilesDeviceAction

Pulls directories and files from the iOS device sandbox at the end of the run.

JSON representation  
---  
      
    
    {
      "paths": [
        {
          object ([PathConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#PathConfig))
        }
      ]
    }  
  
Fields  
---  
`paths[]` |  `object (`[PathConfig](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#PathConfig)`)` Required. Absolute directory or file paths to pull from the device.Limits: - A maximum of 10 paths are allowed.  
  
## PathConfig

The configuration of pulling a file or directory from the iOS device.

JSON representation  
---  
      
    
    {
      "bundleId": string,
      "devicePath": string
    }  
  
Fields  
---  
`bundleId` |  `string` Required. The bundle ID of the application sandbox.  
`devicePath` |  `string` Required. The device path relative to the app sandbox, ex. "/Documents/output/".  
  
## IosInstallPackagesDeviceAction

Installs iOS packages on the device.

JSON representation  
---  
      
    
    {
      "ipas": [
        {
          object ([InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile))
        }
      ]
    }  
  
Fields  
---  
`ipas[]` |  `object (`[InputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#InputFile)`)` Required. Additional iOS packages (IPAs) to install on the device.Limits: - A maximum of 20 IPAs are allowed.  
  
## IosRecordVideoDeviceAction

Records a video of the iOS device screen during the run.

The video will be written to a file named `video.mp4` in the execution output directory.

JSON representation  
---  
      
    
    {
      "discardOnPass": boolean
    }  
  
Fields  
---  
`discardOnPass` |  `boolean` Optional. Whether to discard the video if the test passes. If not specified, the default is false (always keep the video).  
  
## IosAppPrivacyReportDeviceAction

This type has no fields.

Collects the exported iOS App Privacy Report during the test run.

When enabled, the iOS device records application activity (such as network access, domain requests, and sensitive resource access such as photos, camera, or location) and exports Apple's official App Privacy Report.

The report will be written to a file named `AppActivityReport.ndjson` in the execution output directory.

## IosSwitchLocaleDeviceAction

Switches the locale (language and region) of the iOS application.

JSON representation  
---  
      
    
    {
      "localeCode": string
    }  
  
Fields  
---  
`localeCode` |  `string` Required. The locale (language and region) to switch the app to.The format is `language-region` or `language`, ex. "en-US", "zh-CN", "ja", etc.  
  
## SessionNotificationConfig

Config to control session notification.

JSON representation  
---  
      
    
    {
      "pubsubTopic": [
        string
      ]
    }  
  
Fields  
---  
`pubsubTopic[]` |  `string` Optional. The Pub/Sub topics to which session events are published. Format: `projects/{project}/topics/{topic}`. See [Guidelines to name a topic, subscription, schema, or snapshot](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).  
  
## SessionOutputFileDirectoryConfig

Config to control session output file directory.

JSON representation  
---  
      
    
    {
      "flatDirectoryStructure": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsOutputDirectory": {
        object ([GcsPath](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#GcsPath))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`flatDirectoryStructure` |  `boolean` Optional. Whether to write output files directly under the output directory instead of nesting them under service-generated subdirectories.By default (`false`), output files are stored under `<output_directory>/<sessionId>/<job_display_name>/<execution_name>/`.When `true`, the session ID subdirectory is never appended, and the job display name subdirectory is appended only when the session has more than one job. Output files are therefore stored under:

  * `<output_directory>/<execution_name>/` for a single-job session.
  * `<output_directory>/<job_display_name>/<execution_name>/` for a multi-job session.

Set this to `true` when the output directory is already unique per session (for example, when a CI/CD system generates it), to avoid redundant nesting.  
Output directory for the session. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsOutputDirectory` |  `object (`[GcsPath](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#GcsPath)`)` The Google Cloud Storage path of the output directory (ex. `gs://my-bucket/output`). The bucket must exist. If the bucket is located in another project or uses fine-grained access controls, ensure the Device Run Service Agent of the project (`service-<PROJECT_NUMBER>@gcp-sa-devicerun.iam.gserviceaccount.com`) is granted access to the bucket (such as `roles/storage.objectUser`).  
End of mutually exclusive fields.  
  
## SessionReport

The runtime information and result report of a session.

JSON representation  
---  
      
    
    {
      "id": string,
      "jobReports": [
        {
          object ([JobReport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#JobReport))
        }
      ],
      "startTime": string,
      "endTime": string,
      "status": {
        object ([Status](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Status))
      },
      "result": {
        object ([Result](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Result))
      }
    }  
  
Fields  
---  
`id` |  `string` Output only. The unique identifier of the session.  
`jobReports[]` |  `object (`[JobReport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#JobReport)`)` Output only. Reports of the jobs in the session.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the session.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the session.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `object (`[Status](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Status)`)` Output only. The status of the session.  
`result` |  `object (`[Result](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Result)`)` Output only. The result of the session.  
  
## JobReport

The runtime information and result report of a job.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "executionReports": [
        {
          object ([ExecutionReport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#ExecutionReport))
        }
      ],
      "startTime": string,
      "endTime": string,
      "status": {
        object ([Status](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Status))
      },
      "result": {
        object ([Result](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Result))
      },
      "outputFiles": [
        {
          object ([OutputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#OutputFile))
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "warnings": [
        {
          object ([Warning](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Warning))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` Output only. The unique identifier of the job.  
`displayName` |  `string` Output only. The displayName set by users in the JobConfig.  
`executionReports[]` |  `object (`[ExecutionReport](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#ExecutionReport)`)` Output only. Reports of the execution attempts of the job.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the job.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the job.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `object (`[Status](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Status)`)` Output only. The status of the job.  
`result` |  `object (`[Result](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Result)`)` Output only. The result of the job.  
`outputFiles[]` |  `object (`[OutputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#OutputFile)`)` Output only. The output files of the job.  
`labels` |  `map (key: string, value: string)` Output only. The original labels provided by the user during job creation.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`warnings[]` |  `object (`[Warning](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Warning)`)` Output only. Non-fatal warnings collected during the job.  
  
## ExecutionReport

The runtime information and result report of a single on-device execution attempt.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "startTime": string,
      "endTime": string,
      "status": {
        object ([Status](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Status))
      },
      "result": {
        object ([Result](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Result))
      },
      "warnings": [
        {
          object ([Warning](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Warning))
        }
      ],
      "outputFiles": [
        {
          object ([OutputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#OutputFile))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` Output only. The unique identifier of the execution.  
`displayName` |  `string` Output only. The displayName set by users in the ExecutionConfig.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the execution.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the execution.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `object (`[Status](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Status)`)` Output only. The status of the execution.  
`result` |  `object (`[Result](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Result)`)` Output only. The result of the execution.  
`warnings[]` |  `object (`[Warning](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#Warning)`)` Output only. Non-fatal warnings collected during the execution.  
`outputFiles[]` |  `object (`[OutputFile](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#OutputFile)`)` Output only. The output files of the execution.  
  
## Status

The status of a session/job/execution.

JSON representation  
---  
      
    
    {
      "statusType": enum ([StatusType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#StatusType)),
      "progressMessages": [
        string
      ]
    }  
  
Fields  
---  
`statusType` |  `enum (`[StatusType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#StatusType)`)` Output only. The status type of the session/job/execution.  
`progressMessages[]` |  `string` Output only. Human-readable, detailed descriptions of the session/job/execution's progress. For example: "Provisioning a device", "Starting Test". Each message should contain only one line of text.During the course of execution new data may be appended to the end of progressMessages.  
  
## StatusType

All status types.

Enums  
---  
`STATUS_TYPE_UNSPECIFIED` | Unknown status type.  
`PENDING` | The session/job/execution is pending, not started yet.  
`RUNNING` | The session/job/execution is running.  
`DONE` | The session/job/execution is finished.  
`SUSPENDED` | The session/job/execution is suspended due to quota issues.  
  
## Result

The result of a session/job/execution.

JSON representation  
---  
      
    
    {
      "resultType": enum ([ResultType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#ResultType)),
      "cause": {
        object ([ResultCause](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#ResultCause))
      }
    }  
  
Fields  
---  
`resultType` |  `enum (`[ResultType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#ResultType)`)` Output only. The result type of the session/job/execution.  
`cause` |  `object (`[ResultCause](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#ResultCause)`)` Output only. Detailed result cause diagnostics. Set if type is not PASSED.  
  
## ResultType

All result types.

Enums  
---  
`RESULT_TYPE_UNSPECIFIED` | Unknown result type.  
`PASSED` | Finished and passed.  
`FAILED` | Finished but failed. It is usually caused by the user config, problematic test cases, or real bugs of their apps/platform under test.  
`ERROR` | Unclassified error, can be caused by user config/tests/AUT, infra, or the tools that the infra is depending on.  
`TIMED_OUT` | Test timeout.  
`CANCELLED` | Test is aborted by user.  
  
## ResultCause

Describes the cause of the non-passed result occurred during the execution.

JSON representation  
---  
      
    
    {
      "summary": {
        object ([IssueSummary](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IssueSummary))
      }
    }  
  
Fields  
---  
`summary` |  `object (`[IssueSummary](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IssueSummary)`)` Output only. Structured cause detail.  
  
## IssueSummary

Describes the summary of an issue (error or warning) with structured details.

JSON representation  
---  
      
    
    {
      "type": enum ([IssueType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IssueType)),
      "reason": string,
      "message": string
    }  
  
Fields  
---  
`type` |  `enum (`[IssueType](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IssueType)`)` Output only. The issue classification based on responsibility.  
`reason` |  `string` Output only. The reason of the issue. This is a constant value that identifies the proximate cause of the issue. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]*[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`message` |  `string` Output only. Human-readable explanation of the issue in English.  
  
## IssueType

Classification of issue responsibility.

Enums  
---  
`ISSUE_TYPE_UNSPECIFIED` | Unspecified issue type. This value is unused.  
`INFRA` | Platform infrastructure or operational execution environment failure.  
`CUSTOMER` | Customer test script failure, malformed APK, or bad user configuration.  
  
## Warning

Non-fatal operational anomaly, lint observation, or execution insight.

JSON representation  
---  
      
    
    {
      "summary": {
        object ([IssueSummary](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IssueSummary))
      }
    }  
  
Fields  
---  
`summary` |  `object (`[IssueSummary](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#IssueSummary)`)` Output only. Detailed warning summary.  
  
## OutputFile

Output file.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsOutputFile": {
        object ([GcsPath](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#GcsPath))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsOutputFile` |  `object (`[GcsPath](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions#GcsPath)`)` An output file in Google Cloud Storage.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[batchGet](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/batchGet)`

|  Retrieves multiple automation sessions in a single batch request.  
  
### `[cancel](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/cancel)`

|  Cancels an in-progress automation session.  
  
### `[create](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/create)`

|  Starts an automation session with the specified configuration.  
  
### `[delete](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/delete)`

|  Deletes a session.  
  
### `[get](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/get)`

|  Returns information about a previously created automation session.  
  
### `[list](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/list)`

|  Lists previously created automation sessions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
