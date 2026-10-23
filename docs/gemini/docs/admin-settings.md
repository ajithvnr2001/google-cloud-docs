---
url: https://docs.cloud.google.com/gemini/docs/admin-settings/
title: Gemini Code Assist administrator settings \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:51.927847+00:00
---

# Gemini Code Assist administrator settings  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/admin-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Gemini Code Assist administrator settings Stay organized with collections  Save and categorize content based on your preferences. 

This document describes administrator settings for Gemini Code Assist. For Gemini Cloud Assist administrator settings, see the [Gemini Cloud Assist documentation](https://docs.cloud.google.com/cloud-assist/admin-settings).

## Overview

Administrator settings control the project-wide behavior of Gemini Code Assist. An administrator setting is defined and stored in a _container project_ and a binding applies the setting to a _target_. By binding a single administrator setting to multiple targets, you can modify the setting once and have it automatically applied to each target.

  * In the simplest setup, the container project is also the target.

    * In more advanced setups, you can bind the setting to one or more other projects, and the container project does not have to be a target.
  * When working with administrator settings in the Google Cloud console, defining, storing, and binding the settings is handled automatically for you.

  * You can bind different types of administrator settings to the same project, but you can't bind multiple administrator settings of the same type to the same project.




## Available settings

The following lists the Gemini Code Assist administration settings available for projects and the default value for each setting:

Setting name | Setting default  
---|---  
[Release channel](https://docs.cloud.google.com/gemini/docs/codeassist/configure-release-channels) | General Availability channel  
[Logging](https://docs.cloud.google.com/gemini/docs/configure-logging) | Disabled  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
