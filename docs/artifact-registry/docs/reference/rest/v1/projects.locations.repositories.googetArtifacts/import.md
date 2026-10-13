---
url: https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.googetArtifacts/import/
title: Method: projects.locations.repositories.googetArtifacts.import \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:38.075247+00:00
---

# Method: projects.locations.repositories.googetArtifacts.import  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.googetArtifacts/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-registry/docs/apis)



Send feedback 

#  Method: projects.locations.repositories.googetArtifacts.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * ImportGoogetArtifactsGcsSource
    * JSON representation
  * Examples
  * Try it!



Imports GooGet artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 me-central2 us-east7 us eu

  
`POST https://artifactregistry.googleapis.com/v1/{parent=projects/*/locations/*/repositories/*}/googetArtifacts:import`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The name of the parent resource where the artifacts will be imported. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `artifactregistry.googetartifacts.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "gcsSource": {
        object ([ImportGoogetArtifactsGcsSource](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.googetArtifacts/import#ImportGoogetArtifactsGcsSource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. The source location of the package binaries. `source` can be only one of the following:  
`gcsSource` |  `object (`[ImportGoogetArtifactsGcsSource](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.googetArtifacts/import#ImportGoogetArtifactsGcsSource)`)` Google Cloud Storage location where input content is located.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ImportGoogetArtifactsGcsSource

Google Cloud Storage location where the artifacts currently reside.

JSON representation  
---  
      
    
    {
      "uris": [
        string
      ],
      "useWildcards": boolean
    }  
  
Fields  
---  
`uris[]` |  `string` Cloud Storage paths URI (e.g., `gs://my_bucket/my_object`).  
`useWildcards` |  `boolean` Supports URI wildcards for matching multiple objects from a single URI.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-14 UTC."],[],[]] 
