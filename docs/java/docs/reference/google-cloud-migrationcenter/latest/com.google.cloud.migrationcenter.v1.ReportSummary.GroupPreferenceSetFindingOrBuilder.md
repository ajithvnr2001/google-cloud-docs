---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFindingOrBuilder
title: Interface ReportSummary.GroupPreferenceSetFindingOrBuilder (0.81.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:29.475218+00:00
---

# Interface ReportSummary.GroupPreferenceSetFindingOrBuilder (0.81.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFindingOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReportSummary.GroupPreferenceSetFindingOrBuilder (0.81.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.81.0 (latest)  0.77.0  0.76.0  0.75.0  0.73.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.62.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.46.0  0.45.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ReportSummary.GroupPreferenceSetFindingOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getComputeEngineFinding()
    
    
    public abstract ReportSummary.ComputeEngineFinding getComputeEngineFinding()

A set of findings that applies to Compute Engine machines in the input.

` .google.cloud.migrationcenter.v1.ReportSummary.ComputeEngineFinding compute_engine_finding = 10; `

**Returns**  
---  
**Type** | **Description**  
`[ReportSummary.ComputeEngineFinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportSummary.ComputeEngineFinding)` | The computeEngineFinding.  
  
### getComputeEngineFindingOrBuilder()
    
    
    public abstract ReportSummary.ComputeEngineFindingOrBuilder getComputeEngineFindingOrBuilder()

A set of findings that applies to Compute Engine machines in the input.

` .google.cloud.migrationcenter.v1.ReportSummary.ComputeEngineFinding compute_engine_finding = 10; `

**Returns**  
---  
**Type** | **Description**  
`[ReportSummary.ComputeEngineFindingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportSummary.ComputeEngineFindingOrBuilder)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Description for the Preference Set.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Description for the Preference Set.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Display Name of the Preference Set

`string display_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Display Name of the Preference Set

`string display_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getMachinePreferences()
    
    
    public abstract VirtualMachinePreferences getMachinePreferences()

A set of preferences that applies to all machines in the context.

`.google.cloud.migrationcenter.v1.VirtualMachinePreferences machine_preferences = 3; `

**Returns**  
---  
**Type** | **Description**  
`[VirtualMachinePreferences](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.VirtualMachinePreferences)` | The machinePreferences.  
  
### getMachinePreferencesOrBuilder()
    
    
    public abstract VirtualMachinePreferencesOrBuilder getMachinePreferencesOrBuilder()

A set of preferences that applies to all machines in the context.

`.google.cloud.migrationcenter.v1.VirtualMachinePreferences machine_preferences = 3; `

**Returns**  
---  
**Type** | **Description**  
`[VirtualMachinePreferencesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.VirtualMachinePreferencesOrBuilder)` |   
  
### getMonthlyCostCompute()
    
    
    public abstract Money getMonthlyCostCompute()

Compute monthly cost for this preference set.

`.google.type.Money monthly_cost_compute = 5;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Money` | The monthlyCostCompute.  
  
### getMonthlyCostComputeOrBuilder()
    
    
    public abstract MoneyOrBuilder getMonthlyCostComputeOrBuilder()

Compute monthly cost for this preference set.

`.google.type.Money monthly_cost_compute = 5;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.MoneyOrBuilder` |   
  
### getMonthlyCostNetworkEgress()
    
    
    public abstract Money getMonthlyCostNetworkEgress()

Network Egress monthly cost for this preference set.

`.google.type.Money monthly_cost_network_egress = 7;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Money` | The monthlyCostNetworkEgress.  
  
### getMonthlyCostNetworkEgressOrBuilder()
    
    
    public abstract MoneyOrBuilder getMonthlyCostNetworkEgressOrBuilder()

Network Egress monthly cost for this preference set.

`.google.type.Money monthly_cost_network_egress = 7;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.MoneyOrBuilder` |   
  
### getMonthlyCostOsLicense()
    
    
    public abstract Money getMonthlyCostOsLicense()

Licensing monthly cost for this preference set.

`.google.type.Money monthly_cost_os_license = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Money` | The monthlyCostOsLicense.  
  
### getMonthlyCostOsLicenseOrBuilder()
    
    
    public abstract MoneyOrBuilder getMonthlyCostOsLicenseOrBuilder()

Licensing monthly cost for this preference set.

`.google.type.Money monthly_cost_os_license = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.MoneyOrBuilder` |   
  
### getMonthlyCostOther()
    
    
    public abstract Money getMonthlyCostOther()

Miscellaneous monthly cost for this preference set.

`.google.type.Money monthly_cost_other = 9;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Money` | The monthlyCostOther.  
  
### getMonthlyCostOtherOrBuilder()
    
    
    public abstract MoneyOrBuilder getMonthlyCostOtherOrBuilder()

Miscellaneous monthly cost for this preference set.

`.google.type.Money monthly_cost_other = 9;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.MoneyOrBuilder` |   
  
### getMonthlyCostStorage()
    
    
    public abstract Money getMonthlyCostStorage()

Storage monthly cost for this preference set.

`.google.type.Money monthly_cost_storage = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Money` | The monthlyCostStorage.  
  
### getMonthlyCostStorageOrBuilder()
    
    
    public abstract MoneyOrBuilder getMonthlyCostStorageOrBuilder()

Storage monthly cost for this preference set.

`.google.type.Money monthly_cost_storage = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.MoneyOrBuilder` |   
  
### getMonthlyCostTotal()
    
    
    public abstract Money getMonthlyCostTotal()

Total monthly cost for this preference set.

`.google.type.Money monthly_cost_total = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Money` | The monthlyCostTotal.  
  
### getMonthlyCostTotalOrBuilder()
    
    
    public abstract MoneyOrBuilder getMonthlyCostTotalOrBuilder()

Total monthly cost for this preference set.

`.google.type.Money monthly_cost_total = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.MoneyOrBuilder` |   
  
### getSoleTenantFinding()
    
    
    public abstract ReportSummary.SoleTenantFinding getSoleTenantFinding()

A set of findings that applies to Sole-Tenant machines in the input.

` .google.cloud.migrationcenter.v1.ReportSummary.SoleTenantFinding sole_tenant_finding = 12; `

**Returns**  
---  
**Type** | **Description**  
`[ReportSummary.SoleTenantFinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportSummary.SoleTenantFinding)` | The soleTenantFinding.  
  
### getSoleTenantFindingOrBuilder()
    
    
    public abstract ReportSummary.SoleTenantFindingOrBuilder getSoleTenantFindingOrBuilder()

A set of findings that applies to Sole-Tenant machines in the input.

` .google.cloud.migrationcenter.v1.ReportSummary.SoleTenantFinding sole_tenant_finding = 12; `

**Returns**  
---  
**Type** | **Description**  
`[ReportSummary.SoleTenantFindingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportSummary.SoleTenantFindingOrBuilder)` |   
  
### getVmwareEngineFinding()
    
    
    public abstract ReportSummary.VmwareEngineFinding getVmwareEngineFinding()

A set of findings that applies to VMWare machines in the input.

` .google.cloud.migrationcenter.v1.ReportSummary.VmwareEngineFinding vmware_engine_finding = 11; `

**Returns**  
---  
**Type** | **Description**  
`[ReportSummary.VmwareEngineFinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportSummary.VmwareEngineFinding)` | The vmwareEngineFinding.  
  
### getVmwareEngineFindingOrBuilder()
    
    
    public abstract ReportSummary.VmwareEngineFindingOrBuilder getVmwareEngineFindingOrBuilder()

A set of findings that applies to VMWare machines in the input.

` .google.cloud.migrationcenter.v1.ReportSummary.VmwareEngineFinding vmware_engine_finding = 11; `

**Returns**  
---  
**Type** | **Description**  
`[ReportSummary.VmwareEngineFindingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.ReportSummary.VmwareEngineFindingOrBuilder)` |   
  
### hasComputeEngineFinding()
    
    
    public abstract boolean hasComputeEngineFinding()

A set of findings that applies to Compute Engine machines in the input.

` .google.cloud.migrationcenter.v1.ReportSummary.ComputeEngineFinding compute_engine_finding = 10; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computeEngineFinding field is set.  
  
### hasMachinePreferences()
    
    
    public abstract boolean hasMachinePreferences()

A set of preferences that applies to all machines in the context.

`.google.cloud.migrationcenter.v1.VirtualMachinePreferences machine_preferences = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the machinePreferences field is set.  
  
### hasMonthlyCostCompute()
    
    
    public abstract boolean hasMonthlyCostCompute()

Compute monthly cost for this preference set.

`.google.type.Money monthly_cost_compute = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the monthlyCostCompute field is set.  
  
### hasMonthlyCostNetworkEgress()
    
    
    public abstract boolean hasMonthlyCostNetworkEgress()

Network Egress monthly cost for this preference set.

`.google.type.Money monthly_cost_network_egress = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the monthlyCostNetworkEgress field is set.  
  
### hasMonthlyCostOsLicense()
    
    
    public abstract boolean hasMonthlyCostOsLicense()

Licensing monthly cost for this preference set.

`.google.type.Money monthly_cost_os_license = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the monthlyCostOsLicense field is set.  
  
### hasMonthlyCostOther()
    
    
    public abstract boolean hasMonthlyCostOther()

Miscellaneous monthly cost for this preference set.

`.google.type.Money monthly_cost_other = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the monthlyCostOther field is set.  
  
### hasMonthlyCostStorage()
    
    
    public abstract boolean hasMonthlyCostStorage()

Storage monthly cost for this preference set.

`.google.type.Money monthly_cost_storage = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the monthlyCostStorage field is set.  
  
### hasMonthlyCostTotal()
    
    
    public abstract boolean hasMonthlyCostTotal()

Total monthly cost for this preference set.

`.google.type.Money monthly_cost_total = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the monthlyCostTotal field is set.  
  
### hasSoleTenantFinding()
    
    
    public abstract boolean hasSoleTenantFinding()

A set of findings that applies to Sole-Tenant machines in the input.

` .google.cloud.migrationcenter.v1.ReportSummary.SoleTenantFinding sole_tenant_finding = 12; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the soleTenantFinding field is set.  
  
### hasVmwareEngineFinding()
    
    
    public abstract boolean hasVmwareEngineFinding()

A set of findings that applies to VMWare machines in the input.

` .google.cloud.migrationcenter.v1.ReportSummary.VmwareEngineFinding vmware_engine_finding = 11; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vmwareEngineFinding field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
