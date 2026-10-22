---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/required_files/
title: Required Files and Configuration \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:05.162685+00:00
---

# Required Files and Configuration  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/required_files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Required Files and Configuration Stay organized with collections  Save and categorize content based on your preferences. 

Your project must contain, at a minimum, the following files: 

File and Location | Description  
---|---  
`/src/<your_api_class>.py` | The class file (or files, if you implement your API across multiple classes) containing your backend API.  
`/src/<your_api_server>.py` | Optional file containing your API server code, if you don't include it inside your API class.  
`/src/app.yaml` | The web app deployment descriptor required for App Engine configuration.  
  
The contents of each of these required files is documented in the following sections.

## The API class file

The required and optional contents of the class file (or files, if you use a [multi-class API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create-multi-class-api)) are fully described in the topic [Creating an Endpoints API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api).

## The API server file

This file and its contents are fully described under [Creating a Web Server](https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server).

## app.yaml

The bare minimum contents required for this file are as follows:
    
    
    # Copyright 2021 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    runtime: python27
    threadsafe: true
    api_version: 1
    basic_scaling:
      max_instances: 2
    
    skip_files:
    - ^(.*/)?#.*#$
    - ^(.*/)?.*~$
    - ^(.*/)?.*\.py[co]$
    - ^(.*/)?.*/RCS/.*$
    - ^(.*/)?\..*$
    - ^(.*/)?setuptools/script \(dev\).tmpl$
    
    handlers:
    # The endpoints handler must be mapped to /_ah/api.
    - url: /_ah/api/.*
      script: main.api
    
    libraries:
    - name: pycrypto
      version: 2.6
    - name: ssl
      version: 2.7.11
    
    env_variables:
      # The following values are to be replaced by information from the output of
      # 'gcloud endpoints services deploy swagger.json' command.
      ENDPOINTS_SERVICE_NAME: YOUR-PROJECT-ID.appspot.com
      ENDPOINTS_SERVICE_VERSION: 2016-08-01r0

where:

  * `main` is the name of the Python module and variable for your API server.
  * `threadsafe` is set to true if you want App Engine to send multiple requests in parallel, or set to false, if you want App Engine to send requests serially.



Additional but optional settings are available. See the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/python/config/appref) for more information. However, note that the information under _Requiring login or administrator status_ and _Secure URLs_ **do not apply** to backend APIs.

**Important:** The `/_ah/api/.*` URL pattern in the `app.yaml` configuration file must match the base path configured in the `@endpoints.api(base_path=...)` API definition. By default, the base path is `/_ah/api`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
