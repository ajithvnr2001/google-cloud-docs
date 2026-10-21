---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults/
title: Set defaults for gcloud commands \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:16.080271+00:00
---

# Set defaults for gcloud commands  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Set defaults for gcloud commands Stay organized with collections  Save and categorize content based on your preferences. 

In the Google Cloud CLI, configurations enable you to set properties that affect the behavior of the active `gcloud` session. A `default` configuration is created when you initialize Google Cloud CLI and you can create other named configurations.

A configuration can include default values for specific properties so that you do not need to specify them in your commands.

For more information about using configurations, see the [gcloud config](https://docs.cloud.google.com/sdk/gcloud/reference/config) documentation.

## Setting defaults

You can set a default project, repository, and repository location in the Google Cloud CLI active configuration so that you don't need to include them in commands where those values are required.

If you do specify a value for a project, repository, or repository location, that value overrides the configured default. You can do this with the `--repository` or `--location` flag in your command.

If you're using repository modes other than standard mode, or frequently using repositories in different locations, setting default values might not be helpful.

### Setting a default project

**Note:** When you set a default project, the setting applies to all `gcloud` commands that include a `--project` flag. The default repository and repository location settings are specific to Artifact Registry commands.

To set default project for all `gcloud` commands, run the command:
    
    
    gcloud config set project PROJECT
    

Replace PROJECT with the ID of the project or fully qualified identifier for the project.

To override the default, use the `--project` flag in your command. For example
    
    
     gcloud artifacts packages list --project=my-project
    

### Setting a default repository

To set a default repository, run the command:
    
    
    gcloud config set artifacts/repository REPOSITORY
    

Replace REPOSITORY with the name of the repository, or fully qualified identifier for the repository.

To override the default, use the `--repository` flag in your command. For example
    
    
    gcloud artifacts packages list --repository=my-repo
    

### Setting a default location

To set a default repository location, run the command:
    
    
    gcloud config set artifacts/location LOCATION
    

Replace `LOCATION` with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 

To view a list of supported locations, run the command:
    
    
    gcloud artifacts locations list
    

To override the default, use the `--location` flag in your command. For example
    
    
    gcloud artifacts packages list --repository=my-repo --location=us-central1
    

## Removing default values

When you remove a default value for a configuration property, you must specify it in `gcloud` commands that require the property.

To unset the default project run the following command:
    
    
    gcloud config unset project
    

To unset the default repository, run the following command:
    
    
    gcloud config unset artifacts/repository
    

To unset the default location, run the following command:
    
    
    gcloud config unset artifacts/location
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
