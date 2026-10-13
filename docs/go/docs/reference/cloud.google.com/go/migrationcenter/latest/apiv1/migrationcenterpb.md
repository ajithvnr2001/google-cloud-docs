---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/migrationcenter/latest/apiv1/migrationcenterpb/
title: Migration Center API v1 - Package cloud.google.com/go/migrationcenter/apiv1/migrationcenterpb (v1.8.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:03.122429+00:00
---

# Migration Center API v1 - Package cloud.google.com/go/migrationcenter/apiv1/migrationcenterpb (v1.8.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/migrationcenter/latest/apiv1/migrationcenterpb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Migration Center API v1 - Package cloud.google.com/go/migrationcenter/apiv1/migrationcenterpb (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.6  1.0.5  0.2.6  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/migrationcenter/apiv1/migrationcenterpb). 

##  Constants 

### MigrationCenter_ListAssets_FullMethodName, MigrationCenter_GetAsset_FullMethodName, MigrationCenter_UpdateAsset_FullMethodName, MigrationCenter_BatchUpdateAssets_FullMethodName, MigrationCenter_DeleteAsset_FullMethodName, MigrationCenter_BatchDeleteAssets_FullMethodName, MigrationCenter_ReportAssetFrames_FullMethodName, MigrationCenter_AggregateAssetsValues_FullMethodName, MigrationCenter_CreateImportJob_FullMethodName, MigrationCenter_ListImportJobs_FullMethodName, MigrationCenter_GetImportJob_FullMethodName, MigrationCenter_DeleteImportJob_FullMethodName, MigrationCenter_UpdateImportJob_FullMethodName, MigrationCenter_ValidateImportJob_FullMethodName, MigrationCenter_RunImportJob_FullMethodName, MigrationCenter_GetImportDataFile_FullMethodName, MigrationCenter_ListImportDataFiles_FullMethodName, MigrationCenter_CreateImportDataFile_FullMethodName, MigrationCenter_DeleteImportDataFile_FullMethodName, MigrationCenter_ListGroups_FullMethodName, MigrationCenter_GetGroup_FullMethodName, MigrationCenter_CreateGroup_FullMethodName, MigrationCenter_UpdateGroup_FullMethodName, MigrationCenter_DeleteGroup_FullMethodName, MigrationCenter_AddAssetsToGroup_FullMethodName, MigrationCenter_RemoveAssetsFromGroup_FullMethodName, MigrationCenter_ListErrorFrames_FullMethodName, MigrationCenter_GetErrorFrame_FullMethodName, MigrationCenter_ListSources_FullMethodName, MigrationCenter_GetSource_FullMethodName, MigrationCenter_CreateSource_FullMethodName, MigrationCenter_UpdateSource_FullMethodName, MigrationCenter_DeleteSource_FullMethodName, MigrationCenter_ListPreferenceSets_FullMethodName, MigrationCenter_GetPreferenceSet_FullMethodName, MigrationCenter_CreatePreferenceSet_FullMethodName, MigrationCenter_UpdatePreferenceSet_FullMethodName, MigrationCenter_DeletePreferenceSet_FullMethodName, MigrationCenter_GetSettings_FullMethodName, MigrationCenter_UpdateSettings_FullMethodName, MigrationCenter_CreateReportConfig_FullMethodName, MigrationCenter_GetReportConfig_FullMethodName, MigrationCenter_ListReportConfigs_FullMethodName, MigrationCenter_DeleteReportConfig_FullMethodName, MigrationCenter_CreateReport_FullMethodName, MigrationCenter_GetReport_FullMethodName, MigrationCenter_ListReports_FullMethodName, MigrationCenter_DeleteReport_FullMethodName
    
    
    const (
    	MigrationCenter_ListAssets_FullMethodName            = "/google.cloud.migrationcenter.v1.MigrationCenter/ListAssets"
    	MigrationCenter_GetAsset_FullMethodName              = "/google.cloud.migrationcenter.v1.MigrationCenter/GetAsset"
    	MigrationCenter_UpdateAsset_FullMethodName           = "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateAsset"
    	MigrationCenter_BatchUpdateAssets_FullMethodName     = "/google.cloud.migrationcenter.v1.MigrationCenter/BatchUpdateAssets"
    	MigrationCenter_DeleteAsset_FullMethodName           = "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteAsset"
    	MigrationCenter_BatchDeleteAssets_FullMethodName     = "/google.cloud.migrationcenter.v1.MigrationCenter/BatchDeleteAssets"
    	MigrationCenter_ReportAssetFrames_FullMethodName     = "/google.cloud.migrationcenter.v1.MigrationCenter/ReportAssetFrames"
    	MigrationCenter_AggregateAssetsValues_FullMethodName = "/google.cloud.migrationcenter.v1.MigrationCenter/AggregateAssetsValues"
    	MigrationCenter_CreateImportJob_FullMethodName       = "/google.cloud.migrationcenter.v1.MigrationCenter/CreateImportJob"
    	MigrationCenter_ListImportJobs_FullMethodName        = "/google.cloud.migrationcenter.v1.MigrationCenter/ListImportJobs"
    	MigrationCenter_GetImportJob_FullMethodName          = "/google.cloud.migrationcenter.v1.MigrationCenter/GetImportJob"
    	MigrationCenter_DeleteImportJob_FullMethodName       = "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteImportJob"
    	MigrationCenter_UpdateImportJob_FullMethodName       = "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateImportJob"
    	MigrationCenter_ValidateImportJob_FullMethodName     = "/google.cloud.migrationcenter.v1.MigrationCenter/ValidateImportJob"
    	MigrationCenter_RunImportJob_FullMethodName          = "/google.cloud.migrationcenter.v1.MigrationCenter/RunImportJob"
    	MigrationCenter_GetImportDataFile_FullMethodName     = "/google.cloud.migrationcenter.v1.MigrationCenter/GetImportDataFile"
    	MigrationCenter_ListImportDataFiles_FullMethodName   = "/google.cloud.migrationcenter.v1.MigrationCenter/ListImportDataFiles"
    	MigrationCenter_CreateImportDataFile_FullMethodName  = "/google.cloud.migrationcenter.v1.MigrationCenter/CreateImportDataFile"
    	MigrationCenter_DeleteImportDataFile_FullMethodName  = "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteImportDataFile"
    	MigrationCenter_ListGroups_FullMethodName            = "/google.cloud.migrationcenter.v1.MigrationCenter/ListGroups"
    	MigrationCenter_GetGroup_FullMethodName              = "/google.cloud.migrationcenter.v1.MigrationCenter/GetGroup"
    	MigrationCenter_CreateGroup_FullMethodName           = "/google.cloud.migrationcenter.v1.MigrationCenter/CreateGroup"
    	MigrationCenter_UpdateGroup_FullMethodName           = "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateGroup"
    	MigrationCenter_DeleteGroup_FullMethodName           = "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteGroup"
    	MigrationCenter_AddAssetsToGroup_FullMethodName      = "/google.cloud.migrationcenter.v1.MigrationCenter/AddAssetsToGroup"
    	MigrationCenter_RemoveAssetsFromGroup_FullMethodName = "/google.cloud.migrationcenter.v1.MigrationCenter/RemoveAssetsFromGroup"
    	MigrationCenter_ListErrorFrames_FullMethodName       = "/google.cloud.migrationcenter.v1.MigrationCenter/ListErrorFrames"
    	MigrationCenter_GetErrorFrame_FullMethodName         = "/google.cloud.migrationcenter.v1.MigrationCenter/GetErrorFrame"
    	MigrationCenter_ListSources_FullMethodName           = "/google.cloud.migrationcenter.v1.MigrationCenter/ListSources"
    	MigrationCenter_GetSource_FullMethodName             = "/google.cloud.migrationcenter.v1.MigrationCenter/GetSource"
    	MigrationCenter_CreateSource_FullMethodName          = "/google.cloud.migrationcenter.v1.MigrationCenter/CreateSource"
    	MigrationCenter_UpdateSource_FullMethodName          = "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateSource"
    	MigrationCenter_DeleteSource_FullMethodName          = "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteSource"
    	MigrationCenter_ListPreferenceSets_FullMethodName    = "/google.cloud.migrationcenter.v1.MigrationCenter/ListPreferenceSets"
    	MigrationCenter_GetPreferenceSet_FullMethodName      = "/google.cloud.migrationcenter.v1.MigrationCenter/GetPreferenceSet"
    	MigrationCenter_CreatePreferenceSet_FullMethodName   = "/google.cloud.migrationcenter.v1.MigrationCenter/CreatePreferenceSet"
    	MigrationCenter_UpdatePreferenceSet_FullMethodName   = "/google.cloud.migrationcenter.v1.MigrationCenter/UpdatePreferenceSet"
    	MigrationCenter_DeletePreferenceSet_FullMethodName   = "/google.cloud.migrationcenter.v1.MigrationCenter/DeletePreferenceSet"
    	MigrationCenter_GetSettings_FullMethodName           = "/google.cloud.migrationcenter.v1.MigrationCenter/GetSettings"
    	MigrationCenter_UpdateSettings_FullMethodName        = "/google.cloud.migrationcenter.v1.MigrationCenter/UpdateSettings"
    	MigrationCenter_CreateReportConfig_FullMethodName    = "/google.cloud.migrationcenter.v1.MigrationCenter/CreateReportConfig"
    	MigrationCenter_GetReportConfig_FullMethodName       = "/google.cloud.migrationcenter.v1.MigrationCenter/GetReportConfig"
    	MigrationCenter_ListReportConfigs_FullMethodName     = "/google.cloud.migrationcenter.v1.MigrationCenter/ListReportConfigs"
    	MigrationCenter_DeleteReportConfig_FullMethodName    = "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteReportConfig"
    	MigrationCenter_CreateReport_FullMethodName          = "/google.cloud.migrationcenter.v1.MigrationCenter/CreateReport"
    	MigrationCenter_GetReport_FullMethodName             = "/google.cloud.migrationcenter.v1.MigrationCenter/GetReport"
    	MigrationCenter_ListReports_FullMethodName           = "/google.cloud.migrationcenter.v1.MigrationCenter/ListReports"
    	MigrationCenter_DeleteReport_FullMethodName          = "/google.cloud.migrationcenter.v1.MigrationCenter/DeleteReport"
    )

## Variables 

### AssetView_name, AssetView_value
    
    
    var (
    	AssetView_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ASSET_VIEW_UNSPECIFIED",
    		1: "ASSET_VIEW_BASIC",
    		2: "ASSET_VIEW_FULL",
    	}
    	AssetView_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ASSET_VIEW_UNSPECIFIED": 0,
    		"ASSET_VIEW_BASIC":       1,
    		"ASSET_VIEW_FULL":        2,
    	}
    )

Enum value maps for AssetView.

### OperatingSystemFamily_name, OperatingSystemFamily_value
    
    
    var (
    	OperatingSystemFamily_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "OS_FAMILY_UNKNOWN",
    		1: "OS_FAMILY_WINDOWS",
    		2: "OS_FAMILY_LINUX",
    		3: "OS_FAMILY_UNIX",
    	}
    	OperatingSystemFamily_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"OS_FAMILY_UNKNOWN": 0,
    		"OS_FAMILY_WINDOWS": 1,
    		"OS_FAMILY_LINUX":   2,
    		"OS_FAMILY_UNIX":    3,
    	}
    )

Enum value maps for OperatingSystemFamily.

### ImportJobFormat_name, ImportJobFormat_value
    
    
    var (
    	ImportJobFormat_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "IMPORT_JOB_FORMAT_UNSPECIFIED",
    		1: "IMPORT_JOB_FORMAT_RVTOOLS_XLSX",
    		2: "IMPORT_JOB_FORMAT_RVTOOLS_CSV",
    		4: "IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV",
    		5: "IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV",
    		6: "IMPORT_JOB_FORMAT_STRATOZONE_CSV",
    	}
    	ImportJobFormat_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"IMPORT_JOB_FORMAT_UNSPECIFIED":        0,
    		"IMPORT_JOB_FORMAT_RVTOOLS_XLSX":       1,
    		"IMPORT_JOB_FORMAT_RVTOOLS_CSV":        2,
    		"IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV":   4,
    		"IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV": 5,
    		"IMPORT_JOB_FORMAT_STRATOZONE_CSV":     6,
    	}
    )

Enum value maps for ImportJobFormat.

### ImportJobView_name, ImportJobView_value
    
    
    var (
    	ImportJobView_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "IMPORT_JOB_VIEW_UNSPECIFIED",
    		1: "IMPORT_JOB_VIEW_BASIC",
    		2: "IMPORT_JOB_VIEW_FULL",
    	}
    	ImportJobView_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"IMPORT_JOB_VIEW_UNSPECIFIED": 0,
    		"IMPORT_JOB_VIEW_BASIC":       1,
    		"IMPORT_JOB_VIEW_FULL":        2,
    	}
    )

Enum value maps for ImportJobView.

### ErrorFrameView_name, ErrorFrameView_value
    
    
    var (
    	ErrorFrameView_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ERROR_FRAME_VIEW_UNSPECIFIED",
    		1: "ERROR_FRAME_VIEW_BASIC",
    		2: "ERROR_FRAME_VIEW_FULL",
    	}
    	ErrorFrameView_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ERROR_FRAME_VIEW_UNSPECIFIED": 0,
    		"ERROR_FRAME_VIEW_BASIC":       1,
    		"ERROR_FRAME_VIEW_FULL":        2,
    	}
    )

Enum value maps for ErrorFrameView.

### PersistentDiskType_name, PersistentDiskType_value
    
    
    var (
    	PersistentDiskType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "PERSISTENT_DISK_TYPE_UNSPECIFIED",
    		1: "PERSISTENT_DISK_TYPE_STANDARD",
    		2: "PERSISTENT_DISK_TYPE_BALANCED",
    		3: "PERSISTENT_DISK_TYPE_SSD",
    	}
    	PersistentDiskType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"PERSISTENT_DISK_TYPE_UNSPECIFIED": 0,
    		"PERSISTENT_DISK_TYPE_STANDARD":    1,
    		"PERSISTENT_DISK_TYPE_BALANCED":    2,
    		"PERSISTENT_DISK_TYPE_SSD":         3,
    	}
    )

Enum value maps for PersistentDiskType.

### LicenseType_name, LicenseType_value
    
    
    var (
    	LicenseType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "LICENSE_TYPE_UNSPECIFIED",
    		1: "LICENSE_TYPE_DEFAULT",
    		2: "LICENSE_TYPE_BRING_YOUR_OWN_LICENSE",
    	}
    	LicenseType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"LICENSE_TYPE_UNSPECIFIED":            0,
    		"LICENSE_TYPE_DEFAULT":                1,
    		"LICENSE_TYPE_BRING_YOUR_OWN_LICENSE": 2,
    	}
    )

Enum value maps for LicenseType.

### SizingOptimizationStrategy_name, SizingOptimizationStrategy_value
    
    
    var (
    	SizingOptimizationStrategy_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED",
    		1: "SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE",
    		2: "SIZING_OPTIMIZATION_STRATEGY_MODERATE",
    		3: "SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE",
    	}
    	SizingOptimizationStrategy_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED":    0,
    		"SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE": 1,
    		"SIZING_OPTIMIZATION_STRATEGY_MODERATE":       2,
    		"SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE":     3,
    	}
    )

Enum value maps for SizingOptimizationStrategy.

### CommitmentPlan_name, CommitmentPlan_value
    
    
    var (
    	CommitmentPlan_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "COMMITMENT_PLAN_UNSPECIFIED",
    		1: "COMMITMENT_PLAN_NONE",
    		2: "COMMITMENT_PLAN_ONE_YEAR",
    		3: "COMMITMENT_PLAN_THREE_YEARS",
    	}
    	CommitmentPlan_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"COMMITMENT_PLAN_UNSPECIFIED": 0,
    		"COMMITMENT_PLAN_NONE":        1,
    		"COMMITMENT_PLAN_ONE_YEAR":    2,
    		"COMMITMENT_PLAN_THREE_YEARS": 3,
    	}
    )

Enum value maps for CommitmentPlan.

### ComputeMigrationTargetProduct_name, ComputeMigrationTargetProduct_value
    
    
    var (
    	ComputeMigrationTargetProduct_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED",
    		1: "COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE",
    		2: "COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE",
    		3: "COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY",
    	}
    	ComputeMigrationTargetProduct_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED":    0,
    		"COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE": 1,
    		"COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE":  2,
    		"COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY":   3,
    	}
    )

Enum value maps for ComputeMigrationTargetProduct.

### ReportView_name, ReportView_value
    
    
    var (
    	ReportView_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "REPORT_VIEW_UNSPECIFIED",
    		1: "REPORT_VIEW_BASIC",
    		2: "REPORT_VIEW_FULL",
    		3: "REPORT_VIEW_STANDARD",
    	}
    	ReportView_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"REPORT_VIEW_UNSPECIFIED": 0,
    		"REPORT_VIEW_BASIC":       1,
    		"REPORT_VIEW_FULL":        2,
    		"REPORT_VIEW_STANDARD":    3,
    	}
    )

Enum value maps for ReportView.

### ImportJob_ImportJobState_name, ImportJob_ImportJobState_value
    
    
    var (
    	ImportJob_ImportJobState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "IMPORT_JOB_STATE_UNSPECIFIED",
    		1: "IMPORT_JOB_STATE_PENDING",
    		2: "IMPORT_JOB_STATE_RUNNING",
    		3: "IMPORT_JOB_STATE_COMPLETED",
    		4: "IMPORT_JOB_STATE_FAILED",
    		5: "IMPORT_JOB_STATE_VALIDATING",
    		6: "IMPORT_JOB_STATE_FAILED_VALIDATION",
    		7: "IMPORT_JOB_STATE_READY",
    	}
    	ImportJob_ImportJobState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"IMPORT_JOB_STATE_UNSPECIFIED":       0,
    		"IMPORT_JOB_STATE_PENDING":           1,
    		"IMPORT_JOB_STATE_RUNNING":           2,
    		"IMPORT_JOB_STATE_COMPLETED":         3,
    		"IMPORT_JOB_STATE_FAILED":            4,
    		"IMPORT_JOB_STATE_VALIDATING":        5,
    		"IMPORT_JOB_STATE_FAILED_VALIDATION": 6,
    		"IMPORT_JOB_STATE_READY":             7,
    	}
    )

Enum value maps for ImportJob_ImportJobState.

### ImportDataFile_State_name, ImportDataFile_State_value
    
    
    var (
    	ImportDataFile_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "CREATING",
    		2: "ACTIVE",
    	}
    	ImportDataFile_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"CREATING":          1,
    		"ACTIVE":            2,
    	}
    )

Enum value maps for ImportDataFile_State.

### Source_SourceType_name, Source_SourceType_value
    
    
    var (
    	Source_SourceType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SOURCE_TYPE_UNKNOWN",
    		1: "SOURCE_TYPE_UPLOAD",
    		2: "SOURCE_TYPE_GUEST_OS_SCAN",
    		3: "SOURCE_TYPE_INVENTORY_SCAN",
    		4: "SOURCE_TYPE_CUSTOM",
    	}
    	Source_SourceType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SOURCE_TYPE_UNKNOWN":        0,
    		"SOURCE_TYPE_UPLOAD":         1,
    		"SOURCE_TYPE_GUEST_OS_SCAN":  2,
    		"SOURCE_TYPE_INVENTORY_SCAN": 3,
    		"SOURCE_TYPE_CUSTOM":         4,
    	}
    )

Enum value maps for Source_SourceType.

### Source_State_name, Source_State_value
    
    
    var (
    	Source_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ACTIVE",
    		2: "DELETING",
    		3: "INVALID",
    	}
    	Source_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ACTIVE":            1,
    		"DELETING":          2,
    		"INVALID":           3,
    	}
    )

Enum value maps for Source_State.

### Report_Type_name, Report_Type_value
    
    
    var (
    	Report_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "TOTAL_COST_OF_OWNERSHIP",
    	}
    	Report_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED":        0,
    		"TOTAL_COST_OF_OWNERSHIP": 1,
    	}
    )

Enum value maps for Report_Type.

### Report_State_name, Report_State_value
    
    
    var (
    	Report_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "PENDING",
    		2: "SUCCEEDED",
    		3: "FAILED",
    	}
    	Report_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"PENDING":           1,
    		"SUCCEEDED":         2,
    		"FAILED":            3,
    	}
    )

Enum value maps for Report_State.

### MachineDetails_PowerState_name, MachineDetails_PowerState_value
    
    
    var (
    	MachineDetails_PowerState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "POWER_STATE_UNSPECIFIED",
    		1: "PENDING",
    		2: "ACTIVE",
    		3: "SUSPENDING",
    		4: "SUSPENDED",
    		5: "DELETING",
    		6: "DELETED",
    	}
    	MachineDetails_PowerState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"POWER_STATE_UNSPECIFIED": 0,
    		"PENDING":                 1,
    		"ACTIVE":                  2,
    		"SUSPENDING":              3,
    		"SUSPENDED":               4,
    		"DELETING":                5,
    		"DELETED":                 6,
    	}
    )

Enum value maps for MachineDetails_PowerState.

### MachineArchitectureDetails_FirmwareType_name, MachineArchitectureDetails_FirmwareType_value
    
    
    var (
    	MachineArchitectureDetails_FirmwareType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "FIRMWARE_TYPE_UNSPECIFIED",
    		1: "BIOS",
    		2: "EFI",
    	}
    	MachineArchitectureDetails_FirmwareType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"FIRMWARE_TYPE_UNSPECIFIED": 0,
    		"BIOS":                      1,
    		"EFI":                       2,
    	}
    )

Enum value maps for MachineArchitectureDetails_FirmwareType.

### MachineArchitectureDetails_CpuHyperThreading_name, MachineArchitectureDetails_CpuHyperThreading_value
    
    
    var (
    	MachineArchitectureDetails_CpuHyperThreading_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "CPU_HYPER_THREADING_UNSPECIFIED",
    		1: "DISABLED",
    		2: "ENABLED",
    	}
    	MachineArchitectureDetails_CpuHyperThreading_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"CPU_HYPER_THREADING_UNSPECIFIED": 0,
    		"DISABLED":                        1,
    		"ENABLED":                         2,
    	}
    )

Enum value maps for MachineArchitectureDetails_CpuHyperThreading.

### NetworkAddress_AddressAssignment_name, NetworkAddress_AddressAssignment_value
    
    
    var (
    	NetworkAddress_AddressAssignment_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "ADDRESS_ASSIGNMENT_UNSPECIFIED",
    		1: "ADDRESS_ASSIGNMENT_STATIC",
    		2: "ADDRESS_ASSIGNMENT_DHCP",
    	}
    	NetworkAddress_AddressAssignment_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"ADDRESS_ASSIGNMENT_UNSPECIFIED": 0,
    		"ADDRESS_ASSIGNMENT_STATIC":      1,
    		"ADDRESS_ASSIGNMENT_DHCP":        2,
    	}
    )

Enum value maps for NetworkAddress_AddressAssignment.

### DiskEntry_InterfaceType_name, DiskEntry_InterfaceType_value
    
    
    var (
    	DiskEntry_InterfaceType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "INTERFACE_TYPE_UNSPECIFIED",
    		1: "IDE",
    		2: "SATA",
    		3: "SAS",
    		4: "SCSI",
    		5: "NVME",
    		6: "FC",
    		7: "ISCSI",
    	}
    	DiskEntry_InterfaceType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"INTERFACE_TYPE_UNSPECIFIED": 0,
    		"IDE":                        1,
    		"SATA":                       2,
    		"SAS":                        3,
    		"SCSI":                       4,
    		"NVME":                       5,
    		"FC":                         6,
    		"ISCSI":                      7,
    	}
    )

Enum value maps for DiskEntry_InterfaceType.

### VmwareDiskConfig_BackingType_name, VmwareDiskConfig_BackingType_value
    
    
    var (
    	VmwareDiskConfig_BackingType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "BACKING_TYPE_UNSPECIFIED",
    		1: "BACKING_TYPE_FLAT_V1",
    		2: "BACKING_TYPE_FLAT_V2",
    		3: "BACKING_TYPE_PMEM",
    		4: "BACKING_TYPE_RDM_V1",
    		5: "BACKING_TYPE_RDM_V2",
    		6: "BACKING_TYPE_SESPARSE",
    		7: "BACKING_TYPE_SESPARSE_V1",
    		8: "BACKING_TYPE_SESPARSE_V2",
    	}
    	VmwareDiskConfig_BackingType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"BACKING_TYPE_UNSPECIFIED": 0,
    		"BACKING_TYPE_FLAT_V1":     1,
    		"BACKING_TYPE_FLAT_V2":     2,
    		"BACKING_TYPE_PMEM":        3,
    		"BACKING_TYPE_RDM_V1":      4,
    		"BACKING_TYPE_RDM_V2":      5,
    		"BACKING_TYPE_SESPARSE":    6,
    		"BACKING_TYPE_SESPARSE_V1": 7,
    		"BACKING_TYPE_SESPARSE_V2": 8,
    	}
    )

Enum value maps for VmwareDiskConfig_BackingType.

### VmwareDiskConfig_VmdkMode_name, VmwareDiskConfig_VmdkMode_value
    
    
    var (
    	VmwareDiskConfig_VmdkMode_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "VMDK_MODE_UNSPECIFIED",
    		1: "DEPENDENT",
    		2: "INDEPENDENT_PERSISTENT",
    		3: "INDEPENDENT_NONPERSISTENT",
    	}
    	VmwareDiskConfig_VmdkMode_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"VMDK_MODE_UNSPECIFIED":     0,
    		"DEPENDENT":                 1,
    		"INDEPENDENT_PERSISTENT":    2,
    		"INDEPENDENT_NONPERSISTENT": 3,
    	}
    )

Enum value maps for VmwareDiskConfig_VmdkMode.

### VmwareDiskConfig_RdmCompatibility_name, VmwareDiskConfig_RdmCompatibility_value
    
    
    var (
    	VmwareDiskConfig_RdmCompatibility_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "RDM_COMPATIBILITY_UNSPECIFIED",
    		1: "PHYSICAL_COMPATIBILITY",
    		2: "VIRTUAL_COMPATIBILITY",
    	}
    	VmwareDiskConfig_RdmCompatibility_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"RDM_COMPATIBILITY_UNSPECIFIED": 0,
    		"PHYSICAL_COMPATIBILITY":        1,
    		"VIRTUAL_COMPATIBILITY":         2,
    	}
    )

Enum value maps for VmwareDiskConfig_RdmCompatibility.

### GuestConfigDetails_SeLinuxMode_name, GuestConfigDetails_SeLinuxMode_value
    
    
    var (
    	GuestConfigDetails_SeLinuxMode_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SE_LINUX_MODE_UNSPECIFIED",
    		1: "SE_LINUX_MODE_DISABLED",
    		2: "SE_LINUX_MODE_PERMISSIVE",
    		3: "SE_LINUX_MODE_ENFORCING",
    	}
    	GuestConfigDetails_SeLinuxMode_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SE_LINUX_MODE_UNSPECIFIED": 0,
    		"SE_LINUX_MODE_DISABLED":    1,
    		"SE_LINUX_MODE_PERMISSIVE":  2,
    		"SE_LINUX_MODE_ENFORCING":   3,
    	}
    )

Enum value maps for GuestConfigDetails_SeLinuxMode.

### RunningService_State_name, RunningService_State_value
    
    
    var (
    	RunningService_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "ACTIVE",
    		2: "PAUSED",
    		3: "STOPPED",
    	}
    	RunningService_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"ACTIVE":            1,
    		"PAUSED":            2,
    		"STOPPED":           3,
    	}
    )

Enum value maps for RunningService_State.

### RunningService_StartMode_name, RunningService_StartMode_value
    
    
    var (
    	RunningService_StartMode_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "START_MODE_UNSPECIFIED",
    		1: "BOOT",
    		2: "SYSTEM",
    		3: "AUTO",
    		4: "MANUAL",
    		5: "DISABLED",
    	}
    	RunningService_StartMode_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"START_MODE_UNSPECIFIED": 0,
    		"BOOT":                   1,
    		"SYSTEM":                 2,
    		"AUTO":                   3,
    		"MANUAL":                 4,
    		"DISABLED":               5,
    	}
    )

Enum value maps for RunningService_StartMode.

### NetworkConnection_State_name, NetworkConnection_State_value
    
    
    var (
    	NetworkConnection_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "STATE_UNSPECIFIED",
    		1: "OPENING",
    		2: "OPEN",
    		3: "LISTEN",
    		4: "CLOSING",
    		5: "CLOSED",
    	}
    	NetworkConnection_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"STATE_UNSPECIFIED": 0,
    		"OPENING":           1,
    		"OPEN":              2,
    		"LISTEN":            3,
    		"CLOSING":           4,
    		"CLOSED":            5,
    	}
    )

Enum value maps for NetworkConnection_State.

### FitDescriptor_FitLevel_name, FitDescriptor_FitLevel_value
    
    
    var (
    	FitDescriptor_FitLevel_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "FIT_LEVEL_UNSPECIFIED",
    		1: "FIT",
    		2: "NO_FIT",
    		3: "REQUIRES_EFFORT",
    	}
    	FitDescriptor_FitLevel_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"FIT_LEVEL_UNSPECIFIED": 0,
    		"FIT":                   1,
    		"NO_FIT":                2,
    		"REQUIRES_EFFORT":       3,
    	}
    )

Enum value maps for FitDescriptor_FitLevel.

### ImportError_Severity_name, ImportError_Severity_value
    
    
    var (
    	ImportError_Severity_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SEVERITY_UNSPECIFIED",
    		1: "ERROR",
    		2: "WARNING",
    		3: "INFO",
    	}
    	ImportError_Severity_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SEVERITY_UNSPECIFIED": 0,
    		"ERROR":                1,
    		"WARNING":              2,
    		"INFO":                 3,
    	}
    )

Enum value maps for ImportError_Severity.

### VmwareEnginePreferences_CommitmentPlan_name, VmwareEnginePreferences_CommitmentPlan_value
    
    
    var (
    	VmwareEnginePreferences_CommitmentPlan_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "COMMITMENT_PLAN_UNSPECIFIED",
    		1: "ON_DEMAND",
    		2: "COMMITMENT_1_YEAR_MONTHLY_PAYMENTS",
    		3: "COMMITMENT_3_YEAR_MONTHLY_PAYMENTS",
    		4: "COMMITMENT_1_YEAR_UPFRONT_PAYMENT",
    		5: "COMMITMENT_3_YEAR_UPFRONT_PAYMENT",
    	}
    	VmwareEnginePreferences_CommitmentPlan_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"COMMITMENT_PLAN_UNSPECIFIED":        0,
    		"ON_DEMAND":                          1,
    		"COMMITMENT_1_YEAR_MONTHLY_PAYMENTS": 2,
    		"COMMITMENT_3_YEAR_MONTHLY_PAYMENTS": 3,
    		"COMMITMENT_1_YEAR_UPFRONT_PAYMENT":  4,
    		"COMMITMENT_3_YEAR_UPFRONT_PAYMENT":  5,
    	}
    )

Enum value maps for VmwareEnginePreferences_CommitmentPlan.

### SoleTenancyPreferences_HostMaintenancePolicy_name, SoleTenancyPreferences_HostMaintenancePolicy_value
    
    
    var (
    	SoleTenancyPreferences_HostMaintenancePolicy_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "HOST_MAINTENANCE_POLICY_UNSPECIFIED",
    		1: "HOST_MAINTENANCE_POLICY_DEFAULT",
    		2: "HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE",
    		3: "HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP",
    	}
    	SoleTenancyPreferences_HostMaintenancePolicy_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"HOST_MAINTENANCE_POLICY_UNSPECIFIED":               0,
    		"HOST_MAINTENANCE_POLICY_DEFAULT":                   1,
    		"HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE":          2,
    		"HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP": 3,
    	}
    )

Enum value maps for SoleTenancyPreferences_HostMaintenancePolicy.

### SoleTenancyPreferences_CommitmentPlan_name, SoleTenancyPreferences_CommitmentPlan_value
    
    
    var (
    	SoleTenancyPreferences_CommitmentPlan_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "COMMITMENT_PLAN_UNSPECIFIED",
    		1: "ON_DEMAND",
    		2: "COMMITMENT_1_YEAR",
    		3: "COMMITMENT_3_YEAR",
    	}
    	SoleTenancyPreferences_CommitmentPlan_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"COMMITMENT_PLAN_UNSPECIFIED": 0,
    		"ON_DEMAND":                   1,
    		"COMMITMENT_1_YEAR":           2,
    		"COMMITMENT_3_YEAR":           3,
    	}
    )

Enum value maps for SoleTenancyPreferences_CommitmentPlan.

### File_google_cloud_migrationcenter_v1_migrationcenter_proto
    
    
    var File_google_cloud_migrationcenter_v1_migrationcenter_proto protoreflect.FileDescriptor

### MigrationCenter_ServiceDesc
    
    
    var MigrationCenter_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.migrationcenter.v1.MigrationCenter",
    	HandlerType: (*MigrationCenterServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "ListAssets",
    			Handler:    _MigrationCenter_ListAssets_Handler,
    		},
    		{
    			MethodName: "GetAsset",
    			Handler:    _MigrationCenter_GetAsset_Handler,
    		},
    		{
    			MethodName: "UpdateAsset",
    			Handler:    _MigrationCenter_UpdateAsset_Handler,
    		},
    		{
    			MethodName: "BatchUpdateAssets",
    			Handler:    _MigrationCenter_BatchUpdateAssets_Handler,
    		},
    		{
    			MethodName: "DeleteAsset",
    			Handler:    _MigrationCenter_DeleteAsset_Handler,
    		},
    		{
    			MethodName: "BatchDeleteAssets",
    			Handler:    _MigrationCenter_BatchDeleteAssets_Handler,
    		},
    		{
    			MethodName: "ReportAssetFrames",
    			Handler:    _MigrationCenter_ReportAssetFrames_Handler,
    		},
    		{
    			MethodName: "AggregateAssetsValues",
    			Handler:    _MigrationCenter_AggregateAssetsValues_Handler,
    		},
    		{
    			MethodName: "CreateImportJob",
    			Handler:    _MigrationCenter_CreateImportJob_Handler,
    		},
    		{
    			MethodName: "ListImportJobs",
    			Handler:    _MigrationCenter_ListImportJobs_Handler,
    		},
    		{
    			MethodName: "GetImportJob",
    			Handler:    _MigrationCenter_GetImportJob_Handler,
    		},
    		{
    			MethodName: "DeleteImportJob",
    			Handler:    _MigrationCenter_DeleteImportJob_Handler,
    		},
    		{
    			MethodName: "UpdateImportJob",
    			Handler:    _MigrationCenter_UpdateImportJob_Handler,
    		},
    		{
    			MethodName: "ValidateImportJob",
    			Handler:    _MigrationCenter_ValidateImportJob_Handler,
    		},
    		{
    			MethodName: "RunImportJob",
    			Handler:    _MigrationCenter_RunImportJob_Handler,
    		},
    		{
    			MethodName: "GetImportDataFile",
    			Handler:    _MigrationCenter_GetImportDataFile_Handler,
    		},
    		{
    			MethodName: "ListImportDataFiles",
    			Handler:    _MigrationCenter_ListImportDataFiles_Handler,
    		},
    		{
    			MethodName: "CreateImportDataFile",
    			Handler:    _MigrationCenter_CreateImportDataFile_Handler,
    		},
    		{
    			MethodName: "DeleteImportDataFile",
    			Handler:    _MigrationCenter_DeleteImportDataFile_Handler,
    		},
    		{
    			MethodName: "ListGroups",
    			Handler:    _MigrationCenter_ListGroups_Handler,
    		},
    		{
    			MethodName: "GetGroup",
    			Handler:    _MigrationCenter_GetGroup_Handler,
    		},
    		{
    			MethodName: "CreateGroup",
    			Handler:    _MigrationCenter_CreateGroup_Handler,
    		},
    		{
    			MethodName: "UpdateGroup",
    			Handler:    _MigrationCenter_UpdateGroup_Handler,
    		},
    		{
    			MethodName: "DeleteGroup",
    			Handler:    _MigrationCenter_DeleteGroup_Handler,
    		},
    		{
    			MethodName: "AddAssetsToGroup",
    			Handler:    _MigrationCenter_AddAssetsToGroup_Handler,
    		},
    		{
    			MethodName: "RemoveAssetsFromGroup",
    			Handler:    _MigrationCenter_RemoveAssetsFromGroup_Handler,
    		},
    		{
    			MethodName: "ListErrorFrames",
    			Handler:    _MigrationCenter_ListErrorFrames_Handler,
    		},
    		{
    			MethodName: "GetErrorFrame",
    			Handler:    _MigrationCenter_GetErrorFrame_Handler,
    		},
    		{
    			MethodName: "ListSources",
    			Handler:    _MigrationCenter_ListSources_Handler,
    		},
    		{
    			MethodName: "GetSource",
    			Handler:    _MigrationCenter_GetSource_Handler,
    		},
    		{
    			MethodName: "CreateSource",
    			Handler:    _MigrationCenter_CreateSource_Handler,
    		},
    		{
    			MethodName: "UpdateSource",
    			Handler:    _MigrationCenter_UpdateSource_Handler,
    		},
    		{
    			MethodName: "DeleteSource",
    			Handler:    _MigrationCenter_DeleteSource_Handler,
    		},
    		{
    			MethodName: "ListPreferenceSets",
    			Handler:    _MigrationCenter_ListPreferenceSets_Handler,
    		},
    		{
    			MethodName: "GetPreferenceSet",
    			Handler:    _MigrationCenter_GetPreferenceSet_Handler,
    		},
    		{
    			MethodName: "CreatePreferenceSet",
    			Handler:    _MigrationCenter_CreatePreferenceSet_Handler,
    		},
    		{
    			MethodName: "UpdatePreferenceSet",
    			Handler:    _MigrationCenter_UpdatePreferenceSet_Handler,
    		},
    		{
    			MethodName: "DeletePreferenceSet",
    			Handler:    _MigrationCenter_DeletePreferenceSet_Handler,
    		},
    		{
    			MethodName: "GetSettings",
    			Handler:    _MigrationCenter_GetSettings_Handler,
    		},
    		{
    			MethodName: "UpdateSettings",
    			Handler:    _MigrationCenter_UpdateSettings_Handler,
    		},
    		{
    			MethodName: "CreateReportConfig",
    			Handler:    _MigrationCenter_CreateReportConfig_Handler,
    		},
    		{
    			MethodName: "GetReportConfig",
    			Handler:    _MigrationCenter_GetReportConfig_Handler,
    		},
    		{
    			MethodName: "ListReportConfigs",
    			Handler:    _MigrationCenter_ListReportConfigs_Handler,
    		},
    		{
    			MethodName: "DeleteReportConfig",
    			Handler:    _MigrationCenter_DeleteReportConfig_Handler,
    		},
    		{
    			MethodName: "CreateReport",
    			Handler:    _MigrationCenter_CreateReport_Handler,
    		},
    		{
    			MethodName: "GetReport",
    			Handler:    _MigrationCenter_GetReport_Handler,
    		},
    		{
    			MethodName: "ListReports",
    			Handler:    _MigrationCenter_ListReports_Handler,
    		},
    		{
    			MethodName: "DeleteReport",
    			Handler:    _MigrationCenter_DeleteReport_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/migrationcenter/v1/migrationcenter.proto",
    }

MigrationCenter_ServiceDesc is the grpc.ServiceDesc for MigrationCenter service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterMigrationCenterServer 
    
    
    func RegisterMigrationCenterServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv MigrationCenterServer)

## AddAssetsToGroupRequest
    
    
    type AddAssetsToGroupRequest struct {
    
    	// Required. Group reference.
    	Group [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=group,proto3" json:"group,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Required. List of assets to be added.
    	// The maximum number of assets that can be added in a single request is
    	// 1000.
    	Assets *AssetList `protobuf:"bytes,3,opt,name=assets,proto3" json:"assets,omitempty"`
    	// Optional. When this value is set to `false` and one of the given assets is
    	// already an existing member of the group, the operation fails with an
    	// `Already Exists` error. When set to `true` this situation is silently
    	// ignored by the server.
    	//
    	// Default value is `false`.
    	AllowExisting [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=allow_existing,json=allowExisting,proto3" json:"allow_existing,omitempty"`
    	// contains filtered or unexported fields
    }

A request to add assets to a group.

### func (*AddAssetsToGroupRequest) Descriptor 
    
    
    func (*AddAssetsToGroupRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AddAssetsToGroupRequest.ProtoReflect.Descriptor instead.

### func (*AddAssetsToGroupRequest) GetAllowExisting 
    
    
    func (x *AddAssetsToGroupRequest) GetAllowExisting() [bool](https://pkg.go.dev/builtin#bool)

### func (*AddAssetsToGroupRequest) GetAssets 
    
    
    func (x *AddAssetsToGroupRequest) GetAssets() *AssetList

### func (*AddAssetsToGroupRequest) GetGroup 
    
    
    func (x *AddAssetsToGroupRequest) GetGroup() [string](https://pkg.go.dev/builtin#string)

### func (*AddAssetsToGroupRequest) GetRequestId 
    
    
    func (x *AddAssetsToGroupRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*AddAssetsToGroupRequest) ProtoMessage 
    
    
    func (*AddAssetsToGroupRequest) ProtoMessage()

### func (*AddAssetsToGroupRequest) ProtoReflect 
    
    
    func (x *AddAssetsToGroupRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AddAssetsToGroupRequest) Reset 
    
    
    func (x *AddAssetsToGroupRequest) Reset()

### func (*AddAssetsToGroupRequest) String 
    
    
    func (x *AddAssetsToGroupRequest) String() [string](https://pkg.go.dev/builtin#string)

## AggregateAssetsValuesRequest
    
    
    type AggregateAssetsValuesRequest struct {
    
    	// Required. Parent value for `AggregateAssetsValuesRequest`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Array of aggregations to perform.
    	// Up to 25 aggregations can be defined.
    	Aggregations []*Aggregation `protobuf:"bytes,2,rep,name=aggregations,proto3" json:"aggregations,omitempty"`
    	// The aggregation will be performed on assets that match the provided filter.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=filter,proto3" json:"filter,omitempty"`
    	// contains filtered or unexported fields
    }

A request to aggregate one or more values.

### func (*AggregateAssetsValuesRequest) Descriptor 
    
    
    func (*AggregateAssetsValuesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AggregateAssetsValuesRequest.ProtoReflect.Descriptor instead.

### func (*AggregateAssetsValuesRequest) GetAggregations 
    
    
    func (x *AggregateAssetsValuesRequest) GetAggregations() []*Aggregation

### func (*AggregateAssetsValuesRequest) GetFilter 
    
    
    func (x *AggregateAssetsValuesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*AggregateAssetsValuesRequest) GetParent 
    
    
    func (x *AggregateAssetsValuesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*AggregateAssetsValuesRequest) ProtoMessage 
    
    
    func (*AggregateAssetsValuesRequest) ProtoMessage()

### func (*AggregateAssetsValuesRequest) ProtoReflect 
    
    
    func (x *AggregateAssetsValuesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AggregateAssetsValuesRequest) Reset 
    
    
    func (x *AggregateAssetsValuesRequest) Reset()

### func (*AggregateAssetsValuesRequest) String 
    
    
    func (x *AggregateAssetsValuesRequest) String() [string](https://pkg.go.dev/builtin#string)

## AggregateAssetsValuesResponse
    
    
    type AggregateAssetsValuesResponse struct {
    
    	// The aggregation results.
    	Results []*AggregationResult `protobuf:"bytes,1,rep,name=results,proto3" json:"results,omitempty"`
    	// contains filtered or unexported fields
    }

A response to a request to aggregated assets values.

### func (*AggregateAssetsValuesResponse) Descriptor 
    
    
    func (*AggregateAssetsValuesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AggregateAssetsValuesResponse.ProtoReflect.Descriptor instead.

### func (*AggregateAssetsValuesResponse) GetResults 
    
    
    func (x *AggregateAssetsValuesResponse) GetResults() []*AggregationResult

### func (*AggregateAssetsValuesResponse) ProtoMessage 
    
    
    func (*AggregateAssetsValuesResponse) ProtoMessage()

### func (*AggregateAssetsValuesResponse) ProtoReflect 
    
    
    func (x *AggregateAssetsValuesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AggregateAssetsValuesResponse) Reset 
    
    
    func (x *AggregateAssetsValuesResponse) Reset()

### func (*AggregateAssetsValuesResponse) String 
    
    
    func (x *AggregateAssetsValuesResponse) String() [string](https://pkg.go.dev/builtin#string)

## Aggregation
    
    
    type Aggregation struct {
    
    	// The name of the field on which to aggregate.
    	Field [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=field,proto3" json:"field,omitempty"`
    	// Types that are valid to be assigned to AggregationFunction:
    	//
    	//	*Aggregation_Count_
    	//	*Aggregation_Sum_
    	//	*Aggregation_Histogram_
    	//	*Aggregation_Frequency_
    	AggregationFunction isAggregation_AggregationFunction `protobuf_oneof:"aggregation_function"`
    	// contains filtered or unexported fields
    }

Message describing an aggregation. The message includes the aggregation type, parameters, and the field on which to perform the aggregation.

### func (*Aggregation) Descriptor 
    
    
    func (*Aggregation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Aggregation.ProtoReflect.Descriptor instead.

### func (*Aggregation) GetAggregationFunction 
    
    
    func (x *Aggregation) GetAggregationFunction() isAggregation_AggregationFunction

### func (*Aggregation) GetCount 
    
    
    func (x *Aggregation) GetCount() *Aggregation_Count

### func (*Aggregation) GetField 
    
    
    func (x *Aggregation) GetField() [string](https://pkg.go.dev/builtin#string)

### func (*Aggregation) GetFrequency 
    
    
    func (x *Aggregation) GetFrequency() *Aggregation_Frequency

### func (*Aggregation) GetHistogram 
    
    
    func (x *Aggregation) GetHistogram() *Aggregation_Histogram

### func (*Aggregation) GetSum 
    
    
    func (x *Aggregation) GetSum() *Aggregation_Sum

### func (*Aggregation) ProtoMessage 
    
    
    func (*Aggregation) ProtoMessage()

### func (*Aggregation) ProtoReflect 
    
    
    func (x *Aggregation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Aggregation) Reset 
    
    
    func (x *Aggregation) Reset()

### func (*Aggregation) String 
    
    
    func (x *Aggregation) String() [string](https://pkg.go.dev/builtin#string)

## AggregationResult
    
    
    type AggregationResult struct {
    	Field [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=field,proto3" json:"field,omitempty"`
    	// Types that are valid to be assigned to Result:
    	//
    	//	*AggregationResult_Count_
    	//	*AggregationResult_Sum_
    	//	*AggregationResult_Histogram_
    	//	*AggregationResult_Frequency_
    	Result isAggregationResult_Result `protobuf_oneof:"result"`
    	// contains filtered or unexported fields
    }

Message describing a result of an aggregation.

### func (*AggregationResult) Descriptor 
    
    
    func (*AggregationResult) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AggregationResult.ProtoReflect.Descriptor instead.

### func (*AggregationResult) GetCount 
    
    
    func (x *AggregationResult) GetCount() *AggregationResult_Count

### func (*AggregationResult) GetField 
    
    
    func (x *AggregationResult) GetField() [string](https://pkg.go.dev/builtin#string)

### func (*AggregationResult) GetFrequency 
    
    
    func (x *AggregationResult) GetFrequency() *AggregationResult_Frequency

### func (*AggregationResult) GetHistogram 
    
    
    func (x *AggregationResult) GetHistogram() *AggregationResult_Histogram

### func (*AggregationResult) GetResult 
    
    
    func (x *AggregationResult) GetResult() isAggregationResult_Result

### func (*AggregationResult) GetSum 
    
    
    func (x *AggregationResult) GetSum() *AggregationResult_Sum

### func (*AggregationResult) ProtoMessage 
    
    
    func (*AggregationResult) ProtoMessage()

### func (*AggregationResult) ProtoReflect 
    
    
    func (x *AggregationResult) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AggregationResult) Reset 
    
    
    func (x *AggregationResult) Reset()

### func (*AggregationResult) String 
    
    
    func (x *AggregationResult) String() [string](https://pkg.go.dev/builtin#string)

## AggregationResult_Count
    
    
    type AggregationResult_Count struct {
    	Value [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=value,proto3" json:"value,omitempty"`
    	// contains filtered or unexported fields
    }

The result of a count aggregation.

### func (*AggregationResult_Count) Descriptor 
    
    
    func (*AggregationResult_Count) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AggregationResult_Count.ProtoReflect.Descriptor instead.

### func (*AggregationResult_Count) GetValue 
    
    
    func (x *AggregationResult_Count) GetValue() [int64](https://pkg.go.dev/builtin#int64)

### func (*AggregationResult_Count) ProtoMessage 
    
    
    func (*AggregationResult_Count) ProtoMessage()

### func (*AggregationResult_Count) ProtoReflect 
    
    
    func (x *AggregationResult_Count) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AggregationResult_Count) Reset 
    
    
    func (x *AggregationResult_Count) Reset()

### func (*AggregationResult_Count) String 
    
    
    func (x *AggregationResult_Count) String() [string](https://pkg.go.dev/builtin#string)

## AggregationResult_Count_
    
    
    type AggregationResult_Count_ struct {
    	Count *AggregationResult_Count `protobuf:"bytes,2,opt,name=count,proto3,oneof"`
    }

## AggregationResult_Frequency
    
    
    type AggregationResult_Frequency struct {
    	Values map[[string](https://pkg.go.dev/builtin#string)][int64](https://pkg.go.dev/builtin#int64) `protobuf:"bytes,1,rep,name=values,proto3" json:"values,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"varint,2,opt,name=value"`
    	// contains filtered or unexported fields
    }

The result of a frequency distribution aggregation.

### func (*AggregationResult_Frequency) Descriptor 
    
    
    func (*AggregationResult_Frequency) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AggregationResult_Frequency.ProtoReflect.Descriptor instead.

### func (*AggregationResult_Frequency) GetValues 
    
    
    func (x *AggregationResult_Frequency) GetValues() map[[string](https://pkg.go.dev/builtin#string)][int64](https://pkg.go.dev/builtin#int64)

### func (*AggregationResult_Frequency) ProtoMessage 
    
    
    func (*AggregationResult_Frequency) ProtoMessage()

### func (*AggregationResult_Frequency) ProtoReflect 
    
    
    func (x *AggregationResult_Frequency) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AggregationResult_Frequency) Reset 
    
    
    func (x *AggregationResult_Frequency) Reset()

### func (*AggregationResult_Frequency) String 
    
    
    func (x *AggregationResult_Frequency) String() [string](https://pkg.go.dev/builtin#string)

## AggregationResult_Frequency_
    
    
    type AggregationResult_Frequency_ struct {
    	Frequency *AggregationResult_Frequency `protobuf:"bytes,5,opt,name=frequency,proto3,oneof"`
    }

## AggregationResult_Histogram
    
    
    type AggregationResult_Histogram struct {
    
    	// Buckets in the histogram.
    	// There will be `n+1` buckets matching `n` lower bounds in the request.
    	// The first bucket will be from -infinity to the first bound.
    	// Subsequent buckets will be between one bound and the next.
    	// The final bucket will be from the final bound to infinity.
    	Buckets []*AggregationResult_Histogram_Bucket `protobuf:"bytes,1,rep,name=buckets,proto3" json:"buckets,omitempty"`
    	// contains filtered or unexported fields
    }

The result of a bucketed histogram aggregation.

### func (*AggregationResult_Histogram) Descriptor 
    
    
    func (*AggregationResult_Histogram) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AggregationResult_Histogram.ProtoReflect.Descriptor instead.

### func (*AggregationResult_Histogram) GetBuckets 
    
    
    func (x *AggregationResult_Histogram) GetBuckets() []*AggregationResult_Histogram_Bucket

### func (*AggregationResult_Histogram) ProtoMessage 
    
    
    func (*AggregationResult_Histogram) ProtoMessage()

### func (*AggregationResult_Histogram) ProtoReflect 
    
    
    func (x *AggregationResult_Histogram) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AggregationResult_Histogram) Reset 
    
    
    func (x *AggregationResult_Histogram) Reset()

### func (*AggregationResult_Histogram) String 
    
    
    func (x *AggregationResult_Histogram) String() [string](https://pkg.go.dev/builtin#string)

## AggregationResult_Histogram_
    
    
    type AggregationResult_Histogram_ struct {
    	Histogram *AggregationResult_Histogram `protobuf:"bytes,4,opt,name=histogram,proto3,oneof"`
    }

## AggregationResult_Histogram_Bucket
    
    
    type AggregationResult_Histogram_Bucket struct {
    
    	// Lower bound - inclusive.
    	LowerBound [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=lower_bound,json=lowerBound,proto3" json:"lower_bound,omitempty"`
    	// Upper bound - exclusive.
    	UpperBound [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=upper_bound,json=upperBound,proto3" json:"upper_bound,omitempty"`
    	// Count of items in the bucket.
    	Count [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=count,proto3" json:"count,omitempty"`
    	// contains filtered or unexported fields
    }

A histogram bucket with a lower and upper bound, and a count of items with a field value between those bounds. The lower bound is inclusive and the upper bound is exclusive. Lower bound may be -infinity and upper bound may be infinity.

### func (*AggregationResult_Histogram_Bucket) Descriptor 
    
    
    func (*AggregationResult_Histogram_Bucket) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AggregationResult_Histogram_Bucket.ProtoReflect.Descriptor instead.

### func (*AggregationResult_Histogram_Bucket) GetCount 
    
    
    func (x *AggregationResult_Histogram_Bucket) GetCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*AggregationResult_Histogram_Bucket) GetLowerBound 
    
    
    func (x *AggregationResult_Histogram_Bucket) GetLowerBound() [float64](https://pkg.go.dev/builtin#float64)

### func (*AggregationResult_Histogram_Bucket) GetUpperBound 
    
    
    func (x *AggregationResult_Histogram_Bucket) GetUpperBound() [float64](https://pkg.go.dev/builtin#float64)

### func (*AggregationResult_Histogram_Bucket) ProtoMessage 
    
    
    func (*AggregationResult_Histogram_Bucket) ProtoMessage()

### func (*AggregationResult_Histogram_Bucket) ProtoReflect 
    
    
    func (x *AggregationResult_Histogram_Bucket) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AggregationResult_Histogram_Bucket) Reset 
    
    
    func (x *AggregationResult_Histogram_Bucket) Reset()

### func (*AggregationResult_Histogram_Bucket) String 
    
    
    func (x *AggregationResult_Histogram_Bucket) String() [string](https://pkg.go.dev/builtin#string)

## AggregationResult_Sum
    
    
    type AggregationResult_Sum struct {
    	Value [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=value,proto3" json:"value,omitempty"`
    	// contains filtered or unexported fields
    }

The result of a sum aggregation.

### func (*AggregationResult_Sum) Descriptor 
    
    
    func (*AggregationResult_Sum) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AggregationResult_Sum.ProtoReflect.Descriptor instead.

### func (*AggregationResult_Sum) GetValue 
    
    
    func (x *AggregationResult_Sum) GetValue() [float64](https://pkg.go.dev/builtin#float64)

### func (*AggregationResult_Sum) ProtoMessage 
    
    
    func (*AggregationResult_Sum) ProtoMessage()

### func (*AggregationResult_Sum) ProtoReflect 
    
    
    func (x *AggregationResult_Sum) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AggregationResult_Sum) Reset 
    
    
    func (x *AggregationResult_Sum) Reset()

### func (*AggregationResult_Sum) String 
    
    
    func (x *AggregationResult_Sum) String() [string](https://pkg.go.dev/builtin#string)

## AggregationResult_Sum_
    
    
    type AggregationResult_Sum_ struct {
    	Sum *AggregationResult_Sum `protobuf:"bytes,3,opt,name=sum,proto3,oneof"`
    }

## Aggregation_Count
    
    
    type Aggregation_Count struct {
    	// contains filtered or unexported fields
    }

Object count.

### func (*Aggregation_Count) Descriptor 
    
    
    func (*Aggregation_Count) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Aggregation_Count.ProtoReflect.Descriptor instead.

### func (*Aggregation_Count) ProtoMessage 
    
    
    func (*Aggregation_Count) ProtoMessage()

### func (*Aggregation_Count) ProtoReflect 
    
    
    func (x *Aggregation_Count) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Aggregation_Count) Reset 
    
    
    func (x *Aggregation_Count) Reset()

### func (*Aggregation_Count) String 
    
    
    func (x *Aggregation_Count) String() [string](https://pkg.go.dev/builtin#string)

## Aggregation_Count_
    
    
    type Aggregation_Count_ struct {
    	// Count the number of matching objects.
    	Count *Aggregation_Count `protobuf:"bytes,2,opt,name=count,proto3,oneof"`
    }

## Aggregation_Frequency
    
    
    type Aggregation_Frequency struct {
    	// contains filtered or unexported fields
    }

Frequency distribution of all field values.

### func (*Aggregation_Frequency) Descriptor 
    
    
    func (*Aggregation_Frequency) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Aggregation_Frequency.ProtoReflect.Descriptor instead.

### func (*Aggregation_Frequency) ProtoMessage 
    
    
    func (*Aggregation_Frequency) ProtoMessage()

### func (*Aggregation_Frequency) ProtoReflect 
    
    
    func (x *Aggregation_Frequency) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Aggregation_Frequency) Reset 
    
    
    func (x *Aggregation_Frequency) Reset()

### func (*Aggregation_Frequency) String 
    
    
    func (x *Aggregation_Frequency) String() [string](https://pkg.go.dev/builtin#string)

## Aggregation_Frequency_
    
    
    type Aggregation_Frequency_ struct {
    	// Creates a frequency distribution of all field values.
    	Frequency *Aggregation_Frequency `protobuf:"bytes,5,opt,name=frequency,proto3,oneof"`
    }

## Aggregation_Histogram
    
    
    type Aggregation_Histogram struct {
    
    	// Lower bounds of buckets.
    	// The response will contain `n+1` buckets for `n` bounds.
    	// The first bucket will count all assets for which the field value is
    	// smaller than the first bound.
    	// Subsequent buckets will count assets for which the field value is
    	// greater or equal to a lower bound and smaller than the next one.
    	// The last bucket will count assets for which the field value is greater or
    	// equal to the final lower bound.
    	// You can define up to 20 lower bounds.
    	LowerBounds [][float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,rep,packed,name=lower_bounds,json=lowerBounds,proto3" json:"lower_bounds,omitempty"`
    	// contains filtered or unexported fields
    }

Histogram of bucketed assets counts by field value.

### func (*Aggregation_Histogram) Descriptor 
    
    
    func (*Aggregation_Histogram) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Aggregation_Histogram.ProtoReflect.Descriptor instead.

### func (*Aggregation_Histogram) GetLowerBounds 
    
    
    func (x *Aggregation_Histogram) GetLowerBounds() [][float64](https://pkg.go.dev/builtin#float64)

### func (*Aggregation_Histogram) ProtoMessage 
    
    
    func (*Aggregation_Histogram) ProtoMessage()

### func (*Aggregation_Histogram) ProtoReflect 
    
    
    func (x *Aggregation_Histogram) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Aggregation_Histogram) Reset 
    
    
    func (x *Aggregation_Histogram) Reset()

### func (*Aggregation_Histogram) String 
    
    
    func (x *Aggregation_Histogram) String() [string](https://pkg.go.dev/builtin#string)

## Aggregation_Histogram_
    
    
    type Aggregation_Histogram_ struct {
    	// Creates a bucketed histogram of field values.
    	Histogram *Aggregation_Histogram `protobuf:"bytes,4,opt,name=histogram,proto3,oneof"`
    }

## Aggregation_Sum
    
    
    type Aggregation_Sum struct {
    	// contains filtered or unexported fields
    }

Sum of field values.

### func (*Aggregation_Sum) Descriptor 
    
    
    func (*Aggregation_Sum) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Aggregation_Sum.ProtoReflect.Descriptor instead.

### func (*Aggregation_Sum) ProtoMessage 
    
    
    func (*Aggregation_Sum) ProtoMessage()

### func (*Aggregation_Sum) ProtoReflect 
    
    
    func (x *Aggregation_Sum) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Aggregation_Sum) Reset 
    
    
    func (x *Aggregation_Sum) Reset()

### func (*Aggregation_Sum) String 
    
    
    func (x *Aggregation_Sum) String() [string](https://pkg.go.dev/builtin#string)

## Aggregation_Sum_
    
    
    type Aggregation_Sum_ struct {
    	// Sum over a numeric field.
    	Sum *Aggregation_Sum `protobuf:"bytes,3,opt,name=sum,proto3,oneof"`
    }

## Asset
    
    
    type Asset struct {
    
    	// Output only. The full name of the asset.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The timestamp when the asset was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The timestamp when the asset was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Labels as key value pairs.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Generic asset attributes.
    	Attributes map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,rep,name=attributes,proto3" json:"attributes,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// The internal information of an asset. Only one field can be specified
    	// with different attributes based on the type of the asset.
    	//
    	// Types that are valid to be assigned to AssetDetails:
    	//
    	//	*Asset_MachineDetails
    	AssetDetails isAsset_AssetDetails `protobuf_oneof:"AssetDetails"`
    	// Output only. The list of insights associated with the asset.
    	InsightList *InsightList `protobuf:"bytes,20,opt,name=insight_list,json=insightList,proto3" json:"insight_list,omitempty"`
    	// Output only. Performance data for the asset.
    	PerformanceData *AssetPerformanceData `protobuf:"bytes,21,opt,name=performance_data,json=performanceData,proto3" json:"performance_data,omitempty"`
    	// Output only. The list of sources contributing to the asset.
    	Sources [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,22,rep,name=sources,proto3" json:"sources,omitempty"`
    	// Output only. The list of groups that the asset is assigned to.
    	AssignedGroups [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,23,rep,name=assigned_groups,json=assignedGroups,proto3" json:"assigned_groups,omitempty"`
    	// contains filtered or unexported fields
    }

An asset represents a resource in your environment. Asset types include virtual machines and databases.

### func (*Asset) Descriptor 
    
    
    func (*Asset) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Asset.ProtoReflect.Descriptor instead.

### func (*Asset) GetAssetDetails 
    
    
    func (x *Asset) GetAssetDetails() isAsset_AssetDetails

### func (*Asset) GetAssignedGroups 
    
    
    func (x *Asset) GetAssignedGroups() [][string](https://pkg.go.dev/builtin#string)

### func (*Asset) GetAttributes 
    
    
    func (x *Asset) GetAttributes() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Asset) GetCreateTime 
    
    
    func (x *Asset) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Asset) GetInsightList 
    
    
    func (x *Asset) GetInsightList() *InsightList

### func (*Asset) GetLabels 
    
    
    func (x *Asset) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Asset) GetMachineDetails 
    
    
    func (x *Asset) GetMachineDetails() *MachineDetails

### func (*Asset) GetName 
    
    
    func (x *Asset) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Asset) GetPerformanceData 
    
    
    func (x *Asset) GetPerformanceData() *AssetPerformanceData

### func (*Asset) GetSources 
    
    
    func (x *Asset) GetSources() [][string](https://pkg.go.dev/builtin#string)

### func (*Asset) GetUpdateTime 
    
    
    func (x *Asset) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Asset) ProtoMessage 
    
    
    func (*Asset) ProtoMessage()

### func (*Asset) ProtoReflect 
    
    
    func (x *Asset) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Asset) Reset 
    
    
    func (x *Asset) Reset()

### func (*Asset) String 
    
    
    func (x *Asset) String() [string](https://pkg.go.dev/builtin#string)

## AssetFrame
    
    
    type AssetFrame struct {
    
    	// The internal data of the frame is a oneof field depending on the type
    	// of asset information in the frame.
    	//
    	// Types that are valid to be assigned to FrameData:
    	//
    	//	*AssetFrame_MachineDetails
    	FrameData isAssetFrame_FrameData `protobuf_oneof:"FrameData"`
    	// The time the data was reported.
    	ReportTime *timestamppb.Timestamp `protobuf:"bytes,10,opt,name=report_time,json=reportTime,proto3" json:"report_time,omitempty"`
    	// Labels as key value pairs.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Generic asset attributes.
    	Attributes map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,12,rep,name=attributes,proto3" json:"attributes,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Asset performance data samples.
    	// Samples that are from more than 40 days ago or after tomorrow are ignored.
    	PerformanceSamples []*PerformanceSample `protobuf:"bytes,13,rep,name=performance_samples,json=performanceSamples,proto3" json:"performance_samples,omitempty"`
    	// Optional. Trace token is optionally provided to assist with debugging and
    	// traceability.
    	TraceToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,14,opt,name=trace_token,json=traceToken,proto3" json:"trace_token,omitempty"`
    	// contains filtered or unexported fields
    }

Contains data reported from an inventory source on an asset.

### func (*AssetFrame) Descriptor 
    
    
    func (*AssetFrame) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AssetFrame.ProtoReflect.Descriptor instead.

### func (*AssetFrame) GetAttributes 
    
    
    func (x *AssetFrame) GetAttributes() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*AssetFrame) GetFrameData 
    
    
    func (x *AssetFrame) GetFrameData() isAssetFrame_FrameData

### func (*AssetFrame) GetLabels 
    
    
    func (x *AssetFrame) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*AssetFrame) GetMachineDetails 
    
    
    func (x *AssetFrame) GetMachineDetails() *MachineDetails

### func (*AssetFrame) GetPerformanceSamples 
    
    
    func (x *AssetFrame) GetPerformanceSamples() []*PerformanceSample

### func (*AssetFrame) GetReportTime 
    
    
    func (x *AssetFrame) GetReportTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*AssetFrame) GetTraceToken 
    
    
    func (x *AssetFrame) GetTraceToken() [string](https://pkg.go.dev/builtin#string)

### func (*AssetFrame) ProtoMessage 
    
    
    func (*AssetFrame) ProtoMessage()

### func (*AssetFrame) ProtoReflect 
    
    
    func (x *AssetFrame) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AssetFrame) Reset 
    
    
    func (x *AssetFrame) Reset()

### func (*AssetFrame) String 
    
    
    func (x *AssetFrame) String() [string](https://pkg.go.dev/builtin#string)

## AssetFrame_MachineDetails
    
    
    type AssetFrame_MachineDetails struct {
    	// Asset information specific for virtual machines.
    	MachineDetails *MachineDetails `protobuf:"bytes,1,opt,name=machine_details,json=machineDetails,proto3,oneof"`
    }

## AssetList
    
    
    type AssetList struct {
    
    	// Required. A list of asset IDs
    	AssetIds [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=asset_ids,json=assetIds,proto3" json:"asset_ids,omitempty"`
    	// contains filtered or unexported fields
    }

Lists the asset IDs of all assets.

### func (*AssetList) Descriptor 
    
    
    func (*AssetList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AssetList.ProtoReflect.Descriptor instead.

### func (*AssetList) GetAssetIds 
    
    
    func (x *AssetList) GetAssetIds() [][string](https://pkg.go.dev/builtin#string)

### func (*AssetList) ProtoMessage 
    
    
    func (*AssetList) ProtoMessage()

### func (*AssetList) ProtoReflect 
    
    
    func (x *AssetList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AssetList) Reset 
    
    
    func (x *AssetList) Reset()

### func (*AssetList) String 
    
    
    func (x *AssetList) String() [string](https://pkg.go.dev/builtin#string)

## AssetPerformanceData
    
    
    type AssetPerformanceData struct {
    
    	// Daily resource usage aggregations.
    	// Contains all of the data available for an asset, up to the last 420 days.
    	// Aggregations are sorted from oldest to most recent.
    	DailyResourceUsageAggregations []*DailyResourceUsageAggregation `protobuf:"bytes,1,rep,name=daily_resource_usage_aggregations,json=dailyResourceUsageAggregations,proto3" json:"daily_resource_usage_aggregations,omitempty"`
    	// contains filtered or unexported fields
    }

Performance data for an asset.

### func (*AssetPerformanceData) Descriptor 
    
    
    func (*AssetPerformanceData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AssetPerformanceData.ProtoReflect.Descriptor instead.

### func (*AssetPerformanceData) GetDailyResourceUsageAggregations 
    
    
    func (x *AssetPerformanceData) GetDailyResourceUsageAggregations() []*DailyResourceUsageAggregation

### func (*AssetPerformanceData) ProtoMessage 
    
    
    func (*AssetPerformanceData) ProtoMessage()

### func (*AssetPerformanceData) ProtoReflect 
    
    
    func (x *AssetPerformanceData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AssetPerformanceData) Reset 
    
    
    func (x *AssetPerformanceData) Reset()

### func (*AssetPerformanceData) String 
    
    
    func (x *AssetPerformanceData) String() [string](https://pkg.go.dev/builtin#string)

## AssetView
    
    
    type AssetView [int32](https://pkg.go.dev/builtin#int32)

Specifies the types of asset views that provide complete or partial details of an asset.

### AssetView_ASSET_VIEW_UNSPECIFIED, AssetView_ASSET_VIEW_BASIC, AssetView_ASSET_VIEW_FULL
    
    
    const (
    	// The asset view is not specified. The API displays the basic view by
    	// default.
    	AssetView_ASSET_VIEW_UNSPECIFIED AssetView = 0
    	// The asset view includes only basic metadata of the asset.
    	AssetView_ASSET_VIEW_BASIC AssetView = 1
    	// The asset view includes all the metadata of an asset and performance data.
    	AssetView_ASSET_VIEW_FULL AssetView = 2
    )

### func (AssetView) Descriptor 
    
    
    func (AssetView) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (AssetView) Enum 
    
    
    func (x AssetView) Enum() *AssetView

### func (AssetView) EnumDescriptor 
    
    
    func (AssetView) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AssetView.Descriptor instead.

### func (AssetView) Number 
    
    
    func (x AssetView) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (AssetView) String 
    
    
    func (x AssetView) String() [string](https://pkg.go.dev/builtin#string)

### func (AssetView) Type 
    
    
    func (AssetView) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Asset_MachineDetails
    
    
    type Asset_MachineDetails struct {
    	// Output only. Asset information specific for virtual and physical
    	// machines.
    	MachineDetails *MachineDetails `protobuf:"bytes,6,opt,name=machine_details,json=machineDetails,proto3,oneof"`
    }

## AwsEc2PlatformDetails
    
    
    type AwsEc2PlatformDetails struct {
    
    	// AWS platform's machine type label.
    	MachineTypeLabel [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=machine_type_label,json=machineTypeLabel,proto3" json:"machine_type_label,omitempty"`
    	// The location of the machine in the AWS format.
    	Location [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=location,proto3" json:"location,omitempty"`
    	// contains filtered or unexported fields
    }

AWS EC2 specific details.

### func (*AwsEc2PlatformDetails) Descriptor 
    
    
    func (*AwsEc2PlatformDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AwsEc2PlatformDetails.ProtoReflect.Descriptor instead.

### func (*AwsEc2PlatformDetails) GetLocation 
    
    
    func (x *AwsEc2PlatformDetails) GetLocation() [string](https://pkg.go.dev/builtin#string)

### func (*AwsEc2PlatformDetails) GetMachineTypeLabel 
    
    
    func (x *AwsEc2PlatformDetails) GetMachineTypeLabel() [string](https://pkg.go.dev/builtin#string)

### func (*AwsEc2PlatformDetails) ProtoMessage 
    
    
    func (*AwsEc2PlatformDetails) ProtoMessage()

### func (*AwsEc2PlatformDetails) ProtoReflect 
    
    
    func (x *AwsEc2PlatformDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AwsEc2PlatformDetails) Reset 
    
    
    func (x *AwsEc2PlatformDetails) Reset()

### func (*AwsEc2PlatformDetails) String 
    
    
    func (x *AwsEc2PlatformDetails) String() [string](https://pkg.go.dev/builtin#string)

## AzureVmPlatformDetails
    
    
    type AzureVmPlatformDetails struct {
    
    	// Azure platform's machine type label.
    	MachineTypeLabel [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=machine_type_label,json=machineTypeLabel,proto3" json:"machine_type_label,omitempty"`
    	// The location of the machine in the Azure format.
    	Location [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=location,proto3" json:"location,omitempty"`
    	// Azure platform's provisioning state.
    	ProvisioningState [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=provisioning_state,json=provisioningState,proto3" json:"provisioning_state,omitempty"`
    	// contains filtered or unexported fields
    }

Azure VM specific details.

### func (*AzureVmPlatformDetails) Descriptor 
    
    
    func (*AzureVmPlatformDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use AzureVmPlatformDetails.ProtoReflect.Descriptor instead.

### func (*AzureVmPlatformDetails) GetLocation 
    
    
    func (x *AzureVmPlatformDetails) GetLocation() [string](https://pkg.go.dev/builtin#string)

### func (*AzureVmPlatformDetails) GetMachineTypeLabel 
    
    
    func (x *AzureVmPlatformDetails) GetMachineTypeLabel() [string](https://pkg.go.dev/builtin#string)

### func (*AzureVmPlatformDetails) GetProvisioningState 
    
    
    func (x *AzureVmPlatformDetails) GetProvisioningState() [string](https://pkg.go.dev/builtin#string)

### func (*AzureVmPlatformDetails) ProtoMessage 
    
    
    func (*AzureVmPlatformDetails) ProtoMessage()

### func (*AzureVmPlatformDetails) ProtoReflect 
    
    
    func (x *AzureVmPlatformDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*AzureVmPlatformDetails) Reset 
    
    
    func (x *AzureVmPlatformDetails) Reset()

### func (*AzureVmPlatformDetails) String 
    
    
    func (x *AzureVmPlatformDetails) String() [string](https://pkg.go.dev/builtin#string)

## BatchDeleteAssetsRequest
    
    
    type BatchDeleteAssetsRequest struct {
    
    	// Required. Parent value for batch asset delete.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The IDs of the assets to delete.
    	// A maximum of 1000 assets can be deleted in a batch.
    	// Format: projects/{project}/locations/{location}/assets/{name}.
    	Names [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=names,proto3" json:"names,omitempty"`
    	// Optional. When this value is set to `true` the request is a no-op for
    	// non-existing assets. See https://google.aip.dev/135#delete-if-existing for
    	// additional details. Default value is `false`.
    	AllowMissing [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=allow_missing,json=allowMissing,proto3" json:"allow_missing,omitempty"`
    	// contains filtered or unexported fields
    }

A request to delete a list of asset.

### func (*BatchDeleteAssetsRequest) Descriptor 
    
    
    func (*BatchDeleteAssetsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BatchDeleteAssetsRequest.ProtoReflect.Descriptor instead.

### func (*BatchDeleteAssetsRequest) GetAllowMissing 
    
    
    func (x *BatchDeleteAssetsRequest) GetAllowMissing() [bool](https://pkg.go.dev/builtin#bool)

### func (*BatchDeleteAssetsRequest) GetNames 
    
    
    func (x *BatchDeleteAssetsRequest) GetNames() [][string](https://pkg.go.dev/builtin#string)

### func (*BatchDeleteAssetsRequest) GetParent 
    
    
    func (x *BatchDeleteAssetsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*BatchDeleteAssetsRequest) ProtoMessage 
    
    
    func (*BatchDeleteAssetsRequest) ProtoMessage()

### func (*BatchDeleteAssetsRequest) ProtoReflect 
    
    
    func (x *BatchDeleteAssetsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BatchDeleteAssetsRequest) Reset 
    
    
    func (x *BatchDeleteAssetsRequest) Reset()

### func (*BatchDeleteAssetsRequest) String 
    
    
    func (x *BatchDeleteAssetsRequest) String() [string](https://pkg.go.dev/builtin#string)

## BatchUpdateAssetsRequest
    
    
    type BatchUpdateAssetsRequest struct {
    
    	// Required. Parent value for batch asset update.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The request message specifying the resources to update.
    	// A maximum of 1000 assets can be modified in a batch.
    	Requests []*UpdateAssetRequest `protobuf:"bytes,2,rep,name=requests,proto3" json:"requests,omitempty"`
    	// contains filtered or unexported fields
    }

A request to update a list of assets.

### func (*BatchUpdateAssetsRequest) Descriptor 
    
    
    func (*BatchUpdateAssetsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BatchUpdateAssetsRequest.ProtoReflect.Descriptor instead.

### func (*BatchUpdateAssetsRequest) GetParent 
    
    
    func (x *BatchUpdateAssetsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*BatchUpdateAssetsRequest) GetRequests 
    
    
    func (x *BatchUpdateAssetsRequest) GetRequests() []*UpdateAssetRequest

### func (*BatchUpdateAssetsRequest) ProtoMessage 
    
    
    func (*BatchUpdateAssetsRequest) ProtoMessage()

### func (*BatchUpdateAssetsRequest) ProtoReflect 
    
    
    func (x *BatchUpdateAssetsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BatchUpdateAssetsRequest) Reset 
    
    
    func (x *BatchUpdateAssetsRequest) Reset()

### func (*BatchUpdateAssetsRequest) String 
    
    
    func (x *BatchUpdateAssetsRequest) String() [string](https://pkg.go.dev/builtin#string)

## BatchUpdateAssetsResponse
    
    
    type BatchUpdateAssetsResponse struct {
    
    	// Update asset content.
    	// The content only includes values after field mask being applied.
    	Assets []*Asset `protobuf:"bytes,1,rep,name=assets,proto3" json:"assets,omitempty"`
    	// contains filtered or unexported fields
    }

Response for updating a list of assets.

### func (*BatchUpdateAssetsResponse) Descriptor 
    
    
    func (*BatchUpdateAssetsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BatchUpdateAssetsResponse.ProtoReflect.Descriptor instead.

### func (*BatchUpdateAssetsResponse) GetAssets 
    
    
    func (x *BatchUpdateAssetsResponse) GetAssets() []*Asset

### func (*BatchUpdateAssetsResponse) ProtoMessage 
    
    
    func (*BatchUpdateAssetsResponse) ProtoMessage()

### func (*BatchUpdateAssetsResponse) ProtoReflect 
    
    
    func (x *BatchUpdateAssetsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BatchUpdateAssetsResponse) Reset 
    
    
    func (x *BatchUpdateAssetsResponse) Reset()

### func (*BatchUpdateAssetsResponse) String 
    
    
    func (x *BatchUpdateAssetsResponse) String() [string](https://pkg.go.dev/builtin#string)

## BiosDetails
    
    
    type BiosDetails struct {
    
    	// BIOS name.
    	// This fields is deprecated. Please use the `id` field instead.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/migrationcenter/v1/migrationcenter.proto.
    	BiosName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=bios_name,json=biosName,proto3" json:"bios_name,omitempty"`
    	// BIOS ID.
    	Id [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=id,proto3" json:"id,omitempty"`
    	// BIOS manufacturer.
    	Manufacturer [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=manufacturer,proto3" json:"manufacturer,omitempty"`
    	// BIOS version.
    	Version [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=version,proto3" json:"version,omitempty"`
    	// BIOS release date.
    	ReleaseDate *date.Date `protobuf:"bytes,5,opt,name=release_date,json=releaseDate,proto3" json:"release_date,omitempty"`
    	// SMBIOS UUID.
    	SmbiosUuid [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=smbios_uuid,json=smbiosUuid,proto3" json:"smbios_uuid,omitempty"`
    	// contains filtered or unexported fields
    }

Details about the BIOS.

### func (*BiosDetails) Descriptor 
    
    
    func (*BiosDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use BiosDetails.ProtoReflect.Descriptor instead.

### func (*BiosDetails) GetBiosName 
    
    
    func (x *BiosDetails) GetBiosName() [string](https://pkg.go.dev/builtin#string)

Deprecated: Marked as deprecated in google/cloud/migrationcenter/v1/migrationcenter.proto.

### func (*BiosDetails) GetId 
    
    
    func (x *BiosDetails) GetId() [string](https://pkg.go.dev/builtin#string)

### func (*BiosDetails) GetManufacturer 
    
    
    func (x *BiosDetails) GetManufacturer() [string](https://pkg.go.dev/builtin#string)

### func (*BiosDetails) GetReleaseDate 
    
    
    func (x *BiosDetails) GetReleaseDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*BiosDetails) GetSmbiosUuid 
    
    
    func (x *BiosDetails) GetSmbiosUuid() [string](https://pkg.go.dev/builtin#string)

### func (*BiosDetails) GetVersion 
    
    
    func (x *BiosDetails) GetVersion() [string](https://pkg.go.dev/builtin#string)

### func (*BiosDetails) ProtoMessage 
    
    
    func (*BiosDetails) ProtoMessage()

### func (*BiosDetails) ProtoReflect 
    
    
    func (x *BiosDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*BiosDetails) Reset 
    
    
    func (x *BiosDetails) Reset()

### func (*BiosDetails) String 
    
    
    func (x *BiosDetails) String() [string](https://pkg.go.dev/builtin#string)

## CommitmentPlan
    
    
    type CommitmentPlan [int32](https://pkg.go.dev/builtin#int32)

The plan of commitments for VM resource-based committed use discount (CUD).

### CommitmentPlan_COMMITMENT_PLAN_UNSPECIFIED, CommitmentPlan_COMMITMENT_PLAN_NONE, CommitmentPlan_COMMITMENT_PLAN_ONE_YEAR, CommitmentPlan_COMMITMENT_PLAN_THREE_YEARS
    
    
    const (
    	// Unspecified commitment plan.
    	CommitmentPlan_COMMITMENT_PLAN_UNSPECIFIED CommitmentPlan = 0
    	// No commitment plan.
    	CommitmentPlan_COMMITMENT_PLAN_NONE CommitmentPlan = 1
    	// 1 year commitment.
    	CommitmentPlan_COMMITMENT_PLAN_ONE_YEAR CommitmentPlan = 2
    	// 3 years commitment.
    	CommitmentPlan_COMMITMENT_PLAN_THREE_YEARS CommitmentPlan = 3
    )

### func (CommitmentPlan) Descriptor 
    
    
    func (CommitmentPlan) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (CommitmentPlan) Enum 
    
    
    func (x CommitmentPlan) Enum() *CommitmentPlan

### func (CommitmentPlan) EnumDescriptor 
    
    
    func (CommitmentPlan) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CommitmentPlan.Descriptor instead.

### func (CommitmentPlan) Number 
    
    
    func (x CommitmentPlan) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (CommitmentPlan) String 
    
    
    func (x CommitmentPlan) String() [string](https://pkg.go.dev/builtin#string)

### func (CommitmentPlan) Type 
    
    
    func (CommitmentPlan) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ComputeEngineMigrationTarget
    
    
    type ComputeEngineMigrationTarget struct {
    
    	// Description of the suggested shape for the migration target.
    	Shape *ComputeEngineShapeDescriptor `protobuf:"bytes,1,opt,name=shape,proto3" json:"shape,omitempty"`
    	// contains filtered or unexported fields
    }

Compute engine migration target.

### func (*ComputeEngineMigrationTarget) Descriptor 
    
    
    func (*ComputeEngineMigrationTarget) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ComputeEngineMigrationTarget.ProtoReflect.Descriptor instead.

### func (*ComputeEngineMigrationTarget) GetShape 
    
    
    func (x *ComputeEngineMigrationTarget) GetShape() *ComputeEngineShapeDescriptor

### func (*ComputeEngineMigrationTarget) ProtoMessage 
    
    
    func (*ComputeEngineMigrationTarget) ProtoMessage()

### func (*ComputeEngineMigrationTarget) ProtoReflect 
    
    
    func (x *ComputeEngineMigrationTarget) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ComputeEngineMigrationTarget) Reset 
    
    
    func (x *ComputeEngineMigrationTarget) Reset()

### func (*ComputeEngineMigrationTarget) String 
    
    
    func (x *ComputeEngineMigrationTarget) String() [string](https://pkg.go.dev/builtin#string)

## ComputeEnginePreferences
    
    
    type ComputeEnginePreferences struct {
    
    	// Preferences concerning the machine types to consider on Compute Engine.
    	MachinePreferences *MachinePreferences `protobuf:"bytes,2,opt,name=machine_preferences,json=machinePreferences,proto3" json:"machine_preferences,omitempty"`
    	// License type to consider when calculating costs for virtual machine
    	// insights and recommendations. If unspecified, costs are calculated
    	// based on the default licensing plan.
    	LicenseType LicenseType `protobuf:"varint,3,opt,name=license_type,json=licenseType,proto3,enum=google.cloud.migrationcenter.v1.LicenseType" json:"license_type,omitempty"`
    	// contains filtered or unexported fields
    }

The user preferences relating to Compute Engine target platform.

### func (*ComputeEnginePreferences) Descriptor 
    
    
    func (*ComputeEnginePreferences) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ComputeEnginePreferences.ProtoReflect.Descriptor instead.

### func (*ComputeEnginePreferences) GetLicenseType 
    
    
    func (x *ComputeEnginePreferences) GetLicenseType() LicenseType

### func (*ComputeEnginePreferences) GetMachinePreferences 
    
    
    func (x *ComputeEnginePreferences) GetMachinePreferences() *MachinePreferences

### func (*ComputeEnginePreferences) ProtoMessage 
    
    
    func (*ComputeEnginePreferences) ProtoMessage()

### func (*ComputeEnginePreferences) ProtoReflect 
    
    
    func (x *ComputeEnginePreferences) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ComputeEnginePreferences) Reset 
    
    
    func (x *ComputeEnginePreferences) Reset()

### func (*ComputeEnginePreferences) String 
    
    
    func (x *ComputeEnginePreferences) String() [string](https://pkg.go.dev/builtin#string)

## ComputeEngineShapeDescriptor
    
    
    type ComputeEngineShapeDescriptor struct {
    
    	// Memory in mebibytes.
    	MemoryMb [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=memory_mb,json=memoryMb,proto3" json:"memory_mb,omitempty"`
    	// Number of physical cores.
    	PhysicalCoreCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=physical_core_count,json=physicalCoreCount,proto3" json:"physical_core_count,omitempty"`
    	// Number of logical cores.
    	LogicalCoreCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=logical_core_count,json=logicalCoreCount,proto3" json:"logical_core_count,omitempty"`
    	// Compute Engine machine series.
    	Series [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=series,proto3" json:"series,omitempty"`
    	// Compute Engine machine type.
    	MachineType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=machine_type,json=machineType,proto3" json:"machine_type,omitempty"`
    	// Compute Engine storage. Never empty.
    	Storage []*ComputeStorageDescriptor `protobuf:"bytes,6,rep,name=storage,proto3" json:"storage,omitempty"`
    	// contains filtered or unexported fields
    }

Compute Engine target shape descriptor.

### func (*ComputeEngineShapeDescriptor) Descriptor 
    
    
    func (*ComputeEngineShapeDescriptor) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ComputeEngineShapeDescriptor.ProtoReflect.Descriptor instead.

### func (*ComputeEngineShapeDescriptor) GetLogicalCoreCount 
    
    
    func (x *ComputeEngineShapeDescriptor) GetLogicalCoreCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*ComputeEngineShapeDescriptor) GetMachineType 
    
    
    func (x *ComputeEngineShapeDescriptor) GetMachineType() [string](https://pkg.go.dev/builtin#string)

### func (*ComputeEngineShapeDescriptor) GetMemoryMb 
    
    
    func (x *ComputeEngineShapeDescriptor) GetMemoryMb() [int32](https://pkg.go.dev/builtin#int32)

### func (*ComputeEngineShapeDescriptor) GetPhysicalCoreCount 
    
    
    func (x *ComputeEngineShapeDescriptor) GetPhysicalCoreCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*ComputeEngineShapeDescriptor) GetSeries 
    
    
    func (x *ComputeEngineShapeDescriptor) GetSeries() [string](https://pkg.go.dev/builtin#string)

### func (*ComputeEngineShapeDescriptor) GetStorage 
    
    
    func (x *ComputeEngineShapeDescriptor) GetStorage() []*ComputeStorageDescriptor

### func (*ComputeEngineShapeDescriptor) ProtoMessage 
    
    
    func (*ComputeEngineShapeDescriptor) ProtoMessage()

### func (*ComputeEngineShapeDescriptor) ProtoReflect 
    
    
    func (x *ComputeEngineShapeDescriptor) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ComputeEngineShapeDescriptor) Reset 
    
    
    func (x *ComputeEngineShapeDescriptor) Reset()

### func (*ComputeEngineShapeDescriptor) String 
    
    
    func (x *ComputeEngineShapeDescriptor) String() [string](https://pkg.go.dev/builtin#string)

## ComputeMigrationTargetProduct
    
    
    type ComputeMigrationTargetProduct [int32](https://pkg.go.dev/builtin#int32)

The preference for a specific Google Cloud product platform.

### ComputeMigrationTargetProduct_COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED, ComputeMigrationTargetProduct_COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE, ComputeMigrationTargetProduct_COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE, ComputeMigrationTargetProduct_COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY
    
    
    const (
    	// Unspecified (default value).
    	ComputeMigrationTargetProduct_COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED ComputeMigrationTargetProduct = 0
    	// Prefer to migrate to Google Cloud Compute Engine.
    	ComputeMigrationTargetProduct_COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE ComputeMigrationTargetProduct = 1
    	// Prefer to migrate to Google Cloud VMware Engine.
    	ComputeMigrationTargetProduct_COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE ComputeMigrationTargetProduct = 2
    	// Prefer to migrate to Google Cloud Sole Tenant Nodes.
    	ComputeMigrationTargetProduct_COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY ComputeMigrationTargetProduct = 3
    )

### func (ComputeMigrationTargetProduct) Descriptor 
    
    
    func (ComputeMigrationTargetProduct) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ComputeMigrationTargetProduct) Enum 
    
    
    func (x ComputeMigrationTargetProduct) Enum() *ComputeMigrationTargetProduct

### func (ComputeMigrationTargetProduct) EnumDescriptor 
    
    
    func (ComputeMigrationTargetProduct) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ComputeMigrationTargetProduct.Descriptor instead.

### func (ComputeMigrationTargetProduct) Number 
    
    
    func (x ComputeMigrationTargetProduct) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ComputeMigrationTargetProduct) String 
    
    
    func (x ComputeMigrationTargetProduct) String() [string](https://pkg.go.dev/builtin#string)

### func (ComputeMigrationTargetProduct) Type 
    
    
    func (ComputeMigrationTargetProduct) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ComputeStorageDescriptor
    
    
    type ComputeStorageDescriptor struct {
    
    	// Disk type backing the storage.
    	Type PersistentDiskType `protobuf:"varint,1,opt,name=type,proto3,enum=google.cloud.migrationcenter.v1.PersistentDiskType" json:"type,omitempty"`
    	// Disk size in GiB.
    	SizeGb [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=size_gb,json=sizeGb,proto3" json:"size_gb,omitempty"`
    	// contains filtered or unexported fields
    }

Compute Engine storage option descriptor.

### func (*ComputeStorageDescriptor) Descriptor 
    
    
    func (*ComputeStorageDescriptor) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ComputeStorageDescriptor.ProtoReflect.Descriptor instead.

### func (*ComputeStorageDescriptor) GetSizeGb 
    
    
    func (x *ComputeStorageDescriptor) GetSizeGb() [int32](https://pkg.go.dev/builtin#int32)

### func (*ComputeStorageDescriptor) GetType 
    
    
    func (x *ComputeStorageDescriptor) GetType() PersistentDiskType

### func (*ComputeStorageDescriptor) ProtoMessage 
    
    
    func (*ComputeStorageDescriptor) ProtoMessage()

### func (*ComputeStorageDescriptor) ProtoReflect 
    
    
    func (x *ComputeStorageDescriptor) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ComputeStorageDescriptor) Reset 
    
    
    func (x *ComputeStorageDescriptor) Reset()

### func (*ComputeStorageDescriptor) String 
    
    
    func (x *ComputeStorageDescriptor) String() [string](https://pkg.go.dev/builtin#string)

## CpuUsageSample
    
    
    type CpuUsageSample struct {
    
    	// Percentage of total CPU capacity utilized. Must be in the interval [0,
    	// 100]. On most systems can be calculated using 100 - idle percentage.
    	UtilizedPercentage [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,opt,name=utilized_percentage,json=utilizedPercentage,proto3" json:"utilized_percentage,omitempty"`
    	// contains filtered or unexported fields
    }

CPU usage sample.

### func (*CpuUsageSample) Descriptor 
    
    
    func (*CpuUsageSample) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CpuUsageSample.ProtoReflect.Descriptor instead.

### func (*CpuUsageSample) GetUtilizedPercentage 
    
    
    func (x *CpuUsageSample) GetUtilizedPercentage() [float32](https://pkg.go.dev/builtin#float32)

### func (*CpuUsageSample) ProtoMessage 
    
    
    func (*CpuUsageSample) ProtoMessage()

### func (*CpuUsageSample) ProtoReflect 
    
    
    func (x *CpuUsageSample) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CpuUsageSample) Reset 
    
    
    func (x *CpuUsageSample) Reset()

### func (*CpuUsageSample) String 
    
    
    func (x *CpuUsageSample) String() [string](https://pkg.go.dev/builtin#string)

## CreateGroupRequest
    
    
    type CreateGroupRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. User specified ID for the group. It will become the last
    	// component of the group name. The ID must be unique within the project, must
    	// conform with RFC-1034, is restricted to lower-cased letters, and has a
    	// maximum length of 63 characters. The ID must match the regular expression:
    	// `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.
    	GroupId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=group_id,json=groupId,proto3" json:"group_id,omitempty"`
    	// Required. The group resource being created.
    	Group *Group `protobuf:"bytes,3,opt,name=group,proto3" json:"group,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to create a group.

### func (*CreateGroupRequest) Descriptor 
    
    
    func (*CreateGroupRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateGroupRequest.ProtoReflect.Descriptor instead.

### func (*CreateGroupRequest) GetGroup 
    
    
    func (x *CreateGroupRequest) GetGroup() *Group

### func (*CreateGroupRequest) GetGroupId 
    
    
    func (x *CreateGroupRequest) GetGroupId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateGroupRequest) GetParent 
    
    
    func (x *CreateGroupRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateGroupRequest) GetRequestId 
    
    
    func (x *CreateGroupRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateGroupRequest) ProtoMessage 
    
    
    func (*CreateGroupRequest) ProtoMessage()

### func (*CreateGroupRequest) ProtoReflect 
    
    
    func (x *CreateGroupRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateGroupRequest) Reset 
    
    
    func (x *CreateGroupRequest) Reset()

### func (*CreateGroupRequest) String 
    
    
    func (x *CreateGroupRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateImportDataFileRequest
    
    
    type CreateImportDataFileRequest struct {
    
    	// Required. Name of the parent of the ImportDataFile.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The ID of the new data file.
    	ImportDataFileId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=import_data_file_id,json=importDataFileId,proto3" json:"import_data_file_id,omitempty"`
    	// Required. The resource being created.
    	ImportDataFile *ImportDataFile `protobuf:"bytes,3,opt,name=import_data_file,json=importDataFile,proto3" json:"import_data_file,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to create an `ImportDataFile` resource.

### func (*CreateImportDataFileRequest) Descriptor 
    
    
    func (*CreateImportDataFileRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateImportDataFileRequest.ProtoReflect.Descriptor instead.

### func (*CreateImportDataFileRequest) GetImportDataFile 
    
    
    func (x *CreateImportDataFileRequest) GetImportDataFile() *ImportDataFile

### func (*CreateImportDataFileRequest) GetImportDataFileId 
    
    
    func (x *CreateImportDataFileRequest) GetImportDataFileId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateImportDataFileRequest) GetParent 
    
    
    func (x *CreateImportDataFileRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateImportDataFileRequest) GetRequestId 
    
    
    func (x *CreateImportDataFileRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateImportDataFileRequest) ProtoMessage 
    
    
    func (*CreateImportDataFileRequest) ProtoMessage()

### func (*CreateImportDataFileRequest) ProtoReflect 
    
    
    func (x *CreateImportDataFileRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateImportDataFileRequest) Reset 
    
    
    func (x *CreateImportDataFileRequest) Reset()

### func (*CreateImportDataFileRequest) String 
    
    
    func (x *CreateImportDataFileRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateImportJobRequest
    
    
    type CreateImportJobRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. ID of the import job.
    	ImportJobId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=import_job_id,json=importJobId,proto3" json:"import_job_id,omitempty"`
    	// Required. The resource being created.
    	ImportJob *ImportJob `protobuf:"bytes,3,opt,name=import_job,json=importJob,proto3" json:"import_job,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to create an import job.

### func (*CreateImportJobRequest) Descriptor 
    
    
    func (*CreateImportJobRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateImportJobRequest.ProtoReflect.Descriptor instead.

### func (*CreateImportJobRequest) GetImportJob 
    
    
    func (x *CreateImportJobRequest) GetImportJob() *ImportJob

### func (*CreateImportJobRequest) GetImportJobId 
    
    
    func (x *CreateImportJobRequest) GetImportJobId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateImportJobRequest) GetParent 
    
    
    func (x *CreateImportJobRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateImportJobRequest) GetRequestId 
    
    
    func (x *CreateImportJobRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateImportJobRequest) ProtoMessage 
    
    
    func (*CreateImportJobRequest) ProtoMessage()

### func (*CreateImportJobRequest) ProtoReflect 
    
    
    func (x *CreateImportJobRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateImportJobRequest) Reset 
    
    
    func (x *CreateImportJobRequest) Reset()

### func (*CreateImportJobRequest) String 
    
    
    func (x *CreateImportJobRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreatePreferenceSetRequest
    
    
    type CreatePreferenceSetRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. User specified ID for the preference set. It will become the last
    	// component of the preference set name. The ID must be unique within the
    	// project, must conform with RFC-1034, is restricted to lower-cased letters,
    	// and has a maximum length of 63 characters. The ID must match the regular
    	// expression
    	// `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.
    	PreferenceSetId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=preference_set_id,json=preferenceSetId,proto3" json:"preference_set_id,omitempty"`
    	// Required. The preference set resource being created.
    	PreferenceSet *PreferenceSet `protobuf:"bytes,3,opt,name=preference_set,json=preferenceSet,proto3" json:"preference_set,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to create a preference set.

### func (*CreatePreferenceSetRequest) Descriptor 
    
    
    func (*CreatePreferenceSetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreatePreferenceSetRequest.ProtoReflect.Descriptor instead.

### func (*CreatePreferenceSetRequest) GetParent 
    
    
    func (x *CreatePreferenceSetRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreatePreferenceSetRequest) GetPreferenceSet 
    
    
    func (x *CreatePreferenceSetRequest) GetPreferenceSet() *PreferenceSet

### func (*CreatePreferenceSetRequest) GetPreferenceSetId 
    
    
    func (x *CreatePreferenceSetRequest) GetPreferenceSetId() [string](https://pkg.go.dev/builtin#string)

### func (*CreatePreferenceSetRequest) GetRequestId 
    
    
    func (x *CreatePreferenceSetRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreatePreferenceSetRequest) ProtoMessage 
    
    
    func (*CreatePreferenceSetRequest) ProtoMessage()

### func (*CreatePreferenceSetRequest) ProtoReflect 
    
    
    func (x *CreatePreferenceSetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreatePreferenceSetRequest) Reset 
    
    
    func (x *CreatePreferenceSetRequest) Reset()

### func (*CreatePreferenceSetRequest) String 
    
    
    func (x *CreatePreferenceSetRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateReportConfigRequest
    
    
    type CreateReportConfigRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. User specified ID for the report config. It will become the last
    	// component of the report config name. The ID must be unique within the
    	// project, must conform with RFC-1034, is restricted to lower-cased letters,
    	// and has a maximum length of 63 characters. The ID must match the regular
    	// expression: [a-z]([a-z0-9-]{0,61}[a-z0-9])?.
    	ReportConfigId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=report_config_id,json=reportConfigId,proto3" json:"report_config_id,omitempty"`
    	// Required. The report config set resource being created.
    	ReportConfig *ReportConfig `protobuf:"bytes,3,opt,name=report_config,json=reportConfig,proto3" json:"report_config,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to create a `ReportConfig` resource.

### func (*CreateReportConfigRequest) Descriptor 
    
    
    func (*CreateReportConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateReportConfigRequest.ProtoReflect.Descriptor instead.

### func (*CreateReportConfigRequest) GetParent 
    
    
    func (x *CreateReportConfigRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReportConfigRequest) GetReportConfig 
    
    
    func (x *CreateReportConfigRequest) GetReportConfig() *ReportConfig

### func (*CreateReportConfigRequest) GetReportConfigId 
    
    
    func (x *CreateReportConfigRequest) GetReportConfigId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReportConfigRequest) GetRequestId 
    
    
    func (x *CreateReportConfigRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReportConfigRequest) ProtoMessage 
    
    
    func (*CreateReportConfigRequest) ProtoMessage()

### func (*CreateReportConfigRequest) ProtoReflect 
    
    
    func (x *CreateReportConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateReportConfigRequest) Reset 
    
    
    func (x *CreateReportConfigRequest) Reset()

### func (*CreateReportConfigRequest) String 
    
    
    func (x *CreateReportConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateReportRequest
    
    
    type CreateReportRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. User specified id for the report. It will become the last
    	// component of the report name. The id must be unique within the project,
    	// must conform with RFC-1034, is restricted to lower-cased letters, and has a
    	// maximum length of 63 characters. The id must match the regular expression:
    	// [a-z]([a-z0-9-]{0,61}[a-z0-9])?.
    	ReportId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=report_id,json=reportId,proto3" json:"report_id,omitempty"`
    	// Required. The report resource being created.
    	Report *Report `protobuf:"bytes,3,opt,name=report,proto3" json:"report,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

Message for creating a Report.

### func (*CreateReportRequest) Descriptor 
    
    
    func (*CreateReportRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateReportRequest.ProtoReflect.Descriptor instead.

### func (*CreateReportRequest) GetParent 
    
    
    func (x *CreateReportRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReportRequest) GetReport 
    
    
    func (x *CreateReportRequest) GetReport() *Report

### func (*CreateReportRequest) GetReportId 
    
    
    func (x *CreateReportRequest) GetReportId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReportRequest) GetRequestId 
    
    
    func (x *CreateReportRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateReportRequest) ProtoMessage 
    
    
    func (*CreateReportRequest) ProtoMessage()

### func (*CreateReportRequest) ProtoReflect 
    
    
    func (x *CreateReportRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateReportRequest) Reset 
    
    
    func (x *CreateReportRequest) Reset()

### func (*CreateReportRequest) String 
    
    
    func (x *CreateReportRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateSourceRequest
    
    
    type CreateSourceRequest struct {
    
    	// Required. Value for parent.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. User specified ID for the source. It will become the last
    	// component of the source name. The ID must be unique within the project,
    	// must conform with RFC-1034, is restricted to lower-cased letters, and has a
    	// maximum length of 63 characters. The ID must match the regular expression:
    	// `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.
    	SourceId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=source_id,json=sourceId,proto3" json:"source_id,omitempty"`
    	// Required. The resource being created.
    	Source *Source `protobuf:"bytes,3,opt,name=source,proto3" json:"source,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to create a source.

### func (*CreateSourceRequest) Descriptor 
    
    
    func (*CreateSourceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateSourceRequest.ProtoReflect.Descriptor instead.

### func (*CreateSourceRequest) GetParent 
    
    
    func (x *CreateSourceRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateSourceRequest) GetRequestId 
    
    
    func (x *CreateSourceRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateSourceRequest) GetSource 
    
    
    func (x *CreateSourceRequest) GetSource() *Source

### func (*CreateSourceRequest) GetSourceId 
    
    
    func (x *CreateSourceRequest) GetSourceId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateSourceRequest) ProtoMessage 
    
    
    func (*CreateSourceRequest) ProtoMessage()

### func (*CreateSourceRequest) ProtoReflect 
    
    
    func (x *CreateSourceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateSourceRequest) Reset 
    
    
    func (x *CreateSourceRequest) Reset()

### func (*CreateSourceRequest) String 
    
    
    func (x *CreateSourceRequest) String() [string](https://pkg.go.dev/builtin#string)

## DailyResourceUsageAggregation
    
    
    type DailyResourceUsageAggregation struct {
    
    	// Aggregation date. Day boundaries are at midnight UTC.
    	Date *date.Date `protobuf:"bytes,1,opt,name=date,proto3" json:"date,omitempty"`
    	// CPU usage.
    	Cpu *DailyResourceUsageAggregation_CPU `protobuf:"bytes,2,opt,name=cpu,proto3" json:"cpu,omitempty"`
    	// Memory usage.
    	Memory *DailyResourceUsageAggregation_Memory `protobuf:"bytes,3,opt,name=memory,proto3" json:"memory,omitempty"`
    	// Network usage.
    	Network *DailyResourceUsageAggregation_Network `protobuf:"bytes,4,opt,name=network,proto3" json:"network,omitempty"`
    	// Disk usage.
    	Disk *DailyResourceUsageAggregation_Disk `protobuf:"bytes,5,opt,name=disk,proto3" json:"disk,omitempty"`
    	// contains filtered or unexported fields
    }

Usage data aggregation for a single day.

### func (*DailyResourceUsageAggregation) Descriptor 
    
    
    func (*DailyResourceUsageAggregation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DailyResourceUsageAggregation.ProtoReflect.Descriptor instead.

### func (*DailyResourceUsageAggregation) GetCpu 
    
    
    func (x *DailyResourceUsageAggregation) GetCpu() *DailyResourceUsageAggregation_CPU

### func (*DailyResourceUsageAggregation) GetDate 
    
    
    func (x *DailyResourceUsageAggregation) GetDate() *[date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date).[Date](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/date#Date)

### func (*DailyResourceUsageAggregation) GetDisk 
    
    
    func (x *DailyResourceUsageAggregation) GetDisk() *DailyResourceUsageAggregation_Disk

### func (*DailyResourceUsageAggregation) GetMemory 
    
    
    func (x *DailyResourceUsageAggregation) GetMemory() *DailyResourceUsageAggregation_Memory

### func (*DailyResourceUsageAggregation) GetNetwork 
    
    
    func (x *DailyResourceUsageAggregation) GetNetwork() *DailyResourceUsageAggregation_Network

### func (*DailyResourceUsageAggregation) ProtoMessage 
    
    
    func (*DailyResourceUsageAggregation) ProtoMessage()

### func (*DailyResourceUsageAggregation) ProtoReflect 
    
    
    func (x *DailyResourceUsageAggregation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DailyResourceUsageAggregation) Reset 
    
    
    func (x *DailyResourceUsageAggregation) Reset()

### func (*DailyResourceUsageAggregation) String 
    
    
    func (x *DailyResourceUsageAggregation) String() [string](https://pkg.go.dev/builtin#string)

## DailyResourceUsageAggregation_CPU
    
    
    type DailyResourceUsageAggregation_CPU struct {
    
    	// CPU utilization percentage.
    	UtilizationPercentage *DailyResourceUsageAggregation_Stats `protobuf:"bytes,1,opt,name=utilization_percentage,json=utilizationPercentage,proto3" json:"utilization_percentage,omitempty"`
    	// contains filtered or unexported fields
    }

Statistical aggregation of CPU usage.

### func (*DailyResourceUsageAggregation_CPU) Descriptor 
    
    
    func (*DailyResourceUsageAggregation_CPU) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DailyResourceUsageAggregation_CPU.ProtoReflect.Descriptor instead.

### func (*DailyResourceUsageAggregation_CPU) GetUtilizationPercentage 
    
    
    func (x *DailyResourceUsageAggregation_CPU) GetUtilizationPercentage() *DailyResourceUsageAggregation_Stats

### func (*DailyResourceUsageAggregation_CPU) ProtoMessage 
    
    
    func (*DailyResourceUsageAggregation_CPU) ProtoMessage()

### func (*DailyResourceUsageAggregation_CPU) ProtoReflect 
    
    
    func (x *DailyResourceUsageAggregation_CPU) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DailyResourceUsageAggregation_CPU) Reset 
    
    
    func (x *DailyResourceUsageAggregation_CPU) Reset()

### func (*DailyResourceUsageAggregation_CPU) String 
    
    
    func (x *DailyResourceUsageAggregation_CPU) String() [string](https://pkg.go.dev/builtin#string)

## DailyResourceUsageAggregation_Disk
    
    
    type DailyResourceUsageAggregation_Disk struct {
    
    	// Disk I/O operations per second.
    	Iops *DailyResourceUsageAggregation_Stats `protobuf:"bytes,1,opt,name=iops,proto3" json:"iops,omitempty"`
    	// contains filtered or unexported fields
    }

Statistical aggregation of disk usage.

### func (*DailyResourceUsageAggregation_Disk) Descriptor 
    
    
    func (*DailyResourceUsageAggregation_Disk) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DailyResourceUsageAggregation_Disk.ProtoReflect.Descriptor instead.

### func (*DailyResourceUsageAggregation_Disk) GetIops 
    
    
    func (x *DailyResourceUsageAggregation_Disk) GetIops() *DailyResourceUsageAggregation_Stats

### func (*DailyResourceUsageAggregation_Disk) ProtoMessage 
    
    
    func (*DailyResourceUsageAggregation_Disk) ProtoMessage()

### func (*DailyResourceUsageAggregation_Disk) ProtoReflect 
    
    
    func (x *DailyResourceUsageAggregation_Disk) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DailyResourceUsageAggregation_Disk) Reset 
    
    
    func (x *DailyResourceUsageAggregation_Disk) Reset()

### func (*DailyResourceUsageAggregation_Disk) String 
    
    
    func (x *DailyResourceUsageAggregation_Disk) String() [string](https://pkg.go.dev/builtin#string)

## DailyResourceUsageAggregation_Memory
    
    
    type DailyResourceUsageAggregation_Memory struct {
    
    	// Memory utilization percentage.
    	UtilizationPercentage *DailyResourceUsageAggregation_Stats `protobuf:"bytes,1,opt,name=utilization_percentage,json=utilizationPercentage,proto3" json:"utilization_percentage,omitempty"`
    	// contains filtered or unexported fields
    }

Statistical aggregation of memory usage.

### func (*DailyResourceUsageAggregation_Memory) Descriptor 
    
    
    func (*DailyResourceUsageAggregation_Memory) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DailyResourceUsageAggregation_Memory.ProtoReflect.Descriptor instead.

### func (*DailyResourceUsageAggregation_Memory) GetUtilizationPercentage 
    
    
    func (x *DailyResourceUsageAggregation_Memory) GetUtilizationPercentage() *DailyResourceUsageAggregation_Stats

### func (*DailyResourceUsageAggregation_Memory) ProtoMessage 
    
    
    func (*DailyResourceUsageAggregation_Memory) ProtoMessage()

### func (*DailyResourceUsageAggregation_Memory) ProtoReflect 
    
    
    func (x *DailyResourceUsageAggregation_Memory) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DailyResourceUsageAggregation_Memory) Reset 
    
    
    func (x *DailyResourceUsageAggregation_Memory) Reset()

### func (*DailyResourceUsageAggregation_Memory) String 
    
    
    func (x *DailyResourceUsageAggregation_Memory) String() [string](https://pkg.go.dev/builtin#string)

## DailyResourceUsageAggregation_Network
    
    
    type DailyResourceUsageAggregation_Network struct {
    
    	// Network ingress in B/s.
    	IngressBps *DailyResourceUsageAggregation_Stats `protobuf:"bytes,1,opt,name=ingress_bps,json=ingressBps,proto3" json:"ingress_bps,omitempty"`
    	// Network egress in B/s.
    	EgressBps *DailyResourceUsageAggregation_Stats `protobuf:"bytes,2,opt,name=egress_bps,json=egressBps,proto3" json:"egress_bps,omitempty"`
    	// contains filtered or unexported fields
    }

Statistical aggregation of network usage.

### func (*DailyResourceUsageAggregation_Network) Descriptor 
    
    
    func (*DailyResourceUsageAggregation_Network) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DailyResourceUsageAggregation_Network.ProtoReflect.Descriptor instead.

### func (*DailyResourceUsageAggregation_Network) GetEgressBps 
    
    
    func (x *DailyResourceUsageAggregation_Network) GetEgressBps() *DailyResourceUsageAggregation_Stats

### func (*DailyResourceUsageAggregation_Network) GetIngressBps 
    
    
    func (x *DailyResourceUsageAggregation_Network) GetIngressBps() *DailyResourceUsageAggregation_Stats

### func (*DailyResourceUsageAggregation_Network) ProtoMessage 
    
    
    func (*DailyResourceUsageAggregation_Network) ProtoMessage()

### func (*DailyResourceUsageAggregation_Network) ProtoReflect 
    
    
    func (x *DailyResourceUsageAggregation_Network) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DailyResourceUsageAggregation_Network) Reset 
    
    
    func (x *DailyResourceUsageAggregation_Network) Reset()

### func (*DailyResourceUsageAggregation_Network) String 
    
    
    func (x *DailyResourceUsageAggregation_Network) String() [string](https://pkg.go.dev/builtin#string)

## DailyResourceUsageAggregation_Stats
    
    
    type DailyResourceUsageAggregation_Stats struct {
    
    	// Average usage value.
    	Average [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,opt,name=average,proto3" json:"average,omitempty"`
    	// Median usage value.
    	Median [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,2,opt,name=median,proto3" json:"median,omitempty"`
    	// 95th percentile usage value.
    	NinteyFifthPercentile [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,3,opt,name=nintey_fifth_percentile,json=ninteyFifthPercentile,proto3" json:"nintey_fifth_percentile,omitempty"`
    	// Peak usage value.
    	Peak [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,4,opt,name=peak,proto3" json:"peak,omitempty"`
    	// contains filtered or unexported fields
    }

Statistical aggregation of samples for a single resource usage.

### func (*DailyResourceUsageAggregation_Stats) Descriptor 
    
    
    func (*DailyResourceUsageAggregation_Stats) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DailyResourceUsageAggregation_Stats.ProtoReflect.Descriptor instead.

### func (*DailyResourceUsageAggregation_Stats) GetAverage 
    
    
    func (x *DailyResourceUsageAggregation_Stats) GetAverage() [float32](https://pkg.go.dev/builtin#float32)

### func (*DailyResourceUsageAggregation_Stats) GetMedian 
    
    
    func (x *DailyResourceUsageAggregation_Stats) GetMedian() [float32](https://pkg.go.dev/builtin#float32)

### func (*DailyResourceUsageAggregation_Stats) GetNinteyFifthPercentile 
    
    
    func (x *DailyResourceUsageAggregation_Stats) GetNinteyFifthPercentile() [float32](https://pkg.go.dev/builtin#float32)

### func (*DailyResourceUsageAggregation_Stats) GetPeak 
    
    
    func (x *DailyResourceUsageAggregation_Stats) GetPeak() [float32](https://pkg.go.dev/builtin#float32)

### func (*DailyResourceUsageAggregation_Stats) ProtoMessage 
    
    
    func (*DailyResourceUsageAggregation_Stats) ProtoMessage()

### func (*DailyResourceUsageAggregation_Stats) ProtoReflect 
    
    
    func (x *DailyResourceUsageAggregation_Stats) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DailyResourceUsageAggregation_Stats) Reset 
    
    
    func (x *DailyResourceUsageAggregation_Stats) Reset()

### func (*DailyResourceUsageAggregation_Stats) String 
    
    
    func (x *DailyResourceUsageAggregation_Stats) String() [string](https://pkg.go.dev/builtin#string)

## DeleteAssetRequest
    
    
    type DeleteAssetRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to delete an asset.

### func (*DeleteAssetRequest) Descriptor 
    
    
    func (*DeleteAssetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteAssetRequest.ProtoReflect.Descriptor instead.

### func (*DeleteAssetRequest) GetName 
    
    
    func (x *DeleteAssetRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteAssetRequest) GetRequestId 
    
    
    func (x *DeleteAssetRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteAssetRequest) ProtoMessage 
    
    
    func (*DeleteAssetRequest) ProtoMessage()

### func (*DeleteAssetRequest) ProtoReflect 
    
    
    func (x *DeleteAssetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteAssetRequest) Reset 
    
    
    func (x *DeleteAssetRequest) Reset()

### func (*DeleteAssetRequest) String 
    
    
    func (x *DeleteAssetRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteGroupRequest
    
    
    type DeleteGroupRequest struct {
    
    	// Required. Name of the group resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to delete a group.

### func (*DeleteGroupRequest) Descriptor 
    
    
    func (*DeleteGroupRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteGroupRequest.ProtoReflect.Descriptor instead.

### func (*DeleteGroupRequest) GetName 
    
    
    func (x *DeleteGroupRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteGroupRequest) GetRequestId 
    
    
    func (x *DeleteGroupRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteGroupRequest) ProtoMessage 
    
    
    func (*DeleteGroupRequest) ProtoMessage()

### func (*DeleteGroupRequest) ProtoReflect 
    
    
    func (x *DeleteGroupRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteGroupRequest) Reset 
    
    
    func (x *DeleteGroupRequest) Reset()

### func (*DeleteGroupRequest) String 
    
    
    func (x *DeleteGroupRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteImportDataFileRequest
    
    
    type DeleteImportDataFileRequest struct {
    
    	// Required. Name of the ImportDataFile to delete.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to delete an `ImportDataFile` resource.

### func (*DeleteImportDataFileRequest) Descriptor 
    
    
    func (*DeleteImportDataFileRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteImportDataFileRequest.ProtoReflect.Descriptor instead.

### func (*DeleteImportDataFileRequest) GetName 
    
    
    func (x *DeleteImportDataFileRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteImportDataFileRequest) GetRequestId 
    
    
    func (x *DeleteImportDataFileRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteImportDataFileRequest) ProtoMessage 
    
    
    func (*DeleteImportDataFileRequest) ProtoMessage()

### func (*DeleteImportDataFileRequest) ProtoReflect 
    
    
    func (x *DeleteImportDataFileRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteImportDataFileRequest) Reset 
    
    
    func (x *DeleteImportDataFileRequest) Reset()

### func (*DeleteImportDataFileRequest) String 
    
    
    func (x *DeleteImportDataFileRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteImportJobRequest
    
    
    type DeleteImportJobRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. If set to `true`, any `ImportDataFiles` of this job will also be
    	// deleted If set to `false`, the request only works if the job has no data
    	// files.
    	Force [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=force,proto3" json:"force,omitempty"`
    	// contains filtered or unexported fields
    }

A request to delete an import job.

### func (*DeleteImportJobRequest) Descriptor 
    
    
    func (*DeleteImportJobRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteImportJobRequest.ProtoReflect.Descriptor instead.

### func (*DeleteImportJobRequest) GetForce 
    
    
    func (x *DeleteImportJobRequest) GetForce() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteImportJobRequest) GetName 
    
    
    func (x *DeleteImportJobRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteImportJobRequest) GetRequestId 
    
    
    func (x *DeleteImportJobRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteImportJobRequest) ProtoMessage 
    
    
    func (*DeleteImportJobRequest) ProtoMessage()

### func (*DeleteImportJobRequest) ProtoReflect 
    
    
    func (x *DeleteImportJobRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteImportJobRequest) Reset 
    
    
    func (x *DeleteImportJobRequest) Reset()

### func (*DeleteImportJobRequest) String 
    
    
    func (x *DeleteImportJobRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeletePreferenceSetRequest
    
    
    type DeletePreferenceSetRequest struct {
    
    	// Required. Name of the group resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to delete a preference set.

### func (*DeletePreferenceSetRequest) Descriptor 
    
    
    func (*DeletePreferenceSetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeletePreferenceSetRequest.ProtoReflect.Descriptor instead.

### func (*DeletePreferenceSetRequest) GetName 
    
    
    func (x *DeletePreferenceSetRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeletePreferenceSetRequest) GetRequestId 
    
    
    func (x *DeletePreferenceSetRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeletePreferenceSetRequest) ProtoMessage 
    
    
    func (*DeletePreferenceSetRequest) ProtoMessage()

### func (*DeletePreferenceSetRequest) ProtoReflect 
    
    
    func (x *DeletePreferenceSetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeletePreferenceSetRequest) Reset 
    
    
    func (x *DeletePreferenceSetRequest) Reset()

### func (*DeletePreferenceSetRequest) String 
    
    
    func (x *DeletePreferenceSetRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteReportConfigRequest
    
    
    type DeleteReportConfigRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Optional. If set to `true`, any child `Reports` of this entity will also be
    	// deleted. If set to `false`, the request only works if the resource has no
    	// children.
    	Force [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=force,proto3" json:"force,omitempty"`
    	// contains filtered or unexported fields
    }

A request to delete a ReportConfig.

### func (*DeleteReportConfigRequest) Descriptor 
    
    
    func (*DeleteReportConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteReportConfigRequest.ProtoReflect.Descriptor instead.

### func (*DeleteReportConfigRequest) GetForce 
    
    
    func (x *DeleteReportConfigRequest) GetForce() [bool](https://pkg.go.dev/builtin#bool)

### func (*DeleteReportConfigRequest) GetName 
    
    
    func (x *DeleteReportConfigRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteReportConfigRequest) GetRequestId 
    
    
    func (x *DeleteReportConfigRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteReportConfigRequest) ProtoMessage 
    
    
    func (*DeleteReportConfigRequest) ProtoMessage()

### func (*DeleteReportConfigRequest) ProtoReflect 
    
    
    func (x *DeleteReportConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteReportConfigRequest) Reset 
    
    
    func (x *DeleteReportConfigRequest) Reset()

### func (*DeleteReportConfigRequest) String 
    
    
    func (x *DeleteReportConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteReportRequest
    
    
    type DeleteReportRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to delete a Report.

### func (*DeleteReportRequest) Descriptor 
    
    
    func (*DeleteReportRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteReportRequest.ProtoReflect.Descriptor instead.

### func (*DeleteReportRequest) GetName 
    
    
    func (x *DeleteReportRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteReportRequest) GetRequestId 
    
    
    func (x *DeleteReportRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteReportRequest) ProtoMessage 
    
    
    func (*DeleteReportRequest) ProtoMessage()

### func (*DeleteReportRequest) ProtoReflect 
    
    
    func (x *DeleteReportRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteReportRequest) Reset 
    
    
    func (x *DeleteReportRequest) Reset()

### func (*DeleteReportRequest) String 
    
    
    func (x *DeleteReportRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteSourceRequest
    
    
    type DeleteSourceRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to delete a source.

### func (*DeleteSourceRequest) Descriptor 
    
    
    func (*DeleteSourceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteSourceRequest.ProtoReflect.Descriptor instead.

### func (*DeleteSourceRequest) GetName 
    
    
    func (x *DeleteSourceRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteSourceRequest) GetRequestId 
    
    
    func (x *DeleteSourceRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteSourceRequest) ProtoMessage 
    
    
    func (*DeleteSourceRequest) ProtoMessage()

### func (*DeleteSourceRequest) ProtoReflect 
    
    
    func (x *DeleteSourceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteSourceRequest) Reset 
    
    
    func (x *DeleteSourceRequest) Reset()

### func (*DeleteSourceRequest) String 
    
    
    func (x *DeleteSourceRequest) String() [string](https://pkg.go.dev/builtin#string)

## DiskEntry
    
    
    type DiskEntry struct {
    
    	// Disk capacity.
    	CapacityBytes [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=capacity_bytes,json=capacityBytes,proto3" json:"capacity_bytes,omitempty"`
    	// Disk free space.
    	FreeBytes [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=free_bytes,json=freeBytes,proto3" json:"free_bytes,omitempty"`
    	// Disk label.
    	DiskLabel [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=disk_label,json=diskLabel,proto3" json:"disk_label,omitempty"`
    	// Disk label type (e.g. BIOS/GPT)
    	DiskLabelType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=disk_label_type,json=diskLabelType,proto3" json:"disk_label_type,omitempty"`
    	// Disks interface type.
    	InterfaceType DiskEntry_InterfaceType `protobuf:"varint,5,opt,name=interface_type,json=interfaceType,proto3,enum=google.cloud.migrationcenter.v1.DiskEntry_InterfaceType" json:"interface_type,omitempty"`
    	// Partition layout.
    	Partitions *DiskPartitionList `protobuf:"bytes,6,opt,name=partitions,proto3" json:"partitions,omitempty"`
    	// Disk hardware address (e.g. 0:1 for SCSI).
    	HwAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=hw_address,json=hwAddress,proto3" json:"hw_address,omitempty"`
    	// Additional details for specific platforms.
    	//
    	// Types that are valid to be assigned to PlatformSpecific:
    	//
    	//	*DiskEntry_Vmware
    	PlatformSpecific isDiskEntry_PlatformSpecific `protobuf_oneof:"platform_specific"`
    	// contains filtered or unexported fields
    }

Single disk entry.

### func (*DiskEntry) Descriptor 
    
    
    func (*DiskEntry) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DiskEntry.ProtoReflect.Descriptor instead.

### func (*DiskEntry) GetCapacityBytes 
    
    
    func (x *DiskEntry) GetCapacityBytes() [int64](https://pkg.go.dev/builtin#int64)

### func (*DiskEntry) GetDiskLabel 
    
    
    func (x *DiskEntry) GetDiskLabel() [string](https://pkg.go.dev/builtin#string)

### func (*DiskEntry) GetDiskLabelType 
    
    
    func (x *DiskEntry) GetDiskLabelType() [string](https://pkg.go.dev/builtin#string)

### func (*DiskEntry) GetFreeBytes 
    
    
    func (x *DiskEntry) GetFreeBytes() [int64](https://pkg.go.dev/builtin#int64)

### func (*DiskEntry) GetHwAddress 
    
    
    func (x *DiskEntry) GetHwAddress() [string](https://pkg.go.dev/builtin#string)

### func (*DiskEntry) GetInterfaceType 
    
    
    func (x *DiskEntry) GetInterfaceType() DiskEntry_InterfaceType

### func (*DiskEntry) GetPartitions 
    
    
    func (x *DiskEntry) GetPartitions() *DiskPartitionList

### func (*DiskEntry) GetPlatformSpecific 
    
    
    func (x *DiskEntry) GetPlatformSpecific() isDiskEntry_PlatformSpecific

### func (*DiskEntry) GetVmware 
    
    
    func (x *DiskEntry) GetVmware() *VmwareDiskConfig

### func (*DiskEntry) ProtoMessage 
    
    
    func (*DiskEntry) ProtoMessage()

### func (*DiskEntry) ProtoReflect 
    
    
    func (x *DiskEntry) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DiskEntry) Reset 
    
    
    func (x *DiskEntry) Reset()

### func (*DiskEntry) String 
    
    
    func (x *DiskEntry) String() [string](https://pkg.go.dev/builtin#string)

## DiskEntryList
    
    
    type DiskEntryList struct {
    
    	// Disk entries.
    	Entries []*DiskEntry `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

VM disks.

### func (*DiskEntryList) Descriptor 
    
    
    func (*DiskEntryList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DiskEntryList.ProtoReflect.Descriptor instead.

### func (*DiskEntryList) GetEntries 
    
    
    func (x *DiskEntryList) GetEntries() []*DiskEntry

### func (*DiskEntryList) ProtoMessage 
    
    
    func (*DiskEntryList) ProtoMessage()

### func (*DiskEntryList) ProtoReflect 
    
    
    func (x *DiskEntryList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DiskEntryList) Reset 
    
    
    func (x *DiskEntryList) Reset()

### func (*DiskEntryList) String 
    
    
    func (x *DiskEntryList) String() [string](https://pkg.go.dev/builtin#string)

## DiskEntry_InterfaceType
    
    
    type DiskEntry_InterfaceType [int32](https://pkg.go.dev/builtin#int32)

Disks interface type.

### DiskEntry_INTERFACE_TYPE_UNSPECIFIED, DiskEntry_IDE, DiskEntry_SATA, DiskEntry_SAS, DiskEntry_SCSI, DiskEntry_NVME, DiskEntry_FC, DiskEntry_ISCSI
    
    
    const (
    	// Interface type unknown or unspecified.
    	DiskEntry_INTERFACE_TYPE_UNSPECIFIED DiskEntry_InterfaceType = 0
    	// IDE interface type.
    	DiskEntry_IDE DiskEntry_InterfaceType = 1
    	// SATA interface type.
    	DiskEntry_SATA DiskEntry_InterfaceType = 2
    	// SAS interface type.
    	DiskEntry_SAS DiskEntry_InterfaceType = 3
    	// SCSI interface type.
    	DiskEntry_SCSI DiskEntry_InterfaceType = 4
    	// NVME interface type.
    	DiskEntry_NVME DiskEntry_InterfaceType = 5
    	// FC interface type.
    	DiskEntry_FC DiskEntry_InterfaceType = 6
    	// iSCSI interface type.
    	DiskEntry_ISCSI DiskEntry_InterfaceType = 7
    )

### func (DiskEntry_InterfaceType) Descriptor 
    
    
    func (DiskEntry_InterfaceType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (DiskEntry_InterfaceType) Enum 
    
    
    func (x DiskEntry_InterfaceType) Enum() *DiskEntry_InterfaceType

### func (DiskEntry_InterfaceType) EnumDescriptor 
    
    
    func (DiskEntry_InterfaceType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DiskEntry_InterfaceType.Descriptor instead.

### func (DiskEntry_InterfaceType) Number 
    
    
    func (x DiskEntry_InterfaceType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (DiskEntry_InterfaceType) String 
    
    
    func (x DiskEntry_InterfaceType) String() [string](https://pkg.go.dev/builtin#string)

### func (DiskEntry_InterfaceType) Type 
    
    
    func (DiskEntry_InterfaceType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## DiskEntry_Vmware
    
    
    type DiskEntry_Vmware struct {
    	// VMware disk details.
    	Vmware *VmwareDiskConfig `protobuf:"bytes,20,opt,name=vmware,proto3,oneof"`
    }

## DiskPartition
    
    
    type DiskPartition struct {
    
    	// Partition type.
    	Type [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=type,proto3" json:"type,omitempty"`
    	// Partition file system.
    	FileSystem [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=file_system,json=fileSystem,proto3" json:"file_system,omitempty"`
    	// Mount pount (Linux/Windows) or drive letter (Windows).
    	MountPoint [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=mount_point,json=mountPoint,proto3" json:"mount_point,omitempty"`
    	// Partition capacity.
    	CapacityBytes [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=capacity_bytes,json=capacityBytes,proto3" json:"capacity_bytes,omitempty"`
    	// Partition free space.
    	FreeBytes [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,5,opt,name=free_bytes,json=freeBytes,proto3" json:"free_bytes,omitempty"`
    	// Partition UUID.
    	Uuid [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=uuid,proto3" json:"uuid,omitempty"`
    	// Sub-partitions.
    	SubPartitions *DiskPartitionList `protobuf:"bytes,7,opt,name=sub_partitions,json=subPartitions,proto3" json:"sub_partitions,omitempty"`
    	// contains filtered or unexported fields
    }

Disk Partition details.

### func (*DiskPartition) Descriptor 
    
    
    func (*DiskPartition) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DiskPartition.ProtoReflect.Descriptor instead.

### func (*DiskPartition) GetCapacityBytes 
    
    
    func (x *DiskPartition) GetCapacityBytes() [int64](https://pkg.go.dev/builtin#int64)

### func (*DiskPartition) GetFileSystem 
    
    
    func (x *DiskPartition) GetFileSystem() [string](https://pkg.go.dev/builtin#string)

### func (*DiskPartition) GetFreeBytes 
    
    
    func (x *DiskPartition) GetFreeBytes() [int64](https://pkg.go.dev/builtin#int64)

### func (*DiskPartition) GetMountPoint 
    
    
    func (x *DiskPartition) GetMountPoint() [string](https://pkg.go.dev/builtin#string)

### func (*DiskPartition) GetSubPartitions 
    
    
    func (x *DiskPartition) GetSubPartitions() *DiskPartitionList

### func (*DiskPartition) GetType 
    
    
    func (x *DiskPartition) GetType() [string](https://pkg.go.dev/builtin#string)

### func (*DiskPartition) GetUuid 
    
    
    func (x *DiskPartition) GetUuid() [string](https://pkg.go.dev/builtin#string)

### func (*DiskPartition) ProtoMessage 
    
    
    func (*DiskPartition) ProtoMessage()

### func (*DiskPartition) ProtoReflect 
    
    
    func (x *DiskPartition) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DiskPartition) Reset 
    
    
    func (x *DiskPartition) Reset()

### func (*DiskPartition) String 
    
    
    func (x *DiskPartition) String() [string](https://pkg.go.dev/builtin#string)

## DiskPartitionList
    
    
    type DiskPartitionList struct {
    
    	// Partition entries.
    	Entries []*DiskPartition `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

Disk partition list.

### func (*DiskPartitionList) Descriptor 
    
    
    func (*DiskPartitionList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DiskPartitionList.ProtoReflect.Descriptor instead.

### func (*DiskPartitionList) GetEntries 
    
    
    func (x *DiskPartitionList) GetEntries() []*DiskPartition

### func (*DiskPartitionList) ProtoMessage 
    
    
    func (*DiskPartitionList) ProtoMessage()

### func (*DiskPartitionList) ProtoReflect 
    
    
    func (x *DiskPartitionList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DiskPartitionList) Reset 
    
    
    func (x *DiskPartitionList) Reset()

### func (*DiskPartitionList) String 
    
    
    func (x *DiskPartitionList) String() [string](https://pkg.go.dev/builtin#string)

## DiskUsageSample
    
    
    type DiskUsageSample struct {
    
    	// Average IOPS sampled over a short window. Must be non-negative.
    	AverageIops [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,opt,name=average_iops,json=averageIops,proto3" json:"average_iops,omitempty"`
    	// contains filtered or unexported fields
    }

Disk usage sample. Values are across all disks.

### func (*DiskUsageSample) Descriptor 
    
    
    func (*DiskUsageSample) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DiskUsageSample.ProtoReflect.Descriptor instead.

### func (*DiskUsageSample) GetAverageIops 
    
    
    func (x *DiskUsageSample) GetAverageIops() [float32](https://pkg.go.dev/builtin#float32)

### func (*DiskUsageSample) ProtoMessage 
    
    
    func (*DiskUsageSample) ProtoMessage()

### func (*DiskUsageSample) ProtoReflect 
    
    
    func (x *DiskUsageSample) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DiskUsageSample) Reset 
    
    
    func (x *DiskUsageSample) Reset()

### func (*DiskUsageSample) String 
    
    
    func (x *DiskUsageSample) String() [string](https://pkg.go.dev/builtin#string)

## ErrorFrame
    
    
    type ErrorFrame struct {
    
    	// Output only. The identifier of the ErrorFrame.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. All the violations that were detected for the frame.
    	Violations []*FrameViolationEntry `protobuf:"bytes,2,rep,name=violations,proto3" json:"violations,omitempty"`
    	// Output only. The frame that was originally reported.
    	OriginalFrame *AssetFrame `protobuf:"bytes,3,opt,name=original_frame,json=originalFrame,proto3" json:"original_frame,omitempty"`
    	// Output only. Frame ingestion time.
    	IngestionTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=ingestion_time,json=ingestionTime,proto3" json:"ingestion_time,omitempty"`
    	// contains filtered or unexported fields
    }

Message representing a frame which failed to be processed due to an error.

### func (*ErrorFrame) Descriptor 
    
    
    func (*ErrorFrame) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ErrorFrame.ProtoReflect.Descriptor instead.

### func (*ErrorFrame) GetIngestionTime 
    
    
    func (x *ErrorFrame) GetIngestionTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ErrorFrame) GetName 
    
    
    func (x *ErrorFrame) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ErrorFrame) GetOriginalFrame 
    
    
    func (x *ErrorFrame) GetOriginalFrame() *AssetFrame

### func (*ErrorFrame) GetViolations 
    
    
    func (x *ErrorFrame) GetViolations() []*FrameViolationEntry

### func (*ErrorFrame) ProtoMessage 
    
    
    func (*ErrorFrame) ProtoMessage()

### func (*ErrorFrame) ProtoReflect 
    
    
    func (x *ErrorFrame) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ErrorFrame) Reset 
    
    
    func (x *ErrorFrame) Reset()

### func (*ErrorFrame) String 
    
    
    func (x *ErrorFrame) String() [string](https://pkg.go.dev/builtin#string)

## ErrorFrameView
    
    
    type ErrorFrameView [int32](https://pkg.go.dev/builtin#int32)

ErrorFrameView can be specified in ErrorFrames List and Get requests to control the level of details that is returned for the original frame.

### ErrorFrameView_ERROR_FRAME_VIEW_UNSPECIFIED, ErrorFrameView_ERROR_FRAME_VIEW_BASIC, ErrorFrameView_ERROR_FRAME_VIEW_FULL
    
    
    const (
    	// Value is unset. The system will fallback to the default value.
    	ErrorFrameView_ERROR_FRAME_VIEW_UNSPECIFIED ErrorFrameView = 0
    	// Include basic frame data, but not the full contents.
    	ErrorFrameView_ERROR_FRAME_VIEW_BASIC ErrorFrameView = 1
    	// Include everything.
    	ErrorFrameView_ERROR_FRAME_VIEW_FULL ErrorFrameView = 2
    )

### func (ErrorFrameView) Descriptor 
    
    
    func (ErrorFrameView) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ErrorFrameView) Enum 
    
    
    func (x ErrorFrameView) Enum() *ErrorFrameView

### func (ErrorFrameView) EnumDescriptor 
    
    
    func (ErrorFrameView) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ErrorFrameView.Descriptor instead.

### func (ErrorFrameView) Number 
    
    
    func (x ErrorFrameView) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ErrorFrameView) String 
    
    
    func (x ErrorFrameView) String() [string](https://pkg.go.dev/builtin#string)

### func (ErrorFrameView) Type 
    
    
    func (ErrorFrameView) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ExecutionReport
    
    
    type ExecutionReport struct {
    
    	// Total number of asset frames reported for the import job.
    	FramesReported [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=frames_reported,json=framesReported,proto3" json:"frames_reported,omitempty"`
    	// Validation errors encountered during the execution of the import job.
    	ExecutionErrors *ValidationReport `protobuf:"bytes,2,opt,name=execution_errors,json=executionErrors,proto3" json:"execution_errors,omitempty"`
    	// Output only. Total number of rows in the import job.
    	TotalRowsCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=total_rows_count,json=totalRowsCount,proto3" json:"total_rows_count,omitempty"`
    	// contains filtered or unexported fields
    }

A resource that reports result of the import job execution.

### func (*ExecutionReport) Descriptor 
    
    
    func (*ExecutionReport) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ExecutionReport.ProtoReflect.Descriptor instead.

### func (*ExecutionReport) GetExecutionErrors 
    
    
    func (x *ExecutionReport) GetExecutionErrors() *ValidationReport

### func (*ExecutionReport) GetFramesReported 
    
    
    func (x *ExecutionReport) GetFramesReported() [int32](https://pkg.go.dev/builtin#int32)

### func (*ExecutionReport) GetTotalRowsCount 
    
    
    func (x *ExecutionReport) GetTotalRowsCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*ExecutionReport) ProtoMessage 
    
    
    func (*ExecutionReport) ProtoMessage()

### func (*ExecutionReport) ProtoReflect 
    
    
    func (x *ExecutionReport) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ExecutionReport) Reset 
    
    
    func (x *ExecutionReport) Reset()

### func (*ExecutionReport) String 
    
    
    func (x *ExecutionReport) String() [string](https://pkg.go.dev/builtin#string)

## FileValidationReport
    
    
    type FileValidationReport struct {
    
    	// The name of the file.
    	FileName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=file_name,json=fileName,proto3" json:"file_name,omitempty"`
    	// Partial list of rows that encountered validation error.
    	RowErrors []*ImportRowError `protobuf:"bytes,2,rep,name=row_errors,json=rowErrors,proto3" json:"row_errors,omitempty"`
    	// Flag indicating that processing was aborted due to maximum number of
    	// errors.
    	PartialReport [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=partial_report,json=partialReport,proto3" json:"partial_report,omitempty"`
    	// List of file level errors.
    	FileErrors []*ImportError `protobuf:"bytes,4,rep,name=file_errors,json=fileErrors,proto3" json:"file_errors,omitempty"`
    	// contains filtered or unexported fields
    }

A resource that aggregates the validation errors found in an import job file.

### func (*FileValidationReport) Descriptor 
    
    
    func (*FileValidationReport) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FileValidationReport.ProtoReflect.Descriptor instead.

### func (*FileValidationReport) GetFileErrors 
    
    
    func (x *FileValidationReport) GetFileErrors() []*ImportError

### func (*FileValidationReport) GetFileName 
    
    
    func (x *FileValidationReport) GetFileName() [string](https://pkg.go.dev/builtin#string)

### func (*FileValidationReport) GetPartialReport 
    
    
    func (x *FileValidationReport) GetPartialReport() [bool](https://pkg.go.dev/builtin#bool)

### func (*FileValidationReport) GetRowErrors 
    
    
    func (x *FileValidationReport) GetRowErrors() []*ImportRowError

### func (*FileValidationReport) ProtoMessage 
    
    
    func (*FileValidationReport) ProtoMessage()

### func (*FileValidationReport) ProtoReflect 
    
    
    func (x *FileValidationReport) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FileValidationReport) Reset 
    
    
    func (x *FileValidationReport) Reset()

### func (*FileValidationReport) String 
    
    
    func (x *FileValidationReport) String() [string](https://pkg.go.dev/builtin#string)

## FitDescriptor
    
    
    type FitDescriptor struct {
    
    	// Fit level.
    	FitLevel FitDescriptor_FitLevel `protobuf:"varint,1,opt,name=fit_level,json=fitLevel,proto3,enum=google.cloud.migrationcenter.v1.FitDescriptor_FitLevel" json:"fit_level,omitempty"`
    	// contains filtered or unexported fields
    }

Describes the fit level of an asset for migration to a specific target.

### func (*FitDescriptor) Descriptor 
    
    
    func (*FitDescriptor) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FitDescriptor.ProtoReflect.Descriptor instead.

### func (*FitDescriptor) GetFitLevel 
    
    
    func (x *FitDescriptor) GetFitLevel() FitDescriptor_FitLevel

### func (*FitDescriptor) ProtoMessage 
    
    
    func (*FitDescriptor) ProtoMessage()

### func (*FitDescriptor) ProtoReflect 
    
    
    func (x *FitDescriptor) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FitDescriptor) Reset 
    
    
    func (x *FitDescriptor) Reset()

### func (*FitDescriptor) String 
    
    
    func (x *FitDescriptor) String() [string](https://pkg.go.dev/builtin#string)

## FitDescriptor_FitLevel
    
    
    type FitDescriptor_FitLevel [int32](https://pkg.go.dev/builtin#int32)

Fit level.

### FitDescriptor_FIT_LEVEL_UNSPECIFIED, FitDescriptor_FIT, FitDescriptor_NO_FIT, FitDescriptor_REQUIRES_EFFORT
    
    
    const (
    	// Not enough information.
    	FitDescriptor_FIT_LEVEL_UNSPECIFIED FitDescriptor_FitLevel = 0
    	// Fit.
    	FitDescriptor_FIT FitDescriptor_FitLevel = 1
    	// No Fit.
    	FitDescriptor_NO_FIT FitDescriptor_FitLevel = 2
    	// Fit with effort.
    	FitDescriptor_REQUIRES_EFFORT FitDescriptor_FitLevel = 3
    )

### func (FitDescriptor_FitLevel) Descriptor 
    
    
    func (FitDescriptor_FitLevel) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (FitDescriptor_FitLevel) Enum 
    
    
    func (x FitDescriptor_FitLevel) Enum() *FitDescriptor_FitLevel

### func (FitDescriptor_FitLevel) EnumDescriptor 
    
    
    func (FitDescriptor_FitLevel) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FitDescriptor_FitLevel.Descriptor instead.

### func (FitDescriptor_FitLevel) Number 
    
    
    func (x FitDescriptor_FitLevel) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (FitDescriptor_FitLevel) String 
    
    
    func (x FitDescriptor_FitLevel) String() [string](https://pkg.go.dev/builtin#string)

### func (FitDescriptor_FitLevel) Type 
    
    
    func (FitDescriptor_FitLevel) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## FrameViolationEntry
    
    
    type FrameViolationEntry struct {
    
    	// The field of the original frame where the violation occurred.
    	Field [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=field,proto3" json:"field,omitempty"`
    	// A message describing the violation.
    	Violation [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=violation,proto3" json:"violation,omitempty"`
    	// contains filtered or unexported fields
    }

A resource that contains a single violation of a reported `AssetFrame` resource.

### func (*FrameViolationEntry) Descriptor 
    
    
    func (*FrameViolationEntry) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FrameViolationEntry.ProtoReflect.Descriptor instead.

### func (*FrameViolationEntry) GetField 
    
    
    func (x *FrameViolationEntry) GetField() [string](https://pkg.go.dev/builtin#string)

### func (*FrameViolationEntry) GetViolation 
    
    
    func (x *FrameViolationEntry) GetViolation() [string](https://pkg.go.dev/builtin#string)

### func (*FrameViolationEntry) ProtoMessage 
    
    
    func (*FrameViolationEntry) ProtoMessage()

### func (*FrameViolationEntry) ProtoReflect 
    
    
    func (x *FrameViolationEntry) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FrameViolationEntry) Reset 
    
    
    func (x *FrameViolationEntry) Reset()

### func (*FrameViolationEntry) String 
    
    
    func (x *FrameViolationEntry) String() [string](https://pkg.go.dev/builtin#string)

## Frames
    
    
    type Frames struct {
    
    	// A repeated field of asset data.
    	FramesData []*AssetFrame `protobuf:"bytes,1,rep,name=frames_data,json=framesData,proto3" json:"frames_data,omitempty"`
    	// contains filtered or unexported fields
    }

Collection of frame data.

### func (*Frames) Descriptor 
    
    
    func (*Frames) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Frames.ProtoReflect.Descriptor instead.

### func (*Frames) GetFramesData 
    
    
    func (x *Frames) GetFramesData() []*AssetFrame

### func (*Frames) ProtoMessage 
    
    
    func (*Frames) ProtoMessage()

### func (*Frames) ProtoReflect 
    
    
    func (x *Frames) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Frames) Reset 
    
    
    func (x *Frames) Reset()

### func (*Frames) String 
    
    
    func (x *Frames) String() [string](https://pkg.go.dev/builtin#string)

## FstabEntry
    
    
    type FstabEntry struct {
    
    	// The block special device or remote filesystem to be mounted.
    	Spec [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=spec,proto3" json:"spec,omitempty"`
    	// The mount point for the filesystem.
    	File [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=file,proto3" json:"file,omitempty"`
    	// The type of the filesystem.
    	Vfstype [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=vfstype,proto3" json:"vfstype,omitempty"`
    	// Mount options associated with the filesystem.
    	Mntops [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=mntops,proto3" json:"mntops,omitempty"`
    	// Used by dump to determine which filesystems need to be dumped.
    	Freq [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=freq,proto3" json:"freq,omitempty"`
    	// Used by the fsck(8) program to determine the order in which filesystem
    	// checks are done at reboot time.
    	Passno [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,6,opt,name=passno,proto3" json:"passno,omitempty"`
    	// contains filtered or unexported fields
    }

Single fstab entry.

### func (*FstabEntry) Descriptor 
    
    
    func (*FstabEntry) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FstabEntry.ProtoReflect.Descriptor instead.

### func (*FstabEntry) GetFile 
    
    
    func (x *FstabEntry) GetFile() [string](https://pkg.go.dev/builtin#string)

### func (*FstabEntry) GetFreq 
    
    
    func (x *FstabEntry) GetFreq() [int32](https://pkg.go.dev/builtin#int32)

### func (*FstabEntry) GetMntops 
    
    
    func (x *FstabEntry) GetMntops() [string](https://pkg.go.dev/builtin#string)

### func (*FstabEntry) GetPassno 
    
    
    func (x *FstabEntry) GetPassno() [int32](https://pkg.go.dev/builtin#int32)

### func (*FstabEntry) GetSpec 
    
    
    func (x *FstabEntry) GetSpec() [string](https://pkg.go.dev/builtin#string)

### func (*FstabEntry) GetVfstype 
    
    
    func (x *FstabEntry) GetVfstype() [string](https://pkg.go.dev/builtin#string)

### func (*FstabEntry) ProtoMessage 
    
    
    func (*FstabEntry) ProtoMessage()

### func (*FstabEntry) ProtoReflect 
    
    
    func (x *FstabEntry) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FstabEntry) Reset 
    
    
    func (x *FstabEntry) Reset()

### func (*FstabEntry) String 
    
    
    func (x *FstabEntry) String() [string](https://pkg.go.dev/builtin#string)

## FstabEntryList
    
    
    type FstabEntryList struct {
    
    	// Fstab entries.
    	Entries []*FstabEntry `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

Fstab content.

### func (*FstabEntryList) Descriptor 
    
    
    func (*FstabEntryList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use FstabEntryList.ProtoReflect.Descriptor instead.

### func (*FstabEntryList) GetEntries 
    
    
    func (x *FstabEntryList) GetEntries() []*FstabEntry

### func (*FstabEntryList) ProtoMessage 
    
    
    func (*FstabEntryList) ProtoMessage()

### func (*FstabEntryList) ProtoReflect 
    
    
    func (x *FstabEntryList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*FstabEntryList) Reset 
    
    
    func (x *FstabEntryList) Reset()

### func (*FstabEntryList) String 
    
    
    func (x *FstabEntryList) String() [string](https://pkg.go.dev/builtin#string)

## GenericInsight
    
    
    type GenericInsight struct {
    
    	// Output only. Represents a globally unique message id for
    	// this insight, can be used for localization purposes, in case message_code
    	// is not yet known by the client use default_message instead.
    	MessageId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=message_id,json=messageId,proto3" json:"message_id,omitempty"`
    	// Output only. In case message_code is not yet known by the client
    	// default_message will be the message to be used instead.
    	DefaultMessage [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=default_message,json=defaultMessage,proto3" json:"default_message,omitempty"`
    	// Output only. Additional information about the insight, each entry can be a
    	// logical entry and must make sense if it is displayed with line breaks
    	// between each entry. Text can contain md style links.
    	AdditionalInformation [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=additional_information,json=additionalInformation,proto3" json:"additional_information,omitempty"`
    	// contains filtered or unexported fields
    }

A generic insight about an asset.

### func (*GenericInsight) Descriptor 
    
    
    func (*GenericInsight) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenericInsight.ProtoReflect.Descriptor instead.

### func (*GenericInsight) GetAdditionalInformation 
    
    
    func (x *GenericInsight) GetAdditionalInformation() [][string](https://pkg.go.dev/builtin#string)

### func (*GenericInsight) GetDefaultMessage 
    
    
    func (x *GenericInsight) GetDefaultMessage() [string](https://pkg.go.dev/builtin#string)

### func (*GenericInsight) GetMessageId 
    
    
    func (x *GenericInsight) GetMessageId() [int64](https://pkg.go.dev/builtin#int64)

### func (*GenericInsight) ProtoMessage 
    
    
    func (*GenericInsight) ProtoMessage()

### func (*GenericInsight) ProtoReflect 
    
    
    func (x *GenericInsight) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenericInsight) Reset 
    
    
    func (x *GenericInsight) Reset()

### func (*GenericInsight) String 
    
    
    func (x *GenericInsight) String() [string](https://pkg.go.dev/builtin#string)

## GenericPlatformDetails
    
    
    type GenericPlatformDetails struct {
    
    	// Free text representation of the machine location.
    	// The format of this field should not be relied on. Different VMs in the same
    	// location may have different string values for this field.
    	Location [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=location,proto3" json:"location,omitempty"`
    	// contains filtered or unexported fields
    }

Generic platform details.

### func (*GenericPlatformDetails) Descriptor 
    
    
    func (*GenericPlatformDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GenericPlatformDetails.ProtoReflect.Descriptor instead.

### func (*GenericPlatformDetails) GetLocation 
    
    
    func (x *GenericPlatformDetails) GetLocation() [string](https://pkg.go.dev/builtin#string)

### func (*GenericPlatformDetails) ProtoMessage 
    
    
    func (*GenericPlatformDetails) ProtoMessage()

### func (*GenericPlatformDetails) ProtoReflect 
    
    
    func (x *GenericPlatformDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GenericPlatformDetails) Reset 
    
    
    func (x *GenericPlatformDetails) Reset()

### func (*GenericPlatformDetails) String 
    
    
    func (x *GenericPlatformDetails) String() [string](https://pkg.go.dev/builtin#string)

## GetAssetRequest
    
    
    type GetAssetRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// View of the assets. Defaults to BASIC.
    	View AssetView `protobuf:"varint,2,opt,name=view,proto3,enum=google.cloud.migrationcenter.v1.AssetView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

Message for getting a Asset.

### func (*GetAssetRequest) Descriptor 
    
    
    func (*GetAssetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetAssetRequest.ProtoReflect.Descriptor instead.

### func (*GetAssetRequest) GetName 
    
    
    func (x *GetAssetRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetAssetRequest) GetView 
    
    
    func (x *GetAssetRequest) GetView() AssetView

### func (*GetAssetRequest) ProtoMessage 
    
    
    func (*GetAssetRequest) ProtoMessage()

### func (*GetAssetRequest) ProtoReflect 
    
    
    func (x *GetAssetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetAssetRequest) Reset 
    
    
    func (x *GetAssetRequest) Reset()

### func (*GetAssetRequest) String 
    
    
    func (x *GetAssetRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetErrorFrameRequest
    
    
    type GetErrorFrameRequest struct {
    
    	// Required. The name of the frame to retrieve.
    	// Format:
    	// projects/{project}/locations/{location}/sources/{source}/errorFrames/{error_frame}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional view mode to control the level of details for the
    	// frame. The default is a basic frame view.
    	View ErrorFrameView `protobuf:"varint,2,opt,name=view,proto3,enum=google.cloud.migrationcenter.v1.ErrorFrameView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*GetErrorFrameRequest) Descriptor 
    
    
    func (*GetErrorFrameRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetErrorFrameRequest.ProtoReflect.Descriptor instead.

### func (*GetErrorFrameRequest) GetName 
    
    
    func (x *GetErrorFrameRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetErrorFrameRequest) GetView 
    
    
    func (x *GetErrorFrameRequest) GetView() ErrorFrameView

### func (*GetErrorFrameRequest) ProtoMessage 
    
    
    func (*GetErrorFrameRequest) ProtoMessage()

### func (*GetErrorFrameRequest) ProtoReflect 
    
    
    func (x *GetErrorFrameRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetErrorFrameRequest) Reset 
    
    
    func (x *GetErrorFrameRequest) Reset()

### func (*GetErrorFrameRequest) String 
    
    
    func (x *GetErrorFrameRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetGroupRequest
    
    
    type GetGroupRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get a group.

### func (*GetGroupRequest) Descriptor 
    
    
    func (*GetGroupRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetGroupRequest.ProtoReflect.Descriptor instead.

### func (*GetGroupRequest) GetName 
    
    
    func (x *GetGroupRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetGroupRequest) ProtoMessage 
    
    
    func (*GetGroupRequest) ProtoMessage()

### func (*GetGroupRequest) ProtoReflect 
    
    
    func (x *GetGroupRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetGroupRequest) Reset 
    
    
    func (x *GetGroupRequest) Reset()

### func (*GetGroupRequest) String 
    
    
    func (x *GetGroupRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetImportDataFileRequest
    
    
    type GetImportDataFileRequest struct {
    
    	// Required. Name of the ImportDataFile.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get an import data file.

### func (*GetImportDataFileRequest) Descriptor 
    
    
    func (*GetImportDataFileRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetImportDataFileRequest.ProtoReflect.Descriptor instead.

### func (*GetImportDataFileRequest) GetName 
    
    
    func (x *GetImportDataFileRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetImportDataFileRequest) ProtoMessage 
    
    
    func (*GetImportDataFileRequest) ProtoMessage()

### func (*GetImportDataFileRequest) ProtoReflect 
    
    
    func (x *GetImportDataFileRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetImportDataFileRequest) Reset 
    
    
    func (x *GetImportDataFileRequest) Reset()

### func (*GetImportDataFileRequest) String 
    
    
    func (x *GetImportDataFileRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetImportJobRequest
    
    
    type GetImportJobRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. The level of details of the import job.
    	// Default value is FULL.
    	View ImportJobView `protobuf:"varint,2,opt,name=view,proto3,enum=google.cloud.migrationcenter.v1.ImportJobView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get an import job.

### func (*GetImportJobRequest) Descriptor 
    
    
    func (*GetImportJobRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetImportJobRequest.ProtoReflect.Descriptor instead.

### func (*GetImportJobRequest) GetName 
    
    
    func (x *GetImportJobRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetImportJobRequest) GetView 
    
    
    func (x *GetImportJobRequest) GetView() ImportJobView

### func (*GetImportJobRequest) ProtoMessage 
    
    
    func (*GetImportJobRequest) ProtoMessage()

### func (*GetImportJobRequest) ProtoReflect 
    
    
    func (x *GetImportJobRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetImportJobRequest) Reset 
    
    
    func (x *GetImportJobRequest) Reset()

### func (*GetImportJobRequest) String 
    
    
    func (x *GetImportJobRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetPreferenceSetRequest
    
    
    type GetPreferenceSetRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get a preference set.

### func (*GetPreferenceSetRequest) Descriptor 
    
    
    func (*GetPreferenceSetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetPreferenceSetRequest.ProtoReflect.Descriptor instead.

### func (*GetPreferenceSetRequest) GetName 
    
    
    func (x *GetPreferenceSetRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetPreferenceSetRequest) ProtoMessage 
    
    
    func (*GetPreferenceSetRequest) ProtoMessage()

### func (*GetPreferenceSetRequest) ProtoReflect 
    
    
    func (x *GetPreferenceSetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetPreferenceSetRequest) Reset 
    
    
    func (x *GetPreferenceSetRequest) Reset()

### func (*GetPreferenceSetRequest) String 
    
    
    func (x *GetPreferenceSetRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetReportConfigRequest
    
    
    type GetReportConfigRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get a `ReportConfig` resource.

### func (*GetReportConfigRequest) Descriptor 
    
    
    func (*GetReportConfigRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetReportConfigRequest.ProtoReflect.Descriptor instead.

### func (*GetReportConfigRequest) GetName 
    
    
    func (x *GetReportConfigRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetReportConfigRequest) ProtoMessage 
    
    
    func (*GetReportConfigRequest) ProtoMessage()

### func (*GetReportConfigRequest) ProtoReflect 
    
    
    func (x *GetReportConfigRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetReportConfigRequest) Reset 
    
    
    func (x *GetReportConfigRequest) Reset()

### func (*GetReportConfigRequest) String 
    
    
    func (x *GetReportConfigRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetReportRequest
    
    
    type GetReportRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Determines what information to retrieve for the Report.
    	View ReportView `protobuf:"varint,6,opt,name=view,proto3,enum=google.cloud.migrationcenter.v1.ReportView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get a Report.

### func (*GetReportRequest) Descriptor 
    
    
    func (*GetReportRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetReportRequest.ProtoReflect.Descriptor instead.

### func (*GetReportRequest) GetName 
    
    
    func (x *GetReportRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetReportRequest) GetView 
    
    
    func (x *GetReportRequest) GetView() ReportView

### func (*GetReportRequest) ProtoMessage 
    
    
    func (*GetReportRequest) ProtoMessage()

### func (*GetReportRequest) ProtoReflect 
    
    
    func (x *GetReportRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetReportRequest) Reset 
    
    
    func (x *GetReportRequest) Reset()

### func (*GetReportRequest) String 
    
    
    func (x *GetReportRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetSettingsRequest
    
    
    type GetSettingsRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get the settings.

### func (*GetSettingsRequest) Descriptor 
    
    
    func (*GetSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetSettingsRequest.ProtoReflect.Descriptor instead.

### func (*GetSettingsRequest) GetName 
    
    
    func (x *GetSettingsRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetSettingsRequest) ProtoMessage 
    
    
    func (*GetSettingsRequest) ProtoMessage()

### func (*GetSettingsRequest) ProtoReflect 
    
    
    func (x *GetSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetSettingsRequest) Reset 
    
    
    func (x *GetSettingsRequest) Reset()

### func (*GetSettingsRequest) String 
    
    
    func (x *GetSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetSourceRequest
    
    
    type GetSourceRequest struct {
    
    	// Required. Name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get a source.

### func (*GetSourceRequest) Descriptor 
    
    
    func (*GetSourceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetSourceRequest.ProtoReflect.Descriptor instead.

### func (*GetSourceRequest) GetName 
    
    
    func (x *GetSourceRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetSourceRequest) ProtoMessage 
    
    
    func (*GetSourceRequest) ProtoMessage()

### func (*GetSourceRequest) ProtoReflect 
    
    
    func (x *GetSourceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetSourceRequest) Reset 
    
    
    func (x *GetSourceRequest) Reset()

### func (*GetSourceRequest) String 
    
    
    func (x *GetSourceRequest) String() [string](https://pkg.go.dev/builtin#string)

## Group
    
    
    type Group struct {
    
    	// Output only. The name of the group.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The timestamp when the group was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The timestamp when the group was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Labels as key value pairs.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// User-friendly display name.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// The description of the resource.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=description,proto3" json:"description,omitempty"`
    	// contains filtered or unexported fields
    }

A resource that represents an asset group. The purpose of an asset group is to bundle a set of assets that have something in common, while allowing users to add annotations to the group. An asset can belong to multiple groups.

### func (*Group) Descriptor 
    
    
    func (*Group) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Group.ProtoReflect.Descriptor instead.

### func (*Group) GetCreateTime 
    
    
    func (x *Group) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Group) GetDescription 
    
    
    func (x *Group) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Group) GetDisplayName 
    
    
    func (x *Group) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Group) GetLabels 
    
    
    func (x *Group) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*Group) GetName 
    
    
    func (x *Group) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Group) GetUpdateTime 
    
    
    func (x *Group) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Group) ProtoMessage 
    
    
    func (*Group) ProtoMessage()

### func (*Group) ProtoReflect 
    
    
    func (x *Group) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Group) Reset 
    
    
    func (x *Group) Reset()

### func (*Group) String 
    
    
    func (x *Group) String() [string](https://pkg.go.dev/builtin#string)

## GuestConfigDetails
    
    
    type GuestConfigDetails struct {
    
    	// OS issue (typically /etc/issue in Linux).
    	Issue [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=issue,proto3" json:"issue,omitempty"`
    	// Mount list (Linux fstab).
    	Fstab *FstabEntryList `protobuf:"bytes,2,opt,name=fstab,proto3" json:"fstab,omitempty"`
    	// Hosts file (/etc/hosts).
    	Hosts *HostsEntryList `protobuf:"bytes,3,opt,name=hosts,proto3" json:"hosts,omitempty"`
    	// NFS exports.
    	NfsExports *NfsExportList `protobuf:"bytes,4,opt,name=nfs_exports,json=nfsExports,proto3" json:"nfs_exports,omitempty"`
    	// Security-Enhanced Linux (SELinux) mode.
    	SelinuxMode GuestConfigDetails_SeLinuxMode `protobuf:"varint,5,opt,name=selinux_mode,json=selinuxMode,proto3,enum=google.cloud.migrationcenter.v1.GuestConfigDetails_SeLinuxMode" json:"selinux_mode,omitempty"`
    	// contains filtered or unexported fields
    }

Guest OS config information.

### func (*GuestConfigDetails) Descriptor 
    
    
    func (*GuestConfigDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GuestConfigDetails.ProtoReflect.Descriptor instead.

### func (*GuestConfigDetails) GetFstab 
    
    
    func (x *GuestConfigDetails) GetFstab() *FstabEntryList

### func (*GuestConfigDetails) GetHosts 
    
    
    func (x *GuestConfigDetails) GetHosts() *HostsEntryList

### func (*GuestConfigDetails) GetIssue 
    
    
    func (x *GuestConfigDetails) GetIssue() [string](https://pkg.go.dev/builtin#string)

### func (*GuestConfigDetails) GetNfsExports 
    
    
    func (x *GuestConfigDetails) GetNfsExports() *NfsExportList

### func (*GuestConfigDetails) GetSelinuxMode 
    
    
    func (x *GuestConfigDetails) GetSelinuxMode() GuestConfigDetails_SeLinuxMode

### func (*GuestConfigDetails) ProtoMessage 
    
    
    func (*GuestConfigDetails) ProtoMessage()

### func (*GuestConfigDetails) ProtoReflect 
    
    
    func (x *GuestConfigDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GuestConfigDetails) Reset 
    
    
    func (x *GuestConfigDetails) Reset()

### func (*GuestConfigDetails) String 
    
    
    func (x *GuestConfigDetails) String() [string](https://pkg.go.dev/builtin#string)

## GuestConfigDetails_SeLinuxMode
    
    
    type GuestConfigDetails_SeLinuxMode [int32](https://pkg.go.dev/builtin#int32)

Security-Enhanced Linux (SELinux) mode.

### GuestConfigDetails_SE_LINUX_MODE_UNSPECIFIED, GuestConfigDetails_SE_LINUX_MODE_DISABLED, GuestConfigDetails_SE_LINUX_MODE_PERMISSIVE, GuestConfigDetails_SE_LINUX_MODE_ENFORCING
    
    
    const (
    	// SELinux mode unknown or unspecified.
    	GuestConfigDetails_SE_LINUX_MODE_UNSPECIFIED GuestConfigDetails_SeLinuxMode = 0
    	// SELinux is disabled.
    	GuestConfigDetails_SE_LINUX_MODE_DISABLED GuestConfigDetails_SeLinuxMode = 1
    	// SELinux permissive mode.
    	GuestConfigDetails_SE_LINUX_MODE_PERMISSIVE GuestConfigDetails_SeLinuxMode = 2
    	// SELinux enforcing mode.
    	GuestConfigDetails_SE_LINUX_MODE_ENFORCING GuestConfigDetails_SeLinuxMode = 3
    )

### func (GuestConfigDetails_SeLinuxMode) Descriptor 
    
    
    func (GuestConfigDetails_SeLinuxMode) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (GuestConfigDetails_SeLinuxMode) Enum 
    
    
    func (x GuestConfigDetails_SeLinuxMode) Enum() *GuestConfigDetails_SeLinuxMode

### func (GuestConfigDetails_SeLinuxMode) EnumDescriptor 
    
    
    func (GuestConfigDetails_SeLinuxMode) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GuestConfigDetails_SeLinuxMode.Descriptor instead.

### func (GuestConfigDetails_SeLinuxMode) Number 
    
    
    func (x GuestConfigDetails_SeLinuxMode) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (GuestConfigDetails_SeLinuxMode) String 
    
    
    func (x GuestConfigDetails_SeLinuxMode) String() [string](https://pkg.go.dev/builtin#string)

### func (GuestConfigDetails_SeLinuxMode) Type 
    
    
    func (GuestConfigDetails_SeLinuxMode) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## GuestInstalledApplication
    
    
    type GuestInstalledApplication struct {
    
    	// Installed application name.
    	ApplicationName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=application_name,json=applicationName,proto3" json:"application_name,omitempty"`
    	// Installed application vendor.
    	Vendor [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=vendor,proto3" json:"vendor,omitempty"`
    	// The time when the application was installed.
    	InstallTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=install_time,json=installTime,proto3" json:"install_time,omitempty"`
    	// Source path.
    	Path [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=path,proto3" json:"path,omitempty"`
    	// Installed application version.
    	Version [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=version,proto3" json:"version,omitempty"`
    	// contains filtered or unexported fields
    }

Guest installed application information.

### func (*GuestInstalledApplication) Descriptor 
    
    
    func (*GuestInstalledApplication) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GuestInstalledApplication.ProtoReflect.Descriptor instead.

### func (*GuestInstalledApplication) GetApplicationName 
    
    
    func (x *GuestInstalledApplication) GetApplicationName() [string](https://pkg.go.dev/builtin#string)

### func (*GuestInstalledApplication) GetInstallTime 
    
    
    func (x *GuestInstalledApplication) GetInstallTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*GuestInstalledApplication) GetPath 
    
    
    func (x *GuestInstalledApplication) GetPath() [string](https://pkg.go.dev/builtin#string)

### func (*GuestInstalledApplication) GetVendor 
    
    
    func (x *GuestInstalledApplication) GetVendor() [string](https://pkg.go.dev/builtin#string)

### func (*GuestInstalledApplication) GetVersion 
    
    
    func (x *GuestInstalledApplication) GetVersion() [string](https://pkg.go.dev/builtin#string)

### func (*GuestInstalledApplication) ProtoMessage 
    
    
    func (*GuestInstalledApplication) ProtoMessage()

### func (*GuestInstalledApplication) ProtoReflect 
    
    
    func (x *GuestInstalledApplication) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GuestInstalledApplication) Reset 
    
    
    func (x *GuestInstalledApplication) Reset()

### func (*GuestInstalledApplication) String 
    
    
    func (x *GuestInstalledApplication) String() [string](https://pkg.go.dev/builtin#string)

## GuestInstalledApplicationList
    
    
    type GuestInstalledApplicationList struct {
    
    	// Application entries.
    	Entries []*GuestInstalledApplication `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

Guest installed application list.

### func (*GuestInstalledApplicationList) Descriptor 
    
    
    func (*GuestInstalledApplicationList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GuestInstalledApplicationList.ProtoReflect.Descriptor instead.

### func (*GuestInstalledApplicationList) GetEntries 
    
    
    func (x *GuestInstalledApplicationList) GetEntries() []*GuestInstalledApplication

### func (*GuestInstalledApplicationList) ProtoMessage 
    
    
    func (*GuestInstalledApplicationList) ProtoMessage()

### func (*GuestInstalledApplicationList) ProtoReflect 
    
    
    func (x *GuestInstalledApplicationList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GuestInstalledApplicationList) Reset 
    
    
    func (x *GuestInstalledApplicationList) Reset()

### func (*GuestInstalledApplicationList) String 
    
    
    func (x *GuestInstalledApplicationList) String() [string](https://pkg.go.dev/builtin#string)

## GuestOsDetails
    
    
    type GuestOsDetails struct {
    
    	// The name of the operating system.
    	OsName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=os_name,json=osName,proto3" json:"os_name,omitempty"`
    	// What family the OS belong to, if known.
    	Family OperatingSystemFamily `protobuf:"varint,2,opt,name=family,proto3,enum=google.cloud.migrationcenter.v1.OperatingSystemFamily" json:"family,omitempty"`
    	// The version of the operating system.
    	Version [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=version,proto3" json:"version,omitempty"`
    	// OS and app configuration.
    	Config *GuestConfigDetails `protobuf:"bytes,4,opt,name=config,proto3" json:"config,omitempty"`
    	// Runtime information.
    	Runtime *GuestRuntimeDetails `protobuf:"bytes,5,opt,name=runtime,proto3" json:"runtime,omitempty"`
    	// contains filtered or unexported fields
    }

Information from Guest-level collections.

### func (*GuestOsDetails) Descriptor 
    
    
    func (*GuestOsDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GuestOsDetails.ProtoReflect.Descriptor instead.

### func (*GuestOsDetails) GetConfig 
    
    
    func (x *GuestOsDetails) GetConfig() *GuestConfigDetails

### func (*GuestOsDetails) GetFamily 
    
    
    func (x *GuestOsDetails) GetFamily() OperatingSystemFamily

### func (*GuestOsDetails) GetOsName 
    
    
    func (x *GuestOsDetails) GetOsName() [string](https://pkg.go.dev/builtin#string)

### func (*GuestOsDetails) GetRuntime 
    
    
    func (x *GuestOsDetails) GetRuntime() *GuestRuntimeDetails

### func (*GuestOsDetails) GetVersion 
    
    
    func (x *GuestOsDetails) GetVersion() [string](https://pkg.go.dev/builtin#string)

### func (*GuestOsDetails) ProtoMessage 
    
    
    func (*GuestOsDetails) ProtoMessage()

### func (*GuestOsDetails) ProtoReflect 
    
    
    func (x *GuestOsDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GuestOsDetails) Reset 
    
    
    func (x *GuestOsDetails) Reset()

### func (*GuestOsDetails) String 
    
    
    func (x *GuestOsDetails) String() [string](https://pkg.go.dev/builtin#string)

## GuestRuntimeDetails
    
    
    type GuestRuntimeDetails struct {
    
    	// Running background services.
    	Services *RunningServiceList `protobuf:"bytes,1,opt,name=services,proto3" json:"services,omitempty"`
    	// Running processes.
    	Processes *RunningProcessList `protobuf:"bytes,2,opt,name=processes,proto3" json:"processes,omitempty"`
    	// Runtime network information (connections, ports).
    	Network *RuntimeNetworkInfo `protobuf:"bytes,3,opt,name=network,proto3" json:"network,omitempty"`
    	// Last time the OS was booted.
    	LastBootTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=last_boot_time,json=lastBootTime,proto3" json:"last_boot_time,omitempty"`
    	// Domain, e.g. c.stratozone-development.internal.
    	Domain [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=domain,proto3" json:"domain,omitempty"`
    	// Machine name.
    	MachineName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=machine_name,json=machineName,proto3" json:"machine_name,omitempty"`
    	// Installed applications information.
    	InstalledApps *GuestInstalledApplicationList `protobuf:"bytes,7,opt,name=installed_apps,json=installedApps,proto3" json:"installed_apps,omitempty"`
    	// Open files information.
    	OpenFileList *OpenFileList `protobuf:"bytes,8,opt,name=open_file_list,json=openFileList,proto3" json:"open_file_list,omitempty"`
    	// contains filtered or unexported fields
    }

Guest OS runtime information.

### func (*GuestRuntimeDetails) Descriptor 
    
    
    func (*GuestRuntimeDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GuestRuntimeDetails.ProtoReflect.Descriptor instead.

### func (*GuestRuntimeDetails) GetDomain 
    
    
    func (x *GuestRuntimeDetails) GetDomain() [string](https://pkg.go.dev/builtin#string)

### func (*GuestRuntimeDetails) GetInstalledApps 
    
    
    func (x *GuestRuntimeDetails) GetInstalledApps() *GuestInstalledApplicationList

### func (*GuestRuntimeDetails) GetLastBootTime 
    
    
    func (x *GuestRuntimeDetails) GetLastBootTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*GuestRuntimeDetails) GetMachineName 
    
    
    func (x *GuestRuntimeDetails) GetMachineName() [string](https://pkg.go.dev/builtin#string)

### func (*GuestRuntimeDetails) GetNetwork 
    
    
    func (x *GuestRuntimeDetails) GetNetwork() *RuntimeNetworkInfo

### func (*GuestRuntimeDetails) GetOpenFileList 
    
    
    func (x *GuestRuntimeDetails) GetOpenFileList() *OpenFileList

### func (*GuestRuntimeDetails) GetProcesses 
    
    
    func (x *GuestRuntimeDetails) GetProcesses() *RunningProcessList

### func (*GuestRuntimeDetails) GetServices 
    
    
    func (x *GuestRuntimeDetails) GetServices() *RunningServiceList

### func (*GuestRuntimeDetails) ProtoMessage 
    
    
    func (*GuestRuntimeDetails) ProtoMessage()

### func (*GuestRuntimeDetails) ProtoReflect 
    
    
    func (x *GuestRuntimeDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GuestRuntimeDetails) Reset 
    
    
    func (x *GuestRuntimeDetails) Reset()

### func (*GuestRuntimeDetails) String 
    
    
    func (x *GuestRuntimeDetails) String() [string](https://pkg.go.dev/builtin#string)

## HostsEntry
    
    
    type HostsEntry struct {
    
    	// IP (raw, IPv4/6 agnostic).
    	Ip [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=ip,proto3" json:"ip,omitempty"`
    	// List of host names / aliases.
    	HostNames [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=host_names,json=hostNames,proto3" json:"host_names,omitempty"`
    	// contains filtered or unexported fields
    }

Single /etc/hosts entry.

### func (*HostsEntry) Descriptor 
    
    
    func (*HostsEntry) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HostsEntry.ProtoReflect.Descriptor instead.

### func (*HostsEntry) GetHostNames 
    
    
    func (x *HostsEntry) GetHostNames() [][string](https://pkg.go.dev/builtin#string)

### func (*HostsEntry) GetIp 
    
    
    func (x *HostsEntry) GetIp() [string](https://pkg.go.dev/builtin#string)

### func (*HostsEntry) ProtoMessage 
    
    
    func (*HostsEntry) ProtoMessage()

### func (*HostsEntry) ProtoReflect 
    
    
    func (x *HostsEntry) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*HostsEntry) Reset 
    
    
    func (x *HostsEntry) Reset()

### func (*HostsEntry) String 
    
    
    func (x *HostsEntry) String() [string](https://pkg.go.dev/builtin#string)

## HostsEntryList
    
    
    type HostsEntryList struct {
    
    	// Hosts entries.
    	Entries []*HostsEntry `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

Hosts content.

### func (*HostsEntryList) Descriptor 
    
    
    func (*HostsEntryList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HostsEntryList.ProtoReflect.Descriptor instead.

### func (*HostsEntryList) GetEntries 
    
    
    func (x *HostsEntryList) GetEntries() []*HostsEntry

### func (*HostsEntryList) ProtoMessage 
    
    
    func (*HostsEntryList) ProtoMessage()

### func (*HostsEntryList) ProtoReflect 
    
    
    func (x *HostsEntryList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*HostsEntryList) Reset 
    
    
    func (x *HostsEntryList) Reset()

### func (*HostsEntryList) String 
    
    
    func (x *HostsEntryList) String() [string](https://pkg.go.dev/builtin#string)

## ImportDataFile
    
    
    type ImportDataFile struct {
    
    	// Output only. The name of the file.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// User-friendly display name. Maximum length is 63 characters.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Required. The payload format.
    	Format ImportJobFormat `protobuf:"varint,2,opt,name=format,proto3,enum=google.cloud.migrationcenter.v1.ImportJobFormat" json:"format,omitempty"`
    	// Output only. The timestamp when the file was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The state of the import data file.
    	State ImportDataFile_State `protobuf:"varint,4,opt,name=state,proto3,enum=google.cloud.migrationcenter.v1.ImportDataFile_State" json:"state,omitempty"`
    	// Types that are valid to be assigned to FileInfo:
    	//
    	//	*ImportDataFile_UploadFileInfo
    	FileInfo isImportDataFile_FileInfo `protobuf_oneof:"file_info"`
    	// contains filtered or unexported fields
    }

A resource that represents a payload file in an import job.

### func (*ImportDataFile) Descriptor 
    
    
    func (*ImportDataFile) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportDataFile.ProtoReflect.Descriptor instead.

### func (*ImportDataFile) GetCreateTime 
    
    
    func (x *ImportDataFile) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ImportDataFile) GetDisplayName 
    
    
    func (x *ImportDataFile) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*ImportDataFile) GetFileInfo 
    
    
    func (x *ImportDataFile) GetFileInfo() isImportDataFile_FileInfo

### func (*ImportDataFile) GetFormat 
    
    
    func (x *ImportDataFile) GetFormat() ImportJobFormat

### func (*ImportDataFile) GetName 
    
    
    func (x *ImportDataFile) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ImportDataFile) GetState 
    
    
    func (x *ImportDataFile) GetState() ImportDataFile_State

### func (*ImportDataFile) GetUploadFileInfo 
    
    
    func (x *ImportDataFile) GetUploadFileInfo() *UploadFileInfo

### func (*ImportDataFile) ProtoMessage 
    
    
    func (*ImportDataFile) ProtoMessage()

### func (*ImportDataFile) ProtoReflect 
    
    
    func (x *ImportDataFile) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ImportDataFile) Reset 
    
    
    func (x *ImportDataFile) Reset()

### func (*ImportDataFile) String 
    
    
    func (x *ImportDataFile) String() [string](https://pkg.go.dev/builtin#string)

## ImportDataFile_State
    
    
    type ImportDataFile_State [int32](https://pkg.go.dev/builtin#int32)

Enumerates possible states of an import data file.

### ImportDataFile_STATE_UNSPECIFIED, ImportDataFile_CREATING, ImportDataFile_ACTIVE
    
    
    const (
    	// Default value.
    	ImportDataFile_STATE_UNSPECIFIED ImportDataFile_State = 0
    	// The data file is being created.
    	ImportDataFile_CREATING ImportDataFile_State = 1
    	// The data file completed initialization.
    	ImportDataFile_ACTIVE ImportDataFile_State = 2
    )

### func (ImportDataFile_State) Descriptor 
    
    
    func (ImportDataFile_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ImportDataFile_State) Enum 
    
    
    func (x ImportDataFile_State) Enum() *ImportDataFile_State

### func (ImportDataFile_State) EnumDescriptor 
    
    
    func (ImportDataFile_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportDataFile_State.Descriptor instead.

### func (ImportDataFile_State) Number 
    
    
    func (x ImportDataFile_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ImportDataFile_State) String 
    
    
    func (x ImportDataFile_State) String() [string](https://pkg.go.dev/builtin#string)

### func (ImportDataFile_State) Type 
    
    
    func (ImportDataFile_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ImportDataFile_UploadFileInfo
    
    
    type ImportDataFile_UploadFileInfo struct {
    	// Information about a file that is uploaded to a storage service.
    	UploadFileInfo *UploadFileInfo `protobuf:"bytes,5,opt,name=upload_file_info,json=uploadFileInfo,proto3,oneof"`
    }

## ImportError
    
    
    type ImportError struct {
    
    	// The error information.
    	ErrorDetails [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=error_details,json=errorDetails,proto3" json:"error_details,omitempty"`
    	// The severity of the error.
    	Severity ImportError_Severity `protobuf:"varint,2,opt,name=severity,proto3,enum=google.cloud.migrationcenter.v1.ImportError_Severity" json:"severity,omitempty"`
    	// contains filtered or unexported fields
    }

A resource that reports the errors encountered while processing an import job.

### func (*ImportError) Descriptor 
    
    
    func (*ImportError) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportError.ProtoReflect.Descriptor instead.

### func (*ImportError) GetErrorDetails 
    
    
    func (x *ImportError) GetErrorDetails() [string](https://pkg.go.dev/builtin#string)

### func (*ImportError) GetSeverity 
    
    
    func (x *ImportError) GetSeverity() ImportError_Severity

### func (*ImportError) ProtoMessage 
    
    
    func (*ImportError) ProtoMessage()

### func (*ImportError) ProtoReflect 
    
    
    func (x *ImportError) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ImportError) Reset 
    
    
    func (x *ImportError) Reset()

### func (*ImportError) String 
    
    
    func (x *ImportError) String() [string](https://pkg.go.dev/builtin#string)

## ImportError_Severity
    
    
    type ImportError_Severity [int32](https://pkg.go.dev/builtin#int32)

Enumerate possible error severity.

### ImportError_SEVERITY_UNSPECIFIED, ImportError_ERROR, ImportError_WARNING, ImportError_INFO
    
    
    const (
    	ImportError_SEVERITY_UNSPECIFIED ImportError_Severity = 0
    	ImportError_ERROR                ImportError_Severity = 1
    	ImportError_WARNING              ImportError_Severity = 2
    	ImportError_INFO                 ImportError_Severity = 3
    )

### func (ImportError_Severity) Descriptor 
    
    
    func (ImportError_Severity) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ImportError_Severity) Enum 
    
    
    func (x ImportError_Severity) Enum() *ImportError_Severity

### func (ImportError_Severity) EnumDescriptor 
    
    
    func (ImportError_Severity) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportError_Severity.Descriptor instead.

### func (ImportError_Severity) Number 
    
    
    func (x ImportError_Severity) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ImportError_Severity) String 
    
    
    func (x ImportError_Severity) String() [string](https://pkg.go.dev/builtin#string)

### func (ImportError_Severity) Type 
    
    
    func (ImportError_Severity) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ImportJob
    
    
    type ImportJob struct {
    
    	// Output only. The full name of the import job.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// User-friendly display name. Maximum length is 63 characters.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Output only. The timestamp when the import job was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The timestamp when the import job was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Output only. The timestamp when the import job was completed.
    	CompleteTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=complete_time,json=completeTime,proto3" json:"complete_time,omitempty"`
    	// Output only. The state of the import job.
    	State ImportJob_ImportJobState `protobuf:"varint,6,opt,name=state,proto3,enum=google.cloud.migrationcenter.v1.ImportJob_ImportJobState" json:"state,omitempty"`
    	// Labels as key value pairs.
    	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Required. Reference to a source.
    	AssetSource [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=asset_source,json=assetSource,proto3" json:"asset_source,omitempty"`
    	// Holds the various report types of an import job.
    	//
    	// Types that are valid to be assigned to Report:
    	//
    	//	*ImportJob_ValidationReport
    	//	*ImportJob_ExecutionReport
    	Report isImportJob_Report `protobuf_oneof:"report"`
    	// contains filtered or unexported fields
    }

A resource that represents the background job that imports asset frames.

### func (*ImportJob) Descriptor 
    
    
    func (*ImportJob) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportJob.ProtoReflect.Descriptor instead.

### func (*ImportJob) GetAssetSource 
    
    
    func (x *ImportJob) GetAssetSource() [string](https://pkg.go.dev/builtin#string)

### func (*ImportJob) GetCompleteTime 
    
    
    func (x *ImportJob) GetCompleteTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ImportJob) GetCreateTime 
    
    
    func (x *ImportJob) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ImportJob) GetDisplayName 
    
    
    func (x *ImportJob) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*ImportJob) GetExecutionReport 
    
    
    func (x *ImportJob) GetExecutionReport() *ExecutionReport

### func (*ImportJob) GetLabels 
    
    
    func (x *ImportJob) GetLabels() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*ImportJob) GetName 
    
    
    func (x *ImportJob) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ImportJob) GetReport 
    
    
    func (x *ImportJob) GetReport() isImportJob_Report

### func (*ImportJob) GetState 
    
    
    func (x *ImportJob) GetState() ImportJob_ImportJobState

### func (*ImportJob) GetUpdateTime 
    
    
    func (x *ImportJob) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ImportJob) GetValidationReport 
    
    
    func (x *ImportJob) GetValidationReport() *ValidationReport

### func (*ImportJob) ProtoMessage 
    
    
    func (*ImportJob) ProtoMessage()

### func (*ImportJob) ProtoReflect 
    
    
    func (x *ImportJob) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ImportJob) Reset 
    
    
    func (x *ImportJob) Reset()

### func (*ImportJob) String 
    
    
    func (x *ImportJob) String() [string](https://pkg.go.dev/builtin#string)

## ImportJobFormat
    
    
    type ImportJobFormat [int32](https://pkg.go.dev/builtin#int32)

Specifies the data formats supported by Migration Center.

### ImportJobFormat_IMPORT_JOB_FORMAT_UNSPECIFIED, ImportJobFormat_IMPORT_JOB_FORMAT_RVTOOLS_XLSX, ImportJobFormat_IMPORT_JOB_FORMAT_RVTOOLS_CSV, ImportJobFormat_IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV, ImportJobFormat_IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV, ImportJobFormat_IMPORT_JOB_FORMAT_STRATOZONE_CSV
    
    
    const (
    	// Default value.
    	ImportJobFormat_IMPORT_JOB_FORMAT_UNSPECIFIED ImportJobFormat = 0
    	// RVTools format (XLSX).
    	ImportJobFormat_IMPORT_JOB_FORMAT_RVTOOLS_XLSX ImportJobFormat = 1
    	// RVTools format (CSV).
    	ImportJobFormat_IMPORT_JOB_FORMAT_RVTOOLS_CSV ImportJobFormat = 2
    	// CSV format exported from AWS using the
    	// [AWS collection
    	// script][https://github.com/GoogleCloudPlatform/aws-to-stratozone-export].
    	ImportJobFormat_IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV ImportJobFormat = 4
    	// CSV format exported from Azure using the
    	// [Azure collection
    	// script][https://github.com/GoogleCloudPlatform/azure-to-stratozone-export].
    	ImportJobFormat_IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV ImportJobFormat = 5
    	// CSV format created manually and following the StratoZone format. For more
    	// information, see [Manually create and upload data
    	// tables][https://cloud.google.com/migrate/stratozone/docs/import-data-portal].
    	ImportJobFormat_IMPORT_JOB_FORMAT_STRATOZONE_CSV ImportJobFormat = 6
    )

### func (ImportJobFormat) Descriptor 
    
    
    func (ImportJobFormat) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ImportJobFormat) Enum 
    
    
    func (x ImportJobFormat) Enum() *ImportJobFormat

### func (ImportJobFormat) EnumDescriptor 
    
    
    func (ImportJobFormat) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportJobFormat.Descriptor instead.

### func (ImportJobFormat) Number 
    
    
    func (x ImportJobFormat) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ImportJobFormat) String 
    
    
    func (x ImportJobFormat) String() [string](https://pkg.go.dev/builtin#string)

### func (ImportJobFormat) Type 
    
    
    func (ImportJobFormat) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ImportJobView
    
    
    type ImportJobView [int32](https://pkg.go.dev/builtin#int32)

Specifies the types of import job views that provide complete or partial details of an import job.

### ImportJobView_IMPORT_JOB_VIEW_UNSPECIFIED, ImportJobView_IMPORT_JOB_VIEW_BASIC, ImportJobView_IMPORT_JOB_VIEW_FULL
    
    
    const (
    	// The import job view is not specified. The API displays the basic view by
    	// default.
    	ImportJobView_IMPORT_JOB_VIEW_UNSPECIFIED ImportJobView = 0
    	// The import job view includes basic metadata of an import job.
    	// This view does not include payload information.
    	ImportJobView_IMPORT_JOB_VIEW_BASIC ImportJobView = 1
    	// The import job view includes all metadata of an import job.
    	ImportJobView_IMPORT_JOB_VIEW_FULL ImportJobView = 2
    )

### func (ImportJobView) Descriptor 
    
    
    func (ImportJobView) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ImportJobView) Enum 
    
    
    func (x ImportJobView) Enum() *ImportJobView

### func (ImportJobView) EnumDescriptor 
    
    
    func (ImportJobView) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportJobView.Descriptor instead.

### func (ImportJobView) Number 
    
    
    func (x ImportJobView) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ImportJobView) String 
    
    
    func (x ImportJobView) String() [string](https://pkg.go.dev/builtin#string)

### func (ImportJobView) Type 
    
    
    func (ImportJobView) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ImportJob_ExecutionReport
    
    
    type ImportJob_ExecutionReport struct {
    	// Output only. The report with the results of running the import job.
    	ExecutionReport *ExecutionReport `protobuf:"bytes,11,opt,name=execution_report,json=executionReport,proto3,oneof"`
    }

## ImportJob_ImportJobState
    
    
    type ImportJob_ImportJobState [int32](https://pkg.go.dev/builtin#int32)

Enumerates possible states of an import job.

### ImportJob_IMPORT_JOB_STATE_UNSPECIFIED, ImportJob_IMPORT_JOB_STATE_PENDING, ImportJob_IMPORT_JOB_STATE_RUNNING, ImportJob_IMPORT_JOB_STATE_COMPLETED, ImportJob_IMPORT_JOB_STATE_FAILED, ImportJob_IMPORT_JOB_STATE_VALIDATING, ImportJob_IMPORT_JOB_STATE_FAILED_VALIDATION, ImportJob_IMPORT_JOB_STATE_READY
    
    
    const (
    	// Default value.
    	ImportJob_IMPORT_JOB_STATE_UNSPECIFIED ImportJob_ImportJobState = 0
    	// The import job is pending.
    	ImportJob_IMPORT_JOB_STATE_PENDING ImportJob_ImportJobState = 1
    	// The processing of the import job is ongoing.
    	ImportJob_IMPORT_JOB_STATE_RUNNING ImportJob_ImportJobState = 2
    	// The import job processing has completed.
    	ImportJob_IMPORT_JOB_STATE_COMPLETED ImportJob_ImportJobState = 3
    	// The import job failed to be processed.
    	ImportJob_IMPORT_JOB_STATE_FAILED ImportJob_ImportJobState = 4
    	// The import job is being validated.
    	ImportJob_IMPORT_JOB_STATE_VALIDATING ImportJob_ImportJobState = 5
    	// The import job contains blocking errors.
    	ImportJob_IMPORT_JOB_STATE_FAILED_VALIDATION ImportJob_ImportJobState = 6
    	// The validation of the job completed with no blocking errors.
    	ImportJob_IMPORT_JOB_STATE_READY ImportJob_ImportJobState = 7
    )

### func (ImportJob_ImportJobState) Descriptor 
    
    
    func (ImportJob_ImportJobState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ImportJob_ImportJobState) Enum 
    
    
    func (x ImportJob_ImportJobState) Enum() *ImportJob_ImportJobState

### func (ImportJob_ImportJobState) EnumDescriptor 
    
    
    func (ImportJob_ImportJobState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportJob_ImportJobState.Descriptor instead.

### func (ImportJob_ImportJobState) Number 
    
    
    func (x ImportJob_ImportJobState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ImportJob_ImportJobState) String 
    
    
    func (x ImportJob_ImportJobState) String() [string](https://pkg.go.dev/builtin#string)

### func (ImportJob_ImportJobState) Type 
    
    
    func (ImportJob_ImportJobState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ImportJob_ValidationReport
    
    
    type ImportJob_ValidationReport struct {
    	// Output only. The report with the validation results of the import job.
    	ValidationReport *ValidationReport `protobuf:"bytes,10,opt,name=validation_report,json=validationReport,proto3,oneof"`
    }

## ImportRowError
    
    
    type ImportRowError struct {
    
    	// The row number where the error was detected.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/migrationcenter/v1/migrationcenter.proto.
    	RowNumber [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=row_number,json=rowNumber,proto3" json:"row_number,omitempty"`
    	// The name of the VM in the row.
    	VmName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=vm_name,json=vmName,proto3" json:"vm_name,omitempty"`
    	// The VM UUID.
    	VmUuid [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=vm_uuid,json=vmUuid,proto3" json:"vm_uuid,omitempty"`
    	// The list of errors detected in the row.
    	Errors []*ImportError `protobuf:"bytes,4,rep,name=errors,proto3" json:"errors,omitempty"`
    	// contains filtered or unexported fields
    }

A resource that reports the import job errors at row level.

### func (*ImportRowError) Descriptor 
    
    
    func (*ImportRowError) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportRowError.ProtoReflect.Descriptor instead.

### func (*ImportRowError) GetErrors 
    
    
    func (x *ImportRowError) GetErrors() []*ImportError

### func (*ImportRowError) GetRowNumber 
    
    
    func (x *ImportRowError) GetRowNumber() [int32](https://pkg.go.dev/builtin#int32)

Deprecated: Marked as deprecated in google/cloud/migrationcenter/v1/migrationcenter.proto.

### func (*ImportRowError) GetVmName 
    
    
    func (x *ImportRowError) GetVmName() [string](https://pkg.go.dev/builtin#string)

### func (*ImportRowError) GetVmUuid 
    
    
    func (x *ImportRowError) GetVmUuid() [string](https://pkg.go.dev/builtin#string)

### func (*ImportRowError) ProtoMessage 
    
    
    func (*ImportRowError) ProtoMessage()

### func (*ImportRowError) ProtoReflect 
    
    
    func (x *ImportRowError) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ImportRowError) Reset 
    
    
    func (x *ImportRowError) Reset()

### func (*ImportRowError) String 
    
    
    func (x *ImportRowError) String() [string](https://pkg.go.dev/builtin#string)

## Insight
    
    
    type Insight struct {
    
    	// Types that are valid to be assigned to Insight:
    	//
    	//	*Insight_MigrationInsight
    	//	*Insight_GenericInsight
    	Insight isInsight_Insight `protobuf_oneof:"insight"`
    	// contains filtered or unexported fields
    }

An insight about an asset.

### func (*Insight) Descriptor 
    
    
    func (*Insight) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Insight.ProtoReflect.Descriptor instead.

### func (*Insight) GetGenericInsight 
    
    
    func (x *Insight) GetGenericInsight() *GenericInsight

### func (*Insight) GetInsight 
    
    
    func (x *Insight) GetInsight() isInsight_Insight

### func (*Insight) GetMigrationInsight 
    
    
    func (x *Insight) GetMigrationInsight() *MigrationInsight

### func (*Insight) ProtoMessage 
    
    
    func (*Insight) ProtoMessage()

### func (*Insight) ProtoReflect 
    
    
    func (x *Insight) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Insight) Reset 
    
    
    func (x *Insight) Reset()

### func (*Insight) String 
    
    
    func (x *Insight) String() [string](https://pkg.go.dev/builtin#string)

## InsightList
    
    
    type InsightList struct {
    
    	// Output only. Insights of the list.
    	Insights []*Insight `protobuf:"bytes,1,rep,name=insights,proto3" json:"insights,omitempty"`
    	// Output only. Update timestamp.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// contains filtered or unexported fields
    }

Message containing insights list.

### func (*InsightList) Descriptor 
    
    
    func (*InsightList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use InsightList.ProtoReflect.Descriptor instead.

### func (*InsightList) GetInsights 
    
    
    func (x *InsightList) GetInsights() []*Insight

### func (*InsightList) GetUpdateTime 
    
    
    func (x *InsightList) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*InsightList) ProtoMessage 
    
    
    func (*InsightList) ProtoMessage()

### func (*InsightList) ProtoReflect 
    
    
    func (x *InsightList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*InsightList) Reset 
    
    
    func (x *InsightList) Reset()

### func (*InsightList) String 
    
    
    func (x *InsightList) String() [string](https://pkg.go.dev/builtin#string)

## Insight_GenericInsight
    
    
    type Insight_GenericInsight struct {
    	// Output only. A generic insight about an asset
    	GenericInsight *GenericInsight `protobuf:"bytes,2,opt,name=generic_insight,json=genericInsight,proto3,oneof"`
    }

## Insight_MigrationInsight
    
    
    type Insight_MigrationInsight struct {
    	// Output only. An insight about potential migrations for an asset.
    	MigrationInsight *MigrationInsight `protobuf:"bytes,1,opt,name=migration_insight,json=migrationInsight,proto3,oneof"`
    }

## LicenseType
    
    
    type LicenseType [int32](https://pkg.go.dev/builtin#int32)

The License type for premium images (RHEL, RHEL for SAP, SLES, SLES for SAP, Windows Server).

### LicenseType_LICENSE_TYPE_UNSPECIFIED, LicenseType_LICENSE_TYPE_DEFAULT, LicenseType_LICENSE_TYPE_BRING_YOUR_OWN_LICENSE
    
    
    const (
    	// Unspecified (default value).
    	LicenseType_LICENSE_TYPE_UNSPECIFIED LicenseType = 0
    	// Default Google Cloud licensing plan. Licensing is charged per usage.
    	// This a good value to start with.
    	LicenseType_LICENSE_TYPE_DEFAULT LicenseType = 1
    	// Bring-your-own-license (BYOL) plan. User provides the OS license.
    	LicenseType_LICENSE_TYPE_BRING_YOUR_OWN_LICENSE LicenseType = 2
    )

### func (LicenseType) Descriptor 
    
    
    func (LicenseType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (LicenseType) Enum 
    
    
    func (x LicenseType) Enum() *LicenseType

### func (LicenseType) EnumDescriptor 
    
    
    func (LicenseType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use LicenseType.Descriptor instead.

### func (LicenseType) Number 
    
    
    func (x LicenseType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (LicenseType) String 
    
    
    func (x LicenseType) String() [string](https://pkg.go.dev/builtin#string)

### func (LicenseType) Type 
    
    
    func (LicenseType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## ListAssetsRequest
    
    
    type ListAssetsRequest struct {
    
    	// Required. Parent value for `ListAssetsRequest`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. Server may return fewer items than requested.
    	// If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Field to sort by. See https://google.aip.dev/132#ordering for more details.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// View of the assets. Defaults to BASIC.
    	View AssetView `protobuf:"varint,6,opt,name=view,proto3,enum=google.cloud.migrationcenter.v1.AssetView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

Message for requesting a list of assets.

### func (*ListAssetsRequest) Descriptor 
    
    
    func (*ListAssetsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAssetsRequest.ProtoReflect.Descriptor instead.

### func (*ListAssetsRequest) GetFilter 
    
    
    func (x *ListAssetsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsRequest) GetOrderBy 
    
    
    func (x *ListAssetsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsRequest) GetPageSize 
    
    
    func (x *ListAssetsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListAssetsRequest) GetPageToken 
    
    
    func (x *ListAssetsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsRequest) GetParent 
    
    
    func (x *ListAssetsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsRequest) GetView 
    
    
    func (x *ListAssetsRequest) GetView() AssetView

### func (*ListAssetsRequest) ProtoMessage 
    
    
    func (*ListAssetsRequest) ProtoMessage()

### func (*ListAssetsRequest) ProtoReflect 
    
    
    func (x *ListAssetsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAssetsRequest) Reset 
    
    
    func (x *ListAssetsRequest) Reset()

### func (*ListAssetsRequest) String 
    
    
    func (x *ListAssetsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListAssetsResponse
    
    
    type ListAssetsResponse struct {
    
    	// A list of assets.
    	Assets []*Asset `protobuf:"bytes,1,rep,name=assets,proto3" json:"assets,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing assets.

### func (*ListAssetsResponse) Descriptor 
    
    
    func (*ListAssetsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListAssetsResponse.ProtoReflect.Descriptor instead.

### func (*ListAssetsResponse) GetAssets 
    
    
    func (x *ListAssetsResponse) GetAssets() []*Asset

### func (*ListAssetsResponse) GetNextPageToken 
    
    
    func (x *ListAssetsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsResponse) GetUnreachable 
    
    
    func (x *ListAssetsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListAssetsResponse) ProtoMessage 
    
    
    func (*ListAssetsResponse) ProtoMessage()

### func (*ListAssetsResponse) ProtoReflect 
    
    
    func (x *ListAssetsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListAssetsResponse) Reset 
    
    
    func (x *ListAssetsResponse) Reset()

### func (*ListAssetsResponse) String 
    
    
    func (x *ListAssetsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListErrorFramesRequest
    
    
    type ListErrorFramesRequest struct {
    
    	// Required. Parent value (the source) for `ListErrorFramesRequest`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. Server may return fewer items than requested.
    	// If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Optional. An optional view mode to control the level of details of each
    	// error frame. The default is a BASIC frame view.
    	View ErrorFrameView `protobuf:"varint,4,opt,name=view,proto3,enum=google.cloud.migrationcenter.v1.ErrorFrameView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

A request to list error frames for a source.

### func (*ListErrorFramesRequest) Descriptor 
    
    
    func (*ListErrorFramesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListErrorFramesRequest.ProtoReflect.Descriptor instead.

### func (*ListErrorFramesRequest) GetPageSize 
    
    
    func (x *ListErrorFramesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListErrorFramesRequest) GetPageToken 
    
    
    func (x *ListErrorFramesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListErrorFramesRequest) GetParent 
    
    
    func (x *ListErrorFramesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListErrorFramesRequest) GetView 
    
    
    func (x *ListErrorFramesRequest) GetView() ErrorFrameView

### func (*ListErrorFramesRequest) ProtoMessage 
    
    
    func (*ListErrorFramesRequest) ProtoMessage()

### func (*ListErrorFramesRequest) ProtoReflect 
    
    
    func (x *ListErrorFramesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListErrorFramesRequest) Reset 
    
    
    func (x *ListErrorFramesRequest) Reset()

### func (*ListErrorFramesRequest) String 
    
    
    func (x *ListErrorFramesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListErrorFramesResponse
    
    
    type ListErrorFramesResponse struct {
    
    	// The list of error frames.
    	ErrorFrames []*ErrorFrame `protobuf:"bytes,1,rep,name=error_frames,json=errorFrames,proto3" json:"error_frames,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

A response for listing error frames.

### func (*ListErrorFramesResponse) Descriptor 
    
    
    func (*ListErrorFramesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListErrorFramesResponse.ProtoReflect.Descriptor instead.

### func (*ListErrorFramesResponse) GetErrorFrames 
    
    
    func (x *ListErrorFramesResponse) GetErrorFrames() []*ErrorFrame

### func (*ListErrorFramesResponse) GetNextPageToken 
    
    
    func (x *ListErrorFramesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListErrorFramesResponse) GetUnreachable 
    
    
    func (x *ListErrorFramesResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListErrorFramesResponse) ProtoMessage 
    
    
    func (*ListErrorFramesResponse) ProtoMessage()

### func (*ListErrorFramesResponse) ProtoReflect 
    
    
    func (x *ListErrorFramesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListErrorFramesResponse) Reset 
    
    
    func (x *ListErrorFramesResponse) Reset()

### func (*ListErrorFramesResponse) String 
    
    
    func (x *ListErrorFramesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListGroupsRequest
    
    
    type ListGroupsRequest struct {
    
    	// Required. Parent value for `ListGroupsRequest`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. Server may return fewer items than requested.
    	// If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Field to sort by. See https://google.aip.dev/132#ordering for more details.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

A request to list groups.

### func (*ListGroupsRequest) Descriptor 
    
    
    func (*ListGroupsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListGroupsRequest.ProtoReflect.Descriptor instead.

### func (*ListGroupsRequest) GetFilter 
    
    
    func (x *ListGroupsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListGroupsRequest) GetOrderBy 
    
    
    func (x *ListGroupsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListGroupsRequest) GetPageSize 
    
    
    func (x *ListGroupsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListGroupsRequest) GetPageToken 
    
    
    func (x *ListGroupsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListGroupsRequest) GetParent 
    
    
    func (x *ListGroupsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListGroupsRequest) ProtoMessage 
    
    
    func (*ListGroupsRequest) ProtoMessage()

### func (*ListGroupsRequest) ProtoReflect 
    
    
    func (x *ListGroupsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListGroupsRequest) Reset 
    
    
    func (x *ListGroupsRequest) Reset()

### func (*ListGroupsRequest) String 
    
    
    func (x *ListGroupsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListGroupsResponse
    
    
    type ListGroupsResponse struct {
    
    	// The list of Group
    	Groups []*Group `protobuf:"bytes,1,rep,name=groups,proto3" json:"groups,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

A response for listing groups.

### func (*ListGroupsResponse) Descriptor 
    
    
    func (*ListGroupsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListGroupsResponse.ProtoReflect.Descriptor instead.

### func (*ListGroupsResponse) GetGroups 
    
    
    func (x *ListGroupsResponse) GetGroups() []*Group

### func (*ListGroupsResponse) GetNextPageToken 
    
    
    func (x *ListGroupsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListGroupsResponse) GetUnreachable 
    
    
    func (x *ListGroupsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListGroupsResponse) ProtoMessage 
    
    
    func (*ListGroupsResponse) ProtoMessage()

### func (*ListGroupsResponse) ProtoReflect 
    
    
    func (x *ListGroupsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListGroupsResponse) Reset 
    
    
    func (x *ListGroupsResponse) Reset()

### func (*ListGroupsResponse) String 
    
    
    func (x *ListGroupsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListImportDataFilesRequest
    
    
    type ListImportDataFilesRequest struct {
    
    	// Required. Name of the parent of the `ImportDataFiles` resource.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of data files to return. The service may return
    	// fewer than this value. If unspecified, at most 500 data files will be
    	// returned. The maximum value is 1000; values above 1000 will be coerced to
    	// 1000.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A page token, received from a previous `ListImportDataFiles` call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListImportDataFiles`
    	// must match the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Field to sort by. See https://google.aip.dev/132#ordering for more details.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

A request to list import data files of an import job.

### func (*ListImportDataFilesRequest) Descriptor 
    
    
    func (*ListImportDataFilesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListImportDataFilesRequest.ProtoReflect.Descriptor instead.

### func (*ListImportDataFilesRequest) GetFilter 
    
    
    func (x *ListImportDataFilesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportDataFilesRequest) GetOrderBy 
    
    
    func (x *ListImportDataFilesRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportDataFilesRequest) GetPageSize 
    
    
    func (x *ListImportDataFilesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListImportDataFilesRequest) GetPageToken 
    
    
    func (x *ListImportDataFilesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportDataFilesRequest) GetParent 
    
    
    func (x *ListImportDataFilesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportDataFilesRequest) ProtoMessage 
    
    
    func (*ListImportDataFilesRequest) ProtoMessage()

### func (*ListImportDataFilesRequest) ProtoReflect 
    
    
    func (x *ListImportDataFilesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListImportDataFilesRequest) Reset 
    
    
    func (x *ListImportDataFilesRequest) Reset()

### func (*ListImportDataFilesRequest) String 
    
    
    func (x *ListImportDataFilesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListImportDataFilesResponse
    
    
    type ListImportDataFilesResponse struct {
    
    	// The list of import data files.
    	ImportDataFiles []*ImportDataFile `protobuf:"bytes,1,rep,name=import_data_files,json=importDataFiles,proto3" json:"import_data_files,omitempty"`
    	// A token that can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response for listing payload files of an import job.

### func (*ListImportDataFilesResponse) Descriptor 
    
    
    func (*ListImportDataFilesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListImportDataFilesResponse.ProtoReflect.Descriptor instead.

### func (*ListImportDataFilesResponse) GetImportDataFiles 
    
    
    func (x *ListImportDataFilesResponse) GetImportDataFiles() []*ImportDataFile

### func (*ListImportDataFilesResponse) GetNextPageToken 
    
    
    func (x *ListImportDataFilesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportDataFilesResponse) GetUnreachable 
    
    
    func (x *ListImportDataFilesResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListImportDataFilesResponse) ProtoMessage 
    
    
    func (*ListImportDataFilesResponse) ProtoMessage()

### func (*ListImportDataFilesResponse) ProtoReflect 
    
    
    func (x *ListImportDataFilesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListImportDataFilesResponse) Reset 
    
    
    func (x *ListImportDataFilesResponse) Reset()

### func (*ListImportDataFilesResponse) String 
    
    
    func (x *ListImportDataFilesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListImportJobsRequest
    
    
    type ListImportJobsRequest struct {
    
    	// Required. Parent value for `ListImportJobsRequest`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. Server may return fewer items than requested.
    	// If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Field to sort by. See https://google.aip.dev/132#ordering for more details.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// Optional. The level of details of each import job.
    	// Default value is BASIC.
    	View ImportJobView `protobuf:"varint,6,opt,name=view,proto3,enum=google.cloud.migrationcenter.v1.ImportJobView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

A request to list import jobs.

### func (*ListImportJobsRequest) Descriptor 
    
    
    func (*ListImportJobsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListImportJobsRequest.ProtoReflect.Descriptor instead.

### func (*ListImportJobsRequest) GetFilter 
    
    
    func (x *ListImportJobsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportJobsRequest) GetOrderBy 
    
    
    func (x *ListImportJobsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportJobsRequest) GetPageSize 
    
    
    func (x *ListImportJobsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListImportJobsRequest) GetPageToken 
    
    
    func (x *ListImportJobsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportJobsRequest) GetParent 
    
    
    func (x *ListImportJobsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportJobsRequest) GetView 
    
    
    func (x *ListImportJobsRequest) GetView() ImportJobView

### func (*ListImportJobsRequest) ProtoMessage 
    
    
    func (*ListImportJobsRequest) ProtoMessage()

### func (*ListImportJobsRequest) ProtoReflect 
    
    
    func (x *ListImportJobsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListImportJobsRequest) Reset 
    
    
    func (x *ListImportJobsRequest) Reset()

### func (*ListImportJobsRequest) String 
    
    
    func (x *ListImportJobsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListImportJobsResponse
    
    
    type ListImportJobsResponse struct {
    
    	// The list of import jobs.
    	ImportJobs []*ImportJob `protobuf:"bytes,1,rep,name=import_jobs,json=importJobs,proto3" json:"import_jobs,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

A response for listing import jobs.

### func (*ListImportJobsResponse) Descriptor 
    
    
    func (*ListImportJobsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListImportJobsResponse.ProtoReflect.Descriptor instead.

### func (*ListImportJobsResponse) GetImportJobs 
    
    
    func (x *ListImportJobsResponse) GetImportJobs() []*ImportJob

### func (*ListImportJobsResponse) GetNextPageToken 
    
    
    func (x *ListImportJobsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListImportJobsResponse) GetUnreachable 
    
    
    func (x *ListImportJobsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListImportJobsResponse) ProtoMessage 
    
    
    func (*ListImportJobsResponse) ProtoMessage()

### func (*ListImportJobsResponse) ProtoReflect 
    
    
    func (x *ListImportJobsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListImportJobsResponse) Reset 
    
    
    func (x *ListImportJobsResponse) Reset()

### func (*ListImportJobsResponse) String 
    
    
    func (x *ListImportJobsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListPreferenceSetsRequest
    
    
    type ListPreferenceSetsRequest struct {
    
    	// Required. Parent value for `ListPreferenceSetsRequest`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. Server may return fewer items than requested.
    	// If unspecified, at most 500 preference sets will be returned.
    	// The maximum value is 1000; values above 1000 will be coerced to 1000.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Field to sort by. See https://google.aip.dev/132#ordering for more details.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

Request for listing preference sets.

### func (*ListPreferenceSetsRequest) Descriptor 
    
    
    func (*ListPreferenceSetsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListPreferenceSetsRequest.ProtoReflect.Descriptor instead.

### func (*ListPreferenceSetsRequest) GetOrderBy 
    
    
    func (x *ListPreferenceSetsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListPreferenceSetsRequest) GetPageSize 
    
    
    func (x *ListPreferenceSetsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListPreferenceSetsRequest) GetPageToken 
    
    
    func (x *ListPreferenceSetsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListPreferenceSetsRequest) GetParent 
    
    
    func (x *ListPreferenceSetsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListPreferenceSetsRequest) ProtoMessage 
    
    
    func (*ListPreferenceSetsRequest) ProtoMessage()

### func (*ListPreferenceSetsRequest) ProtoReflect 
    
    
    func (x *ListPreferenceSetsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListPreferenceSetsRequest) Reset 
    
    
    func (x *ListPreferenceSetsRequest) Reset()

### func (*ListPreferenceSetsRequest) String 
    
    
    func (x *ListPreferenceSetsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListPreferenceSetsResponse
    
    
    type ListPreferenceSetsResponse struct {
    
    	// The list of PreferenceSets
    	PreferenceSets []*PreferenceSet `protobuf:"bytes,1,rep,name=preference_sets,json=preferenceSets,proto3" json:"preference_sets,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing preference sets.

### func (*ListPreferenceSetsResponse) Descriptor 
    
    
    func (*ListPreferenceSetsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListPreferenceSetsResponse.ProtoReflect.Descriptor instead.

### func (*ListPreferenceSetsResponse) GetNextPageToken 
    
    
    func (x *ListPreferenceSetsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListPreferenceSetsResponse) GetPreferenceSets 
    
    
    func (x *ListPreferenceSetsResponse) GetPreferenceSets() []*PreferenceSet

### func (*ListPreferenceSetsResponse) GetUnreachable 
    
    
    func (x *ListPreferenceSetsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListPreferenceSetsResponse) ProtoMessage 
    
    
    func (*ListPreferenceSetsResponse) ProtoMessage()

### func (*ListPreferenceSetsResponse) ProtoReflect 
    
    
    func (x *ListPreferenceSetsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListPreferenceSetsResponse) Reset 
    
    
    func (x *ListPreferenceSetsResponse) Reset()

### func (*ListPreferenceSetsResponse) String 
    
    
    func (x *ListPreferenceSetsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListReportConfigsRequest
    
    
    type ListReportConfigsRequest struct {
    
    	// Required. Parent value for `ListReportConfigsRequest`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. Server may return fewer items than requested.
    	// If unspecified, server will pick an appropriate default.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Field to sort by. See https://google.aip.dev/132#ordering for more details.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

A request to get a list of `ReportConfig` resources.

### func (*ListReportConfigsRequest) Descriptor 
    
    
    func (*ListReportConfigsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReportConfigsRequest.ProtoReflect.Descriptor instead.

### func (*ListReportConfigsRequest) GetFilter 
    
    
    func (x *ListReportConfigsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsRequest) GetOrderBy 
    
    
    func (x *ListReportConfigsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsRequest) GetPageSize 
    
    
    func (x *ListReportConfigsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListReportConfigsRequest) GetPageToken 
    
    
    func (x *ListReportConfigsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsRequest) GetParent 
    
    
    func (x *ListReportConfigsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsRequest) ProtoMessage 
    
    
    func (*ListReportConfigsRequest) ProtoMessage()

### func (*ListReportConfigsRequest) ProtoReflect 
    
    
    func (x *ListReportConfigsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReportConfigsRequest) Reset 
    
    
    func (x *ListReportConfigsRequest) Reset()

### func (*ListReportConfigsRequest) String 
    
    
    func (x *ListReportConfigsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListReportConfigsResponse
    
    
    type ListReportConfigsResponse struct {
    
    	// A list of report configs.
    	ReportConfigs []*ReportConfig `protobuf:"bytes,1,rep,name=report_configs,json=reportConfigs,proto3" json:"report_configs,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing report configs.

### func (*ListReportConfigsResponse) Descriptor 
    
    
    func (*ListReportConfigsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReportConfigsResponse.ProtoReflect.Descriptor instead.

### func (*ListReportConfigsResponse) GetNextPageToken 
    
    
    func (x *ListReportConfigsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsResponse) GetReportConfigs 
    
    
    func (x *ListReportConfigsResponse) GetReportConfigs() []*ReportConfig

### func (*ListReportConfigsResponse) GetUnreachable 
    
    
    func (x *ListReportConfigsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListReportConfigsResponse) ProtoMessage 
    
    
    func (*ListReportConfigsResponse) ProtoMessage()

### func (*ListReportConfigsResponse) ProtoReflect 
    
    
    func (x *ListReportConfigsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReportConfigsResponse) Reset 
    
    
    func (x *ListReportConfigsResponse) Reset()

### func (*ListReportConfigsResponse) String 
    
    
    func (x *ListReportConfigsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListReportsRequest
    
    
    type ListReportsRequest struct {
    
    	// Required. Parent value for `ListReportsRequest`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. The server may return fewer items than requested.
    	// If unspecified, the server will pick an appropriate default value.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results that the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Field to sort by. See https://google.aip.dev/132#ordering for more details.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// Determines what information to retrieve for each Report.
    	View ReportView `protobuf:"varint,6,opt,name=view,proto3,enum=google.cloud.migrationcenter.v1.ReportView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

A request for a list of Reports.

### func (*ListReportsRequest) Descriptor 
    
    
    func (*ListReportsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReportsRequest.ProtoReflect.Descriptor instead.

### func (*ListReportsRequest) GetFilter 
    
    
    func (x *ListReportsRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportsRequest) GetOrderBy 
    
    
    func (x *ListReportsRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportsRequest) GetPageSize 
    
    
    func (x *ListReportsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListReportsRequest) GetPageToken 
    
    
    func (x *ListReportsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportsRequest) GetParent 
    
    
    func (x *ListReportsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportsRequest) GetView 
    
    
    func (x *ListReportsRequest) GetView() ReportView

### func (*ListReportsRequest) ProtoMessage 
    
    
    func (*ListReportsRequest) ProtoMessage()

### func (*ListReportsRequest) ProtoReflect 
    
    
    func (x *ListReportsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReportsRequest) Reset 
    
    
    func (x *ListReportsRequest) Reset()

### func (*ListReportsRequest) String 
    
    
    func (x *ListReportsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListReportsResponse
    
    
    type ListReportsResponse struct {
    
    	// The list of Reports.
    	Reports []*Report `protobuf:"bytes,1,rep,name=reports,proto3" json:"reports,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing Reports.

### func (*ListReportsResponse) Descriptor 
    
    
    func (*ListReportsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListReportsResponse.ProtoReflect.Descriptor instead.

### func (*ListReportsResponse) GetNextPageToken 
    
    
    func (x *ListReportsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListReportsResponse) GetReports 
    
    
    func (x *ListReportsResponse) GetReports() []*Report

### func (*ListReportsResponse) GetUnreachable 
    
    
    func (x *ListReportsResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListReportsResponse) ProtoMessage 
    
    
    func (*ListReportsResponse) ProtoMessage()

### func (*ListReportsResponse) ProtoReflect 
    
    
    func (x *ListReportsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListReportsResponse) Reset 
    
    
    func (x *ListReportsResponse) Reset()

### func (*ListReportsResponse) String 
    
    
    func (x *ListReportsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListSourcesRequest
    
    
    type ListSourcesRequest struct {
    
    	// Required. Parent value for `ListSourcesRequest`.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Requested page size. The server may return fewer items than requested.
    	// If unspecified, the server will pick an appropriate default value.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A token identifying a page of results that the server should return.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// Filtering results.
    	Filter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=filter,proto3" json:"filter,omitempty"`
    	// Field to sort by. See https://google.aip.dev/132#ordering for more details.
    	OrderBy [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=order_by,json=orderBy,proto3" json:"order_by,omitempty"`
    	// contains filtered or unexported fields
    }

A request for a list of sources.

### func (*ListSourcesRequest) Descriptor 
    
    
    func (*ListSourcesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSourcesRequest.ProtoReflect.Descriptor instead.

### func (*ListSourcesRequest) GetFilter 
    
    
    func (x *ListSourcesRequest) GetFilter() [string](https://pkg.go.dev/builtin#string)

### func (*ListSourcesRequest) GetOrderBy 
    
    
    func (x *ListSourcesRequest) GetOrderBy() [string](https://pkg.go.dev/builtin#string)

### func (*ListSourcesRequest) GetPageSize 
    
    
    func (x *ListSourcesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListSourcesRequest) GetPageToken 
    
    
    func (x *ListSourcesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSourcesRequest) GetParent 
    
    
    func (x *ListSourcesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListSourcesRequest) ProtoMessage 
    
    
    func (*ListSourcesRequest) ProtoMessage()

### func (*ListSourcesRequest) ProtoReflect 
    
    
    func (x *ListSourcesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSourcesRequest) Reset 
    
    
    func (x *ListSourcesRequest) Reset()

### func (*ListSourcesRequest) String 
    
    
    func (x *ListSourcesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListSourcesResponse
    
    
    type ListSourcesResponse struct {
    
    	// The list of sources.
    	Sources []*Source `protobuf:"bytes,1,rep,name=sources,proto3" json:"sources,omitempty"`
    	// A token identifying a page of results the server should return.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// Locations that could not be reached.
    	Unreachable [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=unreachable,proto3" json:"unreachable,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for listing sources.

### func (*ListSourcesResponse) Descriptor 
    
    
    func (*ListSourcesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListSourcesResponse.ProtoReflect.Descriptor instead.

### func (*ListSourcesResponse) GetNextPageToken 
    
    
    func (x *ListSourcesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListSourcesResponse) GetSources 
    
    
    func (x *ListSourcesResponse) GetSources() []*Source

### func (*ListSourcesResponse) GetUnreachable 
    
    
    func (x *ListSourcesResponse) GetUnreachable() [][string](https://pkg.go.dev/builtin#string)

### func (*ListSourcesResponse) ProtoMessage 
    
    
    func (*ListSourcesResponse) ProtoMessage()

### func (*ListSourcesResponse) ProtoReflect 
    
    
    func (x *ListSourcesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListSourcesResponse) Reset 
    
    
    func (x *ListSourcesResponse) Reset()

### func (*ListSourcesResponse) String 
    
    
    func (x *ListSourcesResponse) String() [string](https://pkg.go.dev/builtin#string)

## MachineArchitectureDetails
    
    
    type MachineArchitectureDetails struct {
    
    	// CPU architecture, e.g., "x64-based PC", "x86_64", "i686" etc.
    	CpuArchitecture [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=cpu_architecture,json=cpuArchitecture,proto3" json:"cpu_architecture,omitempty"`
    	// CPU name, e.g., "Intel Xeon E5-2690", "AMD EPYC 7571" etc.
    	CpuName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=cpu_name,json=cpuName,proto3" json:"cpu_name,omitempty"`
    	// Hardware vendor.
    	Vendor [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=vendor,proto3" json:"vendor,omitempty"`
    	// Number of CPU threads allocated to the machine.
    	CpuThreadCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=cpu_thread_count,json=cpuThreadCount,proto3" json:"cpu_thread_count,omitempty"`
    	// Number of processor sockets allocated to the machine.
    	CpuSocketCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=cpu_socket_count,json=cpuSocketCount,proto3" json:"cpu_socket_count,omitempty"`
    	// BIOS Details.
    	Bios *BiosDetails `protobuf:"bytes,6,opt,name=bios,proto3" json:"bios,omitempty"`
    	// Firmware type.
    	FirmwareType MachineArchitectureDetails_FirmwareType `protobuf:"varint,7,opt,name=firmware_type,json=firmwareType,proto3,enum=google.cloud.migrationcenter.v1.MachineArchitectureDetails_FirmwareType" json:"firmware_type,omitempty"`
    	// CPU hyper-threading support.
    	Hyperthreading MachineArchitectureDetails_CpuHyperThreading `protobuf:"varint,8,opt,name=hyperthreading,proto3,enum=google.cloud.migrationcenter.v1.MachineArchitectureDetails_CpuHyperThreading" json:"hyperthreading,omitempty"`
    	// contains filtered or unexported fields
    }

Details of the machine architecture.

### func (*MachineArchitectureDetails) Descriptor 
    
    
    func (*MachineArchitectureDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MachineArchitectureDetails.ProtoReflect.Descriptor instead.

### func (*MachineArchitectureDetails) GetBios 
    
    
    func (x *MachineArchitectureDetails) GetBios() *BiosDetails

### func (*MachineArchitectureDetails) GetCpuArchitecture 
    
    
    func (x *MachineArchitectureDetails) GetCpuArchitecture() [string](https://pkg.go.dev/builtin#string)

### func (*MachineArchitectureDetails) GetCpuName 
    
    
    func (x *MachineArchitectureDetails) GetCpuName() [string](https://pkg.go.dev/builtin#string)

### func (*MachineArchitectureDetails) GetCpuSocketCount 
    
    
    func (x *MachineArchitectureDetails) GetCpuSocketCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*MachineArchitectureDetails) GetCpuThreadCount 
    
    
    func (x *MachineArchitectureDetails) GetCpuThreadCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*MachineArchitectureDetails) GetFirmwareType 
    
    
    func (x *MachineArchitectureDetails) GetFirmwareType() MachineArchitectureDetails_FirmwareType

### func (*MachineArchitectureDetails) GetHyperthreading 
    
    
    func (x *MachineArchitectureDetails) GetHyperthreading() MachineArchitectureDetails_CpuHyperThreading

### func (*MachineArchitectureDetails) GetVendor 
    
    
    func (x *MachineArchitectureDetails) GetVendor() [string](https://pkg.go.dev/builtin#string)

### func (*MachineArchitectureDetails) ProtoMessage 
    
    
    func (*MachineArchitectureDetails) ProtoMessage()

### func (*MachineArchitectureDetails) ProtoReflect 
    
    
    func (x *MachineArchitectureDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MachineArchitectureDetails) Reset 
    
    
    func (x *MachineArchitectureDetails) Reset()

### func (*MachineArchitectureDetails) String 
    
    
    func (x *MachineArchitectureDetails) String() [string](https://pkg.go.dev/builtin#string)

## MachineArchitectureDetails_CpuHyperThreading
    
    
    type MachineArchitectureDetails_CpuHyperThreading [int32](https://pkg.go.dev/builtin#int32)

CPU hyper-threading support.

### MachineArchitectureDetails_CPU_HYPER_THREADING_UNSPECIFIED, MachineArchitectureDetails_DISABLED, MachineArchitectureDetails_ENABLED
    
    
    const (
    	// Unspecified or unknown.
    	MachineArchitectureDetails_CPU_HYPER_THREADING_UNSPECIFIED MachineArchitectureDetails_CpuHyperThreading = 0
    	// Hyper-threading is disabled.
    	MachineArchitectureDetails_DISABLED MachineArchitectureDetails_CpuHyperThreading = 1
    	// Hyper-threading is enabled.
    	MachineArchitectureDetails_ENABLED MachineArchitectureDetails_CpuHyperThreading = 2
    )

### func (MachineArchitectureDetails_CpuHyperThreading) Descriptor 
    
    
    func (MachineArchitectureDetails_CpuHyperThreading) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (MachineArchitectureDetails_CpuHyperThreading) Enum 
    
    
    func (x MachineArchitectureDetails_CpuHyperThreading) Enum() *MachineArchitectureDetails_CpuHyperThreading

### func (MachineArchitectureDetails_CpuHyperThreading) EnumDescriptor 
    
    
    func (MachineArchitectureDetails_CpuHyperThreading) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MachineArchitectureDetails_CpuHyperThreading.Descriptor instead.

### func (MachineArchitectureDetails_CpuHyperThreading) Number 
    
    
    func (x MachineArchitectureDetails_CpuHyperThreading) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (MachineArchitectureDetails_CpuHyperThreading) String 
    
    
    func (x MachineArchitectureDetails_CpuHyperThreading) String() [string](https://pkg.go.dev/builtin#string)

### func (MachineArchitectureDetails_CpuHyperThreading) Type 
    
    
    func (MachineArchitectureDetails_CpuHyperThreading) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## MachineArchitectureDetails_FirmwareType
    
    
    type MachineArchitectureDetails_FirmwareType [int32](https://pkg.go.dev/builtin#int32)

Firmware type.

### MachineArchitectureDetails_FIRMWARE_TYPE_UNSPECIFIED, MachineArchitectureDetails_BIOS, MachineArchitectureDetails_EFI
    
    
    const (
    	// Unspecified or unknown.
    	MachineArchitectureDetails_FIRMWARE_TYPE_UNSPECIFIED MachineArchitectureDetails_FirmwareType = 0
    	// BIOS firmware.
    	MachineArchitectureDetails_BIOS MachineArchitectureDetails_FirmwareType = 1
    	// EFI firmware.
    	MachineArchitectureDetails_EFI MachineArchitectureDetails_FirmwareType = 2
    )

### func (MachineArchitectureDetails_FirmwareType) Descriptor 
    
    
    func (MachineArchitectureDetails_FirmwareType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (MachineArchitectureDetails_FirmwareType) Enum 
    
    
    func (x MachineArchitectureDetails_FirmwareType) Enum() *MachineArchitectureDetails_FirmwareType

### func (MachineArchitectureDetails_FirmwareType) EnumDescriptor 
    
    
    func (MachineArchitectureDetails_FirmwareType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MachineArchitectureDetails_FirmwareType.Descriptor instead.

### func (MachineArchitectureDetails_FirmwareType) Number 
    
    
    func (x MachineArchitectureDetails_FirmwareType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (MachineArchitectureDetails_FirmwareType) String 
    
    
    func (x MachineArchitectureDetails_FirmwareType) String() [string](https://pkg.go.dev/builtin#string)

### func (MachineArchitectureDetails_FirmwareType) Type 
    
    
    func (MachineArchitectureDetails_FirmwareType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## MachineDetails
    
    
    type MachineDetails struct {
    
    	// Machine unique identifier.
    	Uuid [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=uuid,proto3" json:"uuid,omitempty"`
    	// Machine name.
    	MachineName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=machine_name,json=machineName,proto3" json:"machine_name,omitempty"`
    	// Machine creation time.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Number of CPU cores in the machine. Must be non-negative.
    	CoreCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,opt,name=core_count,json=coreCount,proto3" json:"core_count,omitempty"`
    	// The amount of memory in the machine. Must be non-negative.
    	MemoryMb [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=memory_mb,json=memoryMb,proto3" json:"memory_mb,omitempty"`
    	// Power state of the machine.
    	PowerState MachineDetails_PowerState `protobuf:"varint,6,opt,name=power_state,json=powerState,proto3,enum=google.cloud.migrationcenter.v1.MachineDetails_PowerState" json:"power_state,omitempty"`
    	// Architecture details (vendor, CPU architecture).
    	Architecture *MachineArchitectureDetails `protobuf:"bytes,7,opt,name=architecture,proto3" json:"architecture,omitempty"`
    	// Guest OS information.
    	GuestOs *GuestOsDetails `protobuf:"bytes,8,opt,name=guest_os,json=guestOs,proto3" json:"guest_os,omitempty"`
    	// Network details.
    	Network *MachineNetworkDetails `protobuf:"bytes,9,opt,name=network,proto3" json:"network,omitempty"`
    	// Disk details.
    	Disks *MachineDiskDetails `protobuf:"bytes,10,opt,name=disks,proto3" json:"disks,omitempty"`
    	// Platform specific information.
    	Platform *PlatformDetails `protobuf:"bytes,11,opt,name=platform,proto3" json:"platform,omitempty"`
    	// contains filtered or unexported fields
    }

Details of a machine.

### func (*MachineDetails) Descriptor 
    
    
    func (*MachineDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MachineDetails.ProtoReflect.Descriptor instead.

### func (*MachineDetails) GetArchitecture 
    
    
    func (x *MachineDetails) GetArchitecture() *MachineArchitectureDetails

### func (*MachineDetails) GetCoreCount 
    
    
    func (x *MachineDetails) GetCoreCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*MachineDetails) GetCreateTime 
    
    
    func (x *MachineDetails) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*MachineDetails) GetDisks 
    
    
    func (x *MachineDetails) GetDisks() *MachineDiskDetails

### func (*MachineDetails) GetGuestOs 
    
    
    func (x *MachineDetails) GetGuestOs() *GuestOsDetails

### func (*MachineDetails) GetMachineName 
    
    
    func (x *MachineDetails) GetMachineName() [string](https://pkg.go.dev/builtin#string)

### func (*MachineDetails) GetMemoryMb 
    
    
    func (x *MachineDetails) GetMemoryMb() [int32](https://pkg.go.dev/builtin#int32)

### func (*MachineDetails) GetNetwork 
    
    
    func (x *MachineDetails) GetNetwork() *MachineNetworkDetails

### func (*MachineDetails) GetPlatform 
    
    
    func (x *MachineDetails) GetPlatform() *PlatformDetails

### func (*MachineDetails) GetPowerState 
    
    
    func (x *MachineDetails) GetPowerState() MachineDetails_PowerState

### func (*MachineDetails) GetUuid 
    
    
    func (x *MachineDetails) GetUuid() [string](https://pkg.go.dev/builtin#string)

### func (*MachineDetails) ProtoMessage 
    
    
    func (*MachineDetails) ProtoMessage()

### func (*MachineDetails) ProtoReflect 
    
    
    func (x *MachineDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MachineDetails) Reset 
    
    
    func (x *MachineDetails) Reset()

### func (*MachineDetails) String 
    
    
    func (x *MachineDetails) String() [string](https://pkg.go.dev/builtin#string)

## MachineDetails_PowerState
    
    
    type MachineDetails_PowerState [int32](https://pkg.go.dev/builtin#int32)

Machine power state.

### MachineDetails_POWER_STATE_UNSPECIFIED, MachineDetails_PENDING, MachineDetails_ACTIVE, MachineDetails_SUSPENDING, MachineDetails_SUSPENDED, MachineDetails_DELETING, MachineDetails_DELETED
    
    
    const (
    	// Power state is unknown.
    	MachineDetails_POWER_STATE_UNSPECIFIED MachineDetails_PowerState = 0
    	// The machine is preparing to enter the ACTIVE state. An instance may enter
    	// the PENDING state when it launches for the first time, or when it is
    	// started after being in the SUSPENDED state.
    	MachineDetails_PENDING MachineDetails_PowerState = 1
    	// The machine is active.
    	MachineDetails_ACTIVE MachineDetails_PowerState = 2
    	// The machine is being turned off.
    	MachineDetails_SUSPENDING MachineDetails_PowerState = 3
    	// The machine is off.
    	MachineDetails_SUSPENDED MachineDetails_PowerState = 4
    	// The machine is being deleted from the hosting platform.
    	MachineDetails_DELETING MachineDetails_PowerState = 5
    	// The machine is deleted from the hosting platform.
    	MachineDetails_DELETED MachineDetails_PowerState = 6
    )

### func (MachineDetails_PowerState) Descriptor 
    
    
    func (MachineDetails_PowerState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (MachineDetails_PowerState) Enum 
    
    
    func (x MachineDetails_PowerState) Enum() *MachineDetails_PowerState

### func (MachineDetails_PowerState) EnumDescriptor 
    
    
    func (MachineDetails_PowerState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MachineDetails_PowerState.Descriptor instead.

### func (MachineDetails_PowerState) Number 
    
    
    func (x MachineDetails_PowerState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (MachineDetails_PowerState) String 
    
    
    func (x MachineDetails_PowerState) String() [string](https://pkg.go.dev/builtin#string)

### func (MachineDetails_PowerState) Type 
    
    
    func (MachineDetails_PowerState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## MachineDiskDetails
    
    
    type MachineDiskDetails struct {
    
    	// Disk total Capacity.
    	TotalCapacityBytes [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=total_capacity_bytes,json=totalCapacityBytes,proto3" json:"total_capacity_bytes,omitempty"`
    	// Total disk free space.
    	TotalFreeBytes [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=total_free_bytes,json=totalFreeBytes,proto3" json:"total_free_bytes,omitempty"`
    	// List of disks.
    	Disks *DiskEntryList `protobuf:"bytes,3,opt,name=disks,proto3" json:"disks,omitempty"`
    	// contains filtered or unexported fields
    }

Details of machine disks.

### func (*MachineDiskDetails) Descriptor 
    
    
    func (*MachineDiskDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MachineDiskDetails.ProtoReflect.Descriptor instead.

### func (*MachineDiskDetails) GetDisks 
    
    
    func (x *MachineDiskDetails) GetDisks() *DiskEntryList

### func (*MachineDiskDetails) GetTotalCapacityBytes 
    
    
    func (x *MachineDiskDetails) GetTotalCapacityBytes() [int64](https://pkg.go.dev/builtin#int64)

### func (*MachineDiskDetails) GetTotalFreeBytes 
    
    
    func (x *MachineDiskDetails) GetTotalFreeBytes() [int64](https://pkg.go.dev/builtin#int64)

### func (*MachineDiskDetails) ProtoMessage 
    
    
    func (*MachineDiskDetails) ProtoMessage()

### func (*MachineDiskDetails) ProtoReflect 
    
    
    func (x *MachineDiskDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MachineDiskDetails) Reset 
    
    
    func (x *MachineDiskDetails) Reset()

### func (*MachineDiskDetails) String 
    
    
    func (x *MachineDiskDetails) String() [string](https://pkg.go.dev/builtin#string)

## MachineNetworkDetails
    
    
    type MachineNetworkDetails struct {
    
    	// The primary IP address of the machine.
    	PrimaryIpAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=primary_ip_address,json=primaryIpAddress,proto3" json:"primary_ip_address,omitempty"`
    	// The public IP address of the machine.
    	PublicIpAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=public_ip_address,json=publicIpAddress,proto3" json:"public_ip_address,omitempty"`
    	// MAC address of the machine.
    	// This property is used to uniqly identify the machine.
    	PrimaryMacAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=primary_mac_address,json=primaryMacAddress,proto3" json:"primary_mac_address,omitempty"`
    	// List of network adapters.
    	Adapters *NetworkAdapterList `protobuf:"bytes,4,opt,name=adapters,proto3" json:"adapters,omitempty"`
    	// contains filtered or unexported fields
    }

Details of network adapters and settings.

### func (*MachineNetworkDetails) Descriptor 
    
    
    func (*MachineNetworkDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MachineNetworkDetails.ProtoReflect.Descriptor instead.

### func (*MachineNetworkDetails) GetAdapters 
    
    
    func (x *MachineNetworkDetails) GetAdapters() *NetworkAdapterList

### func (*MachineNetworkDetails) GetPrimaryIpAddress 
    
    
    func (x *MachineNetworkDetails) GetPrimaryIpAddress() [string](https://pkg.go.dev/builtin#string)

### func (*MachineNetworkDetails) GetPrimaryMacAddress 
    
    
    func (x *MachineNetworkDetails) GetPrimaryMacAddress() [string](https://pkg.go.dev/builtin#string)

### func (*MachineNetworkDetails) GetPublicIpAddress 
    
    
    func (x *MachineNetworkDetails) GetPublicIpAddress() [string](https://pkg.go.dev/builtin#string)

### func (*MachineNetworkDetails) ProtoMessage 
    
    
    func (*MachineNetworkDetails) ProtoMessage()

### func (*MachineNetworkDetails) ProtoReflect 
    
    
    func (x *MachineNetworkDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MachineNetworkDetails) Reset 
    
    
    func (x *MachineNetworkDetails) Reset()

### func (*MachineNetworkDetails) String 
    
    
    func (x *MachineNetworkDetails) String() [string](https://pkg.go.dev/builtin#string)

## MachinePreferences
    
    
    type MachinePreferences struct {
    
    	// Compute Engine machine series to consider for insights and recommendations.
    	// If empty, no restriction is applied on the machine series.
    	AllowedMachineSeries []*MachineSeries `protobuf:"bytes,1,rep,name=allowed_machine_series,json=allowedMachineSeries,proto3" json:"allowed_machine_series,omitempty"`
    	// contains filtered or unexported fields
    }

The type of machines to consider when calculating virtual machine migration insights and recommendations. Not all machine types are available in all zones and regions.

### func (*MachinePreferences) Descriptor 
    
    
    func (*MachinePreferences) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MachinePreferences.ProtoReflect.Descriptor instead.

### func (*MachinePreferences) GetAllowedMachineSeries 
    
    
    func (x *MachinePreferences) GetAllowedMachineSeries() []*MachineSeries

### func (*MachinePreferences) ProtoMessage 
    
    
    func (*MachinePreferences) ProtoMessage()

### func (*MachinePreferences) ProtoReflect 
    
    
    func (x *MachinePreferences) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MachinePreferences) Reset 
    
    
    func (x *MachinePreferences) Reset()

### func (*MachinePreferences) String 
    
    
    func (x *MachinePreferences) String() [string](https://pkg.go.dev/builtin#string)

## MachineSeries
    
    
    type MachineSeries struct {
    
    	// Code to identify a Compute Engine machine series. Consult
    	// https://cloud.google.com/compute/docs/machine-resource#machine_type_comparison
    	// for more details on the available series.
    	Code [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=code,proto3" json:"code,omitempty"`
    	// contains filtered or unexported fields
    }

A Compute Engine machine series.

### func (*MachineSeries) Descriptor 
    
    
    func (*MachineSeries) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MachineSeries.ProtoReflect.Descriptor instead.

### func (*MachineSeries) GetCode 
    
    
    func (x *MachineSeries) GetCode() [string](https://pkg.go.dev/builtin#string)

### func (*MachineSeries) ProtoMessage 
    
    
    func (*MachineSeries) ProtoMessage()

### func (*MachineSeries) ProtoReflect 
    
    
    func (x *MachineSeries) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MachineSeries) Reset 
    
    
    func (x *MachineSeries) Reset()

### func (*MachineSeries) String 
    
    
    func (x *MachineSeries) String() [string](https://pkg.go.dev/builtin#string)

## MemoryUsageSample
    
    
    type MemoryUsageSample struct {
    
    	// Percentage of system memory utilized. Must be in the interval [0, 100].
    	UtilizedPercentage [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,opt,name=utilized_percentage,json=utilizedPercentage,proto3" json:"utilized_percentage,omitempty"`
    	// contains filtered or unexported fields
    }

Memory usage sample.

### func (*MemoryUsageSample) Descriptor 
    
    
    func (*MemoryUsageSample) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MemoryUsageSample.ProtoReflect.Descriptor instead.

### func (*MemoryUsageSample) GetUtilizedPercentage 
    
    
    func (x *MemoryUsageSample) GetUtilizedPercentage() [float32](https://pkg.go.dev/builtin#float32)

### func (*MemoryUsageSample) ProtoMessage 
    
    
    func (*MemoryUsageSample) ProtoMessage()

### func (*MemoryUsageSample) ProtoReflect 
    
    
    func (x *MemoryUsageSample) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MemoryUsageSample) Reset 
    
    
    func (x *MemoryUsageSample) Reset()

### func (*MemoryUsageSample) String 
    
    
    func (x *MemoryUsageSample) String() [string](https://pkg.go.dev/builtin#string)

## MigrationCenterClient
    
    
    type MigrationCenterClient interface {
    	// Lists all the assets in a given project and location.
    	ListAssets(ctx context.Context, in *ListAssetsRequest, opts ...grpc.CallOption) (*ListAssetsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of an asset.
    	GetAsset(ctx context.Context, in *GetAssetRequest, opts ...grpc.CallOption) (*Asset, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of an asset.
    	UpdateAsset(ctx context.Context, in *UpdateAssetRequest, opts ...grpc.CallOption) (*Asset, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a list of assets.
    	BatchUpdateAssets(ctx context.Context, in *BatchUpdateAssetsRequest, opts ...grpc.CallOption) (*BatchUpdateAssetsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an asset.
    	DeleteAsset(ctx context.Context, in *DeleteAssetRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Deletes list of Assets.
    	BatchDeleteAssets(ctx context.Context, in *BatchDeleteAssetsRequest, opts ...grpc.CallOption) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Reports a set of frames.
    	ReportAssetFrames(ctx context.Context, in *ReportAssetFramesRequest, opts ...grpc.CallOption) (*ReportAssetFramesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Aggregates the requested fields based on provided function.
    	AggregateAssetsValues(ctx context.Context, in *AggregateAssetsValuesRequest, opts ...grpc.CallOption) (*AggregateAssetsValuesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates an import job.
    	CreateImportJob(ctx context.Context, in *CreateImportJobRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all import jobs.
    	ListImportJobs(ctx context.Context, in *ListImportJobsRequest, opts ...grpc.CallOption) (*ListImportJobsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of an import job.
    	GetImportJob(ctx context.Context, in *GetImportJobRequest, opts ...grpc.CallOption) (*ImportJob, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an import job.
    	DeleteImportJob(ctx context.Context, in *DeleteImportJobRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates an import job.
    	UpdateImportJob(ctx context.Context, in *UpdateImportJobRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Validates an import job.
    	ValidateImportJob(ctx context.Context, in *ValidateImportJobRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Runs an import job.
    	RunImportJob(ctx context.Context, in *RunImportJobRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets an import data file.
    	GetImportDataFile(ctx context.Context, in *GetImportDataFileRequest, opts ...grpc.CallOption) (*ImportDataFile, [error](https://pkg.go.dev/builtin#error))
    	// List import data files.
    	ListImportDataFiles(ctx context.Context, in *ListImportDataFilesRequest, opts ...grpc.CallOption) (*ListImportDataFilesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates an import data file.
    	CreateImportDataFile(ctx context.Context, in *CreateImportDataFileRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Delete an import data file.
    	DeleteImportDataFile(ctx context.Context, in *DeleteImportDataFileRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all groups in a given project and location.
    	ListGroups(ctx context.Context, in *ListGroupsRequest, opts ...grpc.CallOption) (*ListGroupsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of a group.
    	GetGroup(ctx context.Context, in *GetGroupRequest, opts ...grpc.CallOption) (*Group, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new group in a given project and location.
    	CreateGroup(ctx context.Context, in *CreateGroupRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a group.
    	UpdateGroup(ctx context.Context, in *UpdateGroupRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a group.
    	DeleteGroup(ctx context.Context, in *DeleteGroupRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Adds assets to a group.
    	AddAssetsToGroup(ctx context.Context, in *AddAssetsToGroupRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Removes assets from a group.
    	RemoveAssetsFromGroup(ctx context.Context, in *RemoveAssetsFromGroupRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all error frames in a given source and location.
    	ListErrorFrames(ctx context.Context, in *ListErrorFramesRequest, opts ...grpc.CallOption) (*ListErrorFramesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of an error frame.
    	GetErrorFrame(ctx context.Context, in *GetErrorFrameRequest, opts ...grpc.CallOption) (*ErrorFrame, [error](https://pkg.go.dev/builtin#error))
    	// Lists all the sources in a given project and location.
    	ListSources(ctx context.Context, in *ListSourcesRequest, opts ...grpc.CallOption) (*ListSourcesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of a source.
    	GetSource(ctx context.Context, in *GetSourceRequest, opts ...grpc.CallOption) (*Source, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new source in a given project and location.
    	CreateSource(ctx context.Context, in *CreateSourceRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a source.
    	UpdateSource(ctx context.Context, in *UpdateSourceRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a source.
    	DeleteSource(ctx context.Context, in *DeleteSourceRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all the preference sets in a given project and location.
    	ListPreferenceSets(ctx context.Context, in *ListPreferenceSetsRequest, opts ...grpc.CallOption) (*ListPreferenceSetsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of a preference set.
    	GetPreferenceSet(ctx context.Context, in *GetPreferenceSetRequest, opts ...grpc.CallOption) (*PreferenceSet, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new preference set in a given project and location.
    	CreatePreferenceSet(ctx context.Context, in *CreatePreferenceSetRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a preference set.
    	UpdatePreferenceSet(ctx context.Context, in *UpdatePreferenceSetRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a preference set.
    	DeletePreferenceSet(ctx context.Context, in *DeletePreferenceSetRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of regional settings.
    	GetSettings(ctx context.Context, in *GetSettingsRequest, opts ...grpc.CallOption) (*Settings, [error](https://pkg.go.dev/builtin#error))
    	// Updates the regional-level project settings.
    	UpdateSettings(ctx context.Context, in *UpdateSettingsRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates a report configuration.
    	CreateReportConfig(ctx context.Context, in *CreateReportConfigRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single ReportConfig.
    	GetReportConfig(ctx context.Context, in *GetReportConfigRequest, opts ...grpc.CallOption) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))
    	// Lists ReportConfigs in a given project and location.
    	ListReportConfigs(ctx context.Context, in *ListReportConfigsRequest, opts ...grpc.CallOption) (*ListReportConfigsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a ReportConfig.
    	DeleteReportConfig(ctx context.Context, in *DeleteReportConfigRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates a report.
    	CreateReport(ctx context.Context, in *CreateReportRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single Report.
    	GetReport(ctx context.Context, in *GetReportRequest, opts ...grpc.CallOption) (*Report, [error](https://pkg.go.dev/builtin#error))
    	// Lists Reports in a given ReportConfig.
    	ListReports(ctx context.Context, in *ListReportsRequest, opts ...grpc.CallOption) (*ListReportsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a Report.
    	DeleteReport(ctx context.Context, in *DeleteReportRequest, opts ...grpc.CallOption) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    }

MigrationCenterClient is the client API for MigrationCenter service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewMigrationCenterClient 
    
    
    func NewMigrationCenterClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) MigrationCenterClient

## MigrationCenterServer
    
    
    type MigrationCenterServer interface {
    	// Lists all the assets in a given project and location.
    	ListAssets(context.Context, *ListAssetsRequest) (*ListAssetsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of an asset.
    	GetAsset(context.Context, *GetAssetRequest) (*Asset, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of an asset.
    	UpdateAsset(context.Context, *UpdateAssetRequest) (*Asset, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a list of assets.
    	BatchUpdateAssets(context.Context, *BatchUpdateAssetsRequest) (*BatchUpdateAssetsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an asset.
    	DeleteAsset(context.Context, *DeleteAssetRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Deletes list of Assets.
    	BatchDeleteAssets(context.Context, *BatchDeleteAssetsRequest) (*emptypb.Empty, [error](https://pkg.go.dev/builtin#error))
    	// Reports a set of frames.
    	ReportAssetFrames(context.Context, *ReportAssetFramesRequest) (*ReportAssetFramesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Aggregates the requested fields based on provided function.
    	AggregateAssetsValues(context.Context, *AggregateAssetsValuesRequest) (*AggregateAssetsValuesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates an import job.
    	CreateImportJob(context.Context, *CreateImportJobRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all import jobs.
    	ListImportJobs(context.Context, *ListImportJobsRequest) (*ListImportJobsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of an import job.
    	GetImportJob(context.Context, *GetImportJobRequest) (*ImportJob, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an import job.
    	DeleteImportJob(context.Context, *DeleteImportJobRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates an import job.
    	UpdateImportJob(context.Context, *UpdateImportJobRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Validates an import job.
    	ValidateImportJob(context.Context, *ValidateImportJobRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Runs an import job.
    	RunImportJob(context.Context, *RunImportJobRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets an import data file.
    	GetImportDataFile(context.Context, *GetImportDataFileRequest) (*ImportDataFile, [error](https://pkg.go.dev/builtin#error))
    	// List import data files.
    	ListImportDataFiles(context.Context, *ListImportDataFilesRequest) (*ListImportDataFilesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates an import data file.
    	CreateImportDataFile(context.Context, *CreateImportDataFileRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Delete an import data file.
    	DeleteImportDataFile(context.Context, *DeleteImportDataFileRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all groups in a given project and location.
    	ListGroups(context.Context, *ListGroupsRequest) (*ListGroupsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of a group.
    	GetGroup(context.Context, *GetGroupRequest) (*Group, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new group in a given project and location.
    	CreateGroup(context.Context, *CreateGroupRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a group.
    	UpdateGroup(context.Context, *UpdateGroupRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a group.
    	DeleteGroup(context.Context, *DeleteGroupRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Adds assets to a group.
    	AddAssetsToGroup(context.Context, *AddAssetsToGroupRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Removes assets from a group.
    	RemoveAssetsFromGroup(context.Context, *RemoveAssetsFromGroupRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all error frames in a given source and location.
    	ListErrorFrames(context.Context, *ListErrorFramesRequest) (*ListErrorFramesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of an error frame.
    	GetErrorFrame(context.Context, *GetErrorFrameRequest) (*ErrorFrame, [error](https://pkg.go.dev/builtin#error))
    	// Lists all the sources in a given project and location.
    	ListSources(context.Context, *ListSourcesRequest) (*ListSourcesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of a source.
    	GetSource(context.Context, *GetSourceRequest) (*Source, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new source in a given project and location.
    	CreateSource(context.Context, *CreateSourceRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a source.
    	UpdateSource(context.Context, *UpdateSourceRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a source.
    	DeleteSource(context.Context, *DeleteSourceRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Lists all the preference sets in a given project and location.
    	ListPreferenceSets(context.Context, *ListPreferenceSetsRequest) (*ListPreferenceSetsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of a preference set.
    	GetPreferenceSet(context.Context, *GetPreferenceSetRequest) (*PreferenceSet, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new preference set in a given project and location.
    	CreatePreferenceSet(context.Context, *CreatePreferenceSetRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Updates the parameters of a preference set.
    	UpdatePreferenceSet(context.Context, *UpdatePreferenceSetRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a preference set.
    	DeletePreferenceSet(context.Context, *DeletePreferenceSetRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets the details of regional settings.
    	GetSettings(context.Context, *GetSettingsRequest) (*Settings, [error](https://pkg.go.dev/builtin#error))
    	// Updates the regional-level project settings.
    	UpdateSettings(context.Context, *UpdateSettingsRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates a report configuration.
    	CreateReportConfig(context.Context, *CreateReportConfigRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single ReportConfig.
    	GetReportConfig(context.Context, *GetReportConfigRequest) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))
    	// Lists ReportConfigs in a given project and location.
    	ListReportConfigs(context.Context, *ListReportConfigsRequest) (*ListReportConfigsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a ReportConfig.
    	DeleteReportConfig(context.Context, *DeleteReportConfigRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Creates a report.
    	CreateReport(context.Context, *CreateReportRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    	// Gets details of a single Report.
    	GetReport(context.Context, *GetReportRequest) (*Report, [error](https://pkg.go.dev/builtin#error))
    	// Lists Reports in a given ReportConfig.
    	ListReports(context.Context, *ListReportsRequest) (*ListReportsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Deletes a Report.
    	DeleteReport(context.Context, *DeleteReportRequest) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))
    }

MigrationCenterServer is the server API for MigrationCenter service. All implementations should embed UnimplementedMigrationCenterServer for forward compatibility

## MigrationInsight
    
    
    type MigrationInsight struct {
    
    	// Output only. Description of how well the asset this insight is associated
    	// with fits the proposed migration.
    	Fit *FitDescriptor `protobuf:"bytes,1,opt,name=fit,proto3" json:"fit,omitempty"`
    	// A target for the migration.
    	//
    	// Types that are valid to be assigned to MigrationTarget:
    	//
    	//	*MigrationInsight_ComputeEngineTarget
    	MigrationTarget isMigrationInsight_MigrationTarget `protobuf_oneof:"migration_target"`
    	// contains filtered or unexported fields
    }

An insight about potential migrations for an asset.

### func (*MigrationInsight) Descriptor 
    
    
    func (*MigrationInsight) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use MigrationInsight.ProtoReflect.Descriptor instead.

### func (*MigrationInsight) GetComputeEngineTarget 
    
    
    func (x *MigrationInsight) GetComputeEngineTarget() *ComputeEngineMigrationTarget

### func (*MigrationInsight) GetFit 
    
    
    func (x *MigrationInsight) GetFit() *FitDescriptor

### func (*MigrationInsight) GetMigrationTarget 
    
    
    func (x *MigrationInsight) GetMigrationTarget() isMigrationInsight_MigrationTarget

### func (*MigrationInsight) ProtoMessage 
    
    
    func (*MigrationInsight) ProtoMessage()

### func (*MigrationInsight) ProtoReflect 
    
    
    func (x *MigrationInsight) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*MigrationInsight) Reset 
    
    
    func (x *MigrationInsight) Reset()

### func (*MigrationInsight) String 
    
    
    func (x *MigrationInsight) String() [string](https://pkg.go.dev/builtin#string)

## MigrationInsight_ComputeEngineTarget
    
    
    type MigrationInsight_ComputeEngineTarget struct {
    	// Output only. A Google Compute Engine target.
    	ComputeEngineTarget *ComputeEngineMigrationTarget `protobuf:"bytes,10,opt,name=compute_engine_target,json=computeEngineTarget,proto3,oneof"`
    }

## NetworkAdapterDetails
    
    
    type NetworkAdapterDetails struct {
    
    	// Network adapter type (e.g. VMXNET3).
    	AdapterType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=adapter_type,json=adapterType,proto3" json:"adapter_type,omitempty"`
    	// MAC address.
    	MacAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=mac_address,json=macAddress,proto3" json:"mac_address,omitempty"`
    	// NetworkAddressList
    	Addresses *NetworkAddressList `protobuf:"bytes,3,opt,name=addresses,proto3" json:"addresses,omitempty"`
    	// contains filtered or unexported fields
    }

Details of network adapter.

### func (*NetworkAdapterDetails) Descriptor 
    
    
    func (*NetworkAdapterDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NetworkAdapterDetails.ProtoReflect.Descriptor instead.

### func (*NetworkAdapterDetails) GetAdapterType 
    
    
    func (x *NetworkAdapterDetails) GetAdapterType() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkAdapterDetails) GetAddresses 
    
    
    func (x *NetworkAdapterDetails) GetAddresses() *NetworkAddressList

### func (*NetworkAdapterDetails) GetMacAddress 
    
    
    func (x *NetworkAdapterDetails) GetMacAddress() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkAdapterDetails) ProtoMessage 
    
    
    func (*NetworkAdapterDetails) ProtoMessage()

### func (*NetworkAdapterDetails) ProtoReflect 
    
    
    func (x *NetworkAdapterDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NetworkAdapterDetails) Reset 
    
    
    func (x *NetworkAdapterDetails) Reset()

### func (*NetworkAdapterDetails) String 
    
    
    func (x *NetworkAdapterDetails) String() [string](https://pkg.go.dev/builtin#string)

## NetworkAdapterList
    
    
    type NetworkAdapterList struct {
    
    	// Network adapter entries.
    	Entries []*NetworkAdapterDetails `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

List of network adapters.

### func (*NetworkAdapterList) Descriptor 
    
    
    func (*NetworkAdapterList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NetworkAdapterList.ProtoReflect.Descriptor instead.

### func (*NetworkAdapterList) GetEntries 
    
    
    func (x *NetworkAdapterList) GetEntries() []*NetworkAdapterDetails

### func (*NetworkAdapterList) ProtoMessage 
    
    
    func (*NetworkAdapterList) ProtoMessage()

### func (*NetworkAdapterList) ProtoReflect 
    
    
    func (x *NetworkAdapterList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NetworkAdapterList) Reset 
    
    
    func (x *NetworkAdapterList) Reset()

### func (*NetworkAdapterList) String 
    
    
    func (x *NetworkAdapterList) String() [string](https://pkg.go.dev/builtin#string)

## NetworkAddress
    
    
    type NetworkAddress struct {
    
    	// Assigned or configured IP Address.
    	IpAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=ip_address,json=ipAddress,proto3" json:"ip_address,omitempty"`
    	// Subnet mask.
    	SubnetMask [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=subnet_mask,json=subnetMask,proto3" json:"subnet_mask,omitempty"`
    	// Broadcast address.
    	Bcast [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=bcast,proto3" json:"bcast,omitempty"`
    	// Fully qualified domain name.
    	Fqdn [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=fqdn,proto3" json:"fqdn,omitempty"`
    	// Whether DHCP is used to assign addresses.
    	Assignment NetworkAddress_AddressAssignment `protobuf:"varint,5,opt,name=assignment,proto3,enum=google.cloud.migrationcenter.v1.NetworkAddress_AddressAssignment" json:"assignment,omitempty"`
    	// contains filtered or unexported fields
    }

Details of network address.

### func (*NetworkAddress) Descriptor 
    
    
    func (*NetworkAddress) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NetworkAddress.ProtoReflect.Descriptor instead.

### func (*NetworkAddress) GetAssignment 
    
    
    func (x *NetworkAddress) GetAssignment() NetworkAddress_AddressAssignment

### func (*NetworkAddress) GetBcast 
    
    
    func (x *NetworkAddress) GetBcast() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkAddress) GetFqdn 
    
    
    func (x *NetworkAddress) GetFqdn() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkAddress) GetIpAddress 
    
    
    func (x *NetworkAddress) GetIpAddress() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkAddress) GetSubnetMask 
    
    
    func (x *NetworkAddress) GetSubnetMask() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkAddress) ProtoMessage 
    
    
    func (*NetworkAddress) ProtoMessage()

### func (*NetworkAddress) ProtoReflect 
    
    
    func (x *NetworkAddress) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NetworkAddress) Reset 
    
    
    func (x *NetworkAddress) Reset()

### func (*NetworkAddress) String 
    
    
    func (x *NetworkAddress) String() [string](https://pkg.go.dev/builtin#string)

## NetworkAddressList
    
    
    type NetworkAddressList struct {
    
    	// Network address entries.
    	Entries []*NetworkAddress `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

List of allocated/assigned network addresses.

### func (*NetworkAddressList) Descriptor 
    
    
    func (*NetworkAddressList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NetworkAddressList.ProtoReflect.Descriptor instead.

### func (*NetworkAddressList) GetEntries 
    
    
    func (x *NetworkAddressList) GetEntries() []*NetworkAddress

### func (*NetworkAddressList) ProtoMessage 
    
    
    func (*NetworkAddressList) ProtoMessage()

### func (*NetworkAddressList) ProtoReflect 
    
    
    func (x *NetworkAddressList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NetworkAddressList) Reset 
    
    
    func (x *NetworkAddressList) Reset()

### func (*NetworkAddressList) String 
    
    
    func (x *NetworkAddressList) String() [string](https://pkg.go.dev/builtin#string)

## NetworkAddress_AddressAssignment
    
    
    type NetworkAddress_AddressAssignment [int32](https://pkg.go.dev/builtin#int32)

Network address assignment.

### NetworkAddress_ADDRESS_ASSIGNMENT_UNSPECIFIED, NetworkAddress_ADDRESS_ASSIGNMENT_STATIC, NetworkAddress_ADDRESS_ASSIGNMENT_DHCP
    
    
    const (
    	// Unknown (default value).
    	NetworkAddress_ADDRESS_ASSIGNMENT_UNSPECIFIED NetworkAddress_AddressAssignment = 0
    	// Staticly assigned IP.
    	NetworkAddress_ADDRESS_ASSIGNMENT_STATIC NetworkAddress_AddressAssignment = 1
    	// Dynamically assigned IP (DHCP).
    	NetworkAddress_ADDRESS_ASSIGNMENT_DHCP NetworkAddress_AddressAssignment = 2
    )

### func (NetworkAddress_AddressAssignment) Descriptor 
    
    
    func (NetworkAddress_AddressAssignment) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (NetworkAddress_AddressAssignment) Enum 
    
    
    func (x NetworkAddress_AddressAssignment) Enum() *NetworkAddress_AddressAssignment

### func (NetworkAddress_AddressAssignment) EnumDescriptor 
    
    
    func (NetworkAddress_AddressAssignment) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NetworkAddress_AddressAssignment.Descriptor instead.

### func (NetworkAddress_AddressAssignment) Number 
    
    
    func (x NetworkAddress_AddressAssignment) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (NetworkAddress_AddressAssignment) String 
    
    
    func (x NetworkAddress_AddressAssignment) String() [string](https://pkg.go.dev/builtin#string)

### func (NetworkAddress_AddressAssignment) Type 
    
    
    func (NetworkAddress_AddressAssignment) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## NetworkConnection
    
    
    type NetworkConnection struct {
    
    	// Connection protocol (e.g. TCP/UDP).
    	Protocol [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=protocol,proto3" json:"protocol,omitempty"`
    	// Local IP address.
    	LocalIpAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=local_ip_address,json=localIpAddress,proto3" json:"local_ip_address,omitempty"`
    	// Local port.
    	LocalPort [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=local_port,json=localPort,proto3" json:"local_port,omitempty"`
    	// Remote IP address.
    	RemoteIpAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=remote_ip_address,json=remoteIpAddress,proto3" json:"remote_ip_address,omitempty"`
    	// Remote port.
    	RemotePort [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=remote_port,json=remotePort,proto3" json:"remote_port,omitempty"`
    	// Network connection state.
    	State NetworkConnection_State `protobuf:"varint,6,opt,name=state,proto3,enum=google.cloud.migrationcenter.v1.NetworkConnection_State" json:"state,omitempty"`
    	// Process ID.
    	Pid [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,7,opt,name=pid,proto3" json:"pid,omitempty"`
    	// Process or service name.
    	ProcessName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=process_name,json=processName,proto3" json:"process_name,omitempty"`
    	// contains filtered or unexported fields
    }

### func (*NetworkConnection) Descriptor 
    
    
    func (*NetworkConnection) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NetworkConnection.ProtoReflect.Descriptor instead.

### func (*NetworkConnection) GetLocalIpAddress 
    
    
    func (x *NetworkConnection) GetLocalIpAddress() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkConnection) GetLocalPort 
    
    
    func (x *NetworkConnection) GetLocalPort() [int32](https://pkg.go.dev/builtin#int32)

### func (*NetworkConnection) GetPid 
    
    
    func (x *NetworkConnection) GetPid() [int64](https://pkg.go.dev/builtin#int64)

### func (*NetworkConnection) GetProcessName 
    
    
    func (x *NetworkConnection) GetProcessName() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkConnection) GetProtocol 
    
    
    func (x *NetworkConnection) GetProtocol() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkConnection) GetRemoteIpAddress 
    
    
    func (x *NetworkConnection) GetRemoteIpAddress() [string](https://pkg.go.dev/builtin#string)

### func (*NetworkConnection) GetRemotePort 
    
    
    func (x *NetworkConnection) GetRemotePort() [int32](https://pkg.go.dev/builtin#int32)

### func (*NetworkConnection) GetState 
    
    
    func (x *NetworkConnection) GetState() NetworkConnection_State

### func (*NetworkConnection) ProtoMessage 
    
    
    func (*NetworkConnection) ProtoMessage()

### func (*NetworkConnection) ProtoReflect 
    
    
    func (x *NetworkConnection) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NetworkConnection) Reset 
    
    
    func (x *NetworkConnection) Reset()

### func (*NetworkConnection) String 
    
    
    func (x *NetworkConnection) String() [string](https://pkg.go.dev/builtin#string)

## NetworkConnectionList
    
    
    type NetworkConnectionList struct {
    
    	// Network connection entries.
    	Entries []*NetworkConnection `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

Network connection list.

### func (*NetworkConnectionList) Descriptor 
    
    
    func (*NetworkConnectionList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NetworkConnectionList.ProtoReflect.Descriptor instead.

### func (*NetworkConnectionList) GetEntries 
    
    
    func (x *NetworkConnectionList) GetEntries() []*NetworkConnection

### func (*NetworkConnectionList) ProtoMessage 
    
    
    func (*NetworkConnectionList) ProtoMessage()

### func (*NetworkConnectionList) ProtoReflect 
    
    
    func (x *NetworkConnectionList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NetworkConnectionList) Reset 
    
    
    func (x *NetworkConnectionList) Reset()

### func (*NetworkConnectionList) String 
    
    
    func (x *NetworkConnectionList) String() [string](https://pkg.go.dev/builtin#string)

## NetworkConnection_State
    
    
    type NetworkConnection_State [int32](https://pkg.go.dev/builtin#int32)

Network connection state.

### NetworkConnection_STATE_UNSPECIFIED, NetworkConnection_OPENING, NetworkConnection_OPEN, NetworkConnection_LISTEN, NetworkConnection_CLOSING, NetworkConnection_CLOSED
    
    
    const (
    	// Connection state is unknown or unspecified.
    	NetworkConnection_STATE_UNSPECIFIED NetworkConnection_State = 0
    	// The connection is being opened.
    	NetworkConnection_OPENING NetworkConnection_State = 1
    	// The connection is open.
    	NetworkConnection_OPEN NetworkConnection_State = 2
    	// Listening for incoming connections.
    	NetworkConnection_LISTEN NetworkConnection_State = 3
    	// The connection is being closed.
    	NetworkConnection_CLOSING NetworkConnection_State = 4
    	// The connection is closed.
    	NetworkConnection_CLOSED NetworkConnection_State = 5
    )

### func (NetworkConnection_State) Descriptor 
    
    
    func (NetworkConnection_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (NetworkConnection_State) Enum 
    
    
    func (x NetworkConnection_State) Enum() *NetworkConnection_State

### func (NetworkConnection_State) EnumDescriptor 
    
    
    func (NetworkConnection_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NetworkConnection_State.Descriptor instead.

### func (NetworkConnection_State) Number 
    
    
    func (x NetworkConnection_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (NetworkConnection_State) String 
    
    
    func (x NetworkConnection_State) String() [string](https://pkg.go.dev/builtin#string)

### func (NetworkConnection_State) Type 
    
    
    func (NetworkConnection_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## NetworkUsageSample
    
    
    type NetworkUsageSample struct {
    
    	// Average network ingress in B/s sampled over a short window.
    	// Must be non-negative.
    	AverageIngressBps [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,1,opt,name=average_ingress_bps,json=averageIngressBps,proto3" json:"average_ingress_bps,omitempty"`
    	// Average network egress in B/s sampled over a short window.
    	// Must be non-negative.
    	AverageEgressBps [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,2,opt,name=average_egress_bps,json=averageEgressBps,proto3" json:"average_egress_bps,omitempty"`
    	// contains filtered or unexported fields
    }

Network usage sample. Values are across all network interfaces.

### func (*NetworkUsageSample) Descriptor 
    
    
    func (*NetworkUsageSample) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NetworkUsageSample.ProtoReflect.Descriptor instead.

### func (*NetworkUsageSample) GetAverageEgressBps 
    
    
    func (x *NetworkUsageSample) GetAverageEgressBps() [float32](https://pkg.go.dev/builtin#float32)

### func (*NetworkUsageSample) GetAverageIngressBps 
    
    
    func (x *NetworkUsageSample) GetAverageIngressBps() [float32](https://pkg.go.dev/builtin#float32)

### func (*NetworkUsageSample) ProtoMessage 
    
    
    func (*NetworkUsageSample) ProtoMessage()

### func (*NetworkUsageSample) ProtoReflect 
    
    
    func (x *NetworkUsageSample) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NetworkUsageSample) Reset 
    
    
    func (x *NetworkUsageSample) Reset()

### func (*NetworkUsageSample) String 
    
    
    func (x *NetworkUsageSample) String() [string](https://pkg.go.dev/builtin#string)

## NfsExport
    
    
    type NfsExport struct {
    
    	// The directory being exported.
    	ExportDirectory [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=export_directory,json=exportDirectory,proto3" json:"export_directory,omitempty"`
    	// The hosts or networks to which the export is being shared.
    	Hosts [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=hosts,proto3" json:"hosts,omitempty"`
    	// contains filtered or unexported fields
    }

NFS export.

### func (*NfsExport) Descriptor 
    
    
    func (*NfsExport) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NfsExport.ProtoReflect.Descriptor instead.

### func (*NfsExport) GetExportDirectory 
    
    
    func (x *NfsExport) GetExportDirectory() [string](https://pkg.go.dev/builtin#string)

### func (*NfsExport) GetHosts 
    
    
    func (x *NfsExport) GetHosts() [][string](https://pkg.go.dev/builtin#string)

### func (*NfsExport) ProtoMessage 
    
    
    func (*NfsExport) ProtoMessage()

### func (*NfsExport) ProtoReflect 
    
    
    func (x *NfsExport) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NfsExport) Reset 
    
    
    func (x *NfsExport) Reset()

### func (*NfsExport) String 
    
    
    func (x *NfsExport) String() [string](https://pkg.go.dev/builtin#string)

## NfsExportList
    
    
    type NfsExportList struct {
    
    	// NFS export entries.
    	Entries []*NfsExport `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

NFS exports.

### func (*NfsExportList) Descriptor 
    
    
    func (*NfsExportList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use NfsExportList.ProtoReflect.Descriptor instead.

### func (*NfsExportList) GetEntries 
    
    
    func (x *NfsExportList) GetEntries() []*NfsExport

### func (*NfsExportList) ProtoMessage 
    
    
    func (*NfsExportList) ProtoMessage()

### func (*NfsExportList) ProtoReflect 
    
    
    func (x *NfsExportList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*NfsExportList) Reset 
    
    
    func (x *NfsExportList) Reset()

### func (*NfsExportList) String 
    
    
    func (x *NfsExportList) String() [string](https://pkg.go.dev/builtin#string)

## OpenFileDetails
    
    
    type OpenFileDetails struct {
    
    	// Opened file command.
    	Command [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=command,proto3" json:"command,omitempty"`
    	// Opened file user.
    	User [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=user,proto3" json:"user,omitempty"`
    	// Opened file file type.
    	FileType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=file_type,json=fileType,proto3" json:"file_type,omitempty"`
    	// Opened file file path.
    	FilePath [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=file_path,json=filePath,proto3" json:"file_path,omitempty"`
    	// contains filtered or unexported fields
    }

Open file Information.

### func (*OpenFileDetails) Descriptor 
    
    
    func (*OpenFileDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OpenFileDetails.ProtoReflect.Descriptor instead.

### func (*OpenFileDetails) GetCommand 
    
    
    func (x *OpenFileDetails) GetCommand() [string](https://pkg.go.dev/builtin#string)

### func (*OpenFileDetails) GetFilePath 
    
    
    func (x *OpenFileDetails) GetFilePath() [string](https://pkg.go.dev/builtin#string)

### func (*OpenFileDetails) GetFileType 
    
    
    func (x *OpenFileDetails) GetFileType() [string](https://pkg.go.dev/builtin#string)

### func (*OpenFileDetails) GetUser 
    
    
    func (x *OpenFileDetails) GetUser() [string](https://pkg.go.dev/builtin#string)

### func (*OpenFileDetails) ProtoMessage 
    
    
    func (*OpenFileDetails) ProtoMessage()

### func (*OpenFileDetails) ProtoReflect 
    
    
    func (x *OpenFileDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OpenFileDetails) Reset 
    
    
    func (x *OpenFileDetails) Reset()

### func (*OpenFileDetails) String 
    
    
    func (x *OpenFileDetails) String() [string](https://pkg.go.dev/builtin#string)

## OpenFileList
    
    
    type OpenFileList struct {
    
    	// Open file details entries.
    	Entries []*OpenFileDetails `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

Open file list.

### func (*OpenFileList) Descriptor 
    
    
    func (*OpenFileList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OpenFileList.ProtoReflect.Descriptor instead.

### func (*OpenFileList) GetEntries 
    
    
    func (x *OpenFileList) GetEntries() []*OpenFileDetails

### func (*OpenFileList) ProtoMessage 
    
    
    func (*OpenFileList) ProtoMessage()

### func (*OpenFileList) ProtoReflect 
    
    
    func (x *OpenFileList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OpenFileList) Reset 
    
    
    func (x *OpenFileList) Reset()

### func (*OpenFileList) String 
    
    
    func (x *OpenFileList) String() [string](https://pkg.go.dev/builtin#string)

## OperatingSystemFamily
    
    
    type OperatingSystemFamily [int32](https://pkg.go.dev/builtin#int32)

Known categories of operating systems.

### OperatingSystemFamily_OS_FAMILY_UNKNOWN, OperatingSystemFamily_OS_FAMILY_WINDOWS, OperatingSystemFamily_OS_FAMILY_LINUX, OperatingSystemFamily_OS_FAMILY_UNIX
    
    
    const (
    	OperatingSystemFamily_OS_FAMILY_UNKNOWN OperatingSystemFamily = 0
    	// Microsoft Windows Server and Desktop.
    	OperatingSystemFamily_OS_FAMILY_WINDOWS OperatingSystemFamily = 1
    	// Various Linux flavors.
    	OperatingSystemFamily_OS_FAMILY_LINUX OperatingSystemFamily = 2
    	// Non-Linux Unix flavors.
    	OperatingSystemFamily_OS_FAMILY_UNIX OperatingSystemFamily = 3
    )

### func (OperatingSystemFamily) Descriptor 
    
    
    func (OperatingSystemFamily) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (OperatingSystemFamily) Enum 
    
    
    func (x OperatingSystemFamily) Enum() *OperatingSystemFamily

### func (OperatingSystemFamily) EnumDescriptor 
    
    
    func (OperatingSystemFamily) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OperatingSystemFamily.Descriptor instead.

### func (OperatingSystemFamily) Number 
    
    
    func (x OperatingSystemFamily) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (OperatingSystemFamily) String 
    
    
    func (x OperatingSystemFamily) String() [string](https://pkg.go.dev/builtin#string)

### func (OperatingSystemFamily) Type 
    
    
    func (OperatingSystemFamily) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## OperationMetadata
    
    
    type OperationMetadata struct {
    
    	// Output only. The time the operation was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The time the operation finished running.
    	EndTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=end_time,json=endTime,proto3" json:"end_time,omitempty"`
    	// Output only. Server-defined resource path for the target of the operation.
    	Target [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=target,proto3" json:"target,omitempty"`
    	// Output only. Name of the verb executed by the operation.
    	Verb [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=verb,proto3" json:"verb,omitempty"`
    	// Output only. Human-readable status of the operation, if any.
    	StatusMessage [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=status_message,json=statusMessage,proto3" json:"status_message,omitempty"`
    	// Output only. Identifies whether the user has requested cancellation
    	// of the operation. Operations that have been cancelled successfully
    	// have [Operation.error][] value with a
    	// [google.rpc.Status.code][google.rpc.Status.code] of 1, corresponding to
    	// `Code.CANCELLED`.
    	RequestedCancellation [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=requested_cancellation,json=requestedCancellation,proto3" json:"requested_cancellation,omitempty"`
    	// Output only. API version used to start the operation.
    	ApiVersion [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,7,opt,name=api_version,json=apiVersion,proto3" json:"api_version,omitempty"`
    	// contains filtered or unexported fields
    }

Represents the metadata of the long-running operation.

### func (*OperationMetadata) Descriptor 
    
    
    func (*OperationMetadata) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OperationMetadata.ProtoReflect.Descriptor instead.

### func (*OperationMetadata) GetApiVersion 
    
    
    func (x *OperationMetadata) GetApiVersion() [string](https://pkg.go.dev/builtin#string)

### func (*OperationMetadata) GetCreateTime 
    
    
    func (x *OperationMetadata) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*OperationMetadata) GetEndTime 
    
    
    func (x *OperationMetadata) GetEndTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*OperationMetadata) GetRequestedCancellation 
    
    
    func (x *OperationMetadata) GetRequestedCancellation() [bool](https://pkg.go.dev/builtin#bool)

### func (*OperationMetadata) GetStatusMessage 
    
    
    func (x *OperationMetadata) GetStatusMessage() [string](https://pkg.go.dev/builtin#string)

### func (*OperationMetadata) GetTarget 
    
    
    func (x *OperationMetadata) GetTarget() [string](https://pkg.go.dev/builtin#string)

### func (*OperationMetadata) GetVerb 
    
    
    func (x *OperationMetadata) GetVerb() [string](https://pkg.go.dev/builtin#string)

### func (*OperationMetadata) ProtoMessage 
    
    
    func (*OperationMetadata) ProtoMessage()

### func (*OperationMetadata) ProtoReflect 
    
    
    func (x *OperationMetadata) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OperationMetadata) Reset 
    
    
    func (x *OperationMetadata) Reset()

### func (*OperationMetadata) String 
    
    
    func (x *OperationMetadata) String() [string](https://pkg.go.dev/builtin#string)

## PerformanceSample
    
    
    type PerformanceSample struct {
    
    	// Time the sample was collected.
    	// If omitted, the frame report time will be used.
    	SampleTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=sample_time,json=sampleTime,proto3" json:"sample_time,omitempty"`
    	// Memory usage sample.
    	Memory *MemoryUsageSample `protobuf:"bytes,2,opt,name=memory,proto3" json:"memory,omitempty"`
    	// CPU usage sample.
    	Cpu *CpuUsageSample `protobuf:"bytes,3,opt,name=cpu,proto3" json:"cpu,omitempty"`
    	// Network usage sample.
    	Network *NetworkUsageSample `protobuf:"bytes,4,opt,name=network,proto3" json:"network,omitempty"`
    	// Disk usage sample.
    	Disk *DiskUsageSample `protobuf:"bytes,5,opt,name=disk,proto3" json:"disk,omitempty"`
    	// contains filtered or unexported fields
    }

Performance data sample.

### func (*PerformanceSample) Descriptor 
    
    
    func (*PerformanceSample) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PerformanceSample.ProtoReflect.Descriptor instead.

### func (*PerformanceSample) GetCpu 
    
    
    func (x *PerformanceSample) GetCpu() *CpuUsageSample

### func (*PerformanceSample) GetDisk 
    
    
    func (x *PerformanceSample) GetDisk() *DiskUsageSample

### func (*PerformanceSample) GetMemory 
    
    
    func (x *PerformanceSample) GetMemory() *MemoryUsageSample

### func (*PerformanceSample) GetNetwork 
    
    
    func (x *PerformanceSample) GetNetwork() *NetworkUsageSample

### func (*PerformanceSample) GetSampleTime 
    
    
    func (x *PerformanceSample) GetSampleTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*PerformanceSample) ProtoMessage 
    
    
    func (*PerformanceSample) ProtoMessage()

### func (*PerformanceSample) ProtoReflect 
    
    
    func (x *PerformanceSample) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PerformanceSample) Reset 
    
    
    func (x *PerformanceSample) Reset()

### func (*PerformanceSample) String 
    
    
    func (x *PerformanceSample) String() [string](https://pkg.go.dev/builtin#string)

## PersistentDiskType
    
    
    type PersistentDiskType [int32](https://pkg.go.dev/builtin#int32)

The persistent disk (PD) types of Compute Engine virtual machines.

### PersistentDiskType_PERSISTENT_DISK_TYPE_UNSPECIFIED, PersistentDiskType_PERSISTENT_DISK_TYPE_STANDARD, PersistentDiskType_PERSISTENT_DISK_TYPE_BALANCED, PersistentDiskType_PERSISTENT_DISK_TYPE_SSD
    
    
    const (
    	// Unspecified (default value).
    	// Selecting this value allows the system to use any disk type according
    	// to reported usage. This a good value to start with.
    	PersistentDiskType_PERSISTENT_DISK_TYPE_UNSPECIFIED PersistentDiskType = 0
    	// Standard HDD Persistent Disk.
    	PersistentDiskType_PERSISTENT_DISK_TYPE_STANDARD PersistentDiskType = 1
    	// Balanced Persistent Disk.
    	PersistentDiskType_PERSISTENT_DISK_TYPE_BALANCED PersistentDiskType = 2
    	// SSD Persistent Disk.
    	PersistentDiskType_PERSISTENT_DISK_TYPE_SSD PersistentDiskType = 3
    )

### func (PersistentDiskType) Descriptor 
    
    
    func (PersistentDiskType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (PersistentDiskType) Enum 
    
    
    func (x PersistentDiskType) Enum() *PersistentDiskType

### func (PersistentDiskType) EnumDescriptor 
    
    
    func (PersistentDiskType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PersistentDiskType.Descriptor instead.

### func (PersistentDiskType) Number 
    
    
    func (x PersistentDiskType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (PersistentDiskType) String 
    
    
    func (x PersistentDiskType) String() [string](https://pkg.go.dev/builtin#string)

### func (PersistentDiskType) Type 
    
    
    func (PersistentDiskType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## PhysicalPlatformDetails
    
    
    type PhysicalPlatformDetails struct {
    
    	// Free text representation of the machine location.
    	// The format of this field should not be relied on. Different machines in the
    	// same location may have different string values for this field.
    	Location [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=location,proto3" json:"location,omitempty"`
    	// contains filtered or unexported fields
    }

Platform specific details for Physical Machines.

### func (*PhysicalPlatformDetails) Descriptor 
    
    
    func (*PhysicalPlatformDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PhysicalPlatformDetails.ProtoReflect.Descriptor instead.

### func (*PhysicalPlatformDetails) GetLocation 
    
    
    func (x *PhysicalPlatformDetails) GetLocation() [string](https://pkg.go.dev/builtin#string)

### func (*PhysicalPlatformDetails) ProtoMessage 
    
    
    func (*PhysicalPlatformDetails) ProtoMessage()

### func (*PhysicalPlatformDetails) ProtoReflect 
    
    
    func (x *PhysicalPlatformDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PhysicalPlatformDetails) Reset 
    
    
    func (x *PhysicalPlatformDetails) Reset()

### func (*PhysicalPlatformDetails) String 
    
    
    func (x *PhysicalPlatformDetails) String() [string](https://pkg.go.dev/builtin#string)

## PlatformDetails
    
    
    type PlatformDetails struct {
    
    	// Types that are valid to be assigned to VendorDetails:
    	//
    	//	*PlatformDetails_VmwareDetails
    	//	*PlatformDetails_AwsEc2Details
    	//	*PlatformDetails_AzureVmDetails
    	//	*PlatformDetails_GenericDetails
    	//	*PlatformDetails_PhysicalDetails
    	VendorDetails isPlatformDetails_VendorDetails `protobuf_oneof:"vendor_details"`
    	// contains filtered or unexported fields
    }

Information about the platform.

### func (*PlatformDetails) Descriptor 
    
    
    func (*PlatformDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PlatformDetails.ProtoReflect.Descriptor instead.

### func (*PlatformDetails) GetAwsEc2Details 
    
    
    func (x *PlatformDetails) GetAwsEc2Details() *AwsEc2PlatformDetails

### func (*PlatformDetails) GetAzureVmDetails 
    
    
    func (x *PlatformDetails) GetAzureVmDetails() *AzureVmPlatformDetails

### func (*PlatformDetails) GetGenericDetails 
    
    
    func (x *PlatformDetails) GetGenericDetails() *GenericPlatformDetails

### func (*PlatformDetails) GetPhysicalDetails 
    
    
    func (x *PlatformDetails) GetPhysicalDetails() *PhysicalPlatformDetails

### func (*PlatformDetails) GetVendorDetails 
    
    
    func (x *PlatformDetails) GetVendorDetails() isPlatformDetails_VendorDetails

### func (*PlatformDetails) GetVmwareDetails 
    
    
    func (x *PlatformDetails) GetVmwareDetails() *VmwarePlatformDetails

### func (*PlatformDetails) ProtoMessage 
    
    
    func (*PlatformDetails) ProtoMessage()

### func (*PlatformDetails) ProtoReflect 
    
    
    func (x *PlatformDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PlatformDetails) Reset 
    
    
    func (x *PlatformDetails) Reset()

### func (*PlatformDetails) String 
    
    
    func (x *PlatformDetails) String() [string](https://pkg.go.dev/builtin#string)

## PlatformDetails_AwsEc2Details
    
    
    type PlatformDetails_AwsEc2Details struct {
    	// AWS EC2 specific details.
    	AwsEc2Details *AwsEc2PlatformDetails `protobuf:"bytes,2,opt,name=aws_ec2_details,json=awsEc2Details,proto3,oneof"`
    }

## PlatformDetails_AzureVmDetails
    
    
    type PlatformDetails_AzureVmDetails struct {
    	// Azure VM specific details.
    	AzureVmDetails *AzureVmPlatformDetails `protobuf:"bytes,3,opt,name=azure_vm_details,json=azureVmDetails,proto3,oneof"`
    }

## PlatformDetails_GenericDetails
    
    
    type PlatformDetails_GenericDetails struct {
    	// Generic platform details.
    	GenericDetails *GenericPlatformDetails `protobuf:"bytes,4,opt,name=generic_details,json=genericDetails,proto3,oneof"`
    }

## PlatformDetails_PhysicalDetails
    
    
    type PlatformDetails_PhysicalDetails struct {
    	// Physical machines platform details.
    	PhysicalDetails *PhysicalPlatformDetails `protobuf:"bytes,5,opt,name=physical_details,json=physicalDetails,proto3,oneof"`
    }

## PlatformDetails_VmwareDetails
    
    
    type PlatformDetails_VmwareDetails struct {
    	// VMware specific details.
    	VmwareDetails *VmwarePlatformDetails `protobuf:"bytes,1,opt,name=vmware_details,json=vmwareDetails,proto3,oneof"`
    }

## PreferenceSet
    
    
    type PreferenceSet struct {
    
    	// Output only. Name of the preference set.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The timestamp when the preference set was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The timestamp when the preference set was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// User-friendly display name. Maximum length is 63 characters.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// A description of the preference set.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=description,proto3" json:"description,omitempty"`
    	// A set of preferences that applies to all virtual machines in the context.
    	VirtualMachinePreferences *VirtualMachinePreferences `protobuf:"bytes,6,opt,name=virtual_machine_preferences,json=virtualMachinePreferences,proto3" json:"virtual_machine_preferences,omitempty"`
    	// contains filtered or unexported fields
    }

The preferences that apply to all assets in a given context.

### func (*PreferenceSet) Descriptor 
    
    
    func (*PreferenceSet) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use PreferenceSet.ProtoReflect.Descriptor instead.

### func (*PreferenceSet) GetCreateTime 
    
    
    func (x *PreferenceSet) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*PreferenceSet) GetDescription 
    
    
    func (x *PreferenceSet) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*PreferenceSet) GetDisplayName 
    
    
    func (x *PreferenceSet) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*PreferenceSet) GetName 
    
    
    func (x *PreferenceSet) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*PreferenceSet) GetUpdateTime 
    
    
    func (x *PreferenceSet) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*PreferenceSet) GetVirtualMachinePreferences 
    
    
    func (x *PreferenceSet) GetVirtualMachinePreferences() *VirtualMachinePreferences

### func (*PreferenceSet) ProtoMessage 
    
    
    func (*PreferenceSet) ProtoMessage()

### func (*PreferenceSet) ProtoReflect 
    
    
    func (x *PreferenceSet) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*PreferenceSet) Reset 
    
    
    func (x *PreferenceSet) Reset()

### func (*PreferenceSet) String 
    
    
    func (x *PreferenceSet) String() [string](https://pkg.go.dev/builtin#string)

## RegionPreferences
    
    
    type RegionPreferences struct {
    
    	// A list of preferred regions,
    	// ordered by the most preferred region first.
    	// Set only valid Google Cloud region names.
    	// See https://cloud.google.com/compute/docs/regions-zones
    	// for available regions.
    	PreferredRegions [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=preferred_regions,json=preferredRegions,proto3" json:"preferred_regions,omitempty"`
    	// contains filtered or unexported fields
    }

The user preferences relating to target regions.

### func (*RegionPreferences) Descriptor 
    
    
    func (*RegionPreferences) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RegionPreferences.ProtoReflect.Descriptor instead.

### func (*RegionPreferences) GetPreferredRegions 
    
    
    func (x *RegionPreferences) GetPreferredRegions() [][string](https://pkg.go.dev/builtin#string)

### func (*RegionPreferences) ProtoMessage 
    
    
    func (*RegionPreferences) ProtoMessage()

### func (*RegionPreferences) ProtoReflect 
    
    
    func (x *RegionPreferences) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RegionPreferences) Reset 
    
    
    func (x *RegionPreferences) Reset()

### func (*RegionPreferences) String 
    
    
    func (x *RegionPreferences) String() [string](https://pkg.go.dev/builtin#string)

## RemoveAssetsFromGroupRequest
    
    
    type RemoveAssetsFromGroupRequest struct {
    
    	// Required. Group reference.
    	Group [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=group,proto3" json:"group,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// Required. List of assets to be removed.
    	// The maximum number of assets that can be removed in a single request is
    	// 1000.
    	Assets *AssetList `protobuf:"bytes,3,opt,name=assets,proto3" json:"assets,omitempty"`
    	// Optional. When this value is set to `false` and one of the given assets is
    	// not an existing member of the group, the operation fails with a `Not Found`
    	// error. When set to `true` this situation is silently ignored by the server.
    	//
    	// Default value is `false`.
    	AllowMissing [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,4,opt,name=allow_missing,json=allowMissing,proto3" json:"allow_missing,omitempty"`
    	// contains filtered or unexported fields
    }

A request to remove assets from a group.

### func (*RemoveAssetsFromGroupRequest) Descriptor 
    
    
    func (*RemoveAssetsFromGroupRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RemoveAssetsFromGroupRequest.ProtoReflect.Descriptor instead.

### func (*RemoveAssetsFromGroupRequest) GetAllowMissing 
    
    
    func (x *RemoveAssetsFromGroupRequest) GetAllowMissing() [bool](https://pkg.go.dev/builtin#bool)

### func (*RemoveAssetsFromGroupRequest) GetAssets 
    
    
    func (x *RemoveAssetsFromGroupRequest) GetAssets() *AssetList

### func (*RemoveAssetsFromGroupRequest) GetGroup 
    
    
    func (x *RemoveAssetsFromGroupRequest) GetGroup() [string](https://pkg.go.dev/builtin#string)

### func (*RemoveAssetsFromGroupRequest) GetRequestId 
    
    
    func (x *RemoveAssetsFromGroupRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*RemoveAssetsFromGroupRequest) ProtoMessage 
    
    
    func (*RemoveAssetsFromGroupRequest) ProtoMessage()

### func (*RemoveAssetsFromGroupRequest) ProtoReflect 
    
    
    func (x *RemoveAssetsFromGroupRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RemoveAssetsFromGroupRequest) Reset 
    
    
    func (x *RemoveAssetsFromGroupRequest) Reset()

### func (*RemoveAssetsFromGroupRequest) String 
    
    
    func (x *RemoveAssetsFromGroupRequest) String() [string](https://pkg.go.dev/builtin#string)

## Report
    
    
    type Report struct {
    
    	// Output only. Name of resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. Creation timestamp.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. Last update timestamp.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// User-friendly display name. Maximum length is 63 characters.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Free-text description.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=description,proto3" json:"description,omitempty"`
    	// Report type.
    	Type Report_Type `protobuf:"varint,6,opt,name=type,proto3,enum=google.cloud.migrationcenter.v1.Report_Type" json:"type,omitempty"`
    	// Report creation state.
    	State Report_State `protobuf:"varint,7,opt,name=state,proto3,enum=google.cloud.migrationcenter.v1.Report_State" json:"state,omitempty"`
    	// Output only. Summary view of the Report.
    	Summary *ReportSummary `protobuf:"bytes,8,opt,name=summary,proto3" json:"summary,omitempty"`
    	// contains filtered or unexported fields
    }

Report represents a point-in-time rendering of the ReportConfig results.

### func (*Report) Descriptor 
    
    
    func (*Report) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Report.ProtoReflect.Descriptor instead.

### func (*Report) GetCreateTime 
    
    
    func (x *Report) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Report) GetDescription 
    
    
    func (x *Report) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Report) GetDisplayName 
    
    
    func (x *Report) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Report) GetName 
    
    
    func (x *Report) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Report) GetState 
    
    
    func (x *Report) GetState() Report_State

### func (*Report) GetSummary 
    
    
    func (x *Report) GetSummary() *ReportSummary

### func (*Report) GetType 
    
    
    func (x *Report) GetType() Report_Type

### func (*Report) GetUpdateTime 
    
    
    func (x *Report) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Report) ProtoMessage 
    
    
    func (*Report) ProtoMessage()

### func (*Report) ProtoReflect 
    
    
    func (x *Report) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Report) Reset 
    
    
    func (x *Report) Reset()

### func (*Report) String 
    
    
    func (x *Report) String() [string](https://pkg.go.dev/builtin#string)

## ReportAssetFramesRequest
    
    
    type ReportAssetFramesRequest struct {
    
    	// Required. Parent of the resource.
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Collection of frames data.
    	Frames *Frames `protobuf:"bytes,2,opt,name=frames,proto3" json:"frames,omitempty"`
    	// Required. Reference to a source.
    	Source [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=source,proto3" json:"source,omitempty"`
    	// contains filtered or unexported fields
    }

A request to report a set of asset frames.

### func (*ReportAssetFramesRequest) Descriptor 
    
    
    func (*ReportAssetFramesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportAssetFramesRequest.ProtoReflect.Descriptor instead.

### func (*ReportAssetFramesRequest) GetFrames 
    
    
    func (x *ReportAssetFramesRequest) GetFrames() *Frames

### func (*ReportAssetFramesRequest) GetParent 
    
    
    func (x *ReportAssetFramesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ReportAssetFramesRequest) GetSource 
    
    
    func (x *ReportAssetFramesRequest) GetSource() [string](https://pkg.go.dev/builtin#string)

### func (*ReportAssetFramesRequest) ProtoMessage 
    
    
    func (*ReportAssetFramesRequest) ProtoMessage()

### func (*ReportAssetFramesRequest) ProtoReflect 
    
    
    func (x *ReportAssetFramesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportAssetFramesRequest) Reset 
    
    
    func (x *ReportAssetFramesRequest) Reset()

### func (*ReportAssetFramesRequest) String 
    
    
    func (x *ReportAssetFramesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ReportAssetFramesResponse
    
    
    type ReportAssetFramesResponse struct {
    	// contains filtered or unexported fields
    }

A response to a call to `ReportAssetFrame`.

### func (*ReportAssetFramesResponse) Descriptor 
    
    
    func (*ReportAssetFramesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportAssetFramesResponse.ProtoReflect.Descriptor instead.

### func (*ReportAssetFramesResponse) ProtoMessage 
    
    
    func (*ReportAssetFramesResponse) ProtoMessage()

### func (*ReportAssetFramesResponse) ProtoReflect 
    
    
    func (x *ReportAssetFramesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportAssetFramesResponse) Reset 
    
    
    func (x *ReportAssetFramesResponse) Reset()

### func (*ReportAssetFramesResponse) String 
    
    
    func (x *ReportAssetFramesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ReportConfig
    
    
    type ReportConfig struct {
    
    	// Output only. Name of resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The timestamp when the resource was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The timestamp when the resource was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// User-friendly display name. Maximum length is 63 characters.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Free-text description.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=description,proto3" json:"description,omitempty"`
    	// Required. Collection of combinations of groups and preference sets.
    	GroupPreferencesetAssignments []*ReportConfig_GroupPreferenceSetAssignment `protobuf:"bytes,6,rep,name=group_preferenceset_assignments,json=groupPreferencesetAssignments,proto3" json:"group_preferenceset_assignments,omitempty"`
    	// contains filtered or unexported fields
    }

The groups and associated preference sets on which we can generate reports.

### func (*ReportConfig) Descriptor 
    
    
    func (*ReportConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportConfig.ProtoReflect.Descriptor instead.

### func (*ReportConfig) GetCreateTime 
    
    
    func (x *ReportConfig) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ReportConfig) GetDescription 
    
    
    func (x *ReportConfig) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*ReportConfig) GetDisplayName 
    
    
    func (x *ReportConfig) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*ReportConfig) GetGroupPreferencesetAssignments 
    
    
    func (x *ReportConfig) GetGroupPreferencesetAssignments() []*ReportConfig_GroupPreferenceSetAssignment

### func (*ReportConfig) GetName 
    
    
    func (x *ReportConfig) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ReportConfig) GetUpdateTime 
    
    
    func (x *ReportConfig) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*ReportConfig) ProtoMessage 
    
    
    func (*ReportConfig) ProtoMessage()

### func (*ReportConfig) ProtoReflect 
    
    
    func (x *ReportConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportConfig) Reset 
    
    
    func (x *ReportConfig) Reset()

### func (*ReportConfig) String 
    
    
    func (x *ReportConfig) String() [string](https://pkg.go.dev/builtin#string)

## ReportConfig_GroupPreferenceSetAssignment
    
    
    type ReportConfig_GroupPreferenceSetAssignment struct {
    
    	// Required. Name of the group.
    	Group [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=group,proto3" json:"group,omitempty"`
    	// Required. Name of the Preference Set.
    	PreferenceSet [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=preference_set,json=preferenceSet,proto3" json:"preference_set,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a combination of a group with a preference set.

### func (*ReportConfig_GroupPreferenceSetAssignment) Descriptor 
    
    
    func (*ReportConfig_GroupPreferenceSetAssignment) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportConfig_GroupPreferenceSetAssignment.ProtoReflect.Descriptor instead.

### func (*ReportConfig_GroupPreferenceSetAssignment) GetGroup 
    
    
    func (x *ReportConfig_GroupPreferenceSetAssignment) GetGroup() [string](https://pkg.go.dev/builtin#string)

### func (*ReportConfig_GroupPreferenceSetAssignment) GetPreferenceSet 
    
    
    func (x *ReportConfig_GroupPreferenceSetAssignment) GetPreferenceSet() [string](https://pkg.go.dev/builtin#string)

### func (*ReportConfig_GroupPreferenceSetAssignment) ProtoMessage 
    
    
    func (*ReportConfig_GroupPreferenceSetAssignment) ProtoMessage()

### func (*ReportConfig_GroupPreferenceSetAssignment) ProtoReflect 
    
    
    func (x *ReportConfig_GroupPreferenceSetAssignment) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportConfig_GroupPreferenceSetAssignment) Reset 
    
    
    func (x *ReportConfig_GroupPreferenceSetAssignment) Reset()

### func (*ReportConfig_GroupPreferenceSetAssignment) String 
    
    
    func (x *ReportConfig_GroupPreferenceSetAssignment) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary
    
    
    type ReportSummary struct {
    
    	// Aggregate statistics for all the assets across all the groups.
    	AllAssetsStats *ReportSummary_AssetAggregateStats `protobuf:"bytes,1,opt,name=all_assets_stats,json=allAssetsStats,proto3" json:"all_assets_stats,omitempty"`
    	// Findings for each Group included in this report.
    	GroupFindings []*ReportSummary_GroupFinding `protobuf:"bytes,2,rep,name=group_findings,json=groupFindings,proto3" json:"group_findings,omitempty"`
    	// contains filtered or unexported fields
    }

Describes the Summary view of a Report, which contains aggregated values for all the groups and preference sets included in this Report.

### func (*ReportSummary) Descriptor 
    
    
    func (*ReportSummary) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary.ProtoReflect.Descriptor instead.

### func (*ReportSummary) GetAllAssetsStats 
    
    
    func (x *ReportSummary) GetAllAssetsStats() *ReportSummary_AssetAggregateStats

### func (*ReportSummary) GetGroupFindings 
    
    
    func (x *ReportSummary) GetGroupFindings() []*ReportSummary_GroupFinding

### func (*ReportSummary) ProtoMessage 
    
    
    func (*ReportSummary) ProtoMessage()

### func (*ReportSummary) ProtoReflect 
    
    
    func (x *ReportSummary) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary) Reset 
    
    
    func (x *ReportSummary) Reset()

### func (*ReportSummary) String 
    
    
    func (x *ReportSummary) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_AssetAggregateStats
    
    
    type ReportSummary_AssetAggregateStats struct {
    
    	// Sum of the memory in bytes of all the assets in this collection.
    	TotalMemoryBytes [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=total_memory_bytes,json=totalMemoryBytes,proto3" json:"total_memory_bytes,omitempty"`
    	// Sum of persistent storage in bytes of all the assets in this collection.
    	TotalStorageBytes [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=total_storage_bytes,json=totalStorageBytes,proto3" json:"total_storage_bytes,omitempty"`
    	// Sum of the CPU core count of all the assets in this collection.
    	TotalCores [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=total_cores,json=totalCores,proto3" json:"total_cores,omitempty"`
    	// Count of the number of unique assets in this collection.
    	TotalAssets [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=total_assets,json=totalAssets,proto3" json:"total_assets,omitempty"`
    	// Total memory split into Used/Free buckets.
    	MemoryUtilizationChart *ReportSummary_UtilizationChartData `protobuf:"bytes,5,opt,name=memory_utilization_chart,json=memoryUtilizationChart,proto3" json:"memory_utilization_chart,omitempty"`
    	// Total memory split into Used/Free buckets.
    	StorageUtilizationChart *ReportSummary_UtilizationChartData `protobuf:"bytes,6,opt,name=storage_utilization_chart,json=storageUtilizationChart,proto3" json:"storage_utilization_chart,omitempty"`
    	// Count of assets grouped by Operating System families.
    	OperatingSystem *ReportSummary_ChartData `protobuf:"bytes,7,opt,name=operating_system,json=operatingSystem,proto3" json:"operating_system,omitempty"`
    	// Histogram showing a distribution of CPU core counts.
    	CoreCountHistogram *ReportSummary_HistogramChartData `protobuf:"bytes,8,opt,name=core_count_histogram,json=coreCountHistogram,proto3" json:"core_count_histogram,omitempty"`
    	// Histogram showing a distribution of memory sizes.
    	MemoryBytesHistogram *ReportSummary_HistogramChartData `protobuf:"bytes,9,opt,name=memory_bytes_histogram,json=memoryBytesHistogram,proto3" json:"memory_bytes_histogram,omitempty"`
    	// Histogram showing a distribution of memory sizes.
    	StorageBytesHistogram *ReportSummary_HistogramChartData `protobuf:"bytes,10,opt,name=storage_bytes_histogram,json=storageBytesHistogram,proto3" json:"storage_bytes_histogram,omitempty"`
    	// contains filtered or unexported fields
    }

Aggregate statistics for a collection of assets.

### func (*ReportSummary_AssetAggregateStats) Descriptor 
    
    
    func (*ReportSummary_AssetAggregateStats) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_AssetAggregateStats.ProtoReflect.Descriptor instead.

### func (*ReportSummary_AssetAggregateStats) GetCoreCountHistogram 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetCoreCountHistogram() *ReportSummary_HistogramChartData

### func (*ReportSummary_AssetAggregateStats) GetMemoryBytesHistogram 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetMemoryBytesHistogram() *ReportSummary_HistogramChartData

### func (*ReportSummary_AssetAggregateStats) GetMemoryUtilizationChart 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetMemoryUtilizationChart() *ReportSummary_UtilizationChartData

### func (*ReportSummary_AssetAggregateStats) GetOperatingSystem 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetOperatingSystem() *ReportSummary_ChartData

### func (*ReportSummary_AssetAggregateStats) GetStorageBytesHistogram 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetStorageBytesHistogram() *ReportSummary_HistogramChartData

### func (*ReportSummary_AssetAggregateStats) GetStorageUtilizationChart 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetStorageUtilizationChart() *ReportSummary_UtilizationChartData

### func (*ReportSummary_AssetAggregateStats) GetTotalAssets 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetTotalAssets() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_AssetAggregateStats) GetTotalCores 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetTotalCores() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_AssetAggregateStats) GetTotalMemoryBytes 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetTotalMemoryBytes() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_AssetAggregateStats) GetTotalStorageBytes 
    
    
    func (x *ReportSummary_AssetAggregateStats) GetTotalStorageBytes() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_AssetAggregateStats) ProtoMessage 
    
    
    func (*ReportSummary_AssetAggregateStats) ProtoMessage()

### func (*ReportSummary_AssetAggregateStats) ProtoReflect 
    
    
    func (x *ReportSummary_AssetAggregateStats) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_AssetAggregateStats) Reset 
    
    
    func (x *ReportSummary_AssetAggregateStats) Reset()

### func (*ReportSummary_AssetAggregateStats) String 
    
    
    func (x *ReportSummary_AssetAggregateStats) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_ChartData
    
    
    type ReportSummary_ChartData struct {
    
    	// Each data point in the chart is represented as a name-value pair
    	// with the name being the x-axis label, and the value being the y-axis
    	// value.
    	DataPoints []*ReportSummary_ChartData_DataPoint `protobuf:"bytes,1,rep,name=data_points,json=dataPoints,proto3" json:"data_points,omitempty"`
    	// contains filtered or unexported fields
    }

Describes a collection of data points rendered as a Chart.

### func (*ReportSummary_ChartData) Descriptor 
    
    
    func (*ReportSummary_ChartData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_ChartData.ProtoReflect.Descriptor instead.

### func (*ReportSummary_ChartData) GetDataPoints 
    
    
    func (x *ReportSummary_ChartData) GetDataPoints() []*ReportSummary_ChartData_DataPoint

### func (*ReportSummary_ChartData) ProtoMessage 
    
    
    func (*ReportSummary_ChartData) ProtoMessage()

### func (*ReportSummary_ChartData) ProtoReflect 
    
    
    func (x *ReportSummary_ChartData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_ChartData) Reset 
    
    
    func (x *ReportSummary_ChartData) Reset()

### func (*ReportSummary_ChartData) String 
    
    
    func (x *ReportSummary_ChartData) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_ChartData_DataPoint
    
    
    type ReportSummary_ChartData_DataPoint struct {
    
    	// The X-axis label for this data point.
    	Label [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=label,proto3" json:"label,omitempty"`
    	// The Y-axis value for this data point.
    	Value [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=value,proto3" json:"value,omitempty"`
    	// contains filtered or unexported fields
    }

Describes a single data point in the Chart.

### func (*ReportSummary_ChartData_DataPoint) Descriptor 
    
    
    func (*ReportSummary_ChartData_DataPoint) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_ChartData_DataPoint.ProtoReflect.Descriptor instead.

### func (*ReportSummary_ChartData_DataPoint) GetLabel 
    
    
    func (x *ReportSummary_ChartData_DataPoint) GetLabel() [string](https://pkg.go.dev/builtin#string)

### func (*ReportSummary_ChartData_DataPoint) GetValue 
    
    
    func (x *ReportSummary_ChartData_DataPoint) GetValue() [float64](https://pkg.go.dev/builtin#float64)

### func (*ReportSummary_ChartData_DataPoint) ProtoMessage 
    
    
    func (*ReportSummary_ChartData_DataPoint) ProtoMessage()

### func (*ReportSummary_ChartData_DataPoint) ProtoReflect 
    
    
    func (x *ReportSummary_ChartData_DataPoint) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_ChartData_DataPoint) Reset 
    
    
    func (x *ReportSummary_ChartData_DataPoint) Reset()

### func (*ReportSummary_ChartData_DataPoint) String 
    
    
    func (x *ReportSummary_ChartData_DataPoint) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_ComputeEngineFinding
    
    
    type ReportSummary_ComputeEngineFinding struct {
    
    	// Set of regions in which the assets were allocated.
    	AllocatedRegions [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=allocated_regions,json=allocatedRegions,proto3" json:"allocated_regions,omitempty"`
    	// Count of assets which were allocated.
    	AllocatedAssetCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=allocated_asset_count,json=allocatedAssetCount,proto3" json:"allocated_asset_count,omitempty"`
    	// Distribution of assets based on the Machine Series.
    	MachineSeriesAllocations []*ReportSummary_MachineSeriesAllocation `protobuf:"bytes,3,rep,name=machine_series_allocations,json=machineSeriesAllocations,proto3" json:"machine_series_allocations,omitempty"`
    	// Set of disk types allocated to assets.
    	AllocatedDiskTypes []PersistentDiskType `protobuf:"varint,4,rep,packed,name=allocated_disk_types,json=allocatedDiskTypes,proto3,enum=google.cloud.migrationcenter.v1.PersistentDiskType" json:"allocated_disk_types,omitempty"`
    	// contains filtered or unexported fields
    }

A set of findings that applies to assets destined for Compute Engine.

### func (*ReportSummary_ComputeEngineFinding) Descriptor 
    
    
    func (*ReportSummary_ComputeEngineFinding) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_ComputeEngineFinding.ProtoReflect.Descriptor instead.

### func (*ReportSummary_ComputeEngineFinding) GetAllocatedAssetCount 
    
    
    func (x *ReportSummary_ComputeEngineFinding) GetAllocatedAssetCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_ComputeEngineFinding) GetAllocatedDiskTypes 
    
    
    func (x *ReportSummary_ComputeEngineFinding) GetAllocatedDiskTypes() []PersistentDiskType

### func (*ReportSummary_ComputeEngineFinding) GetAllocatedRegions 
    
    
    func (x *ReportSummary_ComputeEngineFinding) GetAllocatedRegions() [][string](https://pkg.go.dev/builtin#string)

### func (*ReportSummary_ComputeEngineFinding) GetMachineSeriesAllocations 
    
    
    func (x *ReportSummary_ComputeEngineFinding) GetMachineSeriesAllocations() []*ReportSummary_MachineSeriesAllocation

### func (*ReportSummary_ComputeEngineFinding) ProtoMessage 
    
    
    func (*ReportSummary_ComputeEngineFinding) ProtoMessage()

### func (*ReportSummary_ComputeEngineFinding) ProtoReflect 
    
    
    func (x *ReportSummary_ComputeEngineFinding) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_ComputeEngineFinding) Reset 
    
    
    func (x *ReportSummary_ComputeEngineFinding) Reset()

### func (*ReportSummary_ComputeEngineFinding) String 
    
    
    func (x *ReportSummary_ComputeEngineFinding) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_GroupFinding
    
    
    type ReportSummary_GroupFinding struct {
    
    	// Display Name for the Group.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Description for the Group.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`
    	// Summary statistics for all the assets in this group.
    	AssetAggregateStats *ReportSummary_AssetAggregateStats `protobuf:"bytes,3,opt,name=asset_aggregate_stats,json=assetAggregateStats,proto3" json:"asset_aggregate_stats,omitempty"`
    	// This field is deprecated, do not rely on it having a value.
    	//
    	// Deprecated: Marked as deprecated in google/cloud/migrationcenter/v1/migrationcenter.proto.
    	OverlappingAssetCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=overlapping_asset_count,json=overlappingAssetCount,proto3" json:"overlapping_asset_count,omitempty"`
    	// Findings for each of the PreferenceSets for this group.
    	PreferenceSetFindings []*ReportSummary_GroupPreferenceSetFinding `protobuf:"bytes,5,rep,name=preference_set_findings,json=preferenceSetFindings,proto3" json:"preference_set_findings,omitempty"`
    	// contains filtered or unexported fields
    }

Summary Findings for a specific Group.

### func (*ReportSummary_GroupFinding) Descriptor 
    
    
    func (*ReportSummary_GroupFinding) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_GroupFinding.ProtoReflect.Descriptor instead.

### func (*ReportSummary_GroupFinding) GetAssetAggregateStats 
    
    
    func (x *ReportSummary_GroupFinding) GetAssetAggregateStats() *ReportSummary_AssetAggregateStats

### func (*ReportSummary_GroupFinding) GetDescription 
    
    
    func (x *ReportSummary_GroupFinding) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*ReportSummary_GroupFinding) GetDisplayName 
    
    
    func (x *ReportSummary_GroupFinding) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*ReportSummary_GroupFinding) GetOverlappingAssetCount 
    
    
    func (x *ReportSummary_GroupFinding) GetOverlappingAssetCount() [int64](https://pkg.go.dev/builtin#int64)

Deprecated: Marked as deprecated in google/cloud/migrationcenter/v1/migrationcenter.proto.

### func (*ReportSummary_GroupFinding) GetPreferenceSetFindings 
    
    
    func (x *ReportSummary_GroupFinding) GetPreferenceSetFindings() []*ReportSummary_GroupPreferenceSetFinding

### func (*ReportSummary_GroupFinding) ProtoMessage 
    
    
    func (*ReportSummary_GroupFinding) ProtoMessage()

### func (*ReportSummary_GroupFinding) ProtoReflect 
    
    
    func (x *ReportSummary_GroupFinding) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_GroupFinding) Reset 
    
    
    func (x *ReportSummary_GroupFinding) Reset()

### func (*ReportSummary_GroupFinding) String 
    
    
    func (x *ReportSummary_GroupFinding) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_GroupPreferenceSetFinding
    
    
    type ReportSummary_GroupPreferenceSetFinding struct {
    
    	// Display Name of the Preference Set
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Description for the Preference Set.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`
    	// A set of preferences that applies to all machines in the context.
    	MachinePreferences *VirtualMachinePreferences `protobuf:"bytes,3,opt,name=machine_preferences,json=machinePreferences,proto3" json:"machine_preferences,omitempty"`
    	// Total monthly cost for this preference set.
    	MonthlyCostTotal *money.Money `protobuf:"bytes,4,opt,name=monthly_cost_total,json=monthlyCostTotal,proto3" json:"monthly_cost_total,omitempty"`
    	// Compute monthly cost for this preference set.
    	MonthlyCostCompute *money.Money `protobuf:"bytes,5,opt,name=monthly_cost_compute,json=monthlyCostCompute,proto3" json:"monthly_cost_compute,omitempty"`
    	// Licensing monthly cost for this preference set.
    	MonthlyCostOsLicense *money.Money `protobuf:"bytes,6,opt,name=monthly_cost_os_license,json=monthlyCostOsLicense,proto3" json:"monthly_cost_os_license,omitempty"`
    	// Network Egress monthly cost for this preference set.
    	MonthlyCostNetworkEgress *money.Money `protobuf:"bytes,7,opt,name=monthly_cost_network_egress,json=monthlyCostNetworkEgress,proto3" json:"monthly_cost_network_egress,omitempty"`
    	// Storage monthly cost for this preference set.
    	MonthlyCostStorage *money.Money `protobuf:"bytes,8,opt,name=monthly_cost_storage,json=monthlyCostStorage,proto3" json:"monthly_cost_storage,omitempty"`
    	// Miscellaneous monthly cost for this preference set.
    	MonthlyCostOther *money.Money `protobuf:"bytes,9,opt,name=monthly_cost_other,json=monthlyCostOther,proto3" json:"monthly_cost_other,omitempty"`
    	// A set of findings that applies to Compute Engine machines in the input.
    	ComputeEngineFinding *ReportSummary_ComputeEngineFinding `protobuf:"bytes,10,opt,name=compute_engine_finding,json=computeEngineFinding,proto3" json:"compute_engine_finding,omitempty"`
    	// A set of findings that applies to VMWare machines in the input.
    	VmwareEngineFinding *ReportSummary_VmwareEngineFinding `protobuf:"bytes,11,opt,name=vmware_engine_finding,json=vmwareEngineFinding,proto3" json:"vmware_engine_finding,omitempty"`
    	// A set of findings that applies to Sole-Tenant machines in the input.
    	SoleTenantFinding *ReportSummary_SoleTenantFinding `protobuf:"bytes,12,opt,name=sole_tenant_finding,json=soleTenantFinding,proto3" json:"sole_tenant_finding,omitempty"`
    	// contains filtered or unexported fields
    }

Summary Findings for a specific Group/PreferenceSet combination.

### func (*ReportSummary_GroupPreferenceSetFinding) Descriptor 
    
    
    func (*ReportSummary_GroupPreferenceSetFinding) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_GroupPreferenceSetFinding.ProtoReflect.Descriptor instead.

### func (*ReportSummary_GroupPreferenceSetFinding) GetComputeEngineFinding 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetComputeEngineFinding() *ReportSummary_ComputeEngineFinding

### func (*ReportSummary_GroupPreferenceSetFinding) GetDescription 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*ReportSummary_GroupPreferenceSetFinding) GetDisplayName 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*ReportSummary_GroupPreferenceSetFinding) GetMachinePreferences 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetMachinePreferences() *VirtualMachinePreferences

### func (*ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostCompute 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostCompute() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostNetworkEgress 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostNetworkEgress() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostOsLicense 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostOsLicense() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostOther 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostOther() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostStorage 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostStorage() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostTotal 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetMonthlyCostTotal() *[money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money).[Money](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/money#Money)

### func (*ReportSummary_GroupPreferenceSetFinding) GetSoleTenantFinding 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetSoleTenantFinding() *ReportSummary_SoleTenantFinding

### func (*ReportSummary_GroupPreferenceSetFinding) GetVmwareEngineFinding 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) GetVmwareEngineFinding() *ReportSummary_VmwareEngineFinding

### func (*ReportSummary_GroupPreferenceSetFinding) ProtoMessage 
    
    
    func (*ReportSummary_GroupPreferenceSetFinding) ProtoMessage()

### func (*ReportSummary_GroupPreferenceSetFinding) ProtoReflect 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_GroupPreferenceSetFinding) Reset 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) Reset()

### func (*ReportSummary_GroupPreferenceSetFinding) String 
    
    
    func (x *ReportSummary_GroupPreferenceSetFinding) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_HistogramChartData
    
    
    type ReportSummary_HistogramChartData struct {
    
    	// Buckets in the histogram.
    	// There will be `n+1` buckets matching `n` lower bounds in the request.
    	// The first bucket will be from -infinity to the first bound.
    	// Subsequent buckets will be between one bound and the next.
    	// The final bucket will be from the final bound to infinity.
    	Buckets []*ReportSummary_HistogramChartData_Bucket `protobuf:"bytes,1,rep,name=buckets,proto3" json:"buckets,omitempty"`
    	// contains filtered or unexported fields
    }

A Histogram Chart shows a distribution of values into buckets, showing a count of values which fall into a bucket.

### func (*ReportSummary_HistogramChartData) Descriptor 
    
    
    func (*ReportSummary_HistogramChartData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_HistogramChartData.ProtoReflect.Descriptor instead.

### func (*ReportSummary_HistogramChartData) GetBuckets 
    
    
    func (x *ReportSummary_HistogramChartData) GetBuckets() []*ReportSummary_HistogramChartData_Bucket

### func (*ReportSummary_HistogramChartData) ProtoMessage 
    
    
    func (*ReportSummary_HistogramChartData) ProtoMessage()

### func (*ReportSummary_HistogramChartData) ProtoReflect 
    
    
    func (x *ReportSummary_HistogramChartData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_HistogramChartData) Reset 
    
    
    func (x *ReportSummary_HistogramChartData) Reset()

### func (*ReportSummary_HistogramChartData) String 
    
    
    func (x *ReportSummary_HistogramChartData) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_HistogramChartData_Bucket
    
    
    type ReportSummary_HistogramChartData_Bucket struct {
    
    	// Lower bound - inclusive.
    	LowerBound [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=lower_bound,json=lowerBound,proto3" json:"lower_bound,omitempty"`
    	// Upper bound - exclusive.
    	UpperBound [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=upper_bound,json=upperBound,proto3" json:"upper_bound,omitempty"`
    	// Count of items in the bucket.
    	Count [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=count,proto3" json:"count,omitempty"`
    	// contains filtered or unexported fields
    }

A histogram bucket with a lower and upper bound, and a count of items with a field value between those bounds. The lower bound is inclusive and the upper bound is exclusive. Lower bound may be -infinity and upper bound may be infinity.

### func (*ReportSummary_HistogramChartData_Bucket) Descriptor 
    
    
    func (*ReportSummary_HistogramChartData_Bucket) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_HistogramChartData_Bucket.ProtoReflect.Descriptor instead.

### func (*ReportSummary_HistogramChartData_Bucket) GetCount 
    
    
    func (x *ReportSummary_HistogramChartData_Bucket) GetCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_HistogramChartData_Bucket) GetLowerBound 
    
    
    func (x *ReportSummary_HistogramChartData_Bucket) GetLowerBound() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_HistogramChartData_Bucket) GetUpperBound 
    
    
    func (x *ReportSummary_HistogramChartData_Bucket) GetUpperBound() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_HistogramChartData_Bucket) ProtoMessage 
    
    
    func (*ReportSummary_HistogramChartData_Bucket) ProtoMessage()

### func (*ReportSummary_HistogramChartData_Bucket) ProtoReflect 
    
    
    func (x *ReportSummary_HistogramChartData_Bucket) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_HistogramChartData_Bucket) Reset 
    
    
    func (x *ReportSummary_HistogramChartData_Bucket) Reset()

### func (*ReportSummary_HistogramChartData_Bucket) String 
    
    
    func (x *ReportSummary_HistogramChartData_Bucket) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_MachineSeriesAllocation
    
    
    type ReportSummary_MachineSeriesAllocation struct {
    
    	// The Machine Series (e.g. "E2", "N2")
    	MachineSeries *MachineSeries `protobuf:"bytes,1,opt,name=machine_series,json=machineSeries,proto3" json:"machine_series,omitempty"`
    	// Count of assets allocated to this machine series.
    	AllocatedAssetCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=allocated_asset_count,json=allocatedAssetCount,proto3" json:"allocated_asset_count,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a data point tracking the count of assets allocated for a specific Machine Series.

### func (*ReportSummary_MachineSeriesAllocation) Descriptor 
    
    
    func (*ReportSummary_MachineSeriesAllocation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_MachineSeriesAllocation.ProtoReflect.Descriptor instead.

### func (*ReportSummary_MachineSeriesAllocation) GetAllocatedAssetCount 
    
    
    func (x *ReportSummary_MachineSeriesAllocation) GetAllocatedAssetCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_MachineSeriesAllocation) GetMachineSeries 
    
    
    func (x *ReportSummary_MachineSeriesAllocation) GetMachineSeries() *MachineSeries

### func (*ReportSummary_MachineSeriesAllocation) ProtoMessage 
    
    
    func (*ReportSummary_MachineSeriesAllocation) ProtoMessage()

### func (*ReportSummary_MachineSeriesAllocation) ProtoReflect 
    
    
    func (x *ReportSummary_MachineSeriesAllocation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_MachineSeriesAllocation) Reset 
    
    
    func (x *ReportSummary_MachineSeriesAllocation) Reset()

### func (*ReportSummary_MachineSeriesAllocation) String 
    
    
    func (x *ReportSummary_MachineSeriesAllocation) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_SoleTenantFinding
    
    
    type ReportSummary_SoleTenantFinding struct {
    
    	// Set of regions in which the assets are allocated
    	AllocatedRegions [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=allocated_regions,json=allocatedRegions,proto3" json:"allocated_regions,omitempty"`
    	// Count of assets which are allocated
    	AllocatedAssetCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=allocated_asset_count,json=allocatedAssetCount,proto3" json:"allocated_asset_count,omitempty"`
    	// Set of per-nodetype allocation records
    	NodeAllocations []*ReportSummary_SoleTenantNodeAllocation `protobuf:"bytes,3,rep,name=node_allocations,json=nodeAllocations,proto3" json:"node_allocations,omitempty"`
    	// contains filtered or unexported fields
    }

A set of findings that applies to assets destined for Sole-Tenant nodes.

### func (*ReportSummary_SoleTenantFinding) Descriptor 
    
    
    func (*ReportSummary_SoleTenantFinding) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_SoleTenantFinding.ProtoReflect.Descriptor instead.

### func (*ReportSummary_SoleTenantFinding) GetAllocatedAssetCount 
    
    
    func (x *ReportSummary_SoleTenantFinding) GetAllocatedAssetCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_SoleTenantFinding) GetAllocatedRegions 
    
    
    func (x *ReportSummary_SoleTenantFinding) GetAllocatedRegions() [][string](https://pkg.go.dev/builtin#string)

### func (*ReportSummary_SoleTenantFinding) GetNodeAllocations 
    
    
    func (x *ReportSummary_SoleTenantFinding) GetNodeAllocations() []*ReportSummary_SoleTenantNodeAllocation

### func (*ReportSummary_SoleTenantFinding) ProtoMessage 
    
    
    func (*ReportSummary_SoleTenantFinding) ProtoMessage()

### func (*ReportSummary_SoleTenantFinding) ProtoReflect 
    
    
    func (x *ReportSummary_SoleTenantFinding) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_SoleTenantFinding) Reset 
    
    
    func (x *ReportSummary_SoleTenantFinding) Reset()

### func (*ReportSummary_SoleTenantFinding) String 
    
    
    func (x *ReportSummary_SoleTenantFinding) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_SoleTenantNodeAllocation
    
    
    type ReportSummary_SoleTenantNodeAllocation struct {
    
    	// Sole Tenant node type, e.g. "m3-node-128-3904"
    	Node *SoleTenantNodeType `protobuf:"bytes,1,opt,name=node,proto3" json:"node,omitempty"`
    	// Count of this node type to be provisioned
    	NodeCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=node_count,json=nodeCount,proto3" json:"node_count,omitempty"`
    	// Count of assets allocated to these nodes
    	AllocatedAssetCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=allocated_asset_count,json=allocatedAssetCount,proto3" json:"allocated_asset_count,omitempty"`
    	// contains filtered or unexported fields
    }

Represents the assets allocated to a specific Sole-Tenant node type.

### func (*ReportSummary_SoleTenantNodeAllocation) Descriptor 
    
    
    func (*ReportSummary_SoleTenantNodeAllocation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_SoleTenantNodeAllocation.ProtoReflect.Descriptor instead.

### func (*ReportSummary_SoleTenantNodeAllocation) GetAllocatedAssetCount 
    
    
    func (x *ReportSummary_SoleTenantNodeAllocation) GetAllocatedAssetCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_SoleTenantNodeAllocation) GetNode 
    
    
    func (x *ReportSummary_SoleTenantNodeAllocation) GetNode() *SoleTenantNodeType

### func (*ReportSummary_SoleTenantNodeAllocation) GetNodeCount 
    
    
    func (x *ReportSummary_SoleTenantNodeAllocation) GetNodeCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_SoleTenantNodeAllocation) ProtoMessage 
    
    
    func (*ReportSummary_SoleTenantNodeAllocation) ProtoMessage()

### func (*ReportSummary_SoleTenantNodeAllocation) ProtoReflect 
    
    
    func (x *ReportSummary_SoleTenantNodeAllocation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_SoleTenantNodeAllocation) Reset 
    
    
    func (x *ReportSummary_SoleTenantNodeAllocation) Reset()

### func (*ReportSummary_SoleTenantNodeAllocation) String 
    
    
    func (x *ReportSummary_SoleTenantNodeAllocation) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_UtilizationChartData
    
    
    type ReportSummary_UtilizationChartData struct {
    
    	// Aggregate value which falls into the "Used" bucket.
    	Used [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=used,proto3" json:"used,omitempty"`
    	// Aggregate value which falls into the "Free" bucket.
    	Free [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=free,proto3" json:"free,omitempty"`
    	// contains filtered or unexported fields
    }

Utilization Chart is a specific type of visualization which displays a metric classified into "Used" and "Free" buckets.

### func (*ReportSummary_UtilizationChartData) Descriptor 
    
    
    func (*ReportSummary_UtilizationChartData) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_UtilizationChartData.ProtoReflect.Descriptor instead.

### func (*ReportSummary_UtilizationChartData) GetFree 
    
    
    func (x *ReportSummary_UtilizationChartData) GetFree() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_UtilizationChartData) GetUsed 
    
    
    func (x *ReportSummary_UtilizationChartData) GetUsed() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_UtilizationChartData) ProtoMessage 
    
    
    func (*ReportSummary_UtilizationChartData) ProtoMessage()

### func (*ReportSummary_UtilizationChartData) ProtoReflect 
    
    
    func (x *ReportSummary_UtilizationChartData) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_UtilizationChartData) Reset 
    
    
    func (x *ReportSummary_UtilizationChartData) Reset()

### func (*ReportSummary_UtilizationChartData) String 
    
    
    func (x *ReportSummary_UtilizationChartData) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_VmwareEngineFinding
    
    
    type ReportSummary_VmwareEngineFinding struct {
    
    	// Set of regions in which the assets were allocated
    	AllocatedRegions [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=allocated_regions,json=allocatedRegions,proto3" json:"allocated_regions,omitempty"`
    	// Count of assets which are allocated
    	AllocatedAssetCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=allocated_asset_count,json=allocatedAssetCount,proto3" json:"allocated_asset_count,omitempty"`
    	// Set of per-nodetype allocation records
    	NodeAllocations []*ReportSummary_VmwareNodeAllocation `protobuf:"bytes,3,rep,name=node_allocations,json=nodeAllocations,proto3" json:"node_allocations,omitempty"`
    	// contains filtered or unexported fields
    }

A set of findings that applies to assets destined for VMWare Engine.

### func (*ReportSummary_VmwareEngineFinding) Descriptor 
    
    
    func (*ReportSummary_VmwareEngineFinding) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_VmwareEngineFinding.ProtoReflect.Descriptor instead.

### func (*ReportSummary_VmwareEngineFinding) GetAllocatedAssetCount 
    
    
    func (x *ReportSummary_VmwareEngineFinding) GetAllocatedAssetCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_VmwareEngineFinding) GetAllocatedRegions 
    
    
    func (x *ReportSummary_VmwareEngineFinding) GetAllocatedRegions() [][string](https://pkg.go.dev/builtin#string)

### func (*ReportSummary_VmwareEngineFinding) GetNodeAllocations 
    
    
    func (x *ReportSummary_VmwareEngineFinding) GetNodeAllocations() []*ReportSummary_VmwareNodeAllocation

### func (*ReportSummary_VmwareEngineFinding) ProtoMessage 
    
    
    func (*ReportSummary_VmwareEngineFinding) ProtoMessage()

### func (*ReportSummary_VmwareEngineFinding) ProtoReflect 
    
    
    func (x *ReportSummary_VmwareEngineFinding) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_VmwareEngineFinding) Reset 
    
    
    func (x *ReportSummary_VmwareEngineFinding) Reset()

### func (*ReportSummary_VmwareEngineFinding) String 
    
    
    func (x *ReportSummary_VmwareEngineFinding) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_VmwareNode
    
    
    type ReportSummary_VmwareNode struct {
    
    	// Code to identify VMware Engine node series, e.g. "ve1-standard-72". Based
    	// on the displayName of
    	// cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.nodeTypes
    	Code [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=code,proto3" json:"code,omitempty"`
    	// contains filtered or unexported fields
    }

A VMWare Engine Node

### func (*ReportSummary_VmwareNode) Descriptor 
    
    
    func (*ReportSummary_VmwareNode) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_VmwareNode.ProtoReflect.Descriptor instead.

### func (*ReportSummary_VmwareNode) GetCode 
    
    
    func (x *ReportSummary_VmwareNode) GetCode() [string](https://pkg.go.dev/builtin#string)

### func (*ReportSummary_VmwareNode) ProtoMessage 
    
    
    func (*ReportSummary_VmwareNode) ProtoMessage()

### func (*ReportSummary_VmwareNode) ProtoReflect 
    
    
    func (x *ReportSummary_VmwareNode) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_VmwareNode) Reset 
    
    
    func (x *ReportSummary_VmwareNode) Reset()

### func (*ReportSummary_VmwareNode) String 
    
    
    func (x *ReportSummary_VmwareNode) String() [string](https://pkg.go.dev/builtin#string)

## ReportSummary_VmwareNodeAllocation
    
    
    type ReportSummary_VmwareNodeAllocation struct {
    
    	// VMWare node type, e.g. "ve1-standard-72"
    	VmwareNode *ReportSummary_VmwareNode `protobuf:"bytes,1,opt,name=vmware_node,json=vmwareNode,proto3" json:"vmware_node,omitempty"`
    	// Count of this node type to be provisioned
    	NodeCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=node_count,json=nodeCount,proto3" json:"node_count,omitempty"`
    	// Count of assets allocated to these nodes
    	AllocatedAssetCount [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=allocated_asset_count,json=allocatedAssetCount,proto3" json:"allocated_asset_count,omitempty"`
    	// contains filtered or unexported fields
    }

Represents assets allocated to a specific VMWare Node type.

### func (*ReportSummary_VmwareNodeAllocation) Descriptor 
    
    
    func (*ReportSummary_VmwareNodeAllocation) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportSummary_VmwareNodeAllocation.ProtoReflect.Descriptor instead.

### func (*ReportSummary_VmwareNodeAllocation) GetAllocatedAssetCount 
    
    
    func (x *ReportSummary_VmwareNodeAllocation) GetAllocatedAssetCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_VmwareNodeAllocation) GetNodeCount 
    
    
    func (x *ReportSummary_VmwareNodeAllocation) GetNodeCount() [int64](https://pkg.go.dev/builtin#int64)

### func (*ReportSummary_VmwareNodeAllocation) GetVmwareNode 
    
    
    func (x *ReportSummary_VmwareNodeAllocation) GetVmwareNode() *ReportSummary_VmwareNode

### func (*ReportSummary_VmwareNodeAllocation) ProtoMessage 
    
    
    func (*ReportSummary_VmwareNodeAllocation) ProtoMessage()

### func (*ReportSummary_VmwareNodeAllocation) ProtoReflect 
    
    
    func (x *ReportSummary_VmwareNodeAllocation) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ReportSummary_VmwareNodeAllocation) Reset 
    
    
    func (x *ReportSummary_VmwareNodeAllocation) Reset()

### func (*ReportSummary_VmwareNodeAllocation) String 
    
    
    func (x *ReportSummary_VmwareNodeAllocation) String() [string](https://pkg.go.dev/builtin#string)

## ReportView
    
    
    type ReportView [int32](https://pkg.go.dev/builtin#int32)

Specifies the types of views that provide complete or partial details of a Report.

### ReportView_REPORT_VIEW_UNSPECIFIED, ReportView_REPORT_VIEW_BASIC, ReportView_REPORT_VIEW_FULL, ReportView_REPORT_VIEW_STANDARD
    
    
    const (
    	// The report view is not specified. The API displays the basic view by
    	// default.
    	ReportView_REPORT_VIEW_UNSPECIFIED ReportView = 0
    	// The report view includes only basic metadata of the Report. Useful for
    	// list views.
    	ReportView_REPORT_VIEW_BASIC ReportView = 1
    	// The report view includes all the metadata of the Report. Useful for
    	// preview.
    	ReportView_REPORT_VIEW_FULL ReportView = 2
    	// The report view includes the standard metadata of an report. Useful for
    	// detail view.
    	ReportView_REPORT_VIEW_STANDARD ReportView = 3
    )

### func (ReportView) Descriptor 
    
    
    func (ReportView) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (ReportView) Enum 
    
    
    func (x ReportView) Enum() *ReportView

### func (ReportView) EnumDescriptor 
    
    
    func (ReportView) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ReportView.Descriptor instead.

### func (ReportView) Number 
    
    
    func (x ReportView) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (ReportView) String 
    
    
    func (x ReportView) String() [string](https://pkg.go.dev/builtin#string)

### func (ReportView) Type 
    
    
    func (ReportView) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Report_State
    
    
    type Report_State [int32](https://pkg.go.dev/builtin#int32)

Report creation state.

### Report_STATE_UNSPECIFIED, Report_PENDING, Report_SUCCEEDED, Report_FAILED
    
    
    const (
    	// Default Report creation state.
    	Report_STATE_UNSPECIFIED Report_State = 0
    	// Creating Report.
    	Report_PENDING Report_State = 1
    	// Successfully created Report.
    	Report_SUCCEEDED Report_State = 2
    	// Failed to create Report.
    	Report_FAILED Report_State = 3
    )

### func (Report_State) Descriptor 
    
    
    func (Report_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Report_State) Enum 
    
    
    func (x Report_State) Enum() *Report_State

### func (Report_State) EnumDescriptor 
    
    
    func (Report_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Report_State.Descriptor instead.

### func (Report_State) Number 
    
    
    func (x Report_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Report_State) String 
    
    
    func (x Report_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Report_State) Type 
    
    
    func (Report_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Report_Type
    
    
    type Report_Type [int32](https://pkg.go.dev/builtin#int32)

Report type.

### Report_TYPE_UNSPECIFIED, Report_TOTAL_COST_OF_OWNERSHIP
    
    
    const (
    	// Default Report type.
    	Report_TYPE_UNSPECIFIED Report_Type = 0
    	// Total cost of ownership Report type.
    	Report_TOTAL_COST_OF_OWNERSHIP Report_Type = 1
    )

### func (Report_Type) Descriptor 
    
    
    func (Report_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Report_Type) Enum 
    
    
    func (x Report_Type) Enum() *Report_Type

### func (Report_Type) EnumDescriptor 
    
    
    func (Report_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Report_Type.Descriptor instead.

### func (Report_Type) Number 
    
    
    func (x Report_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Report_Type) String 
    
    
    func (x Report_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (Report_Type) Type 
    
    
    func (Report_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## RunImportJobRequest
    
    
    type RunImportJobRequest struct {
    
    	// Required. The name of the import job to run.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to run an import job.

### func (*RunImportJobRequest) Descriptor 
    
    
    func (*RunImportJobRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RunImportJobRequest.ProtoReflect.Descriptor instead.

### func (*RunImportJobRequest) GetName 
    
    
    func (x *RunImportJobRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*RunImportJobRequest) GetRequestId 
    
    
    func (x *RunImportJobRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*RunImportJobRequest) ProtoMessage 
    
    
    func (*RunImportJobRequest) ProtoMessage()

### func (*RunImportJobRequest) ProtoReflect 
    
    
    func (x *RunImportJobRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RunImportJobRequest) Reset 
    
    
    func (x *RunImportJobRequest) Reset()

### func (*RunImportJobRequest) String 
    
    
    func (x *RunImportJobRequest) String() [string](https://pkg.go.dev/builtin#string)

## RunningProcess
    
    
    type RunningProcess struct {
    
    	// Process ID.
    	Pid [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=pid,proto3" json:"pid,omitempty"`
    	// Process binary path.
    	ExePath [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=exe_path,json=exePath,proto3" json:"exe_path,omitempty"`
    	// Process full command line.
    	Cmdline [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=cmdline,proto3" json:"cmdline,omitempty"`
    	// User running the process.
    	User [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=user,proto3" json:"user,omitempty"`
    	// Process extended attributes.
    	Attributes map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,100,rep,name=attributes,proto3" json:"attributes,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// contains filtered or unexported fields
    }

Guest OS running process details.

### func (*RunningProcess) Descriptor 
    
    
    func (*RunningProcess) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RunningProcess.ProtoReflect.Descriptor instead.

### func (*RunningProcess) GetAttributes 
    
    
    func (x *RunningProcess) GetAttributes() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*RunningProcess) GetCmdline 
    
    
    func (x *RunningProcess) GetCmdline() [string](https://pkg.go.dev/builtin#string)

### func (*RunningProcess) GetExePath 
    
    
    func (x *RunningProcess) GetExePath() [string](https://pkg.go.dev/builtin#string)

### func (*RunningProcess) GetPid 
    
    
    func (x *RunningProcess) GetPid() [int64](https://pkg.go.dev/builtin#int64)

### func (*RunningProcess) GetUser 
    
    
    func (x *RunningProcess) GetUser() [string](https://pkg.go.dev/builtin#string)

### func (*RunningProcess) ProtoMessage 
    
    
    func (*RunningProcess) ProtoMessage()

### func (*RunningProcess) ProtoReflect 
    
    
    func (x *RunningProcess) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RunningProcess) Reset 
    
    
    func (x *RunningProcess) Reset()

### func (*RunningProcess) String 
    
    
    func (x *RunningProcess) String() [string](https://pkg.go.dev/builtin#string)

## RunningProcessList
    
    
    type RunningProcessList struct {
    
    	// Running process entries.
    	Entries []*RunningProcess `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

List of running guest OS processes.

### func (*RunningProcessList) Descriptor 
    
    
    func (*RunningProcessList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RunningProcessList.ProtoReflect.Descriptor instead.

### func (*RunningProcessList) GetEntries 
    
    
    func (x *RunningProcessList) GetEntries() []*RunningProcess

### func (*RunningProcessList) ProtoMessage 
    
    
    func (*RunningProcessList) ProtoMessage()

### func (*RunningProcessList) ProtoReflect 
    
    
    func (x *RunningProcessList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RunningProcessList) Reset 
    
    
    func (x *RunningProcessList) Reset()

### func (*RunningProcessList) String 
    
    
    func (x *RunningProcessList) String() [string](https://pkg.go.dev/builtin#string)

## RunningService
    
    
    type RunningService struct {
    
    	// Service name.
    	ServiceName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=service_name,json=serviceName,proto3" json:"service_name,omitempty"`
    	// Service state (OS-agnostic).
    	State RunningService_State `protobuf:"varint,2,opt,name=state,proto3,enum=google.cloud.migrationcenter.v1.RunningService_State" json:"state,omitempty"`
    	// Service start mode (OS-agnostic).
    	StartMode RunningService_StartMode `protobuf:"varint,3,opt,name=start_mode,json=startMode,proto3,enum=google.cloud.migrationcenter.v1.RunningService_StartMode" json:"start_mode,omitempty"`
    	// Service binary path.
    	ExePath [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=exe_path,json=exePath,proto3" json:"exe_path,omitempty"`
    	// Service command line.
    	Cmdline [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=cmdline,proto3" json:"cmdline,omitempty"`
    	// Service pid.
    	Pid [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,6,opt,name=pid,proto3" json:"pid,omitempty"`
    	// contains filtered or unexported fields
    }

Guest OS running service details.

### func (*RunningService) Descriptor 
    
    
    func (*RunningService) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RunningService.ProtoReflect.Descriptor instead.

### func (*RunningService) GetCmdline 
    
    
    func (x *RunningService) GetCmdline() [string](https://pkg.go.dev/builtin#string)

### func (*RunningService) GetExePath 
    
    
    func (x *RunningService) GetExePath() [string](https://pkg.go.dev/builtin#string)

### func (*RunningService) GetPid 
    
    
    func (x *RunningService) GetPid() [int64](https://pkg.go.dev/builtin#int64)

### func (*RunningService) GetServiceName 
    
    
    func (x *RunningService) GetServiceName() [string](https://pkg.go.dev/builtin#string)

### func (*RunningService) GetStartMode 
    
    
    func (x *RunningService) GetStartMode() RunningService_StartMode

### func (*RunningService) GetState 
    
    
    func (x *RunningService) GetState() RunningService_State

### func (*RunningService) ProtoMessage 
    
    
    func (*RunningService) ProtoMessage()

### func (*RunningService) ProtoReflect 
    
    
    func (x *RunningService) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RunningService) Reset 
    
    
    func (x *RunningService) Reset()

### func (*RunningService) String 
    
    
    func (x *RunningService) String() [string](https://pkg.go.dev/builtin#string)

## RunningServiceList
    
    
    type RunningServiceList struct {
    
    	// Running service entries.
    	Entries []*RunningService `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
    	// contains filtered or unexported fields
    }

List of running guest OS services.

### func (*RunningServiceList) Descriptor 
    
    
    func (*RunningServiceList) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RunningServiceList.ProtoReflect.Descriptor instead.

### func (*RunningServiceList) GetEntries 
    
    
    func (x *RunningServiceList) GetEntries() []*RunningService

### func (*RunningServiceList) ProtoMessage 
    
    
    func (*RunningServiceList) ProtoMessage()

### func (*RunningServiceList) ProtoReflect 
    
    
    func (x *RunningServiceList) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RunningServiceList) Reset 
    
    
    func (x *RunningServiceList) Reset()

### func (*RunningServiceList) String 
    
    
    func (x *RunningServiceList) String() [string](https://pkg.go.dev/builtin#string)

## RunningService_StartMode
    
    
    type RunningService_StartMode [int32](https://pkg.go.dev/builtin#int32)

Service start mode (OS-agnostic).

### RunningService_START_MODE_UNSPECIFIED, RunningService_BOOT, RunningService_SYSTEM, RunningService_AUTO, RunningService_MANUAL, RunningService_DISABLED
    
    
    const (
    	// Start mode unspecified.
    	RunningService_START_MODE_UNSPECIFIED RunningService_StartMode = 0
    	// The service is a device driver started by the system loader.
    	RunningService_BOOT RunningService_StartMode = 1
    	// The service is a device driver started by the IOInitSystem function.
    	RunningService_SYSTEM RunningService_StartMode = 2
    	// The service is started by the operating system, at system start-up
    	RunningService_AUTO RunningService_StartMode = 3
    	// The service is started only manually, by a user.
    	RunningService_MANUAL RunningService_StartMode = 4
    	// The service is disabled.
    	RunningService_DISABLED RunningService_StartMode = 5
    )

### func (RunningService_StartMode) Descriptor 
    
    
    func (RunningService_StartMode) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (RunningService_StartMode) Enum 
    
    
    func (x RunningService_StartMode) Enum() *RunningService_StartMode

### func (RunningService_StartMode) EnumDescriptor 
    
    
    func (RunningService_StartMode) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RunningService_StartMode.Descriptor instead.

### func (RunningService_StartMode) Number 
    
    
    func (x RunningService_StartMode) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (RunningService_StartMode) String 
    
    
    func (x RunningService_StartMode) String() [string](https://pkg.go.dev/builtin#string)

### func (RunningService_StartMode) Type 
    
    
    func (RunningService_StartMode) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## RunningService_State
    
    
    type RunningService_State [int32](https://pkg.go.dev/builtin#int32)

Service state (OS-agnostic).

### RunningService_STATE_UNSPECIFIED, RunningService_ACTIVE, RunningService_PAUSED, RunningService_STOPPED
    
    
    const (
    	// Service state unspecified.
    	RunningService_STATE_UNSPECIFIED RunningService_State = 0
    	// Service is active.
    	RunningService_ACTIVE RunningService_State = 1
    	// Service is paused.
    	RunningService_PAUSED RunningService_State = 2
    	// Service is stopped.
    	RunningService_STOPPED RunningService_State = 3
    )

### func (RunningService_State) Descriptor 
    
    
    func (RunningService_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (RunningService_State) Enum 
    
    
    func (x RunningService_State) Enum() *RunningService_State

### func (RunningService_State) EnumDescriptor 
    
    
    func (RunningService_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RunningService_State.Descriptor instead.

### func (RunningService_State) Number 
    
    
    func (x RunningService_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (RunningService_State) String 
    
    
    func (x RunningService_State) String() [string](https://pkg.go.dev/builtin#string)

### func (RunningService_State) Type 
    
    
    func (RunningService_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## RuntimeNetworkInfo
    
    
    type RuntimeNetworkInfo struct {
    
    	// Time of the last network scan.
    	ScanTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=scan_time,json=scanTime,proto3" json:"scan_time,omitempty"`
    	// Network connections.
    	Connections *NetworkConnectionList `protobuf:"bytes,2,opt,name=connections,proto3" json:"connections,omitempty"`
    	// contains filtered or unexported fields
    }

Runtime networking information.

### func (*RuntimeNetworkInfo) Descriptor 
    
    
    func (*RuntimeNetworkInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RuntimeNetworkInfo.ProtoReflect.Descriptor instead.

### func (*RuntimeNetworkInfo) GetConnections 
    
    
    func (x *RuntimeNetworkInfo) GetConnections() *NetworkConnectionList

### func (*RuntimeNetworkInfo) GetScanTime 
    
    
    func (x *RuntimeNetworkInfo) GetScanTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*RuntimeNetworkInfo) ProtoMessage 
    
    
    func (*RuntimeNetworkInfo) ProtoMessage()

### func (*RuntimeNetworkInfo) ProtoReflect 
    
    
    func (x *RuntimeNetworkInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RuntimeNetworkInfo) Reset 
    
    
    func (x *RuntimeNetworkInfo) Reset()

### func (*RuntimeNetworkInfo) String 
    
    
    func (x *RuntimeNetworkInfo) String() [string](https://pkg.go.dev/builtin#string)

## Settings
    
    
    type Settings struct {
    
    	// Output only. The name of the resource.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// The preference set used by default for a project.
    	PreferenceSet [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=preference_set,json=preferenceSet,proto3" json:"preference_set,omitempty"`
    	// contains filtered or unexported fields
    }

Describes the Migration Center settings related to the project.

### func (*Settings) Descriptor 
    
    
    func (*Settings) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Settings.ProtoReflect.Descriptor instead.

### func (*Settings) GetName 
    
    
    func (x *Settings) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Settings) GetPreferenceSet 
    
    
    func (x *Settings) GetPreferenceSet() [string](https://pkg.go.dev/builtin#string)

### func (*Settings) ProtoMessage 
    
    
    func (*Settings) ProtoMessage()

### func (*Settings) ProtoReflect 
    
    
    func (x *Settings) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Settings) Reset 
    
    
    func (x *Settings) Reset()

### func (*Settings) String 
    
    
    func (x *Settings) String() [string](https://pkg.go.dev/builtin#string)

## SizingOptimizationStrategy
    
    
    type SizingOptimizationStrategy [int32](https://pkg.go.dev/builtin#int32)

The sizing optimization strategy preferences of a virtual machine. This strategy, in addition to actual usage data of the virtual machine, can help determine the recommended shape on the target platform.

### SizingOptimizationStrategy_SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED, SizingOptimizationStrategy_SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE, SizingOptimizationStrategy_SIZING_OPTIMIZATION_STRATEGY_MODERATE, SizingOptimizationStrategy_SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE
    
    
    const (
    	// Unspecified (default value).
    	SizingOptimizationStrategy_SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED SizingOptimizationStrategy = 0
    	// No optimization applied. Virtual machine sizing matches as closely as
    	// possible the machine shape on the source site, not considering any actual
    	// performance data.
    	SizingOptimizationStrategy_SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE SizingOptimizationStrategy = 1
    	// Virtual machine sizing will match the reported usage and shape, with some
    	// slack. This a good value to start with.
    	SizingOptimizationStrategy_SIZING_OPTIMIZATION_STRATEGY_MODERATE SizingOptimizationStrategy = 2
    	// Virtual machine sizing will match the reported usage, with little slack.
    	// Using this option can help reduce costs.
    	SizingOptimizationStrategy_SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE SizingOptimizationStrategy = 3
    )

### func (SizingOptimizationStrategy) Descriptor 
    
    
    func (SizingOptimizationStrategy) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SizingOptimizationStrategy) Enum 
    
    
    func (x SizingOptimizationStrategy) Enum() *SizingOptimizationStrategy

### func (SizingOptimizationStrategy) EnumDescriptor 
    
    
    func (SizingOptimizationStrategy) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SizingOptimizationStrategy.Descriptor instead.

### func (SizingOptimizationStrategy) Number 
    
    
    func (x SizingOptimizationStrategy) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SizingOptimizationStrategy) String 
    
    
    func (x SizingOptimizationStrategy) String() [string](https://pkg.go.dev/builtin#string)

### func (SizingOptimizationStrategy) Type 
    
    
    func (SizingOptimizationStrategy) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SoleTenancyPreferences
    
    
    type SoleTenancyPreferences struct {
    
    	// CPU overcommit ratio.
    	// Acceptable values are between 1.0 and 2.0 inclusive.
    	CpuOvercommitRatio [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=cpu_overcommit_ratio,json=cpuOvercommitRatio,proto3" json:"cpu_overcommit_ratio,omitempty"`
    	// Sole Tenancy nodes maintenance policy.
    	HostMaintenancePolicy SoleTenancyPreferences_HostMaintenancePolicy `protobuf:"varint,2,opt,name=host_maintenance_policy,json=hostMaintenancePolicy,proto3,enum=google.cloud.migrationcenter.v1.SoleTenancyPreferences_HostMaintenancePolicy" json:"host_maintenance_policy,omitempty"`
    	// Commitment plan to consider when calculating costs for virtual machine
    	// insights and recommendations.
    	// If you are unsure which value to set, a 3 year commitment plan is often a
    	// good value to start with.
    	CommitmentPlan SoleTenancyPreferences_CommitmentPlan `protobuf:"varint,3,opt,name=commitment_plan,json=commitmentPlan,proto3,enum=google.cloud.migrationcenter.v1.SoleTenancyPreferences_CommitmentPlan" json:"commitment_plan,omitempty"`
    	// A list of sole tenant node types.
    	// An empty list means that all possible node types will be considered.
    	NodeTypes []*SoleTenantNodeType `protobuf:"bytes,4,rep,name=node_types,json=nodeTypes,proto3" json:"node_types,omitempty"`
    	// contains filtered or unexported fields
    }

Preferences concerning Sole Tenancy nodes and VMs.

### func (*SoleTenancyPreferences) Descriptor 
    
    
    func (*SoleTenancyPreferences) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SoleTenancyPreferences.ProtoReflect.Descriptor instead.

### func (*SoleTenancyPreferences) GetCommitmentPlan 
    
    
    func (x *SoleTenancyPreferences) GetCommitmentPlan() SoleTenancyPreferences_CommitmentPlan

### func (*SoleTenancyPreferences) GetCpuOvercommitRatio 
    
    
    func (x *SoleTenancyPreferences) GetCpuOvercommitRatio() [float64](https://pkg.go.dev/builtin#float64)

### func (*SoleTenancyPreferences) GetHostMaintenancePolicy 
    
    
    func (x *SoleTenancyPreferences) GetHostMaintenancePolicy() SoleTenancyPreferences_HostMaintenancePolicy

### func (*SoleTenancyPreferences) GetNodeTypes 
    
    
    func (x *SoleTenancyPreferences) GetNodeTypes() []*SoleTenantNodeType

### func (*SoleTenancyPreferences) ProtoMessage 
    
    
    func (*SoleTenancyPreferences) ProtoMessage()

### func (*SoleTenancyPreferences) ProtoReflect 
    
    
    func (x *SoleTenancyPreferences) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SoleTenancyPreferences) Reset 
    
    
    func (x *SoleTenancyPreferences) Reset()

### func (*SoleTenancyPreferences) String 
    
    
    func (x *SoleTenancyPreferences) String() [string](https://pkg.go.dev/builtin#string)

## SoleTenancyPreferences_CommitmentPlan
    
    
    type SoleTenancyPreferences_CommitmentPlan [int32](https://pkg.go.dev/builtin#int32)

Type of committed use discount.

### SoleTenancyPreferences_COMMITMENT_PLAN_UNSPECIFIED, SoleTenancyPreferences_ON_DEMAND, SoleTenancyPreferences_COMMITMENT_1_YEAR, SoleTenancyPreferences_COMMITMENT_3_YEAR
    
    
    const (
    	// Unspecified commitment plan.
    	SoleTenancyPreferences_COMMITMENT_PLAN_UNSPECIFIED SoleTenancyPreferences_CommitmentPlan = 0
    	// No commitment plan (on-demand usage).
    	SoleTenancyPreferences_ON_DEMAND SoleTenancyPreferences_CommitmentPlan = 1
    	// 1 year commitment.
    	SoleTenancyPreferences_COMMITMENT_1_YEAR SoleTenancyPreferences_CommitmentPlan = 2
    	// 3 years commitment.
    	SoleTenancyPreferences_COMMITMENT_3_YEAR SoleTenancyPreferences_CommitmentPlan = 3
    )

### func (SoleTenancyPreferences_CommitmentPlan) Descriptor 
    
    
    func (SoleTenancyPreferences_CommitmentPlan) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SoleTenancyPreferences_CommitmentPlan) Enum 
    
    
    func (x SoleTenancyPreferences_CommitmentPlan) Enum() *SoleTenancyPreferences_CommitmentPlan

### func (SoleTenancyPreferences_CommitmentPlan) EnumDescriptor 
    
    
    func (SoleTenancyPreferences_CommitmentPlan) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SoleTenancyPreferences_CommitmentPlan.Descriptor instead.

### func (SoleTenancyPreferences_CommitmentPlan) Number 
    
    
    func (x SoleTenancyPreferences_CommitmentPlan) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SoleTenancyPreferences_CommitmentPlan) String 
    
    
    func (x SoleTenancyPreferences_CommitmentPlan) String() [string](https://pkg.go.dev/builtin#string)

### func (SoleTenancyPreferences_CommitmentPlan) Type 
    
    
    func (SoleTenancyPreferences_CommitmentPlan) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SoleTenancyPreferences_HostMaintenancePolicy
    
    
    type SoleTenancyPreferences_HostMaintenancePolicy [int32](https://pkg.go.dev/builtin#int32)

Sole Tenancy nodes maintenance policy.

### SoleTenancyPreferences_HOST_MAINTENANCE_POLICY_UNSPECIFIED, SoleTenancyPreferences_HOST_MAINTENANCE_POLICY_DEFAULT, SoleTenancyPreferences_HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE, SoleTenancyPreferences_HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP
    
    
    const (
    	// Unspecified host maintenance policy.
    	SoleTenancyPreferences_HOST_MAINTENANCE_POLICY_UNSPECIFIED SoleTenancyPreferences_HostMaintenancePolicy = 0
    	// Default host maintenance policy.
    	SoleTenancyPreferences_HOST_MAINTENANCE_POLICY_DEFAULT SoleTenancyPreferences_HostMaintenancePolicy = 1
    	// Restart in place host maintenance policy.
    	SoleTenancyPreferences_HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE SoleTenancyPreferences_HostMaintenancePolicy = 2
    	// Migrate within node group host maintenance policy.
    	SoleTenancyPreferences_HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP SoleTenancyPreferences_HostMaintenancePolicy = 3
    )

### func (SoleTenancyPreferences_HostMaintenancePolicy) Descriptor 
    
    
    func (SoleTenancyPreferences_HostMaintenancePolicy) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (SoleTenancyPreferences_HostMaintenancePolicy) Enum 
    
    
    func (x SoleTenancyPreferences_HostMaintenancePolicy) Enum() *SoleTenancyPreferences_HostMaintenancePolicy

### func (SoleTenancyPreferences_HostMaintenancePolicy) EnumDescriptor 
    
    
    func (SoleTenancyPreferences_HostMaintenancePolicy) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SoleTenancyPreferences_HostMaintenancePolicy.Descriptor instead.

### func (SoleTenancyPreferences_HostMaintenancePolicy) Number 
    
    
    func (x SoleTenancyPreferences_HostMaintenancePolicy) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (SoleTenancyPreferences_HostMaintenancePolicy) String 
    
    
    func (x SoleTenancyPreferences_HostMaintenancePolicy) String() [string](https://pkg.go.dev/builtin#string)

### func (SoleTenancyPreferences_HostMaintenancePolicy) Type 
    
    
    func (SoleTenancyPreferences_HostMaintenancePolicy) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## SoleTenantNodeType
    
    
    type SoleTenantNodeType struct {
    
    	// Name of the Sole Tenant node. Consult
    	// https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes
    	NodeName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=node_name,json=nodeName,proto3" json:"node_name,omitempty"`
    	// contains filtered or unexported fields
    }

A Sole Tenant node type.

### func (*SoleTenantNodeType) Descriptor 
    
    
    func (*SoleTenantNodeType) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use SoleTenantNodeType.ProtoReflect.Descriptor instead.

### func (*SoleTenantNodeType) GetNodeName 
    
    
    func (x *SoleTenantNodeType) GetNodeName() [string](https://pkg.go.dev/builtin#string)

### func (*SoleTenantNodeType) ProtoMessage 
    
    
    func (*SoleTenantNodeType) ProtoMessage()

### func (*SoleTenantNodeType) ProtoReflect 
    
    
    func (x *SoleTenantNodeType) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*SoleTenantNodeType) Reset 
    
    
    func (x *SoleTenantNodeType) Reset()

### func (*SoleTenantNodeType) String 
    
    
    func (x *SoleTenantNodeType) String() [string](https://pkg.go.dev/builtin#string)

## Source
    
    
    type Source struct {
    
    	// Output only. The full name of the source.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The timestamp when the source was created.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The timestamp when the source was last updated.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// User-friendly display name.
    	DisplayName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
    	// Free-text description.
    	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=description,proto3" json:"description,omitempty"`
    	// Data source type.
    	Type Source_SourceType `protobuf:"varint,6,opt,name=type,proto3,enum=google.cloud.migrationcenter.v1.Source_SourceType" json:"type,omitempty"`
    	// The information confidence of the source.
    	// The higher the value, the higher the confidence.
    	Priority [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,7,opt,name=priority,proto3" json:"priority,omitempty"`
    	// If `true`, the source is managed by other service(s).
    	Managed [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,8,opt,name=managed,proto3" json:"managed,omitempty"`
    	// Output only. Number of frames that are still being processed.
    	PendingFrameCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,9,opt,name=pending_frame_count,json=pendingFrameCount,proto3" json:"pending_frame_count,omitempty"`
    	// Output only. The number of frames that were reported by the source and
    	// contained errors.
    	ErrorFrameCount [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,10,opt,name=error_frame_count,json=errorFrameCount,proto3" json:"error_frame_count,omitempty"`
    	// Output only. The state of the source.
    	State Source_State `protobuf:"varint,11,opt,name=state,proto3,enum=google.cloud.migrationcenter.v1.Source_State" json:"state,omitempty"`
    	// contains filtered or unexported fields
    }

Source represents an object from which asset information is streamed to Migration Center.

### func (*Source) Descriptor 
    
    
    func (*Source) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Source.ProtoReflect.Descriptor instead.

### func (*Source) GetCreateTime 
    
    
    func (x *Source) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Source) GetDescription 
    
    
    func (x *Source) GetDescription() [string](https://pkg.go.dev/builtin#string)

### func (*Source) GetDisplayName 
    
    
    func (x *Source) GetDisplayName() [string](https://pkg.go.dev/builtin#string)

### func (*Source) GetErrorFrameCount 
    
    
    func (x *Source) GetErrorFrameCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*Source) GetManaged 
    
    
    func (x *Source) GetManaged() [bool](https://pkg.go.dev/builtin#bool)

### func (*Source) GetName 
    
    
    func (x *Source) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Source) GetPendingFrameCount 
    
    
    func (x *Source) GetPendingFrameCount() [int32](https://pkg.go.dev/builtin#int32)

### func (*Source) GetPriority 
    
    
    func (x *Source) GetPriority() [int32](https://pkg.go.dev/builtin#int32)

### func (*Source) GetState 
    
    
    func (x *Source) GetState() Source_State

### func (*Source) GetType 
    
    
    func (x *Source) GetType() Source_SourceType

### func (*Source) GetUpdateTime 
    
    
    func (x *Source) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Source) ProtoMessage 
    
    
    func (*Source) ProtoMessage()

### func (*Source) ProtoReflect 
    
    
    func (x *Source) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Source) Reset 
    
    
    func (x *Source) Reset()

### func (*Source) String 
    
    
    func (x *Source) String() [string](https://pkg.go.dev/builtin#string)

## Source_SourceType
    
    
    type Source_SourceType [int32](https://pkg.go.dev/builtin#int32)

### Source_SOURCE_TYPE_UNKNOWN, Source_SOURCE_TYPE_UPLOAD, Source_SOURCE_TYPE_GUEST_OS_SCAN, Source_SOURCE_TYPE_INVENTORY_SCAN, Source_SOURCE_TYPE_CUSTOM
    
    
    const (
    	// Unspecified
    	Source_SOURCE_TYPE_UNKNOWN Source_SourceType = 0
    	// Manually uploaded file (e.g. CSV)
    	Source_SOURCE_TYPE_UPLOAD Source_SourceType = 1
    	// Guest-level info
    	Source_SOURCE_TYPE_GUEST_OS_SCAN Source_SourceType = 2
    	// Inventory-level scan
    	Source_SOURCE_TYPE_INVENTORY_SCAN Source_SourceType = 3
    	// Third-party owned sources.
    	Source_SOURCE_TYPE_CUSTOM Source_SourceType = 4
    )

### func (Source_SourceType) Descriptor 
    
    
    func (Source_SourceType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Source_SourceType) Enum 
    
    
    func (x Source_SourceType) Enum() *Source_SourceType

### func (Source_SourceType) EnumDescriptor 
    
    
    func (Source_SourceType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Source_SourceType.Descriptor instead.

### func (Source_SourceType) Number 
    
    
    func (x Source_SourceType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Source_SourceType) String 
    
    
    func (x Source_SourceType) String() [string](https://pkg.go.dev/builtin#string)

### func (Source_SourceType) Type 
    
    
    func (Source_SourceType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Source_State
    
    
    type Source_State [int32](https://pkg.go.dev/builtin#int32)

Enumerates possible states of a source.

### Source_STATE_UNSPECIFIED, Source_ACTIVE, Source_DELETING, Source_INVALID
    
    
    const (
    	// Unspecified.
    	Source_STATE_UNSPECIFIED Source_State = 0
    	// The source is active and ready to be used.
    	Source_ACTIVE Source_State = 1
    	// In the process of being deleted.
    	Source_DELETING Source_State = 2
    	// Source is in an invalid state. Asset frames reported to it will be
    	// ignored.
    	Source_INVALID Source_State = 3
    )

### func (Source_State) Descriptor 
    
    
    func (Source_State) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Source_State) Enum 
    
    
    func (x Source_State) Enum() *Source_State

### func (Source_State) EnumDescriptor 
    
    
    func (Source_State) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Source_State.Descriptor instead.

### func (Source_State) Number 
    
    
    func (x Source_State) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Source_State) String 
    
    
    func (x Source_State) String() [string](https://pkg.go.dev/builtin#string)

### func (Source_State) Type 
    
    
    func (Source_State) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## UnimplementedMigrationCenterServer
    
    
    type UnimplementedMigrationCenterServer struct {
    }

UnimplementedMigrationCenterServer should be embedded to have forward compatible implementations.

### func (UnimplementedMigrationCenterServer) AddAssetsToGroup 
    
    
    func (UnimplementedMigrationCenterServer) AddAssetsToGroup([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *AddAssetsToGroupRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) AggregateAssetsValues 
    
    
    func (UnimplementedMigrationCenterServer) AggregateAssetsValues([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *AggregateAssetsValuesRequest) (*AggregateAssetsValuesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) BatchDeleteAssets 
    
    
    func (UnimplementedMigrationCenterServer) BatchDeleteAssets([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *BatchDeleteAssetsRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) BatchUpdateAssets 
    
    
    func (UnimplementedMigrationCenterServer) BatchUpdateAssets([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *BatchUpdateAssetsRequest) (*BatchUpdateAssetsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) CreateGroup 
    
    
    func (UnimplementedMigrationCenterServer) CreateGroup([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateGroupRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) CreateImportDataFile 
    
    
    func (UnimplementedMigrationCenterServer) CreateImportDataFile([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateImportDataFileRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) CreateImportJob 
    
    
    func (UnimplementedMigrationCenterServer) CreateImportJob([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateImportJobRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) CreatePreferenceSet 
    
    
    func (UnimplementedMigrationCenterServer) CreatePreferenceSet([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreatePreferenceSetRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) CreateReport 
    
    
    func (UnimplementedMigrationCenterServer) CreateReport([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateReportRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) CreateReportConfig 
    
    
    func (UnimplementedMigrationCenterServer) CreateReportConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateReportConfigRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) CreateSource 
    
    
    func (UnimplementedMigrationCenterServer) CreateSource([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateSourceRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) DeleteAsset 
    
    
    func (UnimplementedMigrationCenterServer) DeleteAsset([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteAssetRequest) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) DeleteGroup 
    
    
    func (UnimplementedMigrationCenterServer) DeleteGroup([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteGroupRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) DeleteImportDataFile 
    
    
    func (UnimplementedMigrationCenterServer) DeleteImportDataFile([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteImportDataFileRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) DeleteImportJob 
    
    
    func (UnimplementedMigrationCenterServer) DeleteImportJob([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteImportJobRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) DeletePreferenceSet 
    
    
    func (UnimplementedMigrationCenterServer) DeletePreferenceSet([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeletePreferenceSetRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) DeleteReport 
    
    
    func (UnimplementedMigrationCenterServer) DeleteReport([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteReportRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) DeleteReportConfig 
    
    
    func (UnimplementedMigrationCenterServer) DeleteReportConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteReportConfigRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) DeleteSource 
    
    
    func (UnimplementedMigrationCenterServer) DeleteSource([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteSourceRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetAsset 
    
    
    func (UnimplementedMigrationCenterServer) GetAsset([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetAssetRequest) (*Asset, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetErrorFrame 
    
    
    func (UnimplementedMigrationCenterServer) GetErrorFrame([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetErrorFrameRequest) (*ErrorFrame, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetGroup 
    
    
    func (UnimplementedMigrationCenterServer) GetGroup([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetGroupRequest) (*Group, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetImportDataFile 
    
    
    func (UnimplementedMigrationCenterServer) GetImportDataFile([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetImportDataFileRequest) (*ImportDataFile, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetImportJob 
    
    
    func (UnimplementedMigrationCenterServer) GetImportJob([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetImportJobRequest) (*ImportJob, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetPreferenceSet 
    
    
    func (UnimplementedMigrationCenterServer) GetPreferenceSet([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetPreferenceSetRequest) (*PreferenceSet, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetReport 
    
    
    func (UnimplementedMigrationCenterServer) GetReport([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetReportRequest) (*Report, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetReportConfig 
    
    
    func (UnimplementedMigrationCenterServer) GetReportConfig([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetReportConfigRequest) (*ReportConfig, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetSettings 
    
    
    func (UnimplementedMigrationCenterServer) GetSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetSettingsRequest) (*Settings, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) GetSource 
    
    
    func (UnimplementedMigrationCenterServer) GetSource([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetSourceRequest) (*Source, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ListAssets 
    
    
    func (UnimplementedMigrationCenterServer) ListAssets([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListAssetsRequest) (*ListAssetsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ListErrorFrames 
    
    
    func (UnimplementedMigrationCenterServer) ListErrorFrames([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListErrorFramesRequest) (*ListErrorFramesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ListGroups 
    
    
    func (UnimplementedMigrationCenterServer) ListGroups([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListGroupsRequest) (*ListGroupsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ListImportDataFiles 
    
    
    func (UnimplementedMigrationCenterServer) ListImportDataFiles([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListImportDataFilesRequest) (*ListImportDataFilesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ListImportJobs 
    
    
    func (UnimplementedMigrationCenterServer) ListImportJobs([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListImportJobsRequest) (*ListImportJobsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ListPreferenceSets 
    
    
    func (UnimplementedMigrationCenterServer) ListPreferenceSets([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListPreferenceSetsRequest) (*ListPreferenceSetsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ListReportConfigs 
    
    
    func (UnimplementedMigrationCenterServer) ListReportConfigs([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListReportConfigsRequest) (*ListReportConfigsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ListReports 
    
    
    func (UnimplementedMigrationCenterServer) ListReports([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListReportsRequest) (*ListReportsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ListSources 
    
    
    func (UnimplementedMigrationCenterServer) ListSources([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListSourcesRequest) (*ListSourcesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) RemoveAssetsFromGroup 
    
    
    func (UnimplementedMigrationCenterServer) RemoveAssetsFromGroup([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *RemoveAssetsFromGroupRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ReportAssetFrames 
    
    
    func (UnimplementedMigrationCenterServer) ReportAssetFrames([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ReportAssetFramesRequest) (*ReportAssetFramesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) RunImportJob 
    
    
    func (UnimplementedMigrationCenterServer) RunImportJob([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *RunImportJobRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) UpdateAsset 
    
    
    func (UnimplementedMigrationCenterServer) UpdateAsset([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateAssetRequest) (*Asset, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) UpdateGroup 
    
    
    func (UnimplementedMigrationCenterServer) UpdateGroup([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateGroupRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) UpdateImportJob 
    
    
    func (UnimplementedMigrationCenterServer) UpdateImportJob([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateImportJobRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) UpdatePreferenceSet 
    
    
    func (UnimplementedMigrationCenterServer) UpdatePreferenceSet([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdatePreferenceSetRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) UpdateSettings 
    
    
    func (UnimplementedMigrationCenterServer) UpdateSettings([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateSettingsRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) UpdateSource 
    
    
    func (UnimplementedMigrationCenterServer) UpdateSource([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateSourceRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMigrationCenterServer) ValidateImportJob 
    
    
    func (UnimplementedMigrationCenterServer) ValidateImportJob([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ValidateImportJobRequest) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

## UnsafeMigrationCenterServer
    
    
    type UnsafeMigrationCenterServer interface {
    	// contains filtered or unexported methods
    }

UnsafeMigrationCenterServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to MigrationCenterServer will result in compilation errors.

## UpdateAssetRequest
    
    
    type UpdateAssetRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// `Asset` resource by the update.
    	// The values specified in the `update_mask` field are relative to the
    	// resource, not the full request.
    	// A field will be overwritten if it is in the mask.
    	// A single * value in the mask lets you to overwrite all fields.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The resource being updated.
    	Asset *Asset `protobuf:"bytes,2,opt,name=asset,proto3" json:"asset,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to update an asset.

### func (*UpdateAssetRequest) Descriptor 
    
    
    func (*UpdateAssetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateAssetRequest.ProtoReflect.Descriptor instead.

### func (*UpdateAssetRequest) GetAsset 
    
    
    func (x *UpdateAssetRequest) GetAsset() *Asset

### func (*UpdateAssetRequest) GetRequestId 
    
    
    func (x *UpdateAssetRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateAssetRequest) GetUpdateMask 
    
    
    func (x *UpdateAssetRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateAssetRequest) ProtoMessage 
    
    
    func (*UpdateAssetRequest) ProtoMessage()

### func (*UpdateAssetRequest) ProtoReflect 
    
    
    func (x *UpdateAssetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateAssetRequest) Reset 
    
    
    func (x *UpdateAssetRequest) Reset()

### func (*UpdateAssetRequest) String 
    
    
    func (x *UpdateAssetRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateGroupRequest
    
    
    type UpdateGroupRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// `Group` resource by the update.
    	// The values specified in the `update_mask` are relative to the resource, not
    	// the full request. A field will be overwritten if it is in the mask.
    	// A single * value in the mask lets you to overwrite all fields.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The group resource being updated.
    	Group *Group `protobuf:"bytes,2,opt,name=group,proto3" json:"group,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to update a group.

### func (*UpdateGroupRequest) Descriptor 
    
    
    func (*UpdateGroupRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateGroupRequest.ProtoReflect.Descriptor instead.

### func (*UpdateGroupRequest) GetGroup 
    
    
    func (x *UpdateGroupRequest) GetGroup() *Group

### func (*UpdateGroupRequest) GetRequestId 
    
    
    func (x *UpdateGroupRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateGroupRequest) GetUpdateMask 
    
    
    func (x *UpdateGroupRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateGroupRequest) ProtoMessage 
    
    
    func (*UpdateGroupRequest) ProtoMessage()

### func (*UpdateGroupRequest) ProtoReflect 
    
    
    func (x *UpdateGroupRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateGroupRequest) Reset 
    
    
    func (x *UpdateGroupRequest) Reset()

### func (*UpdateGroupRequest) String 
    
    
    func (x *UpdateGroupRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateImportJobRequest
    
    
    type UpdateImportJobRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// `Asset` resource by the update.
    	// The values specified in the `update_mask` field are relative to the
    	// resource, not the full request.
    	// A field will be overwritten if it is in the mask.
    	// A single * value in the mask lets you to overwrite all fields.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The resource being updated
    	ImportJob *ImportJob `protobuf:"bytes,2,opt,name=import_job,json=importJob,proto3" json:"import_job,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to update an import job.

### func (*UpdateImportJobRequest) Descriptor 
    
    
    func (*UpdateImportJobRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateImportJobRequest.ProtoReflect.Descriptor instead.

### func (*UpdateImportJobRequest) GetImportJob 
    
    
    func (x *UpdateImportJobRequest) GetImportJob() *ImportJob

### func (*UpdateImportJobRequest) GetRequestId 
    
    
    func (x *UpdateImportJobRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateImportJobRequest) GetUpdateMask 
    
    
    func (x *UpdateImportJobRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateImportJobRequest) ProtoMessage 
    
    
    func (*UpdateImportJobRequest) ProtoMessage()

### func (*UpdateImportJobRequest) ProtoReflect 
    
    
    func (x *UpdateImportJobRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateImportJobRequest) Reset 
    
    
    func (x *UpdateImportJobRequest) Reset()

### func (*UpdateImportJobRequest) String 
    
    
    func (x *UpdateImportJobRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdatePreferenceSetRequest
    
    
    type UpdatePreferenceSetRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// `PreferenceSet` resource by the update.
    	// The values specified in the `update_mask` field are relative to the
    	// resource, not the full request.
    	// A field will be overwritten if it is in the mask.
    	// A single * value in the mask lets you to overwrite all fields.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The preference set resource being updated.
    	PreferenceSet *PreferenceSet `protobuf:"bytes,2,opt,name=preference_set,json=preferenceSet,proto3" json:"preference_set,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to update a preference set.

### func (*UpdatePreferenceSetRequest) Descriptor 
    
    
    func (*UpdatePreferenceSetRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdatePreferenceSetRequest.ProtoReflect.Descriptor instead.

### func (*UpdatePreferenceSetRequest) GetPreferenceSet 
    
    
    func (x *UpdatePreferenceSetRequest) GetPreferenceSet() *PreferenceSet

### func (*UpdatePreferenceSetRequest) GetRequestId 
    
    
    func (x *UpdatePreferenceSetRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdatePreferenceSetRequest) GetUpdateMask 
    
    
    func (x *UpdatePreferenceSetRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdatePreferenceSetRequest) ProtoMessage 
    
    
    func (*UpdatePreferenceSetRequest) ProtoMessage()

### func (*UpdatePreferenceSetRequest) ProtoReflect 
    
    
    func (x *UpdatePreferenceSetRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdatePreferenceSetRequest) Reset 
    
    
    func (x *UpdatePreferenceSetRequest) Reset()

### func (*UpdatePreferenceSetRequest) String 
    
    
    func (x *UpdatePreferenceSetRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateSettingsRequest
    
    
    type UpdateSettingsRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// `Settings` resource by the update.
    	// The values specified in the `update_mask` field are relative to the
    	// resource, not the full request.
    	// A field will be overwritten if it is in the mask.
    	// A single * value in the mask lets you to overwrite all fields.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The project settings resource being updated.
    	Settings *Settings `protobuf:"bytes,2,opt,name=settings,proto3" json:"settings,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to update the settings.

### func (*UpdateSettingsRequest) Descriptor 
    
    
    func (*UpdateSettingsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateSettingsRequest.ProtoReflect.Descriptor instead.

### func (*UpdateSettingsRequest) GetRequestId 
    
    
    func (x *UpdateSettingsRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateSettingsRequest) GetSettings 
    
    
    func (x *UpdateSettingsRequest) GetSettings() *Settings

### func (*UpdateSettingsRequest) GetUpdateMask 
    
    
    func (x *UpdateSettingsRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateSettingsRequest) ProtoMessage 
    
    
    func (*UpdateSettingsRequest) ProtoMessage()

### func (*UpdateSettingsRequest) ProtoReflect 
    
    
    func (x *UpdateSettingsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateSettingsRequest) Reset 
    
    
    func (x *UpdateSettingsRequest) Reset()

### func (*UpdateSettingsRequest) String 
    
    
    func (x *UpdateSettingsRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateSourceRequest
    
    
    type UpdateSourceRequest struct {
    
    	// Required. Field mask is used to specify the fields to be overwritten in the
    	// `Source` resource by the update.
    	// The values specified in the `update_mask` field are relative to the
    	// resource, not the full request.
    	// A field will be overwritten if it is in the mask.
    	// A single * value in the mask lets you to overwrite all fields.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// Required. The resource being updated
    	Source *Source `protobuf:"bytes,2,opt,name=source,proto3" json:"source,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes since the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to update a source.

### func (*UpdateSourceRequest) Descriptor 
    
    
    func (*UpdateSourceRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateSourceRequest.ProtoReflect.Descriptor instead.

### func (*UpdateSourceRequest) GetRequestId 
    
    
    func (x *UpdateSourceRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*UpdateSourceRequest) GetSource 
    
    
    func (x *UpdateSourceRequest) GetSource() *Source

### func (*UpdateSourceRequest) GetUpdateMask 
    
    
    func (x *UpdateSourceRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateSourceRequest) ProtoMessage 
    
    
    func (*UpdateSourceRequest) ProtoMessage()

### func (*UpdateSourceRequest) ProtoReflect 
    
    
    func (x *UpdateSourceRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateSourceRequest) Reset 
    
    
    func (x *UpdateSourceRequest) Reset()

### func (*UpdateSourceRequest) String 
    
    
    func (x *UpdateSourceRequest) String() [string](https://pkg.go.dev/builtin#string)

## UploadFileInfo
    
    
    type UploadFileInfo struct {
    
    	// Output only. Upload URI for the file.
    	SignedUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=signed_uri,json=signedUri,proto3" json:"signed_uri,omitempty"`
    	// Output only. The headers that were used to sign the URI.
    	Headers map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=headers,proto3" json:"headers,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Output only. Expiration time of the upload URI.
    	UriExpirationTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=uri_expiration_time,json=uriExpirationTime,proto3" json:"uri_expiration_time,omitempty"`
    	// contains filtered or unexported fields
    }

A resource that contains a URI to which a data file can be uploaded.

### func (*UploadFileInfo) Descriptor 
    
    
    func (*UploadFileInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UploadFileInfo.ProtoReflect.Descriptor instead.

### func (*UploadFileInfo) GetHeaders 
    
    
    func (x *UploadFileInfo) GetHeaders() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*UploadFileInfo) GetSignedUri 
    
    
    func (x *UploadFileInfo) GetSignedUri() [string](https://pkg.go.dev/builtin#string)

### func (*UploadFileInfo) GetUriExpirationTime 
    
    
    func (x *UploadFileInfo) GetUriExpirationTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*UploadFileInfo) ProtoMessage 
    
    
    func (*UploadFileInfo) ProtoMessage()

### func (*UploadFileInfo) ProtoReflect 
    
    
    func (x *UploadFileInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UploadFileInfo) Reset 
    
    
    func (x *UploadFileInfo) Reset()

### func (*UploadFileInfo) String 
    
    
    func (x *UploadFileInfo) String() [string](https://pkg.go.dev/builtin#string)

## ValidateImportJobRequest
    
    
    type ValidateImportJobRequest struct {
    
    	// Required. The name of the import job to validate.
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Optional. An optional request ID to identify requests. Specify a unique
    	// request ID so that if you must retry your request, the server will know to
    	// ignore the request if it has already been completed. The server will
    	// guarantee that for at least 60 minutes after the first request.
    	//
    	// For example, consider a situation where you make an initial request and
    	// the request times out. If you make the request again with the same request
    	// ID, the server can check if original operation with the same request ID
    	// was received, and if so, will ignore the second request. This prevents
    	// clients from accidentally creating duplicate commitments.
    	//
    	// The request ID must be a valid UUID with the exception that zero UUID is
    	// not supported (00000000-0000-0000-0000-000000000000).
    	RequestId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
    	// contains filtered or unexported fields
    }

A request to validate an import job.

### func (*ValidateImportJobRequest) Descriptor 
    
    
    func (*ValidateImportJobRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ValidateImportJobRequest.ProtoReflect.Descriptor instead.

### func (*ValidateImportJobRequest) GetName 
    
    
    func (x *ValidateImportJobRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*ValidateImportJobRequest) GetRequestId 
    
    
    func (x *ValidateImportJobRequest) GetRequestId() [string](https://pkg.go.dev/builtin#string)

### func (*ValidateImportJobRequest) ProtoMessage 
    
    
    func (*ValidateImportJobRequest) ProtoMessage()

### func (*ValidateImportJobRequest) ProtoReflect 
    
    
    func (x *ValidateImportJobRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ValidateImportJobRequest) Reset 
    
    
    func (x *ValidateImportJobRequest) Reset()

### func (*ValidateImportJobRequest) String 
    
    
    func (x *ValidateImportJobRequest) String() [string](https://pkg.go.dev/builtin#string)

## ValidationReport
    
    
    type ValidationReport struct {
    
    	// List of errors found in files.
    	FileValidations []*FileValidationReport `protobuf:"bytes,1,rep,name=file_validations,json=fileValidations,proto3" json:"file_validations,omitempty"`
    	// List of job level errors.
    	JobErrors []*ImportError `protobuf:"bytes,2,rep,name=job_errors,json=jobErrors,proto3" json:"job_errors,omitempty"`
    	// contains filtered or unexported fields
    }

A resource that aggregates errors across import job files.

### func (*ValidationReport) Descriptor 
    
    
    func (*ValidationReport) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ValidationReport.ProtoReflect.Descriptor instead.

### func (*ValidationReport) GetFileValidations 
    
    
    func (x *ValidationReport) GetFileValidations() []*FileValidationReport

### func (*ValidationReport) GetJobErrors 
    
    
    func (x *ValidationReport) GetJobErrors() []*ImportError

### func (*ValidationReport) ProtoMessage 
    
    
    func (*ValidationReport) ProtoMessage()

### func (*ValidationReport) ProtoReflect 
    
    
    func (x *ValidationReport) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ValidationReport) Reset 
    
    
    func (x *ValidationReport) Reset()

### func (*ValidationReport) String 
    
    
    func (x *ValidationReport) String() [string](https://pkg.go.dev/builtin#string)

## VirtualMachinePreferences
    
    
    type VirtualMachinePreferences struct {
    
    	// Target product for assets using this preference set.
    	// Specify either target product or business goal, but
    	// not both.
    	TargetProduct ComputeMigrationTargetProduct `protobuf:"varint,2,opt,name=target_product,json=targetProduct,proto3,enum=google.cloud.migrationcenter.v1.ComputeMigrationTargetProduct" json:"target_product,omitempty"`
    	// Region preferences for assets using this preference set.
    	// If you are unsure which value to set, the migration service API region is
    	// often a good value to start with.
    	RegionPreferences *RegionPreferences `protobuf:"bytes,3,opt,name=region_preferences,json=regionPreferences,proto3" json:"region_preferences,omitempty"`
    	// Commitment plan to consider when calculating costs for virtual machine
    	// insights and recommendations.
    	// If you are unsure which value to set, a 3 year commitment plan is often a
    	// good value to start with.
    	CommitmentPlan CommitmentPlan `protobuf:"varint,4,opt,name=commitment_plan,json=commitmentPlan,proto3,enum=google.cloud.migrationcenter.v1.CommitmentPlan" json:"commitment_plan,omitempty"`
    	// Sizing optimization strategy specifies the preferred strategy used when
    	// extrapolating usage data to calculate insights and recommendations for a
    	// virtual machine.
    	// If you are unsure which value to set, a moderate sizing optimization
    	// strategy is often a good value to start with.
    	SizingOptimizationStrategy SizingOptimizationStrategy `protobuf:"varint,5,opt,name=sizing_optimization_strategy,json=sizingOptimizationStrategy,proto3,enum=google.cloud.migrationcenter.v1.SizingOptimizationStrategy" json:"sizing_optimization_strategy,omitempty"`
    	// Compute Engine preferences concern insights and recommendations for Compute
    	// Engine target.
    	ComputeEnginePreferences *ComputeEnginePreferences `protobuf:"bytes,6,opt,name=compute_engine_preferences,json=computeEnginePreferences,proto3" json:"compute_engine_preferences,omitempty"`
    	// Preferences concerning insights and recommendations for
    	// Google Cloud VMware Engine.
    	VmwareEnginePreferences *VmwareEnginePreferences `protobuf:"bytes,7,opt,name=vmware_engine_preferences,json=vmwareEnginePreferences,proto3" json:"vmware_engine_preferences,omitempty"`
    	// Preferences concerning Sole Tenant nodes and virtual machines.
    	SoleTenancyPreferences *SoleTenancyPreferences `protobuf:"bytes,8,opt,name=sole_tenancy_preferences,json=soleTenancyPreferences,proto3" json:"sole_tenancy_preferences,omitempty"`
    	// contains filtered or unexported fields
    }

VirtualMachinePreferences enables you to create sets of assumptions, for example, a geographical location and pricing track, for your migrated virtual machines. The set of preferences influence recommendations for migrating virtual machine assets.

### func (*VirtualMachinePreferences) Descriptor 
    
    
    func (*VirtualMachinePreferences) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VirtualMachinePreferences.ProtoReflect.Descriptor instead.

### func (*VirtualMachinePreferences) GetCommitmentPlan 
    
    
    func (x *VirtualMachinePreferences) GetCommitmentPlan() CommitmentPlan

### func (*VirtualMachinePreferences) GetComputeEnginePreferences 
    
    
    func (x *VirtualMachinePreferences) GetComputeEnginePreferences() *ComputeEnginePreferences

### func (*VirtualMachinePreferences) GetRegionPreferences 
    
    
    func (x *VirtualMachinePreferences) GetRegionPreferences() *RegionPreferences

### func (*VirtualMachinePreferences) GetSizingOptimizationStrategy 
    
    
    func (x *VirtualMachinePreferences) GetSizingOptimizationStrategy() SizingOptimizationStrategy

### func (*VirtualMachinePreferences) GetSoleTenancyPreferences 
    
    
    func (x *VirtualMachinePreferences) GetSoleTenancyPreferences() *SoleTenancyPreferences

### func (*VirtualMachinePreferences) GetTargetProduct 
    
    
    func (x *VirtualMachinePreferences) GetTargetProduct() ComputeMigrationTargetProduct

### func (*VirtualMachinePreferences) GetVmwareEnginePreferences 
    
    
    func (x *VirtualMachinePreferences) GetVmwareEnginePreferences() *VmwareEnginePreferences

### func (*VirtualMachinePreferences) ProtoMessage 
    
    
    func (*VirtualMachinePreferences) ProtoMessage()

### func (*VirtualMachinePreferences) ProtoReflect 
    
    
    func (x *VirtualMachinePreferences) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VirtualMachinePreferences) Reset 
    
    
    func (x *VirtualMachinePreferences) Reset()

### func (*VirtualMachinePreferences) String 
    
    
    func (x *VirtualMachinePreferences) String() [string](https://pkg.go.dev/builtin#string)

## VmwareDiskConfig
    
    
    type VmwareDiskConfig struct {
    
    	// VMDK backing type.
    	BackingType VmwareDiskConfig_BackingType `protobuf:"varint,1,opt,name=backing_type,json=backingType,proto3,enum=google.cloud.migrationcenter.v1.VmwareDiskConfig_BackingType" json:"backing_type,omitempty"`
    	// Is VMDK shared with other VMs.
    	Shared [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=shared,proto3" json:"shared,omitempty"`
    	// VMDK disk mode.
    	VmdkMode VmwareDiskConfig_VmdkMode `protobuf:"varint,3,opt,name=vmdk_mode,json=vmdkMode,proto3,enum=google.cloud.migrationcenter.v1.VmwareDiskConfig_VmdkMode" json:"vmdk_mode,omitempty"`
    	// RDM compatibility mode.
    	RdmCompatibility VmwareDiskConfig_RdmCompatibility `protobuf:"varint,4,opt,name=rdm_compatibility,json=rdmCompatibility,proto3,enum=google.cloud.migrationcenter.v1.VmwareDiskConfig_RdmCompatibility" json:"rdm_compatibility,omitempty"`
    	// contains filtered or unexported fields
    }

VMware disk config details.

### func (*VmwareDiskConfig) Descriptor 
    
    
    func (*VmwareDiskConfig) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VmwareDiskConfig.ProtoReflect.Descriptor instead.

### func (*VmwareDiskConfig) GetBackingType 
    
    
    func (x *VmwareDiskConfig) GetBackingType() VmwareDiskConfig_BackingType

### func (*VmwareDiskConfig) GetRdmCompatibility 
    
    
    func (x *VmwareDiskConfig) GetRdmCompatibility() VmwareDiskConfig_RdmCompatibility

### func (*VmwareDiskConfig) GetShared 
    
    
    func (x *VmwareDiskConfig) GetShared() [bool](https://pkg.go.dev/builtin#bool)

### func (*VmwareDiskConfig) GetVmdkMode 
    
    
    func (x *VmwareDiskConfig) GetVmdkMode() VmwareDiskConfig_VmdkMode

### func (*VmwareDiskConfig) ProtoMessage 
    
    
    func (*VmwareDiskConfig) ProtoMessage()

### func (*VmwareDiskConfig) ProtoReflect 
    
    
    func (x *VmwareDiskConfig) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VmwareDiskConfig) Reset 
    
    
    func (x *VmwareDiskConfig) Reset()

### func (*VmwareDiskConfig) String 
    
    
    func (x *VmwareDiskConfig) String() [string](https://pkg.go.dev/builtin#string)

## VmwareDiskConfig_BackingType
    
    
    type VmwareDiskConfig_BackingType [int32](https://pkg.go.dev/builtin#int32)

VMDK backing type possible values.

### VmwareDiskConfig_BACKING_TYPE_UNSPECIFIED, VmwareDiskConfig_BACKING_TYPE_FLAT_V1, VmwareDiskConfig_BACKING_TYPE_FLAT_V2, VmwareDiskConfig_BACKING_TYPE_PMEM, VmwareDiskConfig_BACKING_TYPE_RDM_V1, VmwareDiskConfig_BACKING_TYPE_RDM_V2, VmwareDiskConfig_BACKING_TYPE_SESPARSE, VmwareDiskConfig_BACKING_TYPE_SESPARSE_V1, VmwareDiskConfig_BACKING_TYPE_SESPARSE_V2
    
    
    const (
    	// Default value.
    	VmwareDiskConfig_BACKING_TYPE_UNSPECIFIED VmwareDiskConfig_BackingType = 0
    	// Flat v1.
    	VmwareDiskConfig_BACKING_TYPE_FLAT_V1 VmwareDiskConfig_BackingType = 1
    	// Flat v2.
    	VmwareDiskConfig_BACKING_TYPE_FLAT_V2 VmwareDiskConfig_BackingType = 2
    	// Persistent memory, also known as Non-Volatile Memory (NVM).
    	VmwareDiskConfig_BACKING_TYPE_PMEM VmwareDiskConfig_BackingType = 3
    	// Raw Disk Memory v1.
    	VmwareDiskConfig_BACKING_TYPE_RDM_V1 VmwareDiskConfig_BackingType = 4
    	// Raw Disk Memory v2.
    	VmwareDiskConfig_BACKING_TYPE_RDM_V2 VmwareDiskConfig_BackingType = 5
    	// SEsparse is a snapshot format introduced in vSphere 5.5 for large disks.
    	VmwareDiskConfig_BACKING_TYPE_SESPARSE VmwareDiskConfig_BackingType = 6
    	// SEsparse v1.
    	VmwareDiskConfig_BACKING_TYPE_SESPARSE_V1 VmwareDiskConfig_BackingType = 7
    	// SEsparse v1.
    	VmwareDiskConfig_BACKING_TYPE_SESPARSE_V2 VmwareDiskConfig_BackingType = 8
    )

### func (VmwareDiskConfig_BackingType) Descriptor 
    
    
    func (VmwareDiskConfig_BackingType) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (VmwareDiskConfig_BackingType) Enum 
    
    
    func (x VmwareDiskConfig_BackingType) Enum() *VmwareDiskConfig_BackingType

### func (VmwareDiskConfig_BackingType) EnumDescriptor 
    
    
    func (VmwareDiskConfig_BackingType) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VmwareDiskConfig_BackingType.Descriptor instead.

### func (VmwareDiskConfig_BackingType) Number 
    
    
    func (x VmwareDiskConfig_BackingType) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (VmwareDiskConfig_BackingType) String 
    
    
    func (x VmwareDiskConfig_BackingType) String() [string](https://pkg.go.dev/builtin#string)

### func (VmwareDiskConfig_BackingType) Type 
    
    
    func (VmwareDiskConfig_BackingType) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## VmwareDiskConfig_RdmCompatibility
    
    
    type VmwareDiskConfig_RdmCompatibility [int32](https://pkg.go.dev/builtin#int32)

RDM compatibility mode.

### VmwareDiskConfig_RDM_COMPATIBILITY_UNSPECIFIED, VmwareDiskConfig_PHYSICAL_COMPATIBILITY, VmwareDiskConfig_VIRTUAL_COMPATIBILITY
    
    
    const (
    	// Compatibility mode unspecified or unknown.
    	VmwareDiskConfig_RDM_COMPATIBILITY_UNSPECIFIED VmwareDiskConfig_RdmCompatibility = 0
    	// Physical compatibility mode.
    	VmwareDiskConfig_PHYSICAL_COMPATIBILITY VmwareDiskConfig_RdmCompatibility = 1
    	// Virtual compatibility mode.
    	VmwareDiskConfig_VIRTUAL_COMPATIBILITY VmwareDiskConfig_RdmCompatibility = 2
    )

### func (VmwareDiskConfig_RdmCompatibility) Descriptor 
    
    
    func (VmwareDiskConfig_RdmCompatibility) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (VmwareDiskConfig_RdmCompatibility) Enum 
    
    
    func (x VmwareDiskConfig_RdmCompatibility) Enum() *VmwareDiskConfig_RdmCompatibility

### func (VmwareDiskConfig_RdmCompatibility) EnumDescriptor 
    
    
    func (VmwareDiskConfig_RdmCompatibility) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VmwareDiskConfig_RdmCompatibility.Descriptor instead.

### func (VmwareDiskConfig_RdmCompatibility) Number 
    
    
    func (x VmwareDiskConfig_RdmCompatibility) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (VmwareDiskConfig_RdmCompatibility) String 
    
    
    func (x VmwareDiskConfig_RdmCompatibility) String() [string](https://pkg.go.dev/builtin#string)

### func (VmwareDiskConfig_RdmCompatibility) Type 
    
    
    func (VmwareDiskConfig_RdmCompatibility) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## VmwareDiskConfig_VmdkMode
    
    
    type VmwareDiskConfig_VmdkMode [int32](https://pkg.go.dev/builtin#int32)

VMDK disk mode.

### VmwareDiskConfig_VMDK_MODE_UNSPECIFIED, VmwareDiskConfig_DEPENDENT, VmwareDiskConfig_INDEPENDENT_PERSISTENT, VmwareDiskConfig_INDEPENDENT_NONPERSISTENT
    
    
    const (
    	// VMDK disk mode unspecified or unknown.
    	VmwareDiskConfig_VMDK_MODE_UNSPECIFIED VmwareDiskConfig_VmdkMode = 0
    	// Dependent disk mode.
    	VmwareDiskConfig_DEPENDENT VmwareDiskConfig_VmdkMode = 1
    	// Independent - Persistent disk mode.
    	VmwareDiskConfig_INDEPENDENT_PERSISTENT VmwareDiskConfig_VmdkMode = 2
    	// Independent - Nonpersistent disk mode.
    	VmwareDiskConfig_INDEPENDENT_NONPERSISTENT VmwareDiskConfig_VmdkMode = 3
    )

### func (VmwareDiskConfig_VmdkMode) Descriptor 
    
    
    func (VmwareDiskConfig_VmdkMode) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (VmwareDiskConfig_VmdkMode) Enum 
    
    
    func (x VmwareDiskConfig_VmdkMode) Enum() *VmwareDiskConfig_VmdkMode

### func (VmwareDiskConfig_VmdkMode) EnumDescriptor 
    
    
    func (VmwareDiskConfig_VmdkMode) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VmwareDiskConfig_VmdkMode.Descriptor instead.

### func (VmwareDiskConfig_VmdkMode) Number 
    
    
    func (x VmwareDiskConfig_VmdkMode) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (VmwareDiskConfig_VmdkMode) String 
    
    
    func (x VmwareDiskConfig_VmdkMode) String() [string](https://pkg.go.dev/builtin#string)

### func (VmwareDiskConfig_VmdkMode) Type 
    
    
    func (VmwareDiskConfig_VmdkMode) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## VmwareEnginePreferences
    
    
    type VmwareEnginePreferences struct {
    
    	// CPU overcommit ratio.
    	// Acceptable values are between 1.0 and 8.0, with 0.1 increment.
    	CpuOvercommitRatio [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,1,opt,name=cpu_overcommit_ratio,json=cpuOvercommitRatio,proto3" json:"cpu_overcommit_ratio,omitempty"`
    	// Memory overcommit ratio.
    	// Acceptable values are 1.0, 1.25, 1.5, 1.75 and 2.0.
    	MemoryOvercommitRatio [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,2,opt,name=memory_overcommit_ratio,json=memoryOvercommitRatio,proto3" json:"memory_overcommit_ratio,omitempty"`
    	// The Deduplication and Compression ratio is based on the logical (Used
    	// Before) space required to store data before applying deduplication and
    	// compression, in relation to the physical (Used After) space required after
    	// applying deduplication and compression. Specifically, the ratio is the Used
    	// Before space divided by the Used After space. For example, if the Used
    	// Before space is 3 GB, but the physical Used After space is 1 GB, the
    	// deduplication and compression ratio is 3x. Acceptable values are
    	// between 1.0 and 4.0.
    	StorageDeduplicationCompressionRatio [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,3,opt,name=storage_deduplication_compression_ratio,json=storageDeduplicationCompressionRatio,proto3" json:"storage_deduplication_compression_ratio,omitempty"`
    	// Commitment plan to consider when calculating costs for virtual machine
    	// insights and recommendations.
    	// If you are unsure which value to set, a 3 year commitment plan is often a
    	// good value to start with.
    	CommitmentPlan VmwareEnginePreferences_CommitmentPlan `protobuf:"varint,4,opt,name=commitment_plan,json=commitmentPlan,proto3,enum=google.cloud.migrationcenter.v1.VmwareEnginePreferences_CommitmentPlan" json:"commitment_plan,omitempty"`
    	// contains filtered or unexported fields
    }

The user preferences relating to Google Cloud VMware Engine target platform.

### func (*VmwareEnginePreferences) Descriptor 
    
    
    func (*VmwareEnginePreferences) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VmwareEnginePreferences.ProtoReflect.Descriptor instead.

### func (*VmwareEnginePreferences) GetCommitmentPlan 
    
    
    func (x *VmwareEnginePreferences) GetCommitmentPlan() VmwareEnginePreferences_CommitmentPlan

### func (*VmwareEnginePreferences) GetCpuOvercommitRatio 
    
    
    func (x *VmwareEnginePreferences) GetCpuOvercommitRatio() [float64](https://pkg.go.dev/builtin#float64)

### func (*VmwareEnginePreferences) GetMemoryOvercommitRatio 
    
    
    func (x *VmwareEnginePreferences) GetMemoryOvercommitRatio() [float64](https://pkg.go.dev/builtin#float64)

### func (*VmwareEnginePreferences) GetStorageDeduplicationCompressionRatio 
    
    
    func (x *VmwareEnginePreferences) GetStorageDeduplicationCompressionRatio() [float64](https://pkg.go.dev/builtin#float64)

### func (*VmwareEnginePreferences) ProtoMessage 
    
    
    func (*VmwareEnginePreferences) ProtoMessage()

### func (*VmwareEnginePreferences) ProtoReflect 
    
    
    func (x *VmwareEnginePreferences) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VmwareEnginePreferences) Reset 
    
    
    func (x *VmwareEnginePreferences) Reset()

### func (*VmwareEnginePreferences) String 
    
    
    func (x *VmwareEnginePreferences) String() [string](https://pkg.go.dev/builtin#string)

## VmwareEnginePreferences_CommitmentPlan
    
    
    type VmwareEnginePreferences_CommitmentPlan [int32](https://pkg.go.dev/builtin#int32)

Type of committed use discount.

### VmwareEnginePreferences_COMMITMENT_PLAN_UNSPECIFIED, VmwareEnginePreferences_ON_DEMAND, VmwareEnginePreferences_COMMITMENT_1_YEAR_MONTHLY_PAYMENTS, VmwareEnginePreferences_COMMITMENT_3_YEAR_MONTHLY_PAYMENTS, VmwareEnginePreferences_COMMITMENT_1_YEAR_UPFRONT_PAYMENT, VmwareEnginePreferences_COMMITMENT_3_YEAR_UPFRONT_PAYMENT
    
    
    const (
    	// Unspecified commitment plan.
    	VmwareEnginePreferences_COMMITMENT_PLAN_UNSPECIFIED VmwareEnginePreferences_CommitmentPlan = 0
    	// No commitment plan (on-demand usage).
    	VmwareEnginePreferences_ON_DEMAND VmwareEnginePreferences_CommitmentPlan = 1
    	// 1 year commitment (monthly payments).
    	VmwareEnginePreferences_COMMITMENT_1_YEAR_MONTHLY_PAYMENTS VmwareEnginePreferences_CommitmentPlan = 2
    	// 3 year commitment (monthly payments).
    	VmwareEnginePreferences_COMMITMENT_3_YEAR_MONTHLY_PAYMENTS VmwareEnginePreferences_CommitmentPlan = 3
    	// 1 year commitment (upfront payment).
    	VmwareEnginePreferences_COMMITMENT_1_YEAR_UPFRONT_PAYMENT VmwareEnginePreferences_CommitmentPlan = 4
    	// 3 years commitment (upfront payment).
    	VmwareEnginePreferences_COMMITMENT_3_YEAR_UPFRONT_PAYMENT VmwareEnginePreferences_CommitmentPlan = 5
    )

### func (VmwareEnginePreferences_CommitmentPlan) Descriptor 
    
    
    func (VmwareEnginePreferences_CommitmentPlan) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (VmwareEnginePreferences_CommitmentPlan) Enum 
    
    
    func (x VmwareEnginePreferences_CommitmentPlan) Enum() *VmwareEnginePreferences_CommitmentPlan

### func (VmwareEnginePreferences_CommitmentPlan) EnumDescriptor 
    
    
    func (VmwareEnginePreferences_CommitmentPlan) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VmwareEnginePreferences_CommitmentPlan.Descriptor instead.

### func (VmwareEnginePreferences_CommitmentPlan) Number 
    
    
    func (x VmwareEnginePreferences_CommitmentPlan) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (VmwareEnginePreferences_CommitmentPlan) String 
    
    
    func (x VmwareEnginePreferences_CommitmentPlan) String() [string](https://pkg.go.dev/builtin#string)

### func (VmwareEnginePreferences_CommitmentPlan) Type 
    
    
    func (VmwareEnginePreferences_CommitmentPlan) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## VmwarePlatformDetails
    
    
    type VmwarePlatformDetails struct {
    
    	// vCenter version.
    	VcenterVersion [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=vcenter_version,json=vcenterVersion,proto3" json:"vcenter_version,omitempty"`
    	// ESX version.
    	EsxVersion [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=esx_version,json=esxVersion,proto3" json:"esx_version,omitempty"`
    	// VMware os enum -
    	// https://vdc-repo.vmware.com/vmwb-repository/dcr-public/da47f910-60ac-438b-8b9b-6122f4d14524/16b7274a-bf8b-4b4c-a05e-746f2aa93c8c/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html.
    	Osid [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=osid,proto3" json:"osid,omitempty"`
    	// Folder name in vCenter where asset resides.
    	VcenterFolder [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=vcenter_folder,json=vcenterFolder,proto3" json:"vcenter_folder,omitempty"`
    	// vCenter URI used in collection.
    	VcenterUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=vcenter_uri,json=vcenterUri,proto3" json:"vcenter_uri,omitempty"`
    	// vCenter VM ID.
    	VcenterVmId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=vcenter_vm_id,json=vcenterVmId,proto3" json:"vcenter_vm_id,omitempty"`
    	// contains filtered or unexported fields
    }

VMware specific details.

### func (*VmwarePlatformDetails) Descriptor 
    
    
    func (*VmwarePlatformDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use VmwarePlatformDetails.ProtoReflect.Descriptor instead.

### func (*VmwarePlatformDetails) GetEsxVersion 
    
    
    func (x *VmwarePlatformDetails) GetEsxVersion() [string](https://pkg.go.dev/builtin#string)

### func (*VmwarePlatformDetails) GetOsid 
    
    
    func (x *VmwarePlatformDetails) GetOsid() [string](https://pkg.go.dev/builtin#string)

### func (*VmwarePlatformDetails) GetVcenterFolder 
    
    
    func (x *VmwarePlatformDetails) GetVcenterFolder() [string](https://pkg.go.dev/builtin#string)

### func (*VmwarePlatformDetails) GetVcenterUri 
    
    
    func (x *VmwarePlatformDetails) GetVcenterUri() [string](https://pkg.go.dev/builtin#string)

### func (*VmwarePlatformDetails) GetVcenterVersion 
    
    
    func (x *VmwarePlatformDetails) GetVcenterVersion() [string](https://pkg.go.dev/builtin#string)

### func (*VmwarePlatformDetails) GetVcenterVmId 
    
    
    func (x *VmwarePlatformDetails) GetVcenterVmId() [string](https://pkg.go.dev/builtin#string)

### func (*VmwarePlatformDetails) ProtoMessage 
    
    
    func (*VmwarePlatformDetails) ProtoMessage()

### func (*VmwarePlatformDetails) ProtoReflect 
    
    
    func (x *VmwarePlatformDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*VmwarePlatformDetails) Reset 
    
    
    func (x *VmwarePlatformDetails) Reset()

### func (*VmwarePlatformDetails) String 
    
    
    func (x *VmwarePlatformDetails) String() [string](https://pkg.go.dev/builtin#string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
