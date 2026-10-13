---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ReservationDataOrBuilder
title: Interface ReservationDataOrBuilder (0.22.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:21.513785+00:00
---

# Interface ReservationDataOrBuilder (0.22.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ReservationDataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReservationDataOrBuilder (0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.18.0  0.17.0  0.16.0  0.14.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface ReservationDataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllocations(int index)
    
    
    public abstract Allocation getAllocations(int index)

Allocations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.Allocation allocations = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Allocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.Allocation)` |   
  
### getAllocationsCount()
    
    
    public abstract int getAllocationsCount()

Allocations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.Allocation allocations = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllocationsList()
    
    
    public abstract List<Allocation> getAllocationsList()

Allocations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.Allocation allocations = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Allocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.Allocation)>` |   
  
### getAllocationsOrBuilder(int index)
    
    
    public abstract AllocationOrBuilder getAllocationsOrBuilder(int index)

Allocations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.Allocation allocations = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.AllocationOrBuilder)` |   
  
### getAllocationsOrBuilderList()
    
    
    public abstract List<? extends AllocationOrBuilder> getAllocationsOrBuilderList()

Allocations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.Allocation allocations = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.capacityplanner.v1beta.AllocationOrBuilder>` |   
  
### getFutureReservations(int index)
    
    
    public abstract FutureReservation getFutureReservations(int index)

Future reservations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.FutureReservation future_reservations = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FutureReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.FutureReservation)` |   
  
### getFutureReservationsCount()
    
    
    public abstract int getFutureReservationsCount()

Future reservations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.FutureReservation future_reservations = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFutureReservationsList()
    
    
    public abstract List<FutureReservation> getFutureReservationsList()

Future reservations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.FutureReservation future_reservations = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FutureReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.FutureReservation)>` |   
  
### getFutureReservationsOrBuilder(int index)
    
    
    public abstract FutureReservationOrBuilder getFutureReservationsOrBuilder(int index)

Future reservations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.FutureReservation future_reservations = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FutureReservationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.FutureReservationOrBuilder)` |   
  
### getFutureReservationsOrBuilderList()
    
    
    public abstract List<? extends FutureReservationOrBuilder> getFutureReservationsOrBuilderList()

Future reservations filtered by the criteria.

`repeated .google.cloud.capacityplanner.v1beta.FutureReservation future_reservations = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.capacityplanner.v1beta.FutureReservationOrBuilder>` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/reservations/{reservation_id}` or `organizations/{organization_id}/locations/{location_id}/reservations/{reservation_id}` or `folders/{folder_id}/locations/{location_id}/reservations/{reservation_id}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/reservations/{reservation_id}` or `organizations/{organization_id}/locations/{location_id}/reservations/{reservation_id}` or `folders/{folder_id}/locations/{location_id}/reservations/{reservation_id}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getTimeSeries()
    
    
    public abstract TimeSeries getTimeSeries()

The collection of data points that represent the aggregated reserved value for reservations filtered by the criteria.

`.google.cloud.capacityplanner.v1beta.TimeSeries time_series = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.TimeSeries)` | The timeSeries.  
  
### getTimeSeriesOrBuilder()
    
    
    public abstract TimeSeriesOrBuilder getTimeSeriesOrBuilder()

The collection of data points that represent the aggregated reserved value for reservations filtered by the criteria.

`.google.cloud.capacityplanner.v1beta.TimeSeries time_series = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.TimeSeriesOrBuilder)` |   
  
### getUsedReservationValues()
    
    
    public abstract TimeSeries getUsedReservationValues()

The collection of data points that represent the aggregated used value for reservations filtered by the criteria.

`.google.cloud.capacityplanner.v1beta.TimeSeries used_reservation_values = 5;`

**Returns**  
---  
**Type** | **Description**  
`[TimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.TimeSeries)` | The usedReservationValues.  
  
### getUsedReservationValuesOrBuilder()
    
    
    public abstract TimeSeriesOrBuilder getUsedReservationValuesOrBuilder()

The collection of data points that represent the aggregated used value for reservations filtered by the criteria.

`.google.cloud.capacityplanner.v1beta.TimeSeries used_reservation_values = 5;`

**Returns**  
---  
**Type** | **Description**  
`[TimeSeriesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.TimeSeriesOrBuilder)` |   
  
### hasTimeSeries()
    
    
    public abstract boolean hasTimeSeries()

The collection of data points that represent the aggregated reserved value for reservations filtered by the criteria.

`.google.cloud.capacityplanner.v1beta.TimeSeries time_series = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeSeries field is set.  
  
### hasUsedReservationValues()
    
    
    public abstract boolean hasUsedReservationValues()

The collection of data points that represent the aggregated used value for reservations filtered by the criteria.

`.google.cloud.capacityplanner.v1beta.TimeSeries used_reservation_values = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the usedReservationValues field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
