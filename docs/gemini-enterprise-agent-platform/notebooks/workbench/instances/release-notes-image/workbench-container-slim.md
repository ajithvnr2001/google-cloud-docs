---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/release-notes-image/workbench-container-slim/
title: Image release notes: workbench-container-slim \u00a0|\u00a0 Gemini Enterprise Agent Platform Workbench \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:12.688192+00:00
---

# Image release notes: workbench-container-slim  |  Gemini Enterprise Agent Platform Workbench  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/release-notes-image/workbench-container-slim/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform Workbench ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback 

#  Image release notes: workbench-container-slim Stay organized with collections  Save and categorize content based on your preferences. 

This page documents image releases for the `workbench-container-slim` image family (slim and Python 3.10) of Agent Platform Workbench. Each entry lists the image version that was released and the changes it contains. 

For the versioning scheme and lifecycle dates, see [Image versioning and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/image-versioning). For product-level updates that aren't specific to an image, see [Agent Platform Workbench release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/release-notes). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## October 13, 2026

Change

### 20261013-2230-rc0 Release

Change

Installed latest packages from upstream dependencies.

## October 11, 2026

Change

### 20261011-2230-rc0 Release

Change

Installed latest packages from upstream dependencies.

Fixed

Fixed an issue where gcloud and gsutil failed to load with an AttributeError in OpenSSL.crypto due to a version mismatch between pyOpenSSL and cryptography.

## October 04, 2026

Change

### 20261004-2230-rc0 Release

Change

Installed latest packages from upstream dependencies.

Security

Bulk security patch remediating Critical and High-severity CVEs in the Agent Platform Workbench custom container images.

## September 27, 2026

Change

### 20260927-1408-rc0 Release

Change

Installed latest packages from upstream dependencies.

## September 18, 2026

Change

### 20260918-2230-rc0 Release

Change

Installed latest packages from upstream dependencies.

Feature

JupyterLab now forwards client-side logs (console errors, uncaught exceptions, unhandled promise rejections, and failed network requests) to the instance backend, where they surface in Cloud Logging for easier debugging.

## September 13, 2026

Change

### 20260913-2230-rc0 Release

Change

Installed latest packages from upstream dependencies.

Fixed

Fixed an issue where the `notebook-disable-nbconvert` metadata flag was ignored in custom containers.

Fixed

Fixed the %%bigquery notebook cell magic, which returned an error instead of query results in JupyterLab 4.

## August 30, 2026

Change

### 20260830-2230-rc0 Release

Change

Installed latest packages from upstream dependencies.

## August 23, 2026

Change

### 20260823-2230-rc0 Release

Change

Installed latest packages from upstream dependencies.

## August 16, 2026

Change

### 20260816-2230-rc0 Release

Change

Installed latest packages from upstream dependencies.

## August 09, 2026

Change

### 20260809-2230-rc0 Release

Change

Installed latest packages from upstream dependencies.

## August 02, 2026

Change

### 20260802-2230-rc0 Release

Fixed

Fixed issue with JupyterLab UI silently reverting file changes and interrupting kernels due to Gemini CLI's auto reload extension.

Change

The JupyterLab last-active and auto-reload extensions are now enabled only when Gemini CLI is configured, preventing them from affecting the native JupyterLab UI otherwise.

Change

Installed latest packages from upstream dependencies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
