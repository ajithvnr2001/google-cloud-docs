---
url: https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis-audit-logging/
title: Artifact Analysis Audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:03.066825+00:00
---

# Artifact Analysis Audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Artifact Analysis Audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Artifact Analysis. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Artifact Analysis audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="containeranalysis.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Artifact Analysis generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.devtools.containeranalysis.v1.ContainerAnalysis.GetIamPolicy`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetIamPolicy`  
`google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.GetIamPolicy`  
`ADMIN_WRITE` | `google.devtools.containeranalysis.v1.ContainerAnalysis.SetIamPolicy`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.SetIamPolicy`  
`google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.SetIamPolicy`  
`DATA_READ` | `google.devtools.containeranalysis.v1.ContainerAnalysis.ExportSBOM`  
`google.devtools.containeranalysis.v1.ContainerAnalysis.GetVulnerabilityOccurrencesSummary`  
`google.devtools.containeranalysis.v1.ContainerAnalysis.TestIamPermissions`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetNote`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetOccurrence`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetOccurrenceNote`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetVulnzOccurrencesSummary`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListNoteOccurrences`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListNotes`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListOccurrences`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.TestIamPermissions`  
`google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.ExportSBOM`  
`google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.GeneratePackagesSummary`  
`google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.TestIamPermissions`  
`grafeas.v1.Grafeas.GetNote`  
`grafeas.v1.Grafeas.GetOccurrence`  
`grafeas.v1.Grafeas.GetOccurrenceNote`  
`grafeas.v1.Grafeas.ListNoteOccurrences`  
`grafeas.v1.Grafeas.ListNotes`  
`grafeas.v1.Grafeas.ListOccurrences`  
`grafeas.v1beta1.GrafeasV1Beta1.GetNote`  
`grafeas.v1beta1.GrafeasV1Beta1.GetOccurrence`  
`grafeas.v1beta1.GrafeasV1Beta1.GetOccurrenceNote`  
`grafeas.v1beta1.GrafeasV1Beta1.GetVulnerabilityOccurrencesSummary`  
`grafeas.v1beta1.GrafeasV1Beta1.ListNoteOccurrences`  
`grafeas.v1beta1.GrafeasV1Beta1.ListNotes`  
`grafeas.v1beta1.GrafeasV1Beta1.ListOccurrences`  
`DATA_WRITE` | `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.CreateNote`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.CreateOccurrence`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.DeleteNote`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.DeleteOccurrence`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.UpdateNote`  
`google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.UpdateOccurrence`  
`grafeas.v1.Grafeas.BatchCreateNotes`  
`grafeas.v1.Grafeas.BatchCreateOccurrences`  
`grafeas.v1.Grafeas.CreateNote`  
`grafeas.v1.Grafeas.CreateOccurrence`  
`grafeas.v1.Grafeas.DeleteNote`  
`grafeas.v1.Grafeas.DeleteOccurrence`  
`grafeas.v1.Grafeas.UpdateNote`  
`grafeas.v1.Grafeas.UpdateOccurrence`  
`grafeas.v1beta1.GrafeasV1Beta1.BatchCreateNotes`  
`grafeas.v1beta1.GrafeasV1Beta1.BatchCreateOccurrences`  
`grafeas.v1beta1.GrafeasV1Beta1.CreateNote`  
`grafeas.v1beta1.GrafeasV1Beta1.CreateOccurrence`  
`grafeas.v1beta1.GrafeasV1Beta1.DeleteNote`  
`grafeas.v1beta1.GrafeasV1Beta1.DeleteOccurrence`  
`grafeas.v1beta1.GrafeasV1Beta1.UpdateNote`  
`grafeas.v1beta1.GrafeasV1Beta1.UpdateOccurrence`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Artifact Analysis.

### `google.devtools.containeranalysis.v1.ContainerAnalysis`

The following audit logs are associated with methods belonging to `google.devtools.containeranalysis.v1.ContainerAnalysis`.

#### `ExportSBOM`

  * **Method** : `google.devtools.containeranalysis.v1.ContainerAnalysis.ExportSBOM`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1.ContainerAnalysis.ExportSBOM" `  




