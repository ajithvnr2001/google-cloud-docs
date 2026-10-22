---
url: https://docs.cloud.google.com/bigtable/docs/cbt-overview/
title: cbt CLI overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:19.224683+00:00
---

# cbt CLI overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/cbt-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  cbt CLI overview

The `cbt` CLI lets you perform administrative and data operations on Bigtable directly from your terminal. You can use it to manage instances, create and modify tables, and read or write data without writing custom code. For general information about Bigtable, see the [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview).

## Install the `cbt` CLI 

You can install the `cbt` CLI as a [gcloud CLI component](https://docs.cloud.google.com/sdk/docs/managing-components).

The `cbt` CLI doesn't implement smart retries or error handling. When you work in production environment, use a Bigtable client library or the Google Cloud console.

  1. [Install the gcloud CLI](https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk).
  2. Run the following commands:
         
         gcloud components update
         gcloud components install cbt

If the `cbt` CLI is already installed, the terminal window displays the `All components are up to date` message.


**Note:** If you install the gcloud CLI in a directory that is not your home directory, you might need to update your PATH environment variable to include the path to `google-cloud-sdk/bin`.

## Verify the installation

Run the following `cbt` CLI command to verify installation of the CLI:
    
    
    cbt listinstances
    

The terminal window displays two columns named `Instance Name` and `Info`.

## Create a .cbtrc file

You can store required options and parameters, such as `-project`, `-instance`, `-creds`, `-admin-endpoint`, or `-data-endpoint` options, in a single `.cbtrc` file for convenience.

  1. In your `.cbtrc` file, configure `cbt` to use your project and instance by replacing project-id with the ID for the project where you created your Bigtable instance:
         
         echo project = project-id > ~/.cbtrc
         echo instance = quickstart-instance >> ~/.cbtrc

  2. Verify that you set up the `.cbtrc` file correctly:
         
         cat ~/.cbtrc

The terminal displays the contents of the `.cbtrc` file, which looks similar to the following settings:
         
         project = project-id
         instance = quickstart-instance

Now you can use the `cbt` CLI with your instance.




## Use the `cbt` CLI 

For details about using the `cbt` CLI , including a list of available commands, see the [ `cbt` CLI reference](https://docs.cloud.google.com/bigtable/docs/cbt-reference).

The `cbt` CLI is written in [Go](https://golang.org) using the [Go client library for Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/libraries). Source code is available in the [GoogleCloudPlatform/google-cloud-go](https://github.com/GoogleCloudPlatform/google-cloud-go/tree/master/bigtable/cmd/cbt) GitHub repository, which mirrors [code.googlesource.com/gocloud](https://code.googlesource.com/gocloud/+/master/bigtable/cmd/cbt/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
