---
url: https://docs.cloud.google.com/vision-ai/docs/cloud-environment/
title: Set up a project and a development environment \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:12.528132+00:00
---

# Set up a project and a development environment  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/cloud-environment/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Set up a project and a development environment Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to set up a Google Cloud project to start using Gemini Enterprise Agent Platform Vision.

## Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Vertex AI Vision API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable visionai.googleapis.com

  8. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant the `roles/visionai.editor` IAM role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=roles/visionai.editor

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     4. Generate the key file: 
            
            gcloud iam service-accounts keys create FILE_NAME.json --iam-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace the following: 

        * `FILE_NAME`: a name for the key file
        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
  9. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
         
         set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Vertex AI Vision API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable visionai.googleapis.com

  16. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant the `roles/visionai.editor` IAM role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=roles/visionai.editor

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     4. Generate the key file: 
            
            gcloud iam service-accounts keys create FILE_NAME.json --iam-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace the following: 

        * `FILE_NAME`: a name for the key file
        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
  17. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
         
         set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.


**Roles** : Depending on your use case, the `project.editor` role may be more appropriate. If you grant the `visionai.editor` role alone to your policy binding, you need to grant additional roles for certain operations. For example, you need to add `bigquery.dataEditor` to use a BigQuery connector, `cloudfunctions.developer` to use Cloud Run functions, etc. 

Certain tasks require you to use additional Google Cloud products in addition to Agent Platform Vision. You might need to perform additional setup tasks to use other Google Cloud products.

## Gemini Enterprise Agent Platform Vision SDK

The Agent Platform Vision Software Development Kit (SDK) contains tools and libraries for you to develop programs and custom workflows with Agent Platform Vision.

These tools refer to a set of binary source files that help your productivity when you use or develop solutions using Agent Platform Vision. You can also add these binary source files into your scripting to help manage larger scale deployments. The command line interface (CLI) `vaictl` is an example in this category.

Libraries refers to a set of programming APIs that you can use to programmatically manage, control, and perform I/O of different forms with Agent Platform Vision. The C++ programming API is an example in this category.

The code for both tools and libraries are open source and we welcome developers to build them directly. For tools, we also offer prebuilt binary files on specific platforms that you can download for direct use. We also offer Docker images for cases when your platform is not directly supported.

## Prerequisites

Consider these prerequisites before you use the Gemini Enterprise Agent Platform Vision SDK.

### Supported platforms

We only directly support x86 machines running a Debian-based Linux distribution. We also offer a Docker image with tools already built and installed if you use a different platform.

### Additional software requirements

Most of the third party software dependencies the Gemini Enterprise Agent Platform Vision SDK requires are automatically managed when you install the prebuilt binaries. However, to use certain aspects of the SDK features and workflows you must install additional dependencies. This section lists these exceptions and how to download and install them.

#### Python SDK

The Python pip package installs all of its dependencies automatically. However, your basic underlying Python installation must meet the following conditions:

  * Python >= 3.8.



#### Build from source dependencies

