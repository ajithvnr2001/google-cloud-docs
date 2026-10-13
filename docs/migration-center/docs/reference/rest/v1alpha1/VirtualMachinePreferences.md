---
url: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences/
title: VirtualMachinePreferences \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:46.534046+00:00
---

# VirtualMachinePreferences  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Reference ](https://docs.cloud.google.com/migration-center/docs/api)



Send feedback 

#  VirtualMachinePreferences Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ComputeMigrationTargetProduct
  * NetworkCostParameters
    * JSON representation
  * SizingOptimizationCustomParameters
    * JSON representation
  * AggregationMethod
  * ComputeEnginePreferences
    * JSON representation
  * MachinePreferences
    * JSON representation
  * LicenseType
  * OperatingSystemPricingPreferences
    * JSON representation
  * OperatingSystemPricing
    * JSON representation
  * CommitmentPlan
  * Multithreading
  * VmwareEnginePreferences
    * JSON representation
  * CommitmentPlan
  * VMwareEngineMachinePreferences
    * JSON representation
  * StorageOnlyNodes
  * ProtectedNodes
  * ServiceType
  * SoleTenancyPreferences
    * JSON representation
  * HostMaintenancePolicy
  * CommitmentPlan



VirtualMachinePreferences enables you to create sets of preferences, for example, a geographical location and pricing track, for your migrated virtual machines. The set of preferences influence recommendations for migrating virtual machine assets.

