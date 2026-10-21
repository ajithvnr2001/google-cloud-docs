---
url: https://docs.cloud.google.com/sap/docs/secops/sap-change-document-udm-mapping/
title: SAP Change Document UDM mapping \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:02.828011+00:00
---

# SAP Change Document UDM mapping  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/sap-change-document-udm-mapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP Change Document UDM mapping Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The `SAP_CHANGE_DOCUMENT` parser tracks changes made to business objects in SAP systems, including creations, modifications, and deletions of data.

For information about Google SecOps for SAP, see [Secure SAP applications with Google SecOps](https://docs.cloud.google.com/sap/docs/secops/overview).

## Field mapping reference

The following table describes the mapping between SAP Change Document log fields and Google SecOps UDM fields.

Log field | UDM mapping | Logic  
---|---|---  
`UDATE` | `event.idm.read_only_udm.metadata.event_timestamp` | Date of the change event; combined with UTIME.  
`UTIME` | `event.idm.read_only_udm.metadata.event_timestamp` | Time of the change event; combined with UDATE.  
`MANDANT` | `event.idm.read_only_udm.target.resource.attribute.labels["MANDANT"]` | SAP Client (Tenant) identifier.  
`OBJECTCLAS` | `event.idm.read_only_udm.target.resource.name` | The SAP object class (e.g., EINKBELEG for purchasing documents).  
`OBJECTID` | `event.idm.read_only_udm.target.resource.product_object_id` | The specific identifier of the SAP object.  
`CHANGENR` | `event.idm.read_only_udm.metadata.product_log_id` | Unique SAP change document number.  
`USERNAME` | `event.idm.read_only_udm.principal.user.userid` | The ID of the user who performed the change.  
`TCODE` | `event.idm.read_only_udm.target.application` | SAP Transaction Code used to initiate the change.  
`CHANGE_IND` | `event.idm.read_only_udm.target.resource.attribute.labels["CHANGE_IND"]` | Indicator for the overall change type (U=Update, I=Insert, D=Delete).  
`CHANGE_IND (applied)` | `event.idm.read_only_udm.metadata.event_type` | Used to derive the UDM event type based on user/resource involvement.  
`LANGU` | `event.idm.read_only_udm.target.resource.attribute.labels["LANGU"]` | SAP Language key.  
`VERSION` | `event.idm.read_only_udm.metadata.product_version` | Change document version number.  
`_DATAAGING` | `event.idm.read_only_udm.additional.fields["_DATAAGING"]` | Raw data aging information.  
`CDPOS_ITEMS` | `event.idm.read_only_udm.additional.fields["key_index"]` | Array of position items; each key-value pair is mapped with its index.  
`TABNAME` | `event.idm.read_only_udm.target.resource.attribute.labels["TABNAME"]` | Name of the specific SAP table being changed.  
`TABKEY` | `event.idm.read_only_udm.target.resource.attribute.labels["TABKEY"]` | The specific key/row ID within the target table.  
`FNAME` | `event.idm.read_only_udm.additional.fields["FNAME"]` | Name of the specific field that was modified.  
`CHNGIND` | `event.idm.read_only_udm.target.resource.attribute.labels["CHNGIND"]` | Field-level change indicator.  
`VALUE_OLD` | `event.idm.read_only_udm.additional.fields["VALUE_OLD"]` | Previous value of the field before the change.  
`VALUE_NEW` | `event.idm.read_only_udm.additional.fields["VALUE_NEW"]` | New value of the field after the change.  
`UNIT_OLD` | `event.idm.read_only_udm.additional.fields["UNIT_OLD"]` | Previous unit of measure.  
`UNIT_NEW` | `event.idm.read_only_udm.additional.fields["UNIT_NEW"]` | New unit of measure.  
`CUKY_OLD` | `event.idm.read_only_udm.additional.fields["CUKY_OLD"]` | Previous currency key.  
`CUKY_NEW` | `event.idm.read_only_udm.additional.fields["CUKY_NEW"]` | New currency key.  
`TEXT_CASE` | `event.idm.read_only_udm.target.resource.attribute.labels["TEXT_CASE"]` | Indicates if the change is related to a text object.  
`WAS_PLANND` | `event.idm.read_only_udm.target.resource.attribute.labels["WAS_PLANND"]` | Flag indicating if the change was previously planned.  
`ACT_CHNGNO` | `event.idm.read_only_udm.additional.fields["ACT_CHNGNO"]` | Activation change number.  
`PLANCHNGNR` | `event.idm.read_only_udm.additional.fields["PLANCHNGNR"]` | Planned change number.  
`CDHDR_DATAAGING` | `event.idm.read_only_udm.additional.fields["CDHDR_DATAAGING"]` | Data aging timestamp for the header record.  
`CDPOS_DATAAGING` | `event.idm.read_only_udm.additional.fields["CDPOS_DATAAGING"]` | Data aging timestamp for the position record.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
