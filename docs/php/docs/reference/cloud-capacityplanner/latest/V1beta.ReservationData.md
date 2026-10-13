---
url: https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.ReservationData
title: Google Cloud Capacity Planner V1beta Client - Class ReservationData (0.2.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:06.946026+00:00
---

# Google Cloud Capacity Planner V1beta Client - Class ReservationData (0.2.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.ReservationData

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Capacity Planner V1beta Client - Class ReservationData (0.2.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.4 (latest)  0.1.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Capacity Planner V1beta Client class ReservationData.

Response entity for reservations data.

Generated from protobuf message `google.cloud.capacityplanner.v1beta.ReservationData`

## Namespace

Google \ Cloud \ CapacityPlanner \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/reservations/{reservation_id}` or `organizations/{organization_id}/locations/{location_id}/reservations/{reservation_id}` or `folders/{folder_id}/locations/{location_id}/reservations/{reservation_id}`  
`↳ time_series` |  `[TimeSeries](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.TimeSeries)`   
The collection of data points that represent the aggregated reserved value for reservations filtered by the criteria.  
`↳ used_reservation_values` |  `[TimeSeries](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.TimeSeries)`   
The collection of data points that represent the aggregated used value for reservations filtered by the criteria.  
`↳ future_reservations` |  `array<[FutureReservation](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.FutureReservation)>`   
Future reservations filtered by the criteria.  
`↳ allocations` |  `array<[Allocation](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.Allocation)>`   
Allocations filtered by the criteria.  
  
### getName

Identifier. The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/reservations/{reservation_id}` or `organizations/{organization_id}/locations/{location_id}/reservations/{reservation_id}` or `folders/{folder_id}/locations/{location_id}/reservations/{reservation_id}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/reservations/{reservation_id}` or `organizations/{organization_id}/locations/{location_id}/reservations/{reservation_id}` or `folders/{folder_id}/locations/{location_id}/reservations/{reservation_id}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTimeSeries

The collection of data points that represent the aggregated reserved value for reservations filtered by the criteria.

**Returns**  
---  
**Type** | **Description**  
`[TimeSeries](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.TimeSeries)|null` |   
  
### hasTimeSeries

### clearTimeSeries

### setTimeSeries

The collection of data points that represent the aggregated reserved value for reservations filtered by the criteria.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[TimeSeries](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.TimeSeries)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUsedReservationValues

The collection of data points that represent the aggregated used value for reservations filtered by the criteria.

**Returns**  
---  
**Type** | **Description**  
`[TimeSeries](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.TimeSeries)|null` |   
  
### hasUsedReservationValues

### clearUsedReservationValues

### setUsedReservationValues

The collection of data points that represent the aggregated used value for reservations filtered by the criteria.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[TimeSeries](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.TimeSeries)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFutureReservations

Future reservations filtered by the criteria.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[FutureReservation](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.FutureReservation)>` |   
  
### setFutureReservations

Future reservations filtered by the criteria.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[FutureReservation](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.FutureReservation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAllocations

Allocations filtered by the criteria.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[Allocation](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.Allocation)>` |   
  
### setAllocations

Allocations filtered by the criteria.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Allocation](https://docs.cloud.google.com/php/docs/reference/cloud-capacityplanner/latest/V1beta.Allocation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
