---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/ruby-runtime/
title: The Ruby Runtime \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:31.416255+00:00
---

# The Ruby Runtime  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/ruby-runtime/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# The Ruby Runtime

## Overview

Your Cloud Run function runs in an environment consisting of an operating system version plus add-on packages, language support, and the Functions Framework library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime.

For information about runtimes in general, and to learn which Ubuntu version each Ruby runtime uses, see the [Cloud Run functions execution environment](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#ruby).

## Select your runtime

Cloud Run functions supports several versions of Ruby, listed on the [Runtime support](https://docs.cloud.google.com/functions/1stgendocs/runtime-support#ruby) page. You can select the preferred Ruby runtime for your function during deployment.

If you're using the Google Cloud CLI, specify the runtime by using the `--runtime` parameter. NAME specifies the function name. For example:
    
    
    gcloud functions deploy NAME --no-gen2 --runtime ruby40 --trigger-http

For more deployment parameters, see [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics).

## Source code structure

For Cloud Run functions to find your function's definition, your source code must follow a specific structure. See [Writing Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/writing#structuring_source_code) for more information.

## Function preparation

You can write a function on your local machine and upload it. To prepare your local machine for Ruby development, see [Setting up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup). The library that invokes your function is the [Ruby Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/functions-framework).

**Note:** The only type of [event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing#types_of_cloud_functions) Ruby supports are [CloudEvent functions](https://docs.cloud.google.com/functions/1stgendocs/writing#cloudevent_functions).

## Specifying dependencies

You can specify dependencies for your function by adding them to a project file. For more information, see [Specifying dependencies in Ruby](https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-ruby).

## What's next

  * [Create your first Ruby function](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-ruby-1st-gen) from scratch.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
