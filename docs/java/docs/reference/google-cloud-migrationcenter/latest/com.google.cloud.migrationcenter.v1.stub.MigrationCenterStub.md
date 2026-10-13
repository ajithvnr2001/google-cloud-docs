---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.stub.MigrationCenterStub
title: Class MigrationCenterStub (0.81.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:05.128253+00:00
---

# Class MigrationCenterStub (0.81.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.stub.MigrationCenterStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MigrationCenterStub (0.81.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.81.0 (latest)  0.77.0  0.76.0  0.75.0  0.73.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.62.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.46.0  0.45.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public abstract class MigrationCenterStub implements BackgroundResource

Base stub class for the MigrationCenter service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MigrationCenterStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### MigrationCenterStub()
    
    
    public MigrationCenterStub()

## Methods 

### addAssetsToGroupCallable()
    
    
    public UnaryCallable<AddAssetsToGroupRequest,Operation> addAssetsToGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddAssetsToGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.AddAssetsToGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### addAssetsToGroupOperationCallable()
    
    
    public OperationCallable<AddAssetsToGroupRequest,Group,OperationMetadata> addAssetsToGroupOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddAssetsToGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.AddAssetsToGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Group),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### aggregateAssetsValuesCallable()
    
    
    public UnaryCallable<AggregateAssetsValuesRequest,AggregateAssetsValuesResponse> aggregateAssetsValuesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregateAssetsValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.AggregateAssetsValuesRequest),[AggregateAssetsValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.AggregateAssetsValuesResponse)>` |   
  
### batchDeleteAssetsCallable()
    
    
    public UnaryCallable<BatchDeleteAssetsRequest,Empty> batchDeleteAssetsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeleteAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.BatchDeleteAssetsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### batchUpdateAssetsCallable()
    
    
    public UnaryCallable<BatchUpdateAssetsRequest,BatchUpdateAssetsResponse> batchUpdateAssetsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.BatchUpdateAssetsRequest),[BatchUpdateAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.BatchUpdateAssetsResponse)>` |   
  
### close()
    
    
    public abstract void close()

