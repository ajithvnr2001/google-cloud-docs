---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-set-up-translation/
title: Set up a translation project \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:14.921917+00:00
---

# Set up a translation project  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-set-up-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Set up a translation project Stay organized with collections  Save and categorize content based on your preferences. 

This page helps you set up a Google Distributed Cloud (GDC) air-gapped appliance project to use Vertex AI Translation. This process includes creating a project, enabling the Vertex AI Translation API, installing client libraries, defining environment variables, and authenticating your credentials. If you are new to Vertex AI, [learn more about translation features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-translation).

You set up a translation project using the GDC console and gdcloud CLI as follows:

  * **GDC console** : Enable the Vertex AI Translation API and view the service status and endpoint.
  * **The gdcloud CLI** : Configure service accounts to interact with the Vertex AI Translation API, install client libraries, and authenticate API requests.



## Create a project

Creating a translation project organizes your Vertex AI Translation resources, which include collaborators, enabled APIs, authentication credentials, and access controls.

To create your project, see [Set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project). You need your project ID when making API calls.

**Tip:** Improve security, resource management, and cost tracking by isolating your experimental, testing, and production workloads in separate GDC air-gapped appliance projects.

## Request developer permissions

You must have the AI Translation Developer role in your project to access translation services and generate an API token for request authentication and authorization.

Ask your Project IAM Admin to grant the AI Translation Developer (`ai-translation-developer`) role to your user or service account within your project namespace. For information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ao-permissions).

## Enable the Vertex AI Translation API

You must [enable the Vertex AI Translation pre-trained API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-enable-pre-trained-apis) for your project. If enabled, you can [view the service status and endpoint for the Vertex AI Translation pre-trained API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status).

## Install client libraries

Client libraries are available for the Python programming language. We recommend using these client libraries to make calls to the Vertex AI Translation API because they make it easier to access APIs.

[Install the Vertex AI Translation client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries) and follow these steps to ensure you have the correct version:

  1. Check if the Vertex AI Translation client library is installed and obtain the version number:
         
         pip freeze | grep translation
         

If the client library is already installed, you obtain an output similar to the following example:
         
         google-cloud-translation==3.8.0
         

The version number you obtain must match the client library at the following endpoint:
         
         https://GDC_URL/.well-known/static/client-libraries
         

Replace `GDC_URL` with the URL of your organization in GDC.

  2. If the version numbers don't match, uninstall the client library:
         
         pip uninstall google-cloud-translation
         

  3. If you uninstalled the Vertex AI Translation client library, you must [reinstall it](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries) by specifying the filename corresponding to your operating system.




## Set your environment variables

After installing the Vertex AI Translation client library, you can interact with the API from a Python script.

If you [set up a service account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project#set-up-service) in your project to make authorized API calls programmatically, you can define environment variables in the Python script to access values such as the service account keys when running.

Follow these steps to set required environment variables on a Python script:

  1. Create a Python script.

  2. Add the following code to the Python script:
         
         import os
         
         os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "APPLICATION_DEFAULT_CREDENTIALS_FILENAME"
         

Replace `APPLICATION_DEFAULT_CREDENTIALS_FILENAME` with the name of the JSON file that contains [the service account keys you created](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project#set-up-service) in the project, such as `my-service-key.json`.

  3. Save the Python script with a name, such as `translation.py`.

  4. Run the Python script to set the environment variables:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `translation.py`.


**Note:** Keep the script open when using the environment variables from Python or getting an authentication token.

## Set up authentication

Before you can start using the Vertex AI Translation API, you must authenticate your client credentials and request account access to your project resources. For more information, see [Authenticate API requests](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-auth).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
