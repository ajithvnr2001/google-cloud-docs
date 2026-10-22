---
url: https://docs.cloud.google.com/artifact-analysis/docs/endpoints/
title: Configure data locality by using regional endpoints \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:38.843137+00:00
---

# Configure data locality by using regional endpoints  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Configure data locality by using regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Artifact Analysis global and regional service endpoints and how to use them.

A **service endpoint** is a base URL that specifies the network address of an API service. Artifact Analysis has both global and regional endpoints.

  * **Global endpoint** : By default, Artifact Analysis sends API requests to the global endpoint, `containeranalysis.googleapis.com`. Global endpoints don't guarantee that in-transit data remains in a particular location and can retrieve Artifact Analysis data from any supported region. Your data might be processed outside the region where it is stored.

  * **Regional endpoint** : A service endpoint that enforces regional restrictions, ensuring that data is stored, transmitted, and processed in a specified region. A regional endpoint only allows requests to proceed if the affected resource exists in the location specified by the endpoint. Regional endpoints use the following format:

`containeranalysis.region.rep.googleapis.com`.

Consider using regional endpoints in the following situations:

    * The application that needs to access your data is not geographically close to the region where your data is stored.

    * You are storing data in multiple locations and want to optimize latency, reliability, and availability.

    * You need to comply with data locality policies or regulations that require you to process your data in the same location where the data is stored.




Attestations and build provenance data are stored in the global endpoint. Vulnerability scan results and SBOM data are stored in regional and multi-regional endpoints.

## Locations that support regional endpoints

You can use regional endpoints for most regions that Artifact Analysis supports.

For multi-regions and some regions, Artifact Analysis only supports the global endpoint.

For a list of supported regions and the service endpoints that are supported for each region, see [Metadata storage locations](https://docs.cloud.google.com/artifact-analysis/docs/locations).

## Google Cloud CLI commands

When you use the gcloud CLI, there are two ways to send requests to the regional endpoint:

  * Use the `--location` flag.
  * Set the default regional endpoint that you want to use for Artifact Analysis commands.



### Use the `--location` flag

You can use the `--location` flag with one of the following commands to direct the request to the appropriate service endpoint:

  * [gcloud artifacts sbom export](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/export)
  * [gcloud artifacts sbom list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list)
  * [gcloud artifacts sbom load](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load)
  * [gcloud artifacts version describe](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/versions/describe)
  * [gcloud artifacts vulnerabilities list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/list)
  * [gcloud artifacts vulnerabilities load-vex](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex)



To successfully process the request with a regional endpoint, the specified location must meet the following requirements:

  * The location [supports a regional endpoint](https://docs.cloud.google.com/artifact-analysis/docs/locations).
  * The location matches the region where the artifact metadata is stored.



If you omit the `--location` flag or specify a location that does not support a regional endpoint, the command uses the global endpoint.

For example, the following command lists vulnerabilities for an image stored in `us-east1`:
    
    
    gcloud artifacts vulnerabilities list --location=us-east1 us-east1-docker.pkg.dev/my-project/my-repo/my-image@sha256:49765698074d6d7baa82f
    

### Set a default endpoint for commands

By default, the gcloud CLI commands use the global endpoint. You can set a default regional endpoint for Artifact Analysis commands so that you don't need to specify the location in individual commands.

Make sure you're using the gcloud CLI 402.0.0 or newer.

Before using any of the command data below, make the following replacements: 

  * LOCATION: the [region](https://docs.cloud.google.com/artifact-analysis/docs/locations) where your metadata is stored.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud config set api_endpoint_overrides/containeranalysis https://containeranalysis.LOCATION.rep.googleapis.com

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud config set api_endpoint_overrides/containeranalysis https://containeranalysis.LOCATION.rep.googleapis.com

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud config set api_endpoint_overrides/containeranalysis https://containeranalysis.LOCATION.rep.googleapis.com

## Use a regional endpoint for API methods

Specify the regional endpoint instead of the global endpoint. For example, the following example lists occurrences in the specified region.

Before using any of the request data, make the following replacements: 

  * LOCATION: the [region](https://docs.cloud.google.com/artifact-analysis/docs/locations) where your metadata is stored.
  * PROJECT_ID: the project ID of your Google Cloud project.



HTTP method and URL: 
    
    
    GET https://containeranalysis.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/occurrences

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://containeranalysis.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/occurrences"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://containeranalysis.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/occurrences" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    occurrences: [
      {
        name: "projects/my-project/locations/us-east1/occurrences/030b7805-eca4-4739-9a43-ec65ed98c61f"
        resource_uri: "https://us-east1-docker.pkg.dev/my-project/my-repo/my-image@sha256:b487c4da45ce363eef69d9c066fa26f6666e4f3c9c414d98d1e27bfcc949e544"
        note_name: "projects/goog-vulnz/locations/us-east1/notes/CVE-2018-1272"
        kind: VULNERABILITY
        ...
      }
    

Before the transition to regional metadata storage, occurrences and notes did not include a location name in their identifiers. As newer scans store metadata in regions, API requests using either global or regional endpoints return results that include location identifiers.

An occurrence identifier before the transition looked like this example:
    
    
    name: "projects/my-project/occurrences/030b7805-eca4-4739-9a43-ec65ed98c61f"
    

The same occurrence stored in `us-east1` looks like this:
    
    
    name: "projects/my-project/locations/us-east1/occurrences/030b7805-eca4-4739-9a43-ec65ed98c61f"
    

## Restrict global API endpoint usage

To help enforce the use of regional endpoints, use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

## What's next

  * View [metadata storage locations](https://docs.cloud.google.com/artifact-analysis/docs/locations) and supported service endpoints for each location.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
