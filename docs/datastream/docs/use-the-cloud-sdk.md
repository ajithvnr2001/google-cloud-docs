---
url: https://docs.cloud.google.com/datastream/docs/use-the-cloud-sdk/
title: Use the gcloud CLI \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:26:11.093032+00:00
---

# Use the gcloud CLI  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/use-the-cloud-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Reference ](https://docs.cloud.google.com/datastream/docs/reference/rest)



Send feedback 

#  Use the gcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get started with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) so you can use it to manage private connectivity configurations, connection profiles, and streams in Datastream.

The Google Cloud CLI provides the Google Cloud CLI to interact with Datastream and other Google Cloud services. The gcloud CLI uses the API to access Datastream, so you must enable the API before you can use the tool. 

You can see `gcloud` examples in the following pages of the Datastream documentation:

  * [Manage private connectivity configurations](https://docs.cloud.google.com/datastream/docs/manage-private-connectivity-configurations)
  * [Manage connection profiles](https://docs.cloud.google.com/datastream/docs/manage-connection-profiles)
  * [Manage streams](https://docs.cloud.google.com/datastream/docs/manage-streams)



## Get started with the Google Cloud CLI

To start with the gcloud CLI, review the [Google Cloud CLI Documentation](https://docs.cloud.google.com/sdk/docs). You can get help for the tool, resources, and commands by using the `--help` flag: 
    
    
    gcloud datastream --help
    gcloud datastream private-connections create --help
    gcloud datastream connection-profiles create --help
    gcloud datastream streams create --help

Finally, configure a project as your default project with two commands. The first command below lists the configuration for the gcloud CLI, including any default project already set. The second command sets the default project. 
    
    
    gcloud config list
    gcloud config set project [PROJECT_ID]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