### createGroupCallable()
    
    
    public UnaryCallable<CreateGroupRequest,Operation> createGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGroupOperationCallable()
    
    
    public OperationCallable<CreateGroupRequest,Group,OperationMetadata> createGroupOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Group),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### createImportDataFileCallable()
    
    
    public UnaryCallable<CreateImportDataFileRequest,Operation> createImportDataFileCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateImportDataFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateImportDataFileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createImportDataFileOperationCallable()
    
    
    public OperationCallable<CreateImportDataFileRequest,ImportDataFile,OperationMetadata> createImportDataFileOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateImportDataFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateImportDataFileRequest),[ImportDataFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ImportDataFile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### createImportJobCallable()
    
    
    public UnaryCallable<CreateImportJobRequest,Operation> createImportJobCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateImportJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createImportJobOperationCallable()
    
    
    public OperationCallable<CreateImportJobRequest,ImportJob,OperationMetadata> createImportJobOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateImportJobRequest),[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ImportJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### createPreferenceSetCallable()
    
    
    public UnaryCallable<CreatePreferenceSetRequest,Operation> createPreferenceSetCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreatePreferenceSetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPreferenceSetOperationCallable()
    
    
    public OperationCallable<CreatePreferenceSetRequest,PreferenceSet,OperationMetadata> createPreferenceSetOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreatePreferenceSetRequest),[PreferenceSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.PreferenceSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### createReportCallable()
    
    
    public UnaryCallable<CreateReportRequest,Operation> createReportCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateReportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createReportConfigCallable()
    
    
    public UnaryCallable<CreateReportConfigRequest,Operation> createReportConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateReportConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createReportConfigOperationCallable()
    
    
    public OperationCallable<CreateReportConfigRequest,ReportConfig,OperationMetadata> createReportConfigOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateReportConfigRequest),[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### createReportOperationCallable()
    
    
    public OperationCallable<CreateReportRequest,Report,OperationMetadata> createReportOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateReportRequest),[Report](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Report),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### createSourceCallable()
    
    
    public UnaryCallable<CreateSourceRequest,Operation> createSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSourceOperationCallable()
    
    
    public OperationCallable<CreateSourceRequest,Source,OperationMetadata> createSourceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.CreateSourceRequest),[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Source),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### deleteAssetCallable()
    
    
    public UnaryCallable<DeleteAssetRequest,Empty> deleteAssetCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteAssetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteGroupCallable()
    
    
    public UnaryCallable<DeleteGroupRequest,Operation> deleteGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGroupOperationCallable()
    
    
    public OperationCallable<DeleteGroupRequest,Empty,OperationMetadata> deleteGroupOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### deleteImportDataFileCallable()
    
    
    public UnaryCallable<DeleteImportDataFileRequest,Operation> deleteImportDataFileCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteImportDataFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteImportDataFileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteImportDataFileOperationCallable()
    
    
    public OperationCallable<DeleteImportDataFileRequest,Empty,OperationMetadata> deleteImportDataFileOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteImportDataFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteImportDataFileRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### deleteImportJobCallable()
    
    
    public UnaryCallable<DeleteImportJobRequest,Operation> deleteImportJobCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteImportJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteImportJobOperationCallable()
    
    
    public OperationCallable<DeleteImportJobRequest,Empty,OperationMetadata> deleteImportJobOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteImportJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### deletePreferenceSetCallable()
    
    
    public UnaryCallable<DeletePreferenceSetRequest,Operation> deletePreferenceSetCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeletePreferenceSetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePreferenceSetOperationCallable()
    
    
    public OperationCallable<DeletePreferenceSetRequest,Empty,OperationMetadata> deletePreferenceSetOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeletePreferenceSetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### deleteReportCallable()
    
    
    public UnaryCallable<DeleteReportRequest,Operation> deleteReportCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteReportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteReportConfigCallable()
    
    
    public UnaryCallable<DeleteReportConfigRequest,Operation> deleteReportConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteReportConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteReportConfigOperationCallable()
    
    
    public OperationCallable<DeleteReportConfigRequest,Empty,OperationMetadata> deleteReportConfigOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteReportConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### deleteReportOperationCallable()
    
    
    public OperationCallable<DeleteReportRequest,Empty,OperationMetadata> deleteReportOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteReportRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### deleteSourceCallable()
    
    
    public UnaryCallable<DeleteSourceRequest,Operation> deleteSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSourceOperationCallable()
    
    
    public OperationCallable<DeleteSourceRequest,Empty,OperationMetadata> deleteSourceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DeleteSourceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### getAssetCallable()
    
    
    public UnaryCallable<GetAssetRequest,Asset> getAssetCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetAssetRequest),[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Asset)>` |   
  
### getErrorFrameCallable()
    
    
    public UnaryCallable<GetErrorFrameRequest,ErrorFrame> getErrorFrameCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetErrorFrameRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetErrorFrameRequest),[ErrorFrame](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ErrorFrame)>` |   
  
### getGroupCallable()
    
    
    public UnaryCallable<GetGroupRequest,Group> getGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Group)>` |   
  
### getHttpJsonOperationsStub()
    
    
    public @Nullable OperationsStub getHttpJsonOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.gax.httpjson.longrunning.stub.OperationsStub` |   
  
### getImportDataFileCallable()
    
    
    public UnaryCallable<GetImportDataFileRequest,ImportDataFile> getImportDataFileCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetImportDataFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetImportDataFileRequest),[ImportDataFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ImportDataFile)>` |   
  
### getImportJobCallable()
    
    
    public UnaryCallable<GetImportJobRequest,ImportJob> getImportJobCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetImportJobRequest),[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ImportJob)>` |   
  
### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsStub()
    
    
    public @Nullable OperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.longrunning.stub.OperationsStub` |   
  
### getPreferenceSetCallable()
    
    
    public UnaryCallable<GetPreferenceSetRequest,PreferenceSet> getPreferenceSetCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetPreferenceSetRequest),[PreferenceSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.PreferenceSet)>` |   
  
### getReportCallable()
    
    
    public UnaryCallable<GetReportRequest,Report> getReportCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetReportRequest),[Report](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Report)>` |   
  
### getReportConfigCallable()
    
    
    public UnaryCallable<GetReportConfigRequest,ReportConfig> getReportConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetReportConfigRequest),[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportConfig)>` |   
  
