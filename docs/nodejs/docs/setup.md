---
url: https://docs.cloud.google.com/nodejs/docs/setup/
title: Setting up a Node.js development environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:20.171072+00:00
---

# Setting up a Node.js development environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Guides ](https://docs.cloud.google.com/nodejs/docs/setup)



Send feedback 

#  Setting up a Node.js development environment Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to prepare a local machine for [Node.js](https://nodejs.org/) development, including developing Node.js apps that run on Google Cloud. Follow this tutorial to install Node.js and relevant tools.

## Objectives

  * Install Node Version Manager (NVM).
  * Install Node.js and npm (Node Package Manager).
  * Install an editor.
  * Install the Google Cloud CLI.
  * Install the Cloud Client Libraries for Node.js.
  * Set up authentication.



## Installing NVM

[NVM](https://github.com/creationix/nvm) is a bash script for managing installations of Node.js and `npm`. NVM doesn't support Windows. For more information about managing your Node.js installation on Windows, see [nvm-windows](https://github.com/coreybutler/nvm-windows). 

For details on installing NVM, see the [installation instructions](https://github.com/nvm-sh/nvm#installing-and-updating).

## Installing Node.js and npm

Once NVM is installed, you can install Node.js and npm.

  1. To install the latest version of Node.js, run the following:
         
         nvm install stable
         

  2. Optional: To make this version your default version, run the following:
         
         nvm alias default stable
         

  3. Optional: To check what version of Node.js that you're running, run the following:
         
         node -v
         




npm is the Node Package Manager for Node.js and is normally installed alongside Node.js. You use npm to install Node.js packages from the npm repository. For example:
    
    
    npm install express
    

## Installing an editor

There are several editors that you can use to develop Node.js apps. A few popular ones include the following:

  * [Visual Studio Code](https://code.visualstudio.com/) by Microsoft
  * [IntelliJ IDEA and/or Webstorm](https://www.jetbrains.com/idea/) by JetBrains



For effective Node.js development, these editors offer features (sometimes with the help of plugins) that range from syntax highlighting, intelli-sense, and code completion to fully integrated debugging capabilities.

## Installing the Google Cloud CLI

The [gcloud CLI](https://docs.cloud.google.com/sdk) is a set of tools for Google Cloud. It contains `gcloud` and `bq`, which you can use to access Compute Engine, Cloud Storage, BigQuery, and other products and services from the command line. You can run these tools interactively or in your automated scripts.

For example, the following command deploys any Node.js web application to the App Engine standard environment. After deployment App Engine attempts to start the app with `npm start`. 
    
    
    gcloud app deploy
    

## Installing the Cloud Client Libraries for Node.js

The [Cloud Client Libraries for Node.js](https://github.com/googleapis/google-cloud-node) are the idiomatic ways for Node.js developers to integrate with Google Cloud services such as Datastore and Cloud Storage. For example, you can install the package for an individual API by using the following:
    
    
    npm install @google-cloud/storage
    

## Set up authentication

To use the Cloud Client Libraries in a local development environment, set up Application Default Credentials.

If you're using a local shell, then create local authentication credentials for your user account: 
    
    
    gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

## What's next

  * Browse the [documentation for Google Cloud products](https://docs.cloud.google.com/products).
  * Clone the [Node.js samples repository from GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples).
  * Explore [Node.js tutorials submitted by the community](https://docs.cloud.google.com/community/tutorials?q=%22Node.js%22).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
