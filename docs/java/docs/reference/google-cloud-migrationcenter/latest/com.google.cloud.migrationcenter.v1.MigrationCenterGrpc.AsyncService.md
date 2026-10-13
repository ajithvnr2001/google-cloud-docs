---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterGrpc.AsyncService
title: Interface MigrationCenterGrpc.AsyncService (0.81.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:50.047663+00:00
---

# Interface MigrationCenterGrpc.AsyncService (0.81.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MigrationCenterGrpc.AsyncService (0.81.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.81.0 (latest)  0.77.0  0.76.0  0.75.0  0.73.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.62.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.46.0  0.45.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface MigrationCenterGrpc.AsyncService

Service describing handlers for resources.

## Methods 

### addAssetsToGroup(AddAssetsToGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void addAssetsToGroup(AddAssetsToGroupRequest request, StreamObserver<Operation> responseObserver)

Adds assets to a group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAssetsToGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.AddAssetsToGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### aggregateAssetsValues(AggregateAssetsValuesRequest request, StreamObserver<AggregateAssetsValuesResponse> responseObserver)
    
    
    public default void aggregateAssetsValues(AggregateAssetsValuesRequest request, StreamObserver<AggregateAssetsValuesResponse> responseObserver)

Aggregates the requested fields based on provided function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateAssetsValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.AggregateAssetsValuesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AggregateAssetsValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.AggregateAssetsValuesResponse)>`  
  
  
### batchDeleteAssets(BatchDeleteAssetsRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void batchDeleteAssets(BatchDeleteAssetsRequest request, StreamObserver<Empty> responseObserver)

Deletes list of Assets.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.BatchDeleteAssetsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### batchUpdateAssets(BatchUpdateAssetsRequest request, StreamObserver<BatchUpdateAssetsResponse> responseObserver)
    
    
    public default void batchUpdateAssets(BatchUpdateAssetsRequest request, StreamObserver<BatchUpdateAssetsResponse> responseObserver)

Updates the parameters of a list of assets.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.BatchUpdateAssetsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchUpdateAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.BatchUpdateAssetsResponse)>`  
  
  
### createGroup(CreateGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createGroup(CreateGroupRequest request, StreamObserver<Operation> responseObserver)

