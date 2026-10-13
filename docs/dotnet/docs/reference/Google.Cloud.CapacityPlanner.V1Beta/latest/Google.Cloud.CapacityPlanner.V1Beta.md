---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta
title: Capacity Planner v1beta API - Namespace Google.Cloud.CapacityPlanner.V1Beta (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:47.945271+00:00
---

# Capacity Planner v1beta API - Namespace Google.Cloud.CapacityPlanner.V1Beta (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Capacity Planner v1beta API - Namespace Google.Cloud.CapacityPlanner.V1Beta (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta02 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/1.0.0-beta01/Google.Cloud.CapacityPlanner.V1Beta)



## Classes 

### [Allocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation)

Repesents Allocation which is part of aggregated reservations data response of "QueryReservations".

### [Allocation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types)

Container for nested types declared in the Allocation message type.

### [Allocation.Types.ShareSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.ShareSettings)

The share setting for reservation.

### [Allocation.Types.ShareSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.ShareSettings.Types)

Container for nested types declared in the ShareSettings message type.

### [Allocation.Types.SpecificSKUAllocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.SpecificSKUAllocation)

This reservation type allows to pre allocate specific instance configuration.

### [Allocation.Types.SpecificSKUAllocation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.SpecificSKUAllocation.Types)

Container for nested types declared in the SpecificSKUAllocation message type.

### [Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties)

Properties of the SKU instances being reserved.

### [Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types)

Container for nested types declared in the AllocatedInstanceProperties message type.

### [Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types.AcceleratorConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types.AcceleratorConfig)

A specification of the type and number of accelerator cards attached to the instance.

### [Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types.AllocatedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types.AllocatedDisk)

A specification of the interface and size of disk attached to the instance.

### [Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types.AllocatedDisk.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types.AllocatedDisk.Types)

Container for nested types declared in the AllocatedDisk message type.

### [BigQueryDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.BigQueryDestination)

A BigQuery destination for exporting assets to.

### [BigQueryDestination.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.BigQueryDestination.Types)

Container for nested types declared in the BigQueryDestination message type.

### [ExportForecastsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportForecastsRequest)

The `ExportForecasts` request Next : 13

### [ExportForecastsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportForecastsResponse)

A response message for [UsageService.ExportForecasts].

### [ExportReservationsUsageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportReservationsUsageRequest)

The `ExportReservationsUsage` request

### [ExportReservationsUsageRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportReservationsUsageRequest.Types)

Container for nested types declared in the ExportReservationsUsageRequest message type.

### [ExportReservationsUsageResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportReservationsUsageResponse)

A response message for [UsageService.ExportReservationsUsage].

### [ExportUsageHistoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportUsageHistoriesRequest)

The `ExportUsageHistories` request Next : 12

### [ExportUsageHistoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportUsageHistoriesResponse)

A response message for [UsageService.ExportUsageHistories].

### [Forecast](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Forecast)

A collection of data points that describes the predicted time-varying values of a resource.

### [Forecast.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Forecast.Types)

Container for nested types declared in the Forecast message type.

### [ForecastName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ForecastName)

Resource name for the `Forecast` resource.

### [FutureReservation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.FutureReservation)

Repesents Future Reservation request which is part of aggregated reservations data response of "QueryReservations".

### [FutureReservation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.FutureReservation.Types)

Container for nested types declared in the FutureReservation message type.

### [FutureReservation.Types.SpecificSKUProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.FutureReservation.Types.SpecificSKUProperties)

Represents specific SKU properties for the Future Reservation.

### [FutureReservation.Types.Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.FutureReservation.Types.Status)

Represents status related to the future reservation.

### [FutureReservation.Types.Status.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.FutureReservation.Types.Status.Types)

Container for nested types declared in the Status message type.

### [FutureReservation.Types.TimeWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.FutureReservation.Types.TimeWindow)

Represents time window for the Future Reservation.

### [GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.GcsDestination)

A Cloud Storage location.

### [LocationIdentifier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.LocationIdentifier)

Identifier for a Google Cloud Platform location.

### [LocationIdentifier.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.LocationIdentifier.Types)

Container for nested types declared in the LocationIdentifier message type.

### [LocationIdentifier.Types.LinkedLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.LocationIdentifier.Types.LinkedLocation)

### [MachineShape](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.MachineShape)

Machine shape details Next : 13

### [OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.OperationMetadata)

Represents the metadata of a long-running operation.

### [OutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.OutputConfig)

Output configuration for export destination.

### [Point](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Point)

A single data point in a time series.

### [QueryForecastsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryForecastsRequest)

The `QueryForecasts` request. Next : 14

### [QueryForecastsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryForecastsResponse)

The `QueryForecasts` response.

### [QueryReservationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryReservationsRequest)

The `QueryReservations` request.

### [QueryReservationsRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryReservationsRequest.Types)

Container for nested types declared in the QueryReservationsRequest message type.

### [QueryReservationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryReservationsResponse)

The `QueryReservations` response.

### [QueryUsageHistoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryUsageHistoriesRequest)

The `QueryUsageHistories` request. Next : 16

### [QueryUsageHistoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryUsageHistoriesResponse)

The `QueryUsageHistories` response.

### [ReservationData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ReservationData)

Response entity for reservations data.

### [ReservationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ReservationName)

Resource name for the `Reservation` resource.

### [ResourceAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceAttribute)

An attribute of a Google Cloud Platform resource.

### [ResourceContainer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceContainer)

The resource container of Google Cloud Platform hierarchy such as a project.

### [ResourceContainer.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceContainer.Types)

Container for nested types declared in the ResourceContainer message type.

### [ResourceIdKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceIdKey)

The id for a Google Cloud Platform resource key.

### [ResourceIdentifier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceIdentifier)

The identifier for a Google Cloud Platform resource.

### [ResourceValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceValue)

### [TimeSeries](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.TimeSeries)

A collection of data points that describes the time-varying values of a resource. A time series is identified by its ID. Next : 13

### [TimeSeries.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.TimeSeries.Types)

Container for nested types declared in the TimeSeries message type.

### [UsageHistory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageHistory)

A collection of data points that describes the historical time-varying values of a resource.

### [UsageHistory.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageHistory.Types)

Container for nested types declared in the UsageHistory message type.

### [UsageService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageService)

Provides access to historical and forecasted usage data.

### [UsageService.UsageServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageService.UsageServiceBase)

Base class for server-side implementations of UsageService

### [UsageService.UsageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageService.UsageServiceClient)

Client for UsageService

### [UsageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageServiceClient)

UsageService client wrapper, for convenient use.

### [UsageServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageServiceClientBuilder)

Builder class for [UsageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageServiceClient) to provide simple configuration of credentials, endpoint etc.

### [UsageServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageServiceClientImpl)

UsageService client wrapper implementation, for convenient use.

### [UsageServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageServiceSettings)

Settings for [UsageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageServiceClient) instances.

### [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Value)

## Enums 

### [Allocation.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [Allocation.Types.ShareSettings.Types.ShareType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.ShareSettings.Types.ShareType)

Possible scope in which the reservation can be shared. More granularity can be added in future.

### [Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types.AllocatedDisk.Types.DiskInterface](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.SpecificSKUAllocation.Types.AllocatedInstanceProperties.Types.AllocatedDisk.Types.DiskInterface)

guest device interface options to use for the disk.

### [Allocation.Types.Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Allocation.Types.Status)

The status of the reservation.

### [BigQueryDestination.Types.CreateDisposition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.BigQueryDestination.Types.CreateDisposition)

Specifies the action that occurs if the destination table does not exist. By default, a new table will be created.

### [BigQueryDestination.Types.PartitionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.BigQueryDestination.Types.PartitionKey)

This enum determines the partition key column for the BigQuery tables. Partitioning can improve query performance and reduce query cost by filtering partitions. Refer to <https://cloud.google.com/bigquery/docs/partitioned-tables> for details.

### [BigQueryDestination.Types.WriteDisposition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.BigQueryDestination.Types.WriteDisposition)

Specifies the action that occurs if the destination table or partition already exists. By default, the data will be appended to the existing table.

### [ExportReservationsUsageRequest.ResourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportReservationsUsageRequest.ResourceOneofCase)

Enum of possible cases for the "resource" oneof.

### [ExportReservationsUsageRequest.Types.ShareType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ExportReservationsUsageRequest.Types.ShareType)

Possible scope in which the reservation can be shared.

### [Forecast.Types.Bounds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Forecast.Types.Bounds)

The bounds of the forecast time series.

### [Forecast.Types.ForecastType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Forecast.Types.ForecastType)

The type of the forecast. This describes the method that was used to produce future time series values from historical time series values.

### [Forecast.Types.PredictionInterval](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Forecast.Types.PredictionInterval)

The prediction interval represented by a forecast.

### [ForecastName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ForecastName.ResourceNameType)

The possible contents of [ForecastName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ForecastName).

### [FutureReservation.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.FutureReservation.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [FutureReservation.Types.Status.Types.ProcurementStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.FutureReservation.Types.Status.Types.ProcurementStatus)

Represents procurement status of the Future Reservation.

### [LocationLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.LocationLevel)

The level of the Google Cloud Platform location.

### [OutputConfig.DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.OutputConfig.DestinationOneofCase)

Enum of possible cases for the "destination" oneof.

### [QueryReservationsRequest.Types.OwnershipType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryReservationsRequest.Types.OwnershipType)

Reservation ownership status to provide distinction for Capacity Planning.

### [QueryReservationsRequest.Types.ReservationDataLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryReservationsRequest.Types.ReservationDataLevel)

The form in which data of reservations should be returned. In case of AGGREGATED, timeseries for selected reservations is returned. If unspecified, all levels are included.

### [QueryReservationsRequest.Types.ReservationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryReservationsRequest.Types.ReservationType)

Type of the reservation

### [QueryReservationsRequest.Types.ShareType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.QueryReservationsRequest.Types.ShareType)

Possible scope in which the reservation can be shared.

### [ReservationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ReservationName.ResourceNameType)

The possible contents of [ReservationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ReservationName).

### [ResourceContainer.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceContainer.Types.Type)

### [ResourceIdKey.DemandFieldsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.ResourceIdKey.DemandFieldsOneofCase)

Enum of possible cases for the "demand_fields" oneof.

### [TimeSeries.Types.LocationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.TimeSeries.Types.LocationType)

The type of location that the time series is summarizing.

### [Unit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Unit)

### [UsageHistory.Types.AggregationMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.UsageHistory.Types.AggregationMethod)

Methods for converting sampled data to time series values.

### [Value.ValueOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.Value.ValueOneofCase)

Enum of possible cases for the "value" oneof.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
