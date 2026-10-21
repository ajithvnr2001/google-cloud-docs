---
url: https://docs.cloud.google.com/appengine/docs/admin-api/creating-config-files/
title: Creating JSON Configuration Files for Your Deployments \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:52.504773+00:00
---

# Creating JSON Configuration Files for Your Deployments  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/creating-config-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Creating JSON Configuration Files for Your Deployments Stay organized with collections  Save and categorize content based on your preferences. 

To deploy a version of your app with the Admin API, you define the configuration details of your version using a JSON formatted file. You can either manually create the configuration file or convert an existing `app.yaml` file.

There are two parts to creating a JSON formatted configuration file:

  1. Define the configuration information for the version that you want to deploy.
  2. Define a `deployment` section to specify all your app's files and resources that you want to deploy.

**Tip:** Consider programmatically generating the `app.json` configuration file.

## Before you begin

You must first [upload all the files and resources of your app to a Cloud Storage bucket](https://docs.cloud.google.com/appengine/docs/admin-api/uploading-resources) before you can create the `app.json` configuration file.

## Manually creating the JSON configuration file

Use the following steps if you need to manually create the configuration file, for example, when your app excludes an `app.yaml` or your existing Java app uses an `appengine-web.xml` file.

To manually create the `app.json` configuration file for deploying your app with the Admin API:

  1. Create a file name `app.json`.
  2. Use the configuration information that is provided in the [apps.services.versions collection](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions) to define and configure the version that you want to deploy.
  3. Use the template in the Defining the `deployment` section to specify all the files and resources that you want to deploy from your Cloud Storage bucket.



Also see the Example section below to assist you with creating your `app.json` configuration file.

## Converting an `app.yaml` file into the JSON format

**Note:** The `convert_yaml.py` tool requires Python 2.7 and is incompatible with Python 3. Additionally, this tool doesn't support newer runtimes in the App Engine flexible environment that require the `runtime_config` element to be specified in the `app.yaml` file.

You can use the `convert_yaml.py` tool to convert and generate an `app.json` version from an existing [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml) file.

If an `app.yaml` file exists, which you normally use to [manually deploy versions of your app](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app), you can retain that information by converting those configuration settings into the JSON format.

### Prerequisite

Download and install the [`convert_yaml.py` tool](https://github.com/GoogleCloudPlatform/appengine-config-transformer/blob/master/README.md), including the specified requirements.

### Converting YAML files with the `convert_yaml.py` tool

To convert your `app.yaml` file with the `convert_yaml.py` tool:

  1. Locate and note the directory path to your `app.yaml`.

Example:
         
         cd root/apps-container/my-application/
         

Where the `app.yaml` of the `example-python-app.py` application might look like:
         
         service: default
         version: v1
         runtime: python27
         threadsafe: true
         
         handlers:
         - url: /.*
           script: example-python-app.py
         

  2. Navigate to the local directory where you downloaded the `convert_yaml.py` tool, for example:
         
         cd root/tools/appengine-config-transformer
         

  3. Create the `app.json` file from the `app.yaml` file by running the `convert_yaml.py` tool:
         
         python ./convert_yaml.py [DIRECTORY_PATH]/app.yaml > [DIRECTORY_PATH]/app.json
         

Where `[DIRECTORY_PATH]` is the directory path to your `app.yaml` file.

A JSON version (`app.json`) of your `app.yaml` file is created in the `[DIRECTORY_PATH]` directory.

  4. Ensure that the ID of your version is defined in the `app.json` configuration file.

If your `app.yaml` file excludes the `version: [VERSION_NAME]` element, then the `"id": [VERSION_NAME]` element is not included in your `app.json` file after the conversion. For example, if you want to set your version ID to `v1`, you must manually add the following line to your `app.json` file:
         
         "id": "v1",
         

  5. Use the template in the Defining the `deployment` section to specify all the files and resources of your app that you want to deploy.




Also see the Example section below to assist you with creating your `app.json` configuration file.

## Defining the `deployment` section

To create a `deployment` section in the `app.json` configuration file and manually define all of the resources that are located in your Cloud Storage bucket, you use the reference information in the [`deployment` section](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#deployment) of the `apps.services.versions` collection. If you are defining individual files, you can use the following template:
    
    
    "deployment": {
      "files": {
        "my-resource-file1": {
          "sourceUrl": "https://storage.googleapis.com/[MY_BUCKET_ID]/my-application/my-resource-file1"
        },
      }
    },
    

Where `my-resource-file1` defines the file name and relative directory path of where you want to deploy that file in App Engine.

## Example `app.json` file

Use the following example `app.json` to help you create your configuration file.

In the following `app.json` example, the `v1` version ID is defined along with a [`deployment`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#deployment) section that includes two example source files from the `[MY_BUCKET_ID]` Cloud Storage bucket.
    
    
    {
      "deployment": {
        "files": {
          "example-resource-file1": {
            "sourceUrl": "https://storage.googleapis.com/[MY_BUCKET_ID]/example-application/example-resource-file1"
          },
          "images/example-resource-file2": {
            "sourceUrl": "https://storage.googleapis.com/[MY_BUCKET_ID]/example-application/images/example-resource-file2"
          },
        }
      },
      "id": "v1",
      "handlers": [
        {
          "urlRegex": "/.*",
          "script": {
            "scriptPath": "example-python-app.py"
          }
        },
      ],
      "runtime": "python27",
      "threadsafe": true,
    }
    

**Tip:** Not all of the runtimes that are supported by App Engine include support for a [`ScriptHandler`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#scripthandler). For more information, see the corresponding `app.yaml` or `appengine-web.xml` reference of your [language's runtime](https://docs.cloud.google.com/appengine/docs).

## What's next

  * [Deploying Versions to Your App](https://docs.cloud.google.com/appengine/docs/admin-api/deploying-apps)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
