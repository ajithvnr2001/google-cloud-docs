---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-set-up-stt/
title: Set up a speech recognition project \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:06.305802+00:00
---

# Set up a speech recognition project  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-set-up-stt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Set up a speech recognition project Stay organized with collections  Save and categorize content based on your preferences. 

Speech-to-Text in Google Distributed Cloud (GDC) air-gapped appliance lets you transcribe audio files into text in your applications. After creating a project and requesting developer roles, enable the Speech-to-Text API in the GDC console to view the service status and endpoint. You can then install the Python client library, define environment variables, and use the gdcloud CLI to configure service accounts and authenticate requests. If you are new to Vertex AI, see [Learn about speech recognition features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-stt).

## Create a project

Creating a speech recognition project organizes your Speech-to-Text resources, which include collaborators, enabled APIs, authentication credentials, and access controls.

To create your project, see [Set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project). You need your project ID when making API calls.

**Tip:** Improve security, resource management, and cost tracking by isolating your experimental, testing, and production workloads in separate GDC air-gapped appliance projects.

## Request developer permissions

You must have the AI Speech Developer role in your project to access speech recognition features and generate an API token for request authentication and authorization.

Ask your Project IAM Admin to grant the AI Speech Developer (`ai-speech-developer`) role to your user or service account within your project namespace. For information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ao-permissions).

## Enable the Speech-to-Text API

You must [enable the Speech-to-Text pre-trained API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-enable-pre-trained-apis) for your project. If enabled, you can [view the service status and endpoint for the Speech-to-Text pre-trained API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status).

## Install client libraries

Client libraries are available for the Python programming language. We recommend using these client libraries to make calls to the Speech-to-Text API because they make it easier to access APIs.

[Install the Speech-to-Text client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries) and follow these steps to ensure you have the correct version:

  1. Check if the Speech-to-Text client library is installed and obtain the version number:
         
         pip freeze | grep speech
         

If the client library is already installed, you obtain an output similar to the following example:
         
         google-cloud-speech==2.15.0
         

The version number you obtain must match the client library at the following endpoint:
         
         https://GDC_URL/.well-known/static/client-libraries
         

Replace `GDC_URL` with the URL of your organization in GDC.

  2. If the version numbers don't match, uninstall the client library:
         
         pip uninstall google-cloud-speech
         

  3. If you uninstalled the Speech-to-Text client library, you must [reinstall it](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries) by specifying the filename corresponding to your operating system.




## Set your environment variables

After installing the Speech-to-Text client library, you can interact with the API from a Python script.

If you [set up a service account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project#set-up-service) in your project to make authorized API calls programmatically, you can define environment variables in the Python script to access values such as the service account keys when running.

Follow these steps to set required environment variables on a Python script:

  1. Create a Python script.

  2. Add the following code to the Python script:
         
         import os
         
         os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "APPLICATION_DEFAULT_CREDENTIALS_FILENAME"
         

Replace `APPLICATION_DEFAULT_CREDENTIALS_FILENAME` with the name of the JSON file that contains [the service account keys you created](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project#set-up-service) in the project, such as `my-service-key.json`.

  3. Save the Python script with a name, such as `speech.py`.

  4. Run the Python script to set the environment variables:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `speech.py`.


**Note:** Keep the script open when using the environment variables from Python or getting an authentication token.

## Set up authentication

Before you can start using the Speech-to-Text API, you must authenticate your client credentials and request account access to your project resources. For more information, see [Authenticate API requests](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-auth).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