### getSettingsCallable()
    
    
    public UnaryCallable<GetSettingsRequest,Settings> getSettingsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Settings)>` |   
  
### getSourceCallable()
    
    
    public UnaryCallable<GetSourceRequest,Source> getSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GetSourceRequest),[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Source)>` |   
  
### listAssetsCallable()
    
    
    public UnaryCallable<ListAssetsRequest,ListAssetsResponse> listAssetsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListAssetsRequest),[ListAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListAssetsResponse)>` |   
  
### listAssetsPagedCallable()
    
    
    public UnaryCallable<ListAssetsRequest,MigrationCenterClient.ListAssetsPagedResponse> listAssetsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListAssetsRequest),[ListAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListAssetsPagedResponse)>` |   
  
### listErrorFramesCallable()
    
    
    public UnaryCallable<ListErrorFramesRequest,ListErrorFramesResponse> listErrorFramesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListErrorFramesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListErrorFramesRequest),[ListErrorFramesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListErrorFramesResponse)>` |   
  
### listErrorFramesPagedCallable()
    
    
    public UnaryCallable<ListErrorFramesRequest,MigrationCenterClient.ListErrorFramesPagedResponse> listErrorFramesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListErrorFramesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListErrorFramesRequest),[ListErrorFramesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListErrorFramesPagedResponse)>` |   
  
### listGroupsCallable()
    
    
    public UnaryCallable<ListGroupsRequest,ListGroupsResponse> listGroupsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListGroupsRequest),[ListGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListGroupsResponse)>` |   
  
### listGroupsPagedCallable()
    
    
    public UnaryCallable<ListGroupsRequest,MigrationCenterClient.ListGroupsPagedResponse> listGroupsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListGroupsRequest),[ListGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListGroupsPagedResponse)>` |   
  
### listImportDataFilesCallable()
    
    
    public UnaryCallable<ListImportDataFilesRequest,ListImportDataFilesResponse> listImportDataFilesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListImportDataFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportDataFilesRequest),[ListImportDataFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportDataFilesResponse)>` |   
  
### listImportDataFilesPagedCallable()
    
    
    public UnaryCallable<ListImportDataFilesRequest,MigrationCenterClient.ListImportDataFilesPagedResponse> listImportDataFilesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListImportDataFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportDataFilesRequest),[ListImportDataFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListImportDataFilesPagedResponse)>` |   
  
### listImportJobsCallable()
    
    
    public UnaryCallable<ListImportJobsRequest,ListImportJobsResponse> listImportJobsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListImportJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportJobsRequest),[ListImportJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportJobsResponse)>` |   
  
### listImportJobsPagedCallable()
    
    
    public UnaryCallable<ListImportJobsRequest,MigrationCenterClient.ListImportJobsPagedResponse> listImportJobsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListImportJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListImportJobsRequest),[ListImportJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListImportJobsPagedResponse)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,MigrationCenterClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListLocationsPagedResponse)>` |   
  
### listPreferenceSetsCallable()
    
    
    public UnaryCallable<ListPreferenceSetsRequest,ListPreferenceSetsResponse> listPreferenceSetsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPreferenceSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListPreferenceSetsRequest),[ListPreferenceSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListPreferenceSetsResponse)>` |   
  
### listPreferenceSetsPagedCallable()
    
    
    public UnaryCallable<ListPreferenceSetsRequest,MigrationCenterClient.ListPreferenceSetsPagedResponse> listPreferenceSetsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPreferenceSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListPreferenceSetsRequest),[ListPreferenceSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListPreferenceSetsPagedResponse)>` |   
  
### listReportConfigsCallable()
    
    
    public UnaryCallable<ListReportConfigsRequest,ListReportConfigsResponse> listReportConfigsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReportConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportConfigsRequest),[ListReportConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportConfigsResponse)>` |   
  
### listReportConfigsPagedCallable()
    
    
    public UnaryCallable<ListReportConfigsRequest,MigrationCenterClient.ListReportConfigsPagedResponse> listReportConfigsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReportConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportConfigsRequest),[ListReportConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListReportConfigsPagedResponse)>` |   
  
