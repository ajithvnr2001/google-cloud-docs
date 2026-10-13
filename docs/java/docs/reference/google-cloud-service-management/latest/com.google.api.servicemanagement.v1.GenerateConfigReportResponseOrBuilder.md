---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.GenerateConfigReportResponseOrBuilder
title: Interface GenerateConfigReportResponseOrBuilder (3.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:10.356462+00:00
---

# Interface GenerateConfigReportResponseOrBuilder (3.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.GenerateConfigReportResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GenerateConfigReportResponseOrBuilder (3.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.97.0 (latest)  3.93.0  3.92.0  3.91.0  3.89.0  3.86.0  3.85.0  3.83.0  3.81.0  3.80.0  3.78.0  3.76.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.68.0  3.66.0  3.65.0  3.62.0  3.61.0  3.60.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.7  3.0.1  2.1.7 
    
    
    public interface GenerateConfigReportResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getChangeReports(int index)
    
    
    public abstract ChangeReport getChangeReports(int index)

list of ChangeReport, each corresponding to comparison between two service configurations.

`repeated .google.api.servicemanagement.v1.ChangeReport change_reports = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ChangeReport)` |   
  
### getChangeReportsCount()
    
    
    public abstract int getChangeReportsCount()

list of ChangeReport, each corresponding to comparison between two service configurations.

`repeated .google.api.servicemanagement.v1.ChangeReport change_reports = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getChangeReportsList()
    
    
    public abstract List<ChangeReport> getChangeReportsList()

list of ChangeReport, each corresponding to comparison between two service configurations.

`repeated .google.api.servicemanagement.v1.ChangeReport change_reports = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ChangeReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ChangeReport)>` |   
  
### getChangeReportsOrBuilder(int index)
    
    
    public abstract ChangeReportOrBuilder getChangeReportsOrBuilder(int index)

list of ChangeReport, each corresponding to comparison between two service configurations.

`repeated .google.api.servicemanagement.v1.ChangeReport change_reports = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChangeReportOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ChangeReportOrBuilder)` |   
  
### getChangeReportsOrBuilderList()
    
    
    public abstract List<? extends ChangeReportOrBuilder> getChangeReportsOrBuilderList()

list of ChangeReport, each corresponding to comparison between two service configurations.

`repeated .google.api.servicemanagement.v1.ChangeReport change_reports = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.api.servicemanagement.v1.ChangeReportOrBuilder>` |   
  
### getDiagnostics(int index)
    
    
    public abstract Diagnostic getDiagnostics(int index)

Errors / Linter warnings associated with the service definition this report belongs to.

`repeated .google.api.servicemanagement.v1.Diagnostic diagnostics = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Diagnostic](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.Diagnostic)` |   
  
### getDiagnosticsCount()
    
    
    public abstract int getDiagnosticsCount()

Errors / Linter warnings associated with the service definition this report belongs to.

`repeated .google.api.servicemanagement.v1.Diagnostic diagnostics = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDiagnosticsList()
    
    
    public abstract List<Diagnostic> getDiagnosticsList()

Errors / Linter warnings associated with the service definition this report belongs to.

`repeated .google.api.servicemanagement.v1.Diagnostic diagnostics = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Diagnostic](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.Diagnostic)>` |   
  
### getDiagnosticsOrBuilder(int index)
    
    
    public abstract DiagnosticOrBuilder getDiagnosticsOrBuilder(int index)

Errors / Linter warnings associated with the service definition this report belongs to.

`repeated .google.api.servicemanagement.v1.Diagnostic diagnostics = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiagnosticOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.DiagnosticOrBuilder)` |   
  
### getDiagnosticsOrBuilderList()
    
    
    public abstract List<? extends DiagnosticOrBuilder> getDiagnosticsOrBuilderList()

Errors / Linter warnings associated with the service definition this report belongs to.

`repeated .google.api.servicemanagement.v1.Diagnostic diagnostics = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.api.servicemanagement.v1.DiagnosticOrBuilder>` |   
  
### getId()
    
    
    public abstract String getId()

ID of the service configuration this report belongs to.

`string id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

ID of the service configuration this report belongs to.

`string id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getServiceName()
    
    
    public abstract String getServiceName()

Name of the service this report belongs to.

`string service_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceName.  
  
### getServiceNameBytes()
    
    
    public abstract ByteString getServiceNameBytes()

Name of the service this report belongs to.

`string service_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceName.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