Creates a new group in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createImportDataFile(CreateImportDataFileRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createImportDataFile(CreateImportDataFileRequest request, StreamObserver<Operation> responseObserver)

Creates an import data file.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateImportDataFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateImportDataFileRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createImportJob(CreateImportJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createImportJob(CreateImportJobRequest request, StreamObserver<Operation> responseObserver)

Creates an import job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateImportJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createPreferenceSet(CreatePreferenceSetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createPreferenceSet(CreatePreferenceSetRequest request, StreamObserver<Operation> responseObserver)

Creates a new preference set in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreatePreferenceSetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createReport(CreateReportRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createReport(CreateReportRequest request, StreamObserver<Operation> responseObserver)

Creates a report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createReportConfig(CreateReportConfigRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createReportConfig(CreateReportConfigRequest request, StreamObserver<Operation> responseObserver)

Creates a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateReportConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createSource(CreateSourceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createSource(CreateSourceRequest request, StreamObserver<Operation> responseObserver)

Creates a new source in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteAsset(DeleteAssetRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteAsset(DeleteAssetRequest request, StreamObserver<Empty> responseObserver)

Deletes an asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteAssetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteGroup(DeleteGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteGroup(DeleteGroupRequest request, StreamObserver<Operation> responseObserver)

Deletes a group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteImportDataFile(DeleteImportDataFileRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteImportDataFile(DeleteImportDataFileRequest request, StreamObserver<Operation> responseObserver)

Delete an import data file.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteImportDataFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteImportDataFileRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteImportJob(DeleteImportJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteImportJob(DeleteImportJobRequest request, StreamObserver<Operation> responseObserver)

Deletes an import job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteImportJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deletePreferenceSet(DeletePreferenceSetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deletePreferenceSet(DeletePreferenceSetRequest request, StreamObserver<Operation> responseObserver)

Deletes a preference set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeletePreferenceSetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteReport(DeleteReportRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteReport(DeleteReportRequest request, StreamObserver<Operation> responseObserver)

Deletes a Report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteReportConfig(DeleteReportConfigRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteReportConfig(DeleteReportConfigRequest request, StreamObserver<Operation> responseObserver)

Deletes a ReportConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteReportConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSource(DeleteSourceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteSource(DeleteSourceRequest request, StreamObserver<Operation> responseObserver)

Deletes a source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getAsset(GetAssetRequest request, StreamObserver<Asset> responseObserver)
    
    
    public default void getAsset(GetAssetRequest request, StreamObserver<Asset> responseObserver)

Gets the details of an asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetAssetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Asset)>`  
  
  
### getErrorFrame(GetErrorFrameRequest request, StreamObserver<ErrorFrame> responseObserver)
    
    
    public default void getErrorFrame(GetErrorFrameRequest request, StreamObserver<ErrorFrame> responseObserver)

Gets the details of an error frame.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetErrorFrameRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetErrorFrameRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ErrorFrame](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ErrorFrame)>`  
  
  
### getGroup(GetGroupRequest request, StreamObserver<Group> responseObserver)
    
    
    public default void getGroup(GetGroupRequest request, StreamObserver<Group> responseObserver)

Gets the details of a group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Group)>`  
  
  
### getImportDataFile(GetImportDataFileRequest request, StreamObserver<ImportDataFile> responseObserver)
    
    
    public default void getImportDataFile(GetImportDataFileRequest request, StreamObserver<ImportDataFile> responseObserver)

Gets an import data file.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetImportDataFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetImportDataFileRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ImportDataFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ImportDataFile)>`  
  
  
### getImportJob(GetImportJobRequest request, StreamObserver<ImportJob> responseObserver)
    
    
    public default void getImportJob(GetImportJobRequest request, StreamObserver<ImportJob> responseObserver)

Gets the details of an import job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetImportJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ImportJob)>`  
  
  
### getPreferenceSet(GetPreferenceSetRequest request, StreamObserver<PreferenceSet> responseObserver)
    
    
    public default void getPreferenceSet(GetPreferenceSetRequest request, StreamObserver<PreferenceSet> responseObserver)

Gets the details of a preference set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetPreferenceSetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PreferenceSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.PreferenceSet)>`  
  
  
### getReport(GetReportRequest request, StreamObserver<Report> responseObserver)
    
    
    public default void getReport(GetReportRequest request, StreamObserver<Report> responseObserver)

Gets details of a single Report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Report](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Report)>`  
  
  
### getReportConfig(GetReportConfigRequest request, StreamObserver<ReportConfig> responseObserver)
    
    
    public default void getReportConfig(GetReportConfigRequest request, StreamObserver<ReportConfig> responseObserver)

Gets details of a single ReportConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetReportConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportConfig)>`  
  
  
### getSettings(GetSettingsRequest request, StreamObserver<Settings> responseObserver)
    
    
    public default void getSettings(GetSettingsRequest request, StreamObserver<Settings> responseObserver)

Gets the details of regional settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Settings)>`  
  
  
### getSource(GetSourceRequest request, StreamObserver<Source> responseObserver)
    
    
    public default void getSource(GetSourceRequest request, StreamObserver<Source> responseObserver)

Gets the details of a source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Source)>`  
  
  
### listAssets(ListAssetsRequest request, StreamObserver<ListAssetsResponse> responseObserver)
    
    
    public default void listAssets(ListAssetsRequest request, StreamObserver<ListAssetsResponse> responseObserver)

Lists all the assets in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListAssetsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListAssetsResponse)>`  
  
  
### listErrorFrames(ListErrorFramesRequest request, StreamObserver<ListErrorFramesResponse> responseObserver)
    
    
    public default void listErrorFrames(ListErrorFramesRequest request, StreamObserver<ListErrorFramesResponse> responseObserver)

Lists all error frames in a given source and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListErrorFramesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListErrorFramesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListErrorFramesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListErrorFramesResponse)>`  
  
  
### listGroups(ListGroupsRequest request, StreamObserver<ListGroupsResponse> responseObserver)
    
    
    public default void listGroups(ListGroupsRequest request, StreamObserver<ListGroupsResponse> responseObserver)

Lists all groups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListGroupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListGroupsResponse)>`  
  
  
### listImportDataFiles(ListImportDataFilesRequest request, StreamObserver<ListImportDataFilesResponse> responseObserver)
    
    
    public default void listImportDataFiles(ListImportDataFilesRequest request, StreamObserver<ListImportDataFilesResponse> responseObserver)

List import data files.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListImportDataFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportDataFilesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListImportDataFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportDataFilesResponse)>`  
  
  
### listImportJobs(ListImportJobsRequest request, StreamObserver<ListImportJobsResponse> responseObserver)
    
    
    public default void listImportJobs(ListImportJobsRequest request, StreamObserver<ListImportJobsResponse> responseObserver)

Lists all import jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListImportJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListImportJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportJobsResponse)>`  
  
  
### listPreferenceSets(ListPreferenceSetsRequest request, StreamObserver<ListPreferenceSetsResponse> responseObserver)
    
    
    public default void listPreferenceSets(ListPreferenceSetsRequest request, StreamObserver<ListPreferenceSetsResponse> responseObserver)

Lists all the preference sets in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPreferenceSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListPreferenceSetsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListPreferenceSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListPreferenceSetsResponse)>`  
  
  
### listReportConfigs(ListReportConfigsRequest request, StreamObserver<ListReportConfigsResponse> responseObserver)
    
    
    public default void listReportConfigs(ListReportConfigsRequest request, StreamObserver<ListReportConfigsResponse> responseObserver)

Lists ReportConfigs in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReportConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportConfigsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListReportConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportConfigsResponse)>`  
  
  
### listReports(ListReportsRequest request, StreamObserver<ListReportsResponse> responseObserver)
    
    
    public default void listReports(ListReportsRequest request, StreamObserver<ListReportsResponse> responseObserver)

Lists Reports in a given ReportConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportsResponse)>`  
  
  
### listSources(ListSourcesRequest request, StreamObserver<ListSourcesResponse> responseObserver)
    
    
    public default void listSources(ListSourcesRequest request, StreamObserver<ListSourcesResponse> responseObserver)

Lists all the sources in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListSourcesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListSourcesResponse)>`  
  
  
### removeAssetsFromGroup(RemoveAssetsFromGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void removeAssetsFromGroup(RemoveAssetsFromGroupRequest request, StreamObserver<Operation> responseObserver)

Removes assets from a group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveAssetsFromGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.RemoveAssetsFromGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### reportAssetFrames(ReportAssetFramesRequest request, StreamObserver<ReportAssetFramesResponse> responseObserver)
    
    
    public default void reportAssetFrames(ReportAssetFramesRequest request, StreamObserver<ReportAssetFramesResponse> responseObserver)

Reports a set of frames.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReportAssetFramesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportAssetFramesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReportAssetFramesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportAssetFramesResponse)>`  
  
  
### runImportJob(RunImportJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void runImportJob(RunImportJobRequest request, StreamObserver<Operation> responseObserver)

Runs an import job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.RunImportJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateAsset(UpdateAssetRequest request, StreamObserver<Asset> responseObserver)
    
    
    public default void updateAsset(UpdateAssetRequest request, StreamObserver<Asset> responseObserver)

Updates the parameters of an asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateAssetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Asset)>`  
  
  
### updateGroup(UpdateGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateGroup(UpdateGroupRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateImportJob(UpdateImportJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateImportJob(UpdateImportJobRequest request, StreamObserver<Operation> responseObserver)

Updates an import job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateImportJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updatePreferenceSet(UpdatePreferenceSetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updatePreferenceSet(UpdatePreferenceSetRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a preference set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdatePreferenceSetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateSettings(UpdateSettingsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateSettings(UpdateSettingsRequest request, StreamObserver<Operation> responseObserver)

Updates the regional-level project settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateSource(UpdateSourceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateSource(UpdateSourceRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### validateImportJob(ValidateImportJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void validateImportJob(ValidateImportJobRequest request, StreamObserver<Operation> responseObserver)

Validates an import job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ValidateImportJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
