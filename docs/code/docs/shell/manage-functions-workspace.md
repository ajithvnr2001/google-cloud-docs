---
url: https://docs.cloud.google.com/code/docs/shell/manage-functions-workspace/
title: Manage functions in Shell workspace \u00a0|\u00a0 Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:49.455306+00:00
---

# Manage functions in Shell workspace  |  Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/manage-functions-workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Manage functions in Shell workspace Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to manage multiple [Cloud Functions](https://cloud.google.com/functions/) configurations in a single workspace and how to rearrange your Cloud Run functions Explorer with Cloud Code.

## Before you begin

This guide requires a workspace already setup (a `launch.json` file with at least one configuration listed). To get started with a sample, see the [Create and deploy a function](https://docs.cloud.google.com/code/docs/shell/create-deploy-function) quickstart.

## Manage multiple configurations in a single workspace

To add a new Cloud Function configuration to your `launch.json` file, follow these steps:

  1. Click **Cloud Code** and then expand the **Cloud Functions** Explorer.

  2. In the Cloud Run functions Explorer, right-click **WORKSPACE** and click **Add new cloud function configuration**.

  3. Follow the prompts and perform the following actions:

     1. Enter a function name
     2. Select a Cloud Run functions environment
     3. Enter an entry point (the name of the method to call for this function)
     4. Enter the test input

Alternatively, you can manually enter these values into your `launch.json` file:
    
    {
        "configurations": [
          {
            "name": "Deploy Cloud Function",
            "type": "cloudcode.cloudfunctions",
            "request": "launch",
            "functionName": "hello-world-get",
            "gen": "GEN_2",
            "entryPoint": "helloGet"
          }
        ]
    }
    

Your Cloud Run functions workspace corresponds to the first configuration listed in your `launch.json` file. The workspace name reflects the `functionName` of the first configuration listed in your `launch.json` file:
    
    {
        "configurations": [
          {
            "name": "Deploy Cloud Function",
            "type": "cloudcode.cloudfunctions",
            "request": "launch",
            "functionName": "hello-world-pub-sub",
            "gen": "GEN_2",
            "entryPoint": "helloPubSub"
          },
          {
            "name": "Deploy Cloud Function",
            "type": "cloudcode.cloudfunctions",
            "request": "launch",
            "functionName": "hello-world-get",
            "gen": "GEN_2",
            "entryPoint": "helloGet"
          }
        ]
    }
    

  4. (Optional) To deploy another configuration from your `launch.json` file, move the configuration you want to deploy to the top of the `launch.json` file and click refresh **Refresh Cloud Functions Explorer**.




## Rearrange Cloud Run functions Explorer into your IDE's file Explorer

You can rearrange your Cloud Run functions Explorer into Cloud Shell's file Explorer by performing the following:

  1. Drag your Cloud Run functions Explorer into Cloud Shell's file Explorer:

![Cloud Functions Explorer rearranged](https://docs.cloud.google.com/static/code/docs/shell/images/cloud-functions-workspace-rearranged.png)

This arrangement displays your Cloud Run functions Explorer under the file Explorer so that you can view your deployed functions and Cloud Run functions workspace(s) in the same pane as your project files.

  2. (Optional) To undo this arrangement, drag the **Cloud Code: Cloud Functions** Explorer's heading back to the **Cloud Code** Explorer.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
