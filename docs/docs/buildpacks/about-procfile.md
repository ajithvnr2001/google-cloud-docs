---
url: https://docs.cloud.google.com/docs/buildpacks/about-procfile/
title: About Procfiles \u00a0|\u00a0 Buildpacks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:23.931760+00:00
---

# About Procfiles  |  Buildpacks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/buildpacks/about-procfile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Buildpacks ](https://docs.cloud.google.com/docs/buildpacks)
  * [ Guides ](https://docs.cloud.google.com/docs/buildpacks/overview)



Send feedback 

#  About Procfiles Stay organized with collections  Save and categorize content based on your preferences. 

Use a `Procfile` to define the process that is invoked when a container starts. The `Procfile` can override the default start process for any language type. Procfile support is provided by the [entrypoint buildpack](https://github.com/GoogleCloudPlatform/buildpacks/tree/main/cmd/config/entrypoint).

## Procfile name and location

The `Procfile` is always a plain text file without a file extension.

Google Cloud's buildpacks searches for a file named `Procfile` at the root folder of the project. The `Procfile` must live in your project's root directory and cannot be placed anywhere else.

## Procfile format

A `Procfile` declares its process types on individual lines, each with the following format:
    
    
    PROCESS_TYPE: COMMAND
    

Replace:

  * PROCESS_TYPE with an alphanumeric name for your command, such as `web`, `worker` and `custom`.
  * COMMAND indicates the command that every process type should execute on startup, such as `gunicorn -b :$PORT main:app`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
