---
url: https://docs.cloud.google.com/migration-center/docs/release-notes/codmod-release-notes/
title: App Modernization Assessment tool release notes \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:40.770007+00:00
---

# App Modernization Assessment tool release notes  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/release-notes/codmod-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Resources ](https://docs.cloud.google.com/migration-center/docs/release-notes)



Send feedback 

#  App Modernization Assessment tool release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to the Migration Center App Modernization Assessment tool (`codmod`). Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## October 29, 2025

Feature

**C/C++ application migration to Arm architecture assessment.** The App Modernization Assessment tool now offers a dedicated assessment for C/C++ applications to facilitate their migration to Arm-based architectures (such as Google Cloud Axion C4A VMs). This new feature helps you do the following:

  * **Assess readiness:** understand the effort and readiness required to transition your C/C++ applications from x86-based architectures to Arm.
  * **Identify key challenges:** pinpoint potential code portability issues, architecture-specific dependencies, and necessary build system modifications.
  * **Plan for success:** gain insights into testing considerations crucial for a smooth and successful migration to Arm, whether on Google Cloud or other cloud providers like AWS Graviton instances.



Feature

**Enhanced productivity with command-line completion.** The `codmod` tool now supports shell command-line completion for Bash, Zsh, Fish, and PowerShell, significantly boosting your productivity. This feature lets you quickly type commands, flags, and arguments by pressing the `TAB` key to see and select the available options.

With this feature, you can discover options and see valid flag values. Additionally, suggestions are context-aware, meaning completions are tailored to the specific command. For example, `codmod config set [TAB]` suggests config keys, and file path completion is exclusively available for file and directory flags. For additional details, see [Command-line completion](https://docs.cloud.google.com/migration-center/docs/app-modernization-assessment#shell_auto_completion).

Feature

**Automatic version check and updates.** The `codmod` tool now includes an automatic version check feature to help you stay up-to-date with the latest improvements and fixes. Every 24 hours, the `codmod` tool checks for the availability of a newer version. If an update is available, a notification message appears in your terminal with the new version number and a download link.

  * You can disable the automatic check at any time using the following command: `codmod config set disable_version_check true`.

  * To re-enable automatic checks, simply set the value back to `false`. You can always view the current state and other configurations by running `codmod config list`.




Feature

**Supporting documents for assessment.** The `codmod` tool can now analyze a directory containing additional supporting documents to the codebase. The `codmod` tool supports documentation in textual, PDF, and image (PNG, JPG, JPEG) formats. Provide the directory by passing the `--supporting-documents <directory>` flag to the `create` command.

## August 14, 2025

Feature

**New quantitative metrics.** The report summary section now includes a summary of key quantitative metrics, providing a quick, data-driven overview of the report at a glance.

Feature

**Added file regex flags.** Two new optional flags, `--force-include` and `--force-exclude`, have been added to provide user flexibility in file selection.

Feature

**Added feedback and support links to HTML report.** The feedback and support links point to Google Forms that will be used to gather feedback and support requests.

Announcement

The Migration Center [App Modernization Assessment tool](https://docs.cloud.google.com/migration-center/docs/app-modernization-assessment) version 0.9.0 is available in Preview. 

The Migration Center App Modernization Assessment, powered by Google Gemini (via Vertex AI), is a tool designed to accelerate your application modernization journey. It offers automated, AI-powered analysis to understand your entire codebase in hours, not months, uncovering dependencies and complexities. This enables organizations to swiftly transition their existing codebases to the cloud by identifying potential blockers and providing tailored recommendations based on Google Cloud best practices, ultimately de-risking and planning your transformation with confidence.

Feature

**Create custom report from template.** Use a document as a template to create a custom report. The report will attempt to match the outline and style of the template document.

Change

**Removed`2.5-flash-lite-exp` from Suggested Models.** To improve the quality of generated reports, the support for `2.5-flash-lite-exp` model was removed.

Change

**Smaller Default Report and new Full Report.** The default report has been streamlined to 5 sections, reducing generation time and cost. A comprehensive 12-section report can now be generated using the new `create full` command.

Change

**Added a Content Security Policy (CSP)** to improve the security of locally viewed HTML reports.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
