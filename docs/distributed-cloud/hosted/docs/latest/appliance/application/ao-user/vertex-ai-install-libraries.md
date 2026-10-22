---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries/
title: Install Vertex AI client libraries \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:46.596797+00:00
---

# Install Vertex AI client libraries  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Install Vertex AI client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the various types of client libraries that Google Distributed Cloud (GDC) air-gapped appliance offers for Vertex AI APIs and explains how to install them from the tar file.

GDC air-gapped appliance offers various Vertex AI services, including Optical Character Recognition (OCR), Vertex AI Translation, and Speech-to-Text. Each service provides its own API, which you can install using client libraries.

Client libraries simplify accessing Vertex AI APIs from supported languages on GDC air-gapped appliance. Although you can use Vertex AI APIs directly by making raw server requests, client libraries provide simplifications that reduce the required code.

Client libraries are the recommended method for accessing Vertex AI APIs programmatically. Install a Vertex AI client library by extracting the library file directly from the tar file.

## Vertex AI client libraries

Vertex AI offers different versions of client libraries for CentOS and Ubuntu operating systems.

The naming conventions of Vertex AI client libraries in the tar file are based on the operating system, the service name, and the version. The filenames adhere to the following format:
    
    
    OS-google-cloud-SERVICE-VERSION.tar.gz
    

Replace the following:

  * `OS`: the name of the operating system where you want to install the client library. Allowed values are `centos` and `ubuntu`.
  * `SERVICE`: the name of the Vertex AI service from which you want to download the client library. The following are the allowed values:

    * `aiplatform`: the Vertex AI Platform client library.
    * `speech`: the Speech-to-Text client library.
    * `translate`: the Vertex AI Translation client library.
    * `vision`: the OCR client library.
  * `VERSION`: the version number of the client library, such as `3.8.0`.




The following table contains the Vertex AI client libraries that GDC air-gapped appliance supports:

Vertex AI service | Operating system | Filename  
---|---|---  
OCR | Centos | `centos-google-cloud-vision-3.0.0.tar.gz`  
Ubuntu | `ubuntu-google-cloud-vision-3.0.0.tar.gz`  
Speech-to-Text | Centos | `centos-google-cloud-speech-2.15.0.tar.gz`  
Ubuntu | `ubuntu-google-cloud-speech-2.15.0.tar.gz`  
Vertex AI Translation | Centos | `centos-google-cloud-translate-3.8.0.tar.gz`  
Ubuntu | `ubuntu-google-cloud-translate-3.8.0.tar.gz`  
Vertex AI Platform | Centos | `centos-google-cloud-aiplatform-1.34.0.tar.gz`  
Ubuntu | `ubuntu-google-cloud-aiplatform-1.34.0.tar.gz`  
  
## Before you begin

Before downloading the tar file and extracting client libraries, follow these steps:

  1. [Set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project).

  2. Authenticate with gdcloud CLI:
         
         gdcloud auth login
         

For more information about how to authenticate with your configured identity provider, see [the gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth).

  3. Assign the Cloud AI Viewer (`cloud-ai-viewer`) role to [a service account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project#set-up-service). The service account requires this role to access the Vertex AI services.

  4. Verify that you have installed Python version 3.7.




## Install a client library

After completing the prerequisites, follow these steps to download the tar file, and use the tar file to install a client library:

  1. Download the client library you want to install:
         
         wget https://GDC_URL/.well-known/static/client-libraries/CLIENT_LIBRARY
         

Replace the following:

     * `GDC_URL`: the URL of your organization in GDC.
     * `CLIENT_LIBRARY`: the filename of the client library you want to download.
  2. Extract the library file:
         
         tar -zxf CLIENT_LIBRARY
         

  3. Install the client library in GDC air-gapped appliance:
         
         pip install -r FOLDER_NAME/requirements.txt --no-index --find-links FOLDER_NAME
         

Replace `FOLDER_NAME` with the path to the local directory where you downloaded the library file.

  4. Import the client library using a Python script. The following example shows a code snippet of a Python script that imports the Vertex AI Translation client library to illustrate what importing libraries looks like:
         
         from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
         translate_client = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[Client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)(
          client_options={"API_ENDPOINT": "https://foo-translation.googleapis.com"})
         result
         = translate_client.[translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)(text, target_language="ru")
         
         [...]
         

This code sample is not complete. To make a Vertex AI Translation request, [learn about translation features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-translation).

  5. Save the Python script with a name, such as `translation-service.py`.

  6. Run the Python script:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `translation-service.py`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
