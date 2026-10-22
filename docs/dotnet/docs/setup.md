---
url: https://docs.cloud.google.com/dotnet/docs/setup/
title: Setting up a .NET development environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:51.564824+00:00
---

# Setting up a .NET development environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Guides ](https://docs.cloud.google.com/dotnet/docs/setup)



Send feedback 

#  Setting up a .NET development environment Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to prepare your local machine for developing [.NET](https://dotnet.microsoft.com/en-us/learn/dotnet/what-is-dotnet) and [.NET Framework](https://dotnet.microsoft.com/en-us/learn/dotnet/what-is-dotnet-framework) apps that run on Google Cloud and call Google Cloud APIs.

## Install a development environment

The recommended development environment for running the .NET tutorials and sample apps in this documentation is [Visual Studio](https://www.visualstudio.com/) or [Visual Studio Code](https://code.visualstudio.com/).

## Create a Google Cloud project

[Create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to run your apps. Google Cloud projects form the basis for creating, enabling, and using all Google Cloud services.

## Set up authentication

Your .NET app must authenticate itself to use Google Cloud APIs. You use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials), which let you provide credentials for either local development or in a production environment.

If you're using a local shell, then create local authentication credentials for your user account: 
    
    
    gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries). For general information about authentication, see [Authentication at Google](https://docs.cloud.google.com/docs/authentication).

## (Optional) Install SDKs

Even though you can create and manage Google Cloud resources using your web browser using the [Google Cloud console](http://console.cloud.google.com), if you'd prefer to manage your Google Cloud resources from the command-line, you can consider installing the [Google Cloud CLI](https://docs.cloud.google.com/sdk). The gcloud CLI is a command-line interface for Google Cloud products and services.

## What's next

  * [Transcribe audio to text with Speech-to-Text API](https://docs.cloud.google.com/speech-to-text/docs/transcribe-client-libraries)

  * [Deploy a .NET app to App Engine flexible environment](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/tree/master/appengine/flexible)

  * [Deploy a .NET Framework app to Compute Engine](https://docs.cloud.google.com/dotnet/docs/getting-started/hello-world)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
