---
url: https://docs.cloud.google.com/shell/docs/release-notes/
title: Cloud Shell release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:10.032059+00:00
---

# Cloud Shell release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ Resources ](https://docs.cloud.google.com/shell/docs/resources)



Send feedback 

#  Cloud Shell release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Shell. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/shell-release-notes.xml) directly. 

## July 28, 2026

Security

Cloud Shell enforces stricter `Origin` header validation on WebSocket upgrades and implements an allowed port list for TCP and SSH tunnels, mitigating a Cross-Site WebSocket Hijacking (CSWSH) vulnerability ([CVE-2026-85267](https://www.cve.org/CVERecord?id=CVE-2026-85267)). No customer action is required.

## June 20, 2026

Change

Cloud Shell no longer includes the Terraform CLI by default. Users can [customize their environment](https://docs.cloud.google.com/shell/docs/configuring-cloud-shell#environment_customization) to install the CLI on environment startup, or install the binary to their home directory to persist the install between sessions.

## March 26, 2026

Change

The Cloud Shell Editor is built with Code OSS for Cloud Shell `1.109.5`

## March 10, 2026

Change

The Cloud Shell Editor is built with Code OSS for Cloud Shell `1.108.2`

## April 08, 2024

Feature

Code Transformations for Gemini Code Assist are now available for [Public Preview](https://cloud.google.com/products#product-launch-stages). You can now use an inline text box directly in your code file to do the following:

  * Generate comment lines to document your code.
  * Troubleshoot code with issues.
  * Improve code readability.
  * Make code more efficient.



You can also view context sources of a generated response in the **Gemini: Chat** pane.

For more information, see [Code with Gemini Code Assist](https://docs.cloud.google.com/code/docs/shell/write-code-gemini#use-code-transformation-features).

## November 01, 2023

Feature

Duet AI for Cloud Shell is now available. Use Duet AI, your AI-powered collaborator, to accomplish tasks more effectively and efficiently. Duet AI provides contextualized responses to your prompts to help guide you on what you're trying to do with your code. It also shares source citations regarding which documentation and code samples the assistant used to generate its responses. 

If you use the latest version of the Cloud Shell editor, which is Code - OSS based, you can use Duet AI for Cloud Shell. For more information, see the [Duet AI in Google Cloud overview](https://docs.cloud.google.com/duet-ai/docs/overview) and [Code with Duet AI assistance](https://docs.cloud.google.com/code/docs/shell/write-code-duet-ai).

## February 22, 2023

Change

Golang Extension updated to 0.37.1

See the [Golang Extension release notes](https://github.com/golang/vscode-go/blob/master/extension/CHANGELOG.md#v0371---17-jan-2023) for a full list of features/updates/bug fixes.

Change

Cloud Code Extension updated to 1.21.2

Cloud Code now uses a single activity bar icon to reduce the amount of space on screen and consolidate all explorers to a single convenient view. Additionally the update incorporates new Cloud Functions capabilities, improved snippet accuracy for Cloud APIs, and new Compute Engine functionality, and more! [Review the Cloud Code release notes](https://marketplace.visualstudio.com/items/GoogleCloudTools.cloudcode/changelog) for a complete list of features, updates, and fixes.

Change

Terraform Extension updated to 2.25.2

Review the [Terraform Extension release notes](https://github.com/hashicorp/vscode-terraform/blob/main/CHANGELOG.md#2252-2022-12-15) for a complete list of features/updates/bug fixes.

Change

Cloud Shell Editor is built with Theia 1.34.0

Review the [Theia release notes](https://github.com/eclipse-theia/theia/blob/master/CHANGELOG.md#v1340---01262023) for a complete list of features/updates/bug fixes.

## June 29, 2022

Change

Cloud Shell now defaults to Python 3

Python 2 is still included as a development tool in Cloud Shell and may be invoked using `python2`.

Change

Cloud Code Extension updated to 1.18.3

Update includes a new and improved Kubernetes development experience with the Development Sessions Explorer, support for private clusters, a refreshed welcome page, and more! Review the [Cloud Code release notes](https://marketplace.visualstudio.com/items/GoogleCloudTools.cloudcode/changelog) for a complete list of features, updates, and fixes.

Change

Cloud Shell Editor is built with Theia 1.25.0

Review the [Theia release notes](https://github.com/eclipse-theia/theia/blob/master/CHANGELOG.md#v1250---4282022) for a complete list of features/updates/bug fixes.

## February 16, 2022

Change

.NET 6.0 Support added.

Cloud Shell and the Cloud Shell Editor now support .NET 6.0 development.

Change

Cloud Shell Editor is now built with Theia 1.21.0

For a complete list of features, updates, and bug fixes, see the [Theia release notes](https://github.com/eclipse-theia/theia/blob/master/CHANGELOG.md#v1210---12162021).

Announcement

Upcoming switch to Python 3

Cloud Shell will soon default to Python 3. Python 2 will still be included as a development tool in Cloud Shell and may be invoked by issuing the `python2` command.

Change

Debian 11

Cloud Shell is now built on top of Debian 11. For a full list of updates, see the [Debian 11 release notes](https://www.debian.org/releases/stable/releasenotes).

## October 20, 2021

Change

Cloud Shell Editor is now built with Theia 1.18.0

Review the [Theia release notes](https://github.com/eclipse-theia/theia/blob/master/CHANGELOG.md#v1180---9302021) for a complete list of features/updates/bug fixes.

Change

Cloud Code Extension updated to v1.14.1

Update includes a Kubernetes Development Sessions explorer which provides more insight into task execution and streamlines examining session logs. See the [Cloud Code release notes](https://marketplace.visualstudio.com/items/GoogleCloudTools.cloudcode/changelog) for a full listing of features/updates/bug fixes.

## September 14, 2021

Feature

Cloud Shell is available directly in the [Google Cloud documentation](https://docs.cloud.google.com/docs?shell_enabled=true).

You can use this feature to activate Cloud Shell in the documentation and run sample code in the terminal on the page. For more information, see [Launching within documentation](https://docs.cloud.google.com/shell/docs/launching-cloud-shell?shell_enabled=true#launching_within_documentation).

The following list summarizes known issues that you might encounter:

  * You can only activate Cloud Shell in the documentation when you're using Chrome desktop browsers (version 74 or higher).
  * If Cloud Shell is activated and you open a site search result, the browser asks if you want to leave the site and then closes Cloud Shell.
  * If Cloud Shell is activated and you open a URL that redirects you to a different URL, your Cloud Shell session restarts.



## August 17, 2021

Change

Cloud Shell Editor is now built with Theia 1.16.0

Review the [Theia release notes](https://github.com/eclipse-theia/theia/blob/master/CHANGELOG.md#v1160---7292021) for a complete list of features/updates/bug fixes.

Change

Cloud Code Extension updated to v1.13.1

Updates includes a simplified combined Kubernetes Explorer and GKE Explorer experience, Managed Cloud SDK performance improvements, as well as improved Cloud Run local development webview. Review the [Cloud Code release notes](https://marketplace.visualstudio.com/items/GoogleCloudTools.cloudcode/changelog) for a complete list of features/updates/bug fixes.

Change

.Net 5.0 now comes preinstalled in Cloud Shell.

Checkout the [dotnet-five](https://docs.microsoft.com/en-us/dotnet/core/dotnet-five) documentation for more details.

Change

The Flutter SDK now comes preinstalled in Cloud Shell.

Visit the [Flutter Docs](https://flutter.dev/docs) or simply enter `flutter` in Cloud Shell to get started.

Change

Cloud Shell Editor Built-in Extensions Updated to 1.45.1

All built-in VS Code Extensions used by the Cloud Shell Editor have been updated to 1.45.1 to incorporate upstream changes.

## July 14, 2021

Announcement

Terraform plugin v2.12.0

The Cloud Shell Editor now comes preinstalled with the HashiCorp Terraform extension! The extension adds syntax highlighting and other editing features for Terraform files using Terraform Language Server. Review the [Terraform release notes](https://github.com/hashicorp/vscode-terraform/blob/main/CHANGELOG.md) for a complete list of features/updates/bug fixes.

## June 02, 2021

Change

Cloud Code plugin updated to v1.12.0.

Update includes the ability to build with Cloud Build when deploying to Cloud Run or Running/Debugging on Kubernetes. Review the [Cloud Code release notes](https://marketplace.visualstudio.com/items/GoogleCloudTools.cloudcode/changelog) for a complete list of features/updates/bug fixes.

Change

Golang plugin updated to v0.23.0.

Update includes improved debugging workflow of attaching to local process, and access to Delve DAP (again). Review the [Golang release notes](https://github.com/golang/vscode-go/blob/master/extension/CHANGELOG.md#v0230---4th-mar-2021) for a complete list of features/updates/bug fixes.

Change

Cloud Shell Editor is now built with Theia v1.14.0

Update includes improved plugin support, better debug configuration handling, as well as support for "goto line and column" in file search. Review the [Theia release notes](https://github.com/eclipse-theia/theia/blob/master/CHANGELOG.md#v1140---5272021) for a complete list of features/updates/bug fixes.

## May 26, 2021

Announcement

Cloud Shell Editor now supports Cloud Code v1.11.0

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