#### `GetIamPolicy`

  * **Method** : `google.devtools.containeranalysis.v1.ContainerAnalysis.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.getIamPolicy - ADMIN_READ`
    * `containeranalysis.occurrences.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1.ContainerAnalysis.GetIamPolicy" `  




#### `GetVulnerabilityOccurrencesSummary`

  * **Method** : `google.devtools.containeranalysis.v1.ContainerAnalysis.GetVulnerabilityOccurrencesSummary`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1.ContainerAnalysis.GetVulnerabilityOccurrencesSummary" `  




#### `SetIamPolicy`

  * **Method** : `google.devtools.containeranalysis.v1.ContainerAnalysis.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `containeranalysis.notes.setIamPolicy - ADMIN_WRITE`
    * `containeranalysis.occurrences.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1.ContainerAnalysis.SetIamPolicy" `  




#### `TestIamPermissions`

  * **Method** : `google.devtools.containeranalysis.v1.ContainerAnalysis.TestIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.list - DATA_READ`
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1.ContainerAnalysis.TestIamPermissions" `  




### `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis`

The following audit logs are associated with methods belonging to `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis`.

#### `CreateNote`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.CreateNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.CreateNote" `  




#### `CreateOccurrence`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.CreateOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.CreateOccurrence" `  




#### `DeleteNote`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.DeleteNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.DeleteNote" `  




#### `DeleteOccurrence`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.DeleteOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.DeleteOccurrence" `  




#### `GetIamPolicy`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.getIamPolicy - ADMIN_READ`
    * `containeranalysis.occurrences.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetIamPolicy" `  




#### `GetNote`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetNote" `  




#### `GetOccurrence`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetOccurrence" `  




#### `GetOccurrenceNote`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetOccurrenceNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetOccurrenceNote" `  




#### `GetVulnzOccurrencesSummary`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetVulnzOccurrencesSummary`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetVulnzOccurrencesSummary" `  




#### `ListNoteOccurrences`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListNoteOccurrences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.listOccurrences - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListNoteOccurrences" `  




#### `ListNotes`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListNotes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListNotes" `  




#### `ListOccurrences`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListOccurrences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListOccurrences" `  




#### `SetIamPolicy`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `containeranalysis.notes.setIamPolicy - ADMIN_WRITE`
    * `containeranalysis.occurrences.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.SetIamPolicy" `  




#### `TestIamPermissions`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.TestIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.list - DATA_READ`
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.TestIamPermissions" `  




#### `UpdateNote`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.UpdateNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.UpdateNote" `  




#### `UpdateOccurrence`

  * **Method** : `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.UpdateOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.UpdateOccurrence" `  




### `google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1`

The following audit logs are associated with methods belonging to `google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1`.

#### `ExportSBOM`

  * **Method** : `google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.ExportSBOM`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.create - DATA_WRITE`
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.ExportSBOM" `  




#### `GeneratePackagesSummary`

  * **Method** : `google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.GeneratePackagesSummary`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.GeneratePackagesSummary" `  




#### `GetIamPolicy`

  * **Method** : `google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `containeranalysis.notes.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.SetIamPolicy" `  




#### `TestIamPermissions`

  * **Method** : `google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.TestIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.list - DATA_READ`
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.containeranalysis.v1beta1.ContainerAnalysisV1Beta1.TestIamPermissions" `  




### `grafeas.v1.Grafeas`

The following audit logs are associated with methods belonging to `grafeas.v1.Grafeas`.

#### `BatchCreateNotes`

  * **Method** : `grafeas.v1.Grafeas.BatchCreateNotes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.BatchCreateNotes" `  




#### `BatchCreateOccurrences`

  * **Method** : `grafeas.v1.Grafeas.BatchCreateOccurrences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.attachOccurrence - DATA_WRITE`
    * `containeranalysis.occurrences.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.BatchCreateOccurrences" `  




#### `CreateNote`

  * **Method** : `grafeas.v1.Grafeas.CreateNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.CreateNote" `  




