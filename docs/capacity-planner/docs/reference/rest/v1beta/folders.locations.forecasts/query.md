---
url: https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/folders.locations.forecasts/query/
title: Method: folders.locations.forecasts.query \u00a0|\u00a0 Capacity Planner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:58.384219+00:00
---

# Method: folders.locations.forecasts.query  |  Capacity Planner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/folders.locations.forecasts/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Capacity Planner ](https://docs.cloud.google.com/capacity-planner/docs)



Send feedback 

#  Method: folders.locations.forecasts.query Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Returns a list of the forecasts that are in the parent parameter and match your specified filters.

### HTTP request

`POST https://capacityplanner.googleapis.com/v1beta/{parent=folders/*/locations/*}/forecasts:query`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The compute engine resource and location for the time series values to return. The format is:projects/{project}/locations/{location} or organizations/{organization}/locations/{location} or folders/{folder}/locations/{location}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "machineFamily": string,
      "machineShape": {
        object ([MachineShape](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/MachineShape))
      },
      "diskType": string,
      "confidentialMode": boolean,
      "gpuType": string,
      "tpuType": string,
      "cloudResourceType": string,
      "forecastType": enum ([ForecastType](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/ForecastType)),
      "predictionInterval": enum ([PredictionInterval](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/PredictionInterval)),
      "aggregationMethod": enum ([AggregationMethod](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/AggregationMethod)),
      "startDate": {
        object ([Date](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/Date))
      },
      "endDate": {
        object ([Date](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/Date))
      },
      "generationDate": {
        object ([Date](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/Date))
      }
    }  
  
Fields  
---  
`machineFamily` |  `string` The machine family to use to select the `Forecast` values to return. Possible values include "n1", and "n2d". Empty machineFamily will return results matching all machine families.  
`machineShape` |  `object (`[MachineShape](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/MachineShape)`)` Optional. The machine shape for the time series values to return.  
`diskType` |  `string` Optional. The diskType for the `Forecast` values to return with request persistent-disk cloudResourceType. Empty diskType will return results matching all disk types.  
`confidentialMode` |  `boolean` Optional. Whether the persistent disk is in confidential mode.  
`gpuType` |  `string` Optional. The GPU type for the `Forecast` values to return. Sample values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See <https://cloud.google.com/compute/docs/gpus> for a list. Empty gpuType will return results matching all GPUs.  
`tpuType` |  `string` Optional. The TPU type for the `Forecast` values to return. Empty tpuType will return results matching all TPUs.  
`cloudResourceType` |  `string` Required. The resource for the `Forecast` values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-persistent-disk", "gce-gpu" and "gce-tpu".  
`forecastType` |  `enum (`[ForecastType](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/ForecastType)`)` The type of forecast to use to select the `Forecast` values to return. FORECAST_TYPE_UNSPECIFIED will return results matching all the forecast types.  
`predictionInterval` |  `enum (`[PredictionInterval](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/PredictionInterval)`)` The prediction interval to use to select the `Forecast` values to return. PREDICTION_INTERVAL_UNSPECIFIED will return results matching all prediction intervals.  
`aggregationMethod` |  `enum (`[AggregationMethod](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/AggregationMethod)`)` Aggregation Method of the historical usage for which the forecast is generated  
`startDate` |  `object (`[Date](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/Date)`)` Optional. The start date (inclusive) from which you want the `Forecast` records to be returned.  
`endDate` |  `object (`[Date](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/Date)`)` Optional. The last date (inclusive) until which you want the `Forecast` records to be returned.  
`generationDate` |  `object (`[Date](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/Date)`)` Optional. If you specify a date for this field, then the API returns the `Forecast` snapshot data that was calculated on the provided `generationDate`. If you don't specify a date for this field, then the API returns the most recently generated forecast.  
  
### Response body

If successful, the response body contains an instance of `[QueryForecastsResponse](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/QueryForecastsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/devstorage.full_control`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `capacityplanner.forecasts.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-07 UTC."],[],[]] 
