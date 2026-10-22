---
url: https://docs.cloud.google.com/developer-device-platform/device-run/migrate/
title: Migrate from Firebase Test Lab to Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:49.447500+00:00
---

# Migrate from Firebase Test Lab to Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/device-run/migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Migrate from Firebase Test Lab to Developer Device Platform Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

We are excited to announce the Preview of the **`gcloud beta device-run`** command line interface in Developer Device Platform (DDP), an enhancement to the `gcloud firebase test` CLI.

The `gcloud beta device-run` CLI simplifies and modernizes running automation and instrumentation tests on-device, both physical and virtual. In the Preview release, **Android Instrumentation** and **iOS XCTest** are supported. See the [Device Run Overview](https://docs.cloud.google.com/developer-device-platform/device-run) for instructions.

## Overview and benefits

Switching from Firebase Test Lab to the Developer Device Platform (DDP) offers several major advantages, particularly in terms of cost savings, test execution speed, advanced debugging, and built-in support for AI-driven workflows.

Developers running mobile tests in the cloud have to juggle between different configuration models (Firebase Test Lab) or maintain additional pipelines and tooling wrapper layers (Flank).

The `gcloud beta device-run` CLI in the Developer Device Platform merges these capabilities directly into the core Google Cloud CLI. It provides a more robust, declarative, and scalable backend interface that runs tests predictably and efficiently on both physical and virtual devices.

The key features and capabilities that make DDP a superior platform compared to Firebase Test Lab include:

### Advanced Smart Sharding

While Firebase Test Lab relies on single-run timing data to shard tests, DDP's Smart Sharding is far more intelligent:

  * _30-Day historical data_ : DDP analyzes up to 30 days of execution history to distribute tests into stable, optimized shards.
  * _Device-specific duration tracking_ : DDP tracks test execution runtimes per specific device model rather than using generalized platform averages across all devices.
  * _Orchestrator overhead modeling_ : DDP factors in the startup overhead of the Android Test Orchestrator for each test instance, ensuring shards don't overrun their target durations.



### Fine-grained and cost-effective retries

In Test Lab, if a single test case within a shard fails, the entire shard (potentially dozens of tests) must be retried, which inflates both execution times and billing costs. DDP introduces highly efficient retry mechanisms:

  * _Targeted test-case-level retries_ : Isolates and retries _only_ the specific failing test cases within a shard.
  * _Sequential flaky test retries_ : Executes retries for flaky tests sequentially by default (instead of concurrently like Test Lab). Combining this with test-case-level retries dramatically cuts down total test runs, resulting in significant savings on device billing costs.



### Advanced support for Android tests

DDP addresses long-standing limitations in the Test Lab testing API:

  * _Test APK only_ (no dummy apps): Test Lab historically required a dummy app to run self-instrumenting tests. DDP supports running instrumentation tests with only a test APK.
  * _Extended shard timeout_ : DDP increases the maximum execution limit for a single instrumentation test shard from Test Lab's 45-minute cap to 3 hours.
  * _Multiple Orchestrators_ : DDP supports multiple Android Test Orchestrator versions.
  * _Built-in C++ binary support_ : DDP supports executing Android C++ binaries.



### Enriched device interactions and advanced debugging

DDP provides deeper on-device interactions and much richer debugging artifacts than those available in Test Lab:

  * _Mock locations_ : DDP supports mocking device GPS coordinates.
  * _ApkSets support_ : Developers can install ApkSets (.`apks` files) directly onto the remote devices.
  * _Advanced debugging_ : DDP exposes vital system logs and debugging information, including `dumpsys` and `bugreport`, straight to the developer.



### Highly-scalable Device Catalog

DDP replaces Test Lab's rigid and heavy environment catalog with a completely redesigned Device Catalog API:

  * _Server-side filtering_ : Speeds up queries and decreases payload latency by allowing developers to filter devices on the server side.
  * _Real-time availability data_ : DDP provides real-time device availability information directly to Device Run so you can choose highly available devices and avoid long queue times—a feature Test Lab completely lacks.



## Choose your migration path

### Automate your migration with AI

To make this transition smooth, we have developed a dedicated translation agent skill: [**`migrating-device-run`**](https://docs.cloud.google.com/static/developer-device-platform/device-run/migrate/migration-skill.md.txt).

If you are using AI coding agents, such as **Antigravity** , **Claude Code** , **Codex** , you can readily translate your custom testing scripts. Simply copy the URL of the [migration skill](https://docs.cloud.google.com/static/developer-device-platform/device-run/migrate/migration-skill.md.txt) schema and paste it into your AI assistant workspace as described here.

#### Migration prompt template
    
    
    You are an expert migration assistant. I want to migrate my test command and
    configuration to the new `gcloud beta device-run` command format.
    
    Use this migration guideline as your ruleset:
    https://docs.cloud.google.com/developer-device-platform/device-run/migrate/migration-skill.md.txt
    
    Translate the following command and configuration to the new `gcloud beta
    device-run` CLI: (Insert your raw Firebase Test / Flank YAML or bash script
    here.)
    

### Migrate manually

Follow our [command and flag translations](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation) to migrate manually from Firebase Test Lab to DDP. As you prepare to migrate, keep the following structural differences in mind:

  * _Resource-centric CLI architecture_ : `gcloud beta device-run` adopts a modern `<resource> <verb>` command pattern across three main resource groups: 
    * _`devices`_ : Direct CLI access to device catalog inventory and comprehensive device details, replacing fragmented legacy `firebase test android/ios models/versions/locales` commands.
    * _`software-versions`_ : Direct CLI access to supported software versions (such as Xcode and Android Test Orchestrator versions), replacing legacy `firebase test ios xcode-versions list`.
    * _`sessions`_ : End-to-end session lifecycle management directly in the terminal, including `sessions submit instrumentation`, `sessions submit xctest`, `sessions wait`, `sessions describe [--full]`, `sessions list`, and `sessions cancel`.
  * _Subcommand structure_ : Test types are standardized and nested under `sessions submit` as clean subcommands rather than using type flags. 
    * DDP: `gcloud beta device-run sessions submit instrumentation` (Android) or `gcloud alpha device-run sessions submit xctest` (iOS)
    * Test Lab: `gcloud firebase test android run --type=instrumentation` (Android) or `gcloud firebase test ios run --type=xctest` (iOS)
  * _Pluralized and merged apps_ : Standard and supplementary APKs are merged under the pluralized `--apps` flag list (ex. `--apps=app.apk,helper.apk`) instead of split into `--app` and `--additional-apks`.
  * _Structured dictionary and list arguments_ : Replaced comma-separated files or environment lists with structured CLI dictionary and list formats: `--other-files-to-push KEY=VALUE`, `--additional-test-options KEY=VALUE`, `--paths-to-pull`, and `--test-targets`.
  * _Unified sharding and retry controls_ : Seamless support for Uniform Sharding and Smart Sharding, along with parallel retries (`--flaky-test-parallel-retry`, `--flaky-test-retry-level`) and runtime diagnostics (`--dumpsys`, `--bugreport`, `--video`).
  * _Async execution_ : `gcloud beta device-run` supports asynchronous execution, allowing you to run tests without waiting for them to complete. Use `gcloud beta device-run sessions wait <SESSION_ID>` to wait for completion.
  * _Declarative YAML configuration (`--flags-file`)_: Teams migrating from Flank who prefer version-controlled YAML files over shell script strings can use `gcloud`'s universal `--flags-file=device-run-flags.yaml` support.



## What's next

  1. Use our [Quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart) to set up the Developer Device Platform.
  2. Explore our [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog) to find all available devices.
  3. Learn about [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run) to begin running tests.
  4. Visit our [command and flag translations](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation) to see a mapping of Test Lab and Flank flags to DDP.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