#### `CreateOccurrence`

  * **Method** : `grafeas.v1.Grafeas.CreateOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.attachOccurrence - DATA_WRITE`
    * `containeranalysis.occurrences.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.CreateOccurrence" `  




#### `DeleteNote`

  * **Method** : `grafeas.v1.Grafeas.DeleteNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.DeleteNote" `  




#### `DeleteOccurrence`

  * **Method** : `grafeas.v1.Grafeas.DeleteOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.attachOccurrence - DATA_WRITE`
    * `containeranalysis.occurrences.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.DeleteOccurrence" `  




#### `GetNote`

  * **Method** : `grafeas.v1.Grafeas.GetNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.GetNote" `  




#### `GetOccurrence`

  * **Method** : `grafeas.v1.Grafeas.GetOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.GetOccurrence" `  




#### `GetOccurrenceNote`

  * **Method** : `grafeas.v1.Grafeas.GetOccurrenceNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.GetOccurrenceNote" `  




#### `ListNoteOccurrences`

  * **Method** : `grafeas.v1.Grafeas.ListNoteOccurrences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.listOccurrences - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.ListNoteOccurrences" `  




#### `ListNotes`

  * **Method** : `grafeas.v1.Grafeas.ListNotes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.ListNotes" `  




#### `ListOccurrences`

  * **Method** : `grafeas.v1.Grafeas.ListOccurrences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.ListOccurrences" `  




#### `UpdateNote`

  * **Method** : `grafeas.v1.Grafeas.UpdateNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.UpdateNote" `  




#### `UpdateOccurrence`

  * **Method** : `grafeas.v1.Grafeas.UpdateOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.attachOccurrence - DATA_WRITE`
    * `containeranalysis.occurrences.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1.Grafeas.UpdateOccurrence" `  




### `grafeas.v1beta1.GrafeasV1Beta1`

The following audit logs are associated with methods belonging to `grafeas.v1beta1.GrafeasV1Beta1`.

#### `BatchCreateNotes`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.BatchCreateNotes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.BatchCreateNotes" `  




#### `BatchCreateOccurrences`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.BatchCreateOccurrences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.BatchCreateOccurrences" `  




#### `CreateNote`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.CreateNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.CreateNote" `  




#### `CreateOccurrence`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.CreateOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.attachOccurrence - DATA_WRITE`
    * `containeranalysis.occurrences.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.CreateOccurrence" `  




#### `DeleteNote`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.DeleteNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.DeleteNote" `  




#### `DeleteOccurrence`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.DeleteOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.attachOccurrence - DATA_WRITE`
    * `containeranalysis.occurrences.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.DeleteOccurrence" `  




#### `GetNote`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.GetNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.GetNote" `  




#### `GetOccurrence`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.GetOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.GetOccurrence" `  




#### `GetOccurrenceNote`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.GetOccurrenceNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.GetOccurrenceNote" `  




#### `GetVulnerabilityOccurrencesSummary`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.GetVulnerabilityOccurrencesSummary`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.GetVulnerabilityOccurrencesSummary" `  




#### `ListNoteOccurrences`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.ListNoteOccurrences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.listOccurrences - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.ListNoteOccurrences" `  




#### `ListNotes`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.ListNotes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.ListNotes" `  




#### `ListOccurrences`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.ListOccurrences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.occurrences.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.ListOccurrences" `  




#### `UpdateNote`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.UpdateNote`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.UpdateNote" `  




#### `UpdateOccurrence`

  * **Method** : `grafeas.v1beta1.GrafeasV1Beta1.UpdateOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `containeranalysis.notes.attachOccurrence - DATA_WRITE`
    * `containeranalysis.occurrences.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="grafeas.v1beta1.GrafeasV1Beta1.UpdateOccurrence" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.CreateOperation`
  * `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.GetScanConfig`
  * `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.ListScanConfigs`
  * `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.UpdateOperation`
  * `google.devtools.containeranalysis.v1alpha1.ContainerAnalysis.UpdateScanConfig`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
