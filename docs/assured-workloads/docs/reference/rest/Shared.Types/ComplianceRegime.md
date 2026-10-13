---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime/
title: ComplianceRegime \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:30.937729+00:00
---

# ComplianceRegime  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  ComplianceRegime Stay organized with collections  Save and categorize content based on your preferences. 

[Assured Workloads control packages](https://cloud.google.com/assured-workloads/docs/control-packages) that provide compliant data boundaries in Google Cloud. The names of some of these control packages and their enums have changed. While old enums are backwards compatible with the new enums, we recommend using the new enums. See the [Control package renaming notice](https://cloud.google.com/assured-workloads/docs/overview#name-change) for more information.

Enums  
---  
`COMPLIANCE_REGIME_UNSPECIFIED` | The default value. This value is used if the control package is omitted or unknown.  
`ASSURED_WORKLOADS_FOR_PARTNERS` | Specifies a [Sovereign Controls by Partners](https://cloud.google.com/sovereign-controls-by-partners/docs/overview) control package. To use this control package, you must also specify the partner field from the list of Sovereign Controls by Partners.  
`AUSTRALIA_DATA_BOUNDARY_AND_SUPPORT` | Australia Data Boundary and Support  
`CANADA_DATA_BOUNDARY_AND_SUPPORT` | Canada Data Boundary and Support  
`DATA_BOUNDARY_FOR_CANADA_CONTROLLED_GOODS` | Data Boundary for Canada Controlled Goods  
`DATA_BOUNDARY_FOR_CANADA_PROTECTED_B` | Data Boundary for Canada Protected B  
`DATA_BOUNDARY_FOR_CJIS` | Data Boundary for Criminal Justice Information Systems (CJIS)  
`DATA_BOUNDARY_FOR_FEDRAMP_HIGH` | Data Boundary for FedRAMP High  
`DATA_BOUNDARY_FOR_FEDRAMP_MODERATE` | Data Boundary for FedRAMP Moderate  
`DATA_BOUNDARY_FOR_IL2` | Data Boundary for Impact Level 2 (IL2)  
`DATA_BOUNDARY_FOR_IL4` | Data Boundary for Impact Level 4 (IL4)  
`DATA_BOUNDARY_FOR_IL5` | Data Boundary for Impact Level 5 (IL5)  
`DATA_BOUNDARY_FOR_IRS_PUBLICATION_1075` | Data Boundary for IRS Publication 1075  
`DATA_BOUNDARY_FOR_ITAR` | Data Boundary for International Traffic in Arms Regulations (ITAR)  
`EU_DATA_BOUNDARY_AND_SUPPORT` | European Union (EU) Data Boundary and Support  
`ISRAEL_DATA_BOUNDARY_AND_SUPPORT` | Israel Data Boundary and Support  
`JAPAN_DATA_BOUNDARY` | Japan Data Boundary  
`KSA_DATA_BOUNDARY_WITH_ACCESS_JUSTIFICATIONS` | Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications  
`REGIONAL_DATA_BOUNDARY` | Data boundary for one of Assured Workloads' _Free tier_ control packages. Determines the region by specifying the data location during workload creation.  
`US_DATA_BOUNDARY_AND_SUPPORT` | United States (US) Data Boundary and Support  
`US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES` | United States (US) Data Boundary for Healthcare and Life Sciences  
`US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES_WITH_SUPPORT` | United States (US) Data Boundary for Healthcare and Life Sciences with Support  
`AU_REGIONS_AND_US_SUPPORT` | Use the `[AUSTRALIA_DATA_BOUNDARY_AND_SUPPORT](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.AUSTRALIA_DATA_BOUNDARY_AND_SUPPORT)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`CA_PROTECTED_B` | Use the `[DATA_BOUNDARY_FOR_CANADA_PROTECTED_B](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_CANADA_PROTECTED_B)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`CA_REGIONS_AND_SUPPORT` | Use the `[CANADA_DATA_BOUNDARY_AND_SUPPORT](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.CANADA_DATA_BOUNDARY_AND_SUPPORT)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`CANADA_CONTROLLED_GOODS` | Use the `[DATA_BOUNDARY_FOR_CANADA_CONTROLLED_GOODS](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_CANADA_CONTROLLED_GOODS)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`CJIS` | Use the `[DATA_BOUNDARY_FOR_CJIS](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_CJIS)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`EU_REGIONS_AND_SUPPORT` | Use the `[EU_DATA_BOUNDARY_AND_SUPPORT](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.EU_DATA_BOUNDARY_AND_SUPPORT)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`FEDRAMP_HIGH` | Use the `[DATA_BOUNDARY_FOR_FEDRAMP_HIGH](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_FEDRAMP_HIGH)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`FEDRAMP_MODERATE` | Use the `[DATA_BOUNDARY_FOR_FEDRAMP_MODERATE](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_FEDRAMP_MODERATE)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS` | Use the `[US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS_US_SUPPORT` | Use the `[US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES_WITH_SUPPORT](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES_WITH_SUPPORT)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`HIPAA` | Deprecated: Consider using the Data Boundary for US Healthcare and Life Sciences control package instead.This item is deprecated!  
`HITRUST` | Deprecated: Consider using the Data Boundary for US Healthcare and Life Sciences control package instead.This item is deprecated!  
`IL2` | Use the `[DATA_BOUNDARY_FOR_IL2](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_IL2)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`IL4` | Use the `[DATA_BOUNDARY_FOR_IL4](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_IL4)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`IL5` | Use the `[DATA_BOUNDARY_FOR_IL5](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_IL5)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`IRS_1075` | Use the `[DATA_BOUNDARY_FOR_IRS_PUBLICATION_1075](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_IRS_PUBLICATION_1075)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`ISR_REGIONS` | Use the `[ISRAEL_DATA_BOUNDARY_AND_SUPPORT](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.ISRAEL_DATA_BOUNDARY_AND_SUPPORT)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`ISR_REGIONS_AND_SUPPORT` | Use the `[ISRAEL_DATA_BOUNDARY_AND_SUPPORT](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.ISRAEL_DATA_BOUNDARY_AND_SUPPORT)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`ITAR` | Use the `[DATA_BOUNDARY_FOR_ITAR](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.DATA_BOUNDARY_FOR_ITAR)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`JP_REGIONS_AND_SUPPORT` | Use the `[JAPAN_DATA_BOUNDARY](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.JAPAN_DATA_BOUNDARY)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`KSA_REGIONS_AND_SUPPORT_WITH_SOVEREIGNTY_CONTROLS` | Use the `[KSA_DATA_BOUNDARY_WITH_ACCESS_JUSTIFICATIONS](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.KSA_DATA_BOUNDARY_WITH_ACCESS_JUSTIFICATIONS)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`REGIONAL_CONTROLS` | Use the `[REGIONAL_DATA_BOUNDARY](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.REGIONAL_DATA_BOUNDARY)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
`US_REGIONAL_ACCESS` | Use the `[US_DATA_BOUNDARY_AND_SUPPORT](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ComplianceRegime#ENUM_VALUES.US_DATA_BOUNDARY_AND_SUPPORT)` enum for this control package instead, as the name of the associated Assured Workloads control package has changed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-27 UTC."],[],[]] 
