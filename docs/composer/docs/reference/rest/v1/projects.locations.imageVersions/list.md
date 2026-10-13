---
url: https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.imageVersions/list/
title: Method: projects.locations.imageVersions.list \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:30.830073+00:00
---

# Method: projects.locations.imageVersions.list  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.imageVersions/list/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Reference ](https://docs.cloud.google.com/composer/docs/apis)



Send feedback 

#  Method: projects.locations.imageVersions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * ImageVersion
    * JSON representation
  * Try it!



List ImageVersions for provided location.

### HTTP request

`GET https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/imageVersions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` List ImageVersions in the given project and location, in the form: "projects/{projectId}/locations/{locationId}" Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `composer.imageversions.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of imageVersions to return.  
`pageToken` |  `string` The nextPageToken value returned from a previous List request, if any.  
`includePastReleases` |  `boolean` Whether or not image versions from old releases should be included.  
  
### Request body

The request body must be empty.

### Response body

The ImageVersions in a project and location.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "imageVersions": [
        {
          object ([ImageVersion](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.imageVersions/list#ImageVersion))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`imageVersions[]` |  `object (`[ImageVersion](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.imageVersions/list#ImageVersion)`)` The list of supported ImageVersions in a location.  
`nextPageToken` |  `string` The page token used to query for the next page if one exists.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudcomposer.readonly`
  * ` https://www.googleapis.com/auth/cloudcomposer`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ImageVersion

ImageVersion information

JSON representation  
---  
      
    
    {
      "imageVersionId": string,
      "isDefault": boolean,
      "supportedPythonVersions": [
        string
      ],
      "releaseDate": {
        object ([Date](https://docs.cloud.google.com/composer/docs/reference/rest/Shared.Types/Date))
      },
      "creationDisabled": boolean,
      "upgradeDisabled": boolean
    }  
  
Fields  
---  
`imageVersionId` |  `string` The string identifier of the ImageVersion, in the form: "composer-x.y.z-airflow-a.b.c"  
`isDefault` |  `boolean` Whether this is the default ImageVersion used by Composer during environment creation if no input ImageVersion is specified.  
`supportedPythonVersions[]` |  `string` supported python versions  
`releaseDate` |  `object (`[Date](https://docs.cloud.google.com/composer/docs/reference/rest/Shared.Types/Date)`)` The date of the version release.  
`creationDisabled` |  `boolean` Whether it is impossible to create an environment with the image version.  
`upgradeDisabled` |  `boolean` Whether it is impossible to upgrade an environment running with the image version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-29 UTC."],[],[]] 
