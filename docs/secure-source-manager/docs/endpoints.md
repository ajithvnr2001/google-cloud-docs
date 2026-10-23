---
url: https://docs.cloud.google.com/secure-source-manager/docs/endpoints/
title: Configure data locality by using regional endpoints \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:10.017536+00:00
---

# Configure data locality by using regional endpoints  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Configure data locality by using regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the global and regional service endpoints for the Secure Source Manager control plane.

A **service endpoint** is a base URL that specifies the network address of an API service. The Secure Source Manager control plane has both global and regional endpoints.

  * **Global endpoint** : By default, Secure Source Manager sends API requests to the global endpoint, `securesourcemanager.googleapis.com`. Global endpoints don't guarantee that in-transit data remains in a particular location and can retrieve Secure Source Manager data from any supported region. Your data might be processed outside the region where it is stored.

  * **Regional endpoint** : A service endpoint that enforces regional restrictions, ensuring that in-transit data remains in a particular location. A regional endpoint only allows requests to proceed if the affected resource exists in the location specified by the endpoint. Regional endpoints use the following format:

`securesourcemanager.LOCATION.rep.googleapis.com`.

For a list of supported regions, see [Locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).




Consider using regional endpoints in the following situations:

  * You are storing data in multiple locations and want to optimize latency, reliability, and availability.

  * You need to comply with data locality policies or regulations that require you to process your data in the same location where the data is stored.




## Supported commands

You can use regional endpoints to run commands for instances, locations, and operations.

## Specify a regional endpoint

### gcloud

You can override the global endpoint with a regional endpoint for Secure Source Manager commands. 

Make sure you're using the Google Cloud CLI 402.0.0 or newer.

Before using any of the command data below, make the following replacements: 

  * LOCATION: the [region](https://docs.cloud.google.com/secure-source-manager/docs/locations) where the instance is located.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud config set api_endpoint_overrides/securesourcemanager https://securesourcemanager.LOCATION.rep.googleapis.com

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud config set api_endpoint_overrides/securesourcemanager https://securesourcemanager.LOCATION.rep.googleapis.com

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud config set api_endpoint_overrides/securesourcemanager https://securesourcemanager.LOCATION.rep.googleapis.com

### REST

Use the regional endpoint in your commands instead of the global endpoint. For example, the following command list details for all repositories in a specified region for a specified instance. 

Before using any of the request data, make the following replacements: 

  * LOCATION: the [region](https://docs.cloud.google.com/secure-source-manager/docs/locations) where the instance is located.
  * INSTANCE_ID: the name of the instance.
  * PROJECT_ID: the project ID of the project where the instance is located.



HTTP method and URL: 
    
    
    GET https://securesourcemanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instance_id=INSTANCE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securesourcemanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instance_id=INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securesourcemanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instance_id=INSTANCE_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

Use the API override to set the regional endpoint. 

Before using any of the command data below, make the following replacements:

  * LOCATION: the [region](https://docs.cloud.google.com/secure-source-manager/docs/locations) where the instance is located.


    
    
    provider "google" {
      secure_source_manager_custom_endpoint = "https://securesourcemanager.LOCATION.rep.googleapis.com/v1/"
    }
    

### Client Libraries

See [Secure Source Manager client libraries](https://docs.cloud.google.com/secure-source-manager/docs/reference/libraries) for instructions to install client libraries and set up authetication.

Each client library provides a way to override the default endpoint with a regional endpoint.

  * **C++** : Use the struct `EndpointOption`. The Secure Source Manager [client library documentation](https://docs.cloud.google.com/cpp/docs/reference/securesourcemanager/latest/securesourcemanager-override-endpoint) includes an example that overrides the default endpoint with the Private Google Access endpoint, but you can use the same approach to set a regional endpoint as the default.

  * **Go** : Use the `endpoint` client option. See the [Endpoint Override](https://pkg.go.dev/cloud.google.com/go#hdr-Endpoint_Override) section of the Go client library documentation for more information and an example.

  * **Python** : Use the `api_endpoint` parameter of the `ClientOptions` class to override the default endpoint with a regional endpoint. See the [ClientOptions](https://googleapis.dev/python/google-api-core/latest/client_options.html#google.api_core.client_options.ClientOptions) documentation for more information and examples. 




## What's next

  * View [supported locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