JSON representation  
---  
      
    
    {
      "targetProduct": enum ([ComputeMigrationTargetProduct](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#ComputeMigrationTargetProduct)),
      "regionPreferences": {
        object ([RegionPreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/RegionPreferences))
      },
      "commitmentPlan": enum ([CommitmentPlan](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/CommitmentPlan)),
      "networkCostParameters": {
        object ([NetworkCostParameters](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#NetworkCostParameters))
      },
      "sizingOptimizationStrategy": enum ([SizingOptimizationStrategy](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/SizingOptimizationStrategy)),
      "sizingOptimizationCustomParameters": {
        object ([SizingOptimizationCustomParameters](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#SizingOptimizationCustomParameters))
      },
      "computeEnginePreferences": {
        object ([ComputeEnginePreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#ComputeEnginePreferences))
      },
      "vmwareEnginePreferences": {
        object ([VmwareEnginePreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#VmwareEnginePreferences))
      },
      "soleTenancyPreferences": {
        object ([SoleTenancyPreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#SoleTenancyPreferences))
      }
    }  
  
Fields  
---  
`targetProduct` |  `enum (`[ComputeMigrationTargetProduct](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#ComputeMigrationTargetProduct)`)` Target product for assets using this preference set. Specify either target product or business goal, but not both.  
`regionPreferences` |  `object (`[RegionPreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/RegionPreferences)`)` Region preferences for assets using this preference set. If you are unsure which value to set, the migration service API region is often a good value to start with. If PreferenceSet.RegionPreferences is specified, it overrides this field.  
`commitmentPlan` |  `enum (`[CommitmentPlan](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/CommitmentPlan)`)` Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with.  
`networkCostParameters` |  `object (`[NetworkCostParameters](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#NetworkCostParameters)`)` Optional. Parameters that affect network cost estimations. If not set, default values will be used for the parameters.  
`sizingOptimizationStrategy` |  `enum (`[SizingOptimizationStrategy](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/SizingOptimizationStrategy)`)` Sizing optimization strategy specifies the preferred strategy used when extrapolating usage data to calculate insights and recommendations for a virtual machine. If you are unsure which value to set, a moderate sizing optimization strategy is often a good value to start with.  
`sizingOptimizationCustomParameters` |  `object (`[SizingOptimizationCustomParameters](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#SizingOptimizationCustomParameters)`)` Optional. Custom data to use for sizing optimizations. Relevant when SizingOptimizationStrategy is set to "custom".  
`computeEnginePreferences` |  `object (`[ComputeEnginePreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#ComputeEnginePreferences)`)` Optional. Compute Engine preferences concern insights and recommendations for Compute Engine target.  
`vmwareEnginePreferences` |  `object (`[VmwareEnginePreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#VmwareEnginePreferences)`)` Preferences concerning insights and recommendations for Google Cloud VMware Engine.  
`soleTenancyPreferences` |  `object (`[SoleTenancyPreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#SoleTenancyPreferences)`)` Preferences concerning Sole Tenant nodes and virtual machines.  
  
## ComputeMigrationTargetProduct

The preference for a specific Google Cloud product platform.

Enums  
---  
`COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED` | Unspecified (default value).  
`COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE` | Prefer to migrate to Google Cloud Compute Engine.  
`COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE` | Prefer to migrate to Google Cloud VMware Engine.  
`COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY` | Prefer to migrate to Google Cloud Sole Tenant Nodes.  
  
## NetworkCostParameters

Parameters that affect network cost estimations.

JSON representation  
---  
      
    
    {
      "estimatedEgressTrafficPercentage": integer
    }  
  
Fields  
---  
`estimatedEgressTrafficPercentage` |  `integer` Optional. An estimated percentage of priced outbound traffic (egress traffic) from the measured outbound traffic. Must be in the interval [0, 100].  
  
## SizingOptimizationCustomParameters

Custom data to use for sizing optimizations.

JSON representation  
---  
      
    
    {
      "aggregationMethod": enum ([AggregationMethod](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#AggregationMethod)),
      "storageMultiplier": number,
      "cpuUsagePercentage": integer,
      "memoryUsagePercentage": integer
    }  
  
Fields  
---  
`aggregationMethod` |  `enum (`[AggregationMethod](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#AggregationMethod)`)` Optional. Type of statistical aggregation of a resource utilization data, on which to base the sizing metrics.  
`storageMultiplier` |  `number` Optional. Desired increase factor of storage, relative to currently used storage. Must be in the interval [1.0, 2.0] (or 0 for default value).  
`cpuUsagePercentage` |  `integer` Optional. Desired percentage of CPU usage. Must be in the interval [1, 100] (or 0 for default value).  
`memoryUsagePercentage` |  `integer` Optional. Desired percentage of memory usage. Must be in the interval [1, 100] (or 0 for default value).  
  
## AggregationMethod

Type of statistical aggregation of a resource utilization data, on which to base the sizing metrics.

Enums  
---  
`AGGREGATION_METHOD_UNSPECIFIED` | Unspecified aggregation method. Can be used for default value.  
`AGGREGATION_METHOD_AVERAGE` | Average of utilization data.  
`AGGREGATION_METHOD_MEDIAN` | Median of utilization data.  
`AGGREGATION_METHOD_NINETY_FIFTH_PERCENTILE` | 95th percentile of utilization data.  
`AGGREGATION_METHOD_PEAK` | Peak of utilization data.  
  
## ComputeEnginePreferences

The user preferences relating to Compute Engine target platform.

JSON representation  
---  
      
    
    {
      "persistentDiskType": enum ([PersistentDiskType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/PersistentDiskType)),
      "machinePreferences": {
        object ([MachinePreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#MachinePreferences))
      },
      "licenseType": enum ([LicenseType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#LicenseType)),
      "osPricingPreferences": {
        object ([OperatingSystemPricingPreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricingPreferences))
      },
      "multithreading": enum ([Multithreading](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#Multithreading))
    }  
  
Fields  
---  
`persistentDiskType` |  `enum (`[PersistentDiskType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/PersistentDiskType)`)` Persistent disk type to use. If unspecified (default), all types are considered, based on available usage data.  
`machinePreferences` |  `object (`[MachinePreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#MachinePreferences)`)` Preferences concerning the machine types to consider on Compute Engine.  
`licenseType` |  `enum (`[LicenseType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#LicenseType)`)` License type to consider when calculating costs for operating systems. If unspecified, costs are calculated based on the default licensing plan. If osPricingPreferences is specified, it overrides this field.  
`osPricingPreferences` |  `object (`[OperatingSystemPricingPreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricingPreferences)`)` Optional. Pricing options for OS images.  
`multithreading` |  `enum (`[Multithreading](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#Multithreading)`)` Optional. Preferences for multithreading support on Windows Server.  
  
## MachinePreferences

The type of machines to consider when calculating virtual machine migration insights and recommendations for Compute Engine. Not all machine types are available in all zones and regions.

JSON representation  
---  
      
    
    {
      "allowedMachineSeries": [
        {
          object ([MachineSeries](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/MachineSeries))
        }
      ]
    }  
  
Fields  
---  
`allowedMachineSeries[]` |  `object (`[MachineSeries](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/MachineSeries)`)` Compute Engine machine series to consider for insights and recommendations. If empty, no restriction is applied on the machine series.  
  
## LicenseType

License type specifies whether to use Google provided licenses or your own.

Enums  
---  
`LICENSE_TYPE_UNSPECIFIED` | Unspecified (default value).  
`LICENSE_TYPE_DEFAULT` | Default Google Cloud licensing plan. Licensing is charged per usage. This a good value to start with.  
`LICENSE_TYPE_BRING_YOUR_OWN_LICENSE` | Bring-your-own-license (BYOL) plan. User provides the license.  
  
## OperatingSystemPricingPreferences

Pricing options for OS images.

JSON representation  
---  
      
    
    {
      "windows": {
        object ([OperatingSystemPricing](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricing))
      },
      "rhel": {
        object ([OperatingSystemPricing](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricing))
      },
      "sles": {
        object ([OperatingSystemPricing](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricing))
      },
      "slesForSap": {
        object ([OperatingSystemPricing](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricing))
      }
    }  
  
Fields  
---  
`windows` |  `object (`[OperatingSystemPricing](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricing)`)` Optional. Pricing options for Windows images. No commitment plans are available, set it to unspecified.  
`rhel` |  `object (`[OperatingSystemPricing](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricing)`)` Optional. Pricing options for RHEL images.  
`sles` |  `object (`[OperatingSystemPricing](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricing)`)` Optional. Pricing options for SLES images.  
`slesForSap` |  `object (`[OperatingSystemPricing](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricing)`)` Optional. Pricing options for SLES for SAP images.  
  
## OperatingSystemPricing

Pricing options of an OS image.

JSON representation  
---  
      
    
    {
      "licenseType": enum ([LicenseType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#LicenseType)),
      "commitmentPlan": enum ([CommitmentPlan](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#CommitmentPlan))
    }  
  
Fields  
---  
`licenseType` |  `enum (`[LicenseType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#LicenseType)`)` Optional. License type for premium images (RHEL, RHEL for SAP, SLES, SLES for SAP, Windows Server).  
`commitmentPlan` |  `enum (`[CommitmentPlan](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#CommitmentPlan)`)` Optional. The plan of commitments for committed use discounts (CUD).  
  
## CommitmentPlan

The plan of commitments for committed use discounts (CUD).

Enums  
---  
`COMMITMENT_PLAN_UNSPECIFIED` | Unspecified commitment plan.  
`COMMITMENT_PLAN_ON_DEMAND` | No commitment plan (on-demand usage).  
`COMMITMENT_PLAN_1_YEAR` | 1-year committed use discount.  
`COMMITMENT_PLAN_3_YEAR` | 3-year committed use discount.  
  
## Multithreading

Preferences for multithreading support. See <https://cloud.google.com/compute/docs/instances/set-threads-per-core> for more details.

Enums  
---  
`MULTITHREADING_UNSPECIFIED` | Same as MULTITHREADING_AUTO.  
`MULTITHREADING_DISABLED` | Disable simultaneous multithreading.  
`MULTITHREADING_ENABLED` | Enable simultaneous multithreading.  
`MULTITHREADING_DISABLED_WITH_COMPENSATION` | Disable simultaneous multithreading and increase number of VCPUs to compensate.  
  
## VmwareEnginePreferences

The user preferences relating to Google Cloud VMware Engine target platform.

JSON representation  
---  
      
    
    {
      "cpuOvercommitRatio": number,
      "memoryOvercommitRatio": number,
      "storageDeduplicationCompressionRatio": number,
      "commitmentPlan": enum ([CommitmentPlan](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#CommitmentPlan_1)),
      "machinePreferences": {
        object ([VMwareEngineMachinePreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#VMwareEngineMachinePreferences))
      },
      "serviceType": enum ([ServiceType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#ServiceType)),
      "licenseDiscountPercentage": number
    }  
  
Fields  
---  
`cpuOvercommitRatio` |  `number` CPU overcommit ratio. Acceptable values are between 1.0 and 8.0, with 0.1 increment.  
`memoryOvercommitRatio` |  `number` Memory overcommit ratio. Acceptable values are 1.0, 1.25, 1.5, 1.75 and 2.0.  
`storageDeduplicationCompressionRatio` |  `number` The Deduplication and Compression ratio is based on the logical (Used Before) space required to store data before applying deduplication and compression, in relation to the physical (Used After) space required after applying deduplication and compression. Specifically, the ratio is the Used Before space divided by the Used After space. For example, if the Used Before space is 3 GB, but the physical Used After space is 1 GB, the deduplication and compression ratio is 3x. Acceptable values are between 1.0 and 4.0.  
`commitmentPlan` |  `enum (`[CommitmentPlan](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#CommitmentPlan_1)`)` Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with.  
`machinePreferences` |  `object (`[VMwareEngineMachinePreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#VMwareEngineMachinePreferences)`)` Optional. Preferences concerning the machine types to consider on Google Cloud VMware Engine.  
`serviceType` |  `enum (`[ServiceType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#ServiceType)`)` Optional. GCVE service type (fully licensed or portable license).  
`licenseDiscountPercentage` |  `number` Optional. Discount percentage for the license offered to you by Broadcom. Must be between 0 and 100. Only valid when serviceType is set to SERVICE_TYPE_PORTABLE_LICENSE.  
  
## CommitmentPlan

Type of committed use discount.

Enums  
---  
`COMMITMENT_PLAN_UNSPECIFIED` | Unspecified commitment plan.  
`ON_DEMAND` | No commitment plan (on-demand usage).  
`COMMITMENT_1_YEAR_MONTHLY_PAYMENTS` | 1 year commitment (monthly payments).  
`COMMITMENT_3_YEAR_MONTHLY_PAYMENTS` | 3 year commitment (monthly payments).  
`COMMITMENT_1_YEAR_UPFRONT_PAYMENT` | 1 year commitment (upfront payment).  
`COMMITMENT_3_YEAR_UPFRONT_PAYMENT` | 3 years commitment (upfront payment).  
`COMMITMENT_FLEXIBLE_3_YEAR_MONTHLY_PAYMENTS` | 3-year flexible commitment (monthly payments). While not supported in the v1 API, this value is converted to UNSPECIFIED in conversions to the v1 API.  
`COMMITMENT_FLEXIBLE_3_YEAR_UPFRONT_PAYMENT` | 3-year flexible commitment (upfront payment). While not supported in the v1 API, this value is converted to UNSPECIFIED in conversions to the v1 API.  
  
## VMwareEngineMachinePreferences

The type of machines to consider when calculating virtual machine migration insights and recommendations for VMware Engine. Not all machine types are available in all zones and regions.

JSON representation  
---  
      
    
    {
      "allowedMachineSeries": [
        {
          object ([MachineSeries](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/MachineSeries))
        }
      ],
      "storageOnlyNodes": enum ([StorageOnlyNodes](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#StorageOnlyNodes)),
      "protectedNodes": enum ([ProtectedNodes](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#ProtectedNodes))
    }  
  
Fields  
---  
`allowedMachineSeries[]` |  `object (`[MachineSeries](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/MachineSeries)`)` Optional. VMware Engine on Google Cloud machine series to consider for insights and recommendations. If empty, no restriction is applied on the machine series.  
`storageOnlyNodes` |  `enum (`[StorageOnlyNodes](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#StorageOnlyNodes)`)` Optional. Whether to use storage-only nodes, if those are available.  
`protectedNodes` |  `enum (`[ProtectedNodes](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#ProtectedNodes)`)` Optional. Whether to use VMware Engine Protected offering.  
  
## StorageOnlyNodes

Preferences regarding storage-only nodes.

Enums  
---  
`STORAGE_ONLY_NODES_UNSPECIFIED` | Unspecified storage-only nodes preference.  
`STORAGE_ONLY_NODES_ENABLED` | Use storage-only nodes for selected allowedMachineSeries, if available.  
`STORAGE_ONLY_NODES_DISABLED` | Do not use storage-only nodes.  
  
## ProtectedNodes

Preferences regarding protected nodes.

Enums  
---  
`PROTECTED_NODES_UNSPECIFIED` | Unspecified protected nodes preference.  
`PROTECTED_NODES_ENABLED` | Use only protected nodes for the selected allowedMachineSeries.  
`PROTECTED_NODES_DISABLED` | Do not use protected nodes.  
  
## ServiceType

The GCVE service (license) type.

Enums  
---  
`SERVICE_TYPE_UNSPECIFIED` | Same as SERVICE_TYPE_FULLY_LICENSED.  
`SERVICE_TYPE_FULLY_LICENSED` | Google provided VCF license.  
`SERVICE_TYPE_PORTABLE_LICENSE` | Bring Your Own License.  
  
## SoleTenancyPreferences

Preferences concerning Sole Tenancy nodes and VMs.

JSON representation  
---  
      
    
    {
      "cpuOvercommitRatio": number,
      "hostMaintenancePolicy": enum ([HostMaintenancePolicy](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#HostMaintenancePolicy)),
      "commitmentPlan": enum ([CommitmentPlan](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#CommitmentPlan_2)),
      "osPricingPreferences": {
        object ([OperatingSystemPricingPreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricingPreferences))
      },
      "nodeTypes": [
        {
          object ([SoleTenantNodeType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/SoleTenantNodeType))
        }
      ]
    }  
  
Fields  
---  
`cpuOvercommitRatio` |  `number` CPU overcommit ratio. Acceptable values are between 1.0 and 2.0 inclusive.  
`hostMaintenancePolicy` |  `enum (`[HostMaintenancePolicy](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#HostMaintenancePolicy)`)` Sole Tenancy nodes maintenance policy.  
`commitmentPlan` |  `enum (`[CommitmentPlan](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#CommitmentPlan_2)`)` Commitment plan to consider when calculating costs for virtual machine insights and recommendations. If you are unsure which value to set, a 3 year commitment plan is often a good value to start with.  
`osPricingPreferences` |  `object (`[OperatingSystemPricingPreferences](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/VirtualMachinePreferences#OperatingSystemPricingPreferences)`)` Optional. Pricing options for OS images.  
`nodeTypes[]` |  `object (`[SoleTenantNodeType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/SoleTenantNodeType)`)` A list of sole tenant node types. An empty list means that all possible node types will be considered.  
  
## HostMaintenancePolicy

Sole Tenancy nodes maintenance policy.

Enums  
---  
`HOST_MAINTENANCE_POLICY_UNSPECIFIED` | Unspecified host maintenance policy.  
`HOST_MAINTENANCE_POLICY_DEFAULT` | Default host maintenance policy.  
`HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE` | Restart in place host maintenance policy.  
`HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP` | Migrate within node group host maintenance policy.  
  
## CommitmentPlan

Type of committed use discount.

Enums  
---  
`COMMITMENT_PLAN_UNSPECIFIED` | Unspecified commitment plan.  
`ON_DEMAND` | No commitment plan (on-demand usage).  
`COMMITMENT_1_YEAR` | 1-year regular committed use discount.  
`COMMITMENT_3_YEAR` | 3-year regular committed use discount.  
`COMMITMENT_FLEXIBLE_1_YEAR` | 1-year flexible committed use discount. While not supported in the v1 API, this value is converted to UNSPECIFIED in conversions to the v1 API.  
`COMMITMENT_FLEXIBLE_3_YEAR` | 3-year flexible committed use discount. While not supported in the v1 API, this value is converted to UNSPECIFIED in conversions to the v1 API.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