Most users can use the prebuilt SDK binaries for their workflow. If you want to develop and build the SDK from source, you must also make sure your system meets the following requirements.

  * Install Bazel. For installation instructions, see the [Bazel documentation](https://bazel.build/install/ubuntu).
  * On Ubuntu 20.04, you also need several system dependencies. You can install them with the following command:
        
        apt-get install -y --no-install-recommends \
            autoconf \
            automake \
            build-essential \
            ca-certificates \
            flex \
            bison \
            python3 \
            nasm \
            libjpeg-dev
        




## Get prebuilt binaries

The `vaictl` tool is the ready-made binary tool that can be used to control Agent Platform Vision, as well as to send and receive data that it processes.

This section shows ways for you to download and install this tool.

### Install the Debian package

You have two options for using the `vaictl` command-line tool, which you need to work with I/O (stream data):

  * Install the command-line tool locally (OS: Debian GNU/Linux, CPU architecture: x86_64) _or_
  * Run the commands in a Docker image that has all dependencies installed.



Use the following steps to get the `vaictl` command-line tool:

### Download package

For direct installations, we only support Debian/Ubuntu distributions. 

You can also download this Debian package from the [Gemini Enterprise Agent Platform Vision SDK GitHub releases page](https://github.com/google/visionai/releases). 

  1. (Optional) Remove prior versions of `vaictl`.

Before you can install the `vaictl` command-line tool, you must delete any prior versions of the tool on your machine:
         
         sudo apt-get remove visionai

  2. Download the required package. You can download the package from the [GitHub releases page](https://github.com/google/visionai/releases), or use the following command: 
         
         wget https://github.com/google/visionai/releases/download/v0.0.5/visionai_0.0-5_amd64.deb

  3. After downloading the package, run the following command in the directory you downloaded the file: 
         
         sudo apt install ./visionai_0.0-5_amd64.deb

  4. Verify installation: 
         
         vaictl --help




### Get Docker

You can get a Docker image that has the Gemini Enterprise Agent Platform Vision SDK and all its dependencies already pre-installed. This Docker image is available at `gcr.io/visionai-public-images/vaictl`. 

  1. Download the image from Container Registry: 
         
         docker pull gcr.io/visionai-public-images/vaictl

  2. Run an interactive container terminal. 
         
         docker run -it --rm gcr.io/visionai-public-images/vaictl /bin/bash

  3. Verify functionality: 
         
         vaictl --help




### Get the source code

The Gemini Enterprise Agent Platform Vision SDK is open-source and publicly available on [GitHub](https://github.com/google/visionai).

While the SDK depends on the service API definitions, this dependency is already automatically managed by [Bazel](https://github.com/bazelbuild/bazel) and you don't need to explicitly acquire it. However, if you need direct access to the service APIs, you can get them on the [`googleapis` GitHub repository](https://github.com/googleapis/googleapis/tree/master/google/cloud/visionai/v1).

## The Python programming SDK

Agent Platform Vision also supports a Python SDK. To program with this SDK, just make sure that you have met the basic Python SDK dependencies before you install the Python SDK.

For SDK reference information, see the [Python SDK reference](https://docs.cloud.google.com/vision-ai/docs/reference/python/visionai).

For example codes that use the Python SDK, see the [Face blur with the Python SDK tutorial](https://docs.cloud.google.com/vision-ai/docs/face-blur-python), or see some examples in the source distribution in the `visionai/python/examples/` directory.

### Get the Python SDK package

The Gemini Enterprise Agent Platform Vision SDK also contains a Python library. Download and install the prebuilt version of the Python SDK with the following instructions.

  1. Download the package.

You can download the Python SDK package from the [Gemini Enterprise Agent Platform Vision SDK GitHub releases page](https://github.com/google/visionai/releases), or you can run the command:
         
         wget https://github.com/google/visionai/releases/download/v0.0.5/visionai-0.0.5-py3-none-any.whl
         

  2. Optional. Create and activate a new virtual environment:
         
         python3 -m venv vaivenv
         source vaivenv/bin/activate
         

  3. Install the package:
         
         pip3 install visionai-0.0.5-py3-none-any.whl
         

  4. Optional. Confirm that installation worked:
         
         python3
         
         
         import visionai
         

  5. Optional. Deactivate your virtual environment:
         
         deactivate
         




## The C++ programming SDK

C++ is the first programming SDK we support. The C++ public SDK is located in `visionai/public/streams.h`. For reference information, see the [reference documentation](https://docs.cloud.google.com/vision-ai/docs/reference/cpp).

## What's next

  * Optional: Learn how to [build and test using the C++ SDK](https://docs.cloud.google.com/vision-ai/docs/build-test-cpp).
  * Learn how to [ingest data](https://docs.cloud.google.com/vision-ai/docs/create-manage-streams#ingest-videos) into an app and read about processing components you can add in [Build an app](https://docs.cloud.google.com/vision-ai/docs/build-app).
  * Learn about output storage and processing options in [Connect app output to a data destination ](https://docs.cloud.google.com/vision-ai/docs/connect-data-destination).
  * Read about how to [Search Warehouse data in the console](https://docs.cloud.google.com/vision-ai/docs/search-streaming-warehouse).



[ Previous arrow_back  Quickstart: Build an app in the console  ](https://docs.cloud.google.com/vision-ai/docs/build-app-console-quickstart)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
