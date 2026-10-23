---
url: https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery-apis/
title: Shadow API Discovery: management APIs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:26.386472+00:00
---

# Shadow API Discovery: management APIs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Shadow API Discovery: management APIs Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

**Preview — Shadow API Discovery**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides reference syntax for managing Apigee Shadow API Discovery from the Apigee Management (APIM) APIs. Documentation for the Management APIs related to Shadow API Discovery, including information on each field in a request, can be found at <https://cloud.google.com/apigee/docs/reference/apis/apim/rest> and <https://cloud.google.com/apigee/docs/reference/apis/apim/rpc>

For an overview of Shadow API Discovery and instructions for managing it using the Apigee UI in Cloud console, see [Shadow API discovery](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery). Information on the general behaviors and limitations of Shadow API Discovery is in [Behaviors and limitations](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery#behaviors-and-limitations). 

## Parameters in reference API calls

The API calls on this page can use the following parameters, which refer to either your Apigee account information (such as your project) or information used when creating observation jobs. See [Create observation jobs](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery#create-observation-jobs) for more information on each of these fields. 

  * OBSERVATION_JOB_LOCATION is a location for an observation job.
  * OBSERVATION_JOB_NAME is an observation job name.
  * OBSERVATION_SOURCE_LOCATION is a source location for the observation job.
  * OBSERVATION_SOURCE_NAME is an observation source name.
  * PROJECT is your Apigee project.



## Create an observation job

Creating an observation job requires multiple steps/API requests.

  1. **Create an observation source:** To create a new observation source rather than using an existing one, make a POST request to the observationSources endpoint with the observation source details.  

         
         curl \ https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_SOURCE_LOCATION/observationSources?observation_source_id=OBSERVATION_SOURCE_NAME \
         -X POST \
         -H 'Content-type: application/json' \
         -d @- <<'EOF'
         {
           "gclbObservationSource": {
             "pscNetworkConfigs": [
               {
                 "network": "projects/PROJECT/global/networks/{network_name}",
                 "subnetwork":"projects/PROJECT/regions/OBSERVATION_SOURCE_LOCATION/subnetworks/{subnet_name}"
               }
             ]
           }
         }
         EOF

Creation of an observation source requires several minutes and starts an [LRO](https://google.aip.dev/151), with a response like this: 
         
         {
         "name": "projects/{project/locations/OBSERVATION_SOURCE_LOCATION/operations/operation-",
         "metadata": {
           "@type": "type.googleapis.com/google.cloud.apim.vl.ApiDiscoveryOperationMetadata",
           "createTime": "",
           "target": "projects/PROJECT/locations/OBSERVATION_SOURCE_LOCATION/observationSources/OBSERVATION_SOURCE_NAME",
           "verb": "create",
           "requestedCancellation": false,
           "apiVersion": "vl"
         },
         "done": false
         }

  2. To view the newly created observation source: 
         
         curl \
         https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_SOURCE_LOCATION/observationSources/OBSERVATION_SOURCE_NAME

  3. **Create an observation job:** Create a job that looks for shadow APIs using the source you just created: 
         
         curl \
         https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_JOB_LOCATION/observationJobs?observation_job_id=OBSERVATION_JOB_NAME \
         -X POST \
         -H 'Content-type: application/json' \
         -d @- <<'EOF'
         {
           "sources": [
             "projects/PROJECT/locations/OBSERVATION_SOURCE_LOCATION/observationSources/OBSERVATION_SOURCE_NAME"
           ]
         }
         EOF




## Enable an observation job

Use the following command to enable a new observation job or a disabled existing job.
    
    
    curl https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_JOB_LOCATION/observationJobs/OBSERVATION_JOB_NAME:enable \
    -X POST \
    -H 'Content-type: application/json' \
    -d @- <<'EOF'
    {}
    EOF

## View discovered APIs

To view APIs discovered by enabled observation jobs, submit this command:
    
    
    curl https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_JOB_LOCATION/observationJobs/OBSERVATION_JOB_NAME/apiObservations \
    -X GET

## Manage tags on observation results

To list the tags already added to results:
    
    
    curl -H "https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_JOB_LOCATION:listApiObservationTags"
      

To manage tags:
    
    
    curl -H "Content-Type: appication/json" \
    "https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_JOB_LOCATION/observationJobs/OBSERVATION_JOB_NAME/apiObservations:batchEditTags" \
    -X POST -d @- <<'EOF'
    {
      "requests": [
        {
          "apiObservationId": "API_OBSERVATION_ID",
          "tagActions": [
          {
            "tag": "demo",
            "action": "REMOVE"
          },
          {
            "tag": "Needs Attentions",
            "action": "ADD"
          }]
        }
      ]
    }
    EOF

## Disable an observation job

This request disables an observation job without deleting it.
    
    
    curl https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_JOB_LOCATION/observationsJobs/OBSERVATION_JOB_NAME:disable \
    -X POST \
    -H 'Content-type: application/json' \
    -d @- <<'EOF'
    {
    }

## Delete an observation job

This request deletes an observation job.
    
    
    curl -X DELETE https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_JOB_LOCATION/observationJobs/OBSERVATION_JOB_NAME

## Delete an observation source

This request deletes an observation source.
    
    
    curl -X DELETE https://apim.googleapis.com/v1alpha/projects/PROJECT/locations/OBSERVATION_SOURCE_LOCATION/observationSources/OBSERVATION_SOURCE_NAME

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
