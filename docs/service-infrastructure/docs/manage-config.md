---
url: https://docs.cloud.google.com/service-infrastructure/docs/manage-config/
title: Managing Service Configurations \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:20.468355+00:00
---

# Managing Service Configurations  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/manage-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Managing Service Configurations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage service configurations using Service Infrastructure.

A [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/glossary#config) is a specification that describes different aspects of a [managed service](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed).

The Service Management API methods typically involved in managing service configurations are:

  * Using [`services.configs.create`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/create) or [`services.configs.submit`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit) to submit service configurations.
  * Using [`services.configs.list`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/list) and [`services.configs.get`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/get) to retrieve service configurations.
  * Using [`services.generateConfigReport`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport) to get a change report between two service configurations.



## Before you begin

To run the examples in this guide, make sure you first follow the instructions to complete the initial setup in [Getting Started with the Service Management API](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started).

### Submitting service configuration source files

To update your service configuration, you need to submit a list of service configuration source files to the Service Management API, and the server will compile them into a validated service configuration.

The source files can have the following formats:

  * [OpenAPI](https://github.com/OAI/OpenAPI-Specification) v2
  * Protocol Buffers descriptor
  * [`google.api.Service`](https://github.com/googleapis/googleapis/blob/master/google/api/service.proto) in JSON or YAML format



The Service Management API does not take `.proto` files, you need to generate protobuf descriptors from your `.proto` files before submitting them. You can use use the following command to generate the descriptor files:
    
    
    $ protoc hello.proto --include_source_info --include_imports --descriptor_set_out=service.descriptors *.proto
    

The recommended way to submit service configuration source files is to use the gcloud CLI.
    
    
    $ gcloud auth login
    $ gcloud endpoints services deploy [a list of service configuration source files]
    

You can also call the Service Management API directly to submit source files. For example, if you have this OpenAPI definition (`hello.json`):
    
    
    {
      "swagger": "2.0",
      "info": {
        "title": "Hello Endpoints API.",
        "description": "Hello Endpoints API.",
        "version": "v1"
      },
      "host": "endpointsapis.appspot.com",
      "schemes": ["https"],
      "paths": {
        "/v1/hello": {
          "get": {
            "tags": ["endpointsapis"],
            "operationId": "GetHello",
            "description": "Returns \"Hello\" with given name in the response.",
            "parameters": [
              {
                "name": "name",
                "description": "Name to be greeted.",
                "in": "query",
                "type": "string"
              }
            ],
            "responses": {
              "default": {
                "description": "Successful operation",
                "schema": {
                  "$ref": "#/definitions/GetHelloResponse"
                }
              }
            }
          }
        }
      },
      "definitions": {
        "GetHelloResponse": {
          "description": "Response message for GetHello method.",
          "type": "object",
          "properties": {
            "response": {
              "description": "String of \"Hello \" + `name` provided in the request.",
              "type": "string"
            }
          }
        }
      }
    }
    

You can make the following API call to submit the OpenAPI spec:
    
    
    $ gcurl -d "
    {
      'serviceName': 'endpointsapis.appspot.com',
      'configSource':
      {
        'files': [
          {
            'fileContents': '$(base64 hello.json | sed ':a;N;$!ba;s/\n//g')',
            'fileType': 'OPEN_API_JSON',
            'filePath': 'hello.json',
          }
        ]
      }
    }" https://servicemanagement.googleapis.com/v1/services/endpointsapis.appspot.com/configs:submit
    {
      "name": "operations/serviceConfigs.endpointsapis.appspot.com:a7651c15-9017-4274-b065-d644cc337847",
      "metadata": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.OperationMetadata",
        "resourceNames": [
          "services/endpointsapis.appspot.com/configs/2016-07-29r10"
        ],
        "startTime": "2016-07-29r10T23:59:21.081Z",
        "persisted": true
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.SubmitConfigSourceResponse",
        "serviceConfig": {
          "name": "endpointsapis.appspot.com",
          "title": "Hello Endpoints API.",
      ...
    }
    

## Generating service configuration reports

Before submitting a new service configuration version, you might want to call the [`services.generateConfigReport`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport) method to get a report of changes relative to an existing service configuration version. You can specify the version to be compared against using the `old_config` field in the request, or you can simply skip this field to generate a report against the latest service configuration version.

Assuming the new OpenAPI configuration file is called `hello.json`, you can run the following command:
    
    
    $ gcurl -d "
    {
      'newConfig':
      {
        '@type': 'type.googleapis.com/google.api.servicemanagement.v1.ConfigSource',
        'files': [
          {
            'fileContents': '$(base64 hello.json | sed ':a;N;$!ba;s/\n//g')',
            'fileType': 'OPEN_API_JSON',
            'filePath': 'hello.json',
          }
        ],
      }
    }" https://servicemanagement.googleapis.com/v1/services:generateConfigReport
    

If you want to generate report for a specific configuration version, you can run:
    
    
    # Generate config report for the local configuration from `/tmp/hello.json`
    # and the configuration version `2016-07-29r10`.
    $ gcurl -d "
    {
      'newConfig':
      {
        '@type': 'type.googleapis.com/google.api.servicemanagement.v1.ConfigSource',
        'files': [
          {
            'fileContents': '$(base64 hello.json | sed ':a;N;$!ba;s/\n//g')',
            'fileType': 'OPEN_API_JSON',
            'filePath': 'hello.json',
          }
        ],
      },
      'oldConfig':
      {
        '@type': 'type.googleapis.com/google.api.servicemanagement.v1.ConfigRef',
        'name': 'services/endpointsapis.appspot.com/configs/2016-07-29r10'
      }
    }" https://servicemanagement.googleapis.com/v1/services:generateConfigReport
    

## Getting prior service configuration versions

The Service Management API keeps a version history of submitted service configurations. You can list them or retrieve a specific version using the [`services.configs.list`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/list) or [`services.configs.get`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/get) methods, as illustrated by the following commands:
    
    
    # List the service configuration history for a managed service.
    $ gcurl https://servicemanagement.googleapis.com/v1/services/endpointsapis.appspot.com/configs
    {
      "serviceConfigs": [
        {
          "name": "endpointsapis.appspot.com",
          "title": "Hello Endpoints API",
          "id": "2016-07-16r1",
          ...
        },
        {
          "name": "endpointsapis.appspot.com",
          "title": "Hello Endpoints API",
          "id": "2016-07-16r0",
          ...
        }
      ]
    }
    
    # Get a specific version of the service configuration for a managed service.
    $ gcurl https://servicemanagement.googleapis.com/v1/services/endpointsapis.appspot.com/configs/2016-07-16r0
    {
      "name": "endpointsapis.appspot.com",
      "title": "Hello Endpoints API",
      "id": "2016-07-16r0",
      ...
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
