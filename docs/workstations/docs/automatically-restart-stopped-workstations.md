---
url: https://docs.cloud.google.com/workstations/docs/automatically-restart-stopped-workstations/
title: Automatic restarts for stopped workstations \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:01.969547+00:00
---

# Automatic restarts for stopped workstations  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/automatically-restart-stopped-workstations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Automatic restarts for stopped workstations Stay organized with collections  Save and categorize content based on your preferences. 

By default, Cloud Workstations automatically restarts stopped workstations when a user attempts to connect to them. This behavior is managed by the **Workstation launcher URL** setting in the workstation cluster configuration.

For clusters created before April 2026, you must manually configure this setting.

## Default launcher behavior

When you create or update a workstation cluster, the Workstation launcher URL is populated with the default Google Cloud console launcher URL: `https://console.cloud.google.com/workstations/launch`.

If a user tries to connect to a workstation that is not running, Cloud Workstations redirects them to this URL, automatically starts the stopped workstation, and then redirects the user back to their workstation once it is ready. This streamlines the user experience by avoiding the need for users to manually start their workstations.

For data residency, you can use a jurisdictional Google Cloud console URL, such as `https://console-us.cloud.google.com/workstations/launch` for US-based traffic or `https://console-eu.cloud.google.com/workstations/launch` for EU-based traffic. These jurisdictional URLs also support automatic restarts.

## Custom launcher URLs

If you specify a custom URL instead of the default, users are redirected to your custom page when they attempt to connect to a stopped workstation. In this scenario, Cloud Workstations does not automatically restart the workstation.

## Configure the launcher URL

To configure this setting, see [Create a workstation cluster](https://docs.cloud.google.com/workstations/docs/create-cluster).

### Bookmark or install your workstation

To bypass the Google Cloud console and connect to your environment directly, you can bookmark your workstation URL or install it as a progressive web app (PWA).

#### Bookmark your workstation

To access your workstation without navigating the Google Cloud console, bookmark the workstation URL in your browser.

#### Install your workstation as a web app

If you use the **Code OSS** editor image, you can install your workstation as a PWA. This provides a standalone window experience similar to a desktop application.

  1. Open your workstation in a Chrome browser.
  2. Follow the instructions to [install a web app](https://support.google.com/chrome/answer/9658361).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