### listReportsCallable()
    
    
    public UnaryCallable<ListReportsRequest,ListReportsResponse> listReportsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportsRequest),[ListReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportsResponse)>` |   
  
### listReportsPagedCallable()
    
    
    public UnaryCallable<ListReportsRequest,MigrationCenterClient.ListReportsPagedResponse> listReportsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListReportsRequest),[ListReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListReportsPagedResponse)>` |   
  
### listSourcesCallable()
    
    
    public UnaryCallable<ListSourcesRequest,ListSourcesResponse> listSourcesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListSourcesRequest),[ListSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListSourcesResponse)>` |   
  
### listSourcesPagedCallable()
    
    
    public UnaryCallable<ListSourcesRequest,MigrationCenterClient.ListSourcesPagedResponse> listSourcesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ListSourcesRequest),[ListSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MigrationCenterClient.ListSourcesPagedResponse)>` |   
  
### removeAssetsFromGroupCallable()
    
    
    public UnaryCallable<RemoveAssetsFromGroupRequest,Operation> removeAssetsFromGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveAssetsFromGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.RemoveAssetsFromGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### removeAssetsFromGroupOperationCallable()
    
    
    public OperationCallable<RemoveAssetsFromGroupRequest,Group,OperationMetadata> removeAssetsFromGroupOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveAssetsFromGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.RemoveAssetsFromGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Group),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### reportAssetFramesCallable()
    
    
    public UnaryCallable<ReportAssetFramesRequest,ReportAssetFramesResponse> reportAssetFramesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReportAssetFramesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportAssetFramesRequest),[ReportAssetFramesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportAssetFramesResponse)>` |   
  
### runImportJobCallable()
    
    
    public UnaryCallable<RunImportJobRequest,Operation> runImportJobCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.RunImportJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### runImportJobOperationCallable()
    
    
    public OperationCallable<RunImportJobRequest,Empty,OperationMetadata> runImportJobOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RunImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.RunImportJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### updateAssetCallable()
    
    
    public UnaryCallable<UpdateAssetRequest,Asset> updateAssetCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateAssetRequest),[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Asset)>` |   
  
### updateGroupCallable()
    
    
    public UnaryCallable<UpdateGroupRequest,Operation> updateGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGroupOperationCallable()
    
    
    public OperationCallable<UpdateGroupRequest,Group,OperationMetadata> updateGroupOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Group),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### updateImportJobCallable()
    
    
    public UnaryCallable<UpdateImportJobRequest,Operation> updateImportJobCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateImportJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateImportJobOperationCallable()
    
    
    public OperationCallable<UpdateImportJobRequest,ImportJob,OperationMetadata> updateImportJobOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateImportJobRequest),[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ImportJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### updatePreferenceSetCallable()
    
    
    public UnaryCallable<UpdatePreferenceSetRequest,Operation> updatePreferenceSetCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdatePreferenceSetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePreferenceSetOperationCallable()
    
    
    public OperationCallable<UpdatePreferenceSetRequest,PreferenceSet,OperationMetadata> updatePreferenceSetOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePreferenceSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdatePreferenceSetRequest),[PreferenceSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.PreferenceSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### updateSettingsCallable()
    
    
    public UnaryCallable<UpdateSettingsRequest,Operation> updateSettingsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSettingsOperationCallable()
    
    
    public OperationCallable<UpdateSettingsRequest,Settings,OperationMetadata> updateSettingsOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Settings),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### updateSourceCallable()
    
    
    public UnaryCallable<UpdateSourceRequest,Operation> updateSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSourceOperationCallable()
    
    
    public OperationCallable<UpdateSourceRequest,Source,OperationMetadata> updateSourceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.UpdateSourceRequest),[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.Source),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
### validateImportJobCallable()
    
    
    public UnaryCallable<ValidateImportJobRequest,Operation> validateImportJobCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ValidateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ValidateImportJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### validateImportJobOperationCallable()
    
    
    public OperationCallable<ValidateImportJobRequest,Empty,OperationMetadata> validateImportJobOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ValidateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ValidateImportJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
