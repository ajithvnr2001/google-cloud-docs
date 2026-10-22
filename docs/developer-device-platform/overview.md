---
url: https://docs.cloud.google.com/developer-device-platform/overview/
title: Developer Device Platform overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:31.666341+00:00
---

# Developer Device Platform overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Developer Device Platform overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Developer Device Platform is a next-generation, commercial-grade suite for remote device orchestration. Developer Device Platform is designed to provide an enterprise-scale, cloud-native offering. It acts as a managed device farm for developers to build and test applications using remote infrastructure, natively integrating with Google Cloud.

If you are migrating from [Firebase Test Lab](https://firebase.google.com/docs/test-lab) to Developer Device Platform, see our [migration guide](https://docs.cloud.google.com/developer-device-platform/device-run/migrate), [command and flag translation](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation), and [migration skill](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/migration-skill) for AI agents.

Developer Device Platform offers:

  * [_Device Catalog_](https://docs.cloud.google.com/developer-device-platform/device-catalog) \- Use the Device Catalog to find, sort and delve into devices in the Developer Device Platform.
  * [_Device Run_](https://docs.cloud.google.com/developer-device-platform/device-run) \- Run tests on devices in the Developer Device Platform lab and see the results in Google Cloud.
  * _[Device Streaming API](https://docs.cloud.google.com/device-streaming/docs)_ \- Connect to remote physical Android devices and interact with your app as if it is connected to your local machine.
  * [_Agent Skill_](https://docs.cloud.google.com/developer-device-platform/agent-skill) \- Give coding agents the ability to find, reserve and manipulate devices for you.



## Key platform offerings

At Preview, the platform is restricted to a subset of core services, and available to Android application developers (iOS support is coming soon):

  * Device Run API (AutomationJob Service): Designed for automated batch testing (such as instrumentation and JUnit tests). It uses a three-tiered hierarchy of Sessions, Jobs, and Executions to orchestrate device allocation, test runs, and result reporting.
  * Device Streaming API: Establishes interactive connections, allowing developers to remotely control physical and virtual device screens in real time and communicate over Android Debug Bridge (ADB).
  * Agentic Workflows (Device Action Service): A major differentiator of Developer Device Platform. It introduces an open source Developer Device Platform Agent Skill on GitHub that enables AI coding agents (such as Clockwork Code and Anti-gravity) to programmatically manage remote device sessions, run tests, capture screenshots, and execute shell commands.



## What Developer Device Platform provides

The Developer Device Platform allows developers to run and monitor tests in Google Cloud:

  * **Platform Integration** : Developer Device Platform is integrated into the **Google Cloud** ecosystem, with its documentation organized according to Google Cloud standards and hosted under cloud.google.com.
  * **Tooling and APIs** : Developer Device Platform is accessible by the newly introduced `device-run` command in [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) or by calling the Device Run and Device Streaming APIs directly.
  * **Platform Support at Launch** : In its initial launch, Developer Device Platform supports only **Android app developers** , with iOS support planned later.
  * **Billing** : Developer Device Platform is tied to Google Cloud billing, meaning developers need a **paid Google Cloud account** where costs are paid directly by the users/developers.



## Key orchestration benefits

By wrapping both device allocation and test execution inside a single service, users gain access to Developer Device Platform's advanced orchestration capabilities:

  * **Hardware Flakiness Mitigation** : If an allocated device encounters connection drops or hardware failures, the backend automatically acquires a different device, restarts the test, and returns the successful retry results seamlessly.
  * **Large-Scale Parallel Execution** : Built-in support for _Smart Sharding_ (which uses historical execution data to partition test suites based on a target run duration) and _Uniform Sharding_ reduces the end-to-end execution times of massive test suites.



## What's next

Use our [Quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart) to set up your environment for Developer Device Platform. Then follow the instructions for each workflow:

  * [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog)
  * [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run)
  * [Share Storage](https://docs.cloud.google.com/developer-device-platform/device-run/share-storage)
  * [Find Logs](https://docs.cloud.google.com/developer-device-platform/device-run/find-logs)
  * [Device Streaming](https://docs.cloud.google.com/device-streaming/docs)
  * [Agent Skill](https://docs.cloud.google.com/developer-device-platform/agent-skill)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
