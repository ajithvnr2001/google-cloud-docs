---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/
title: Sensitive Data Protection (DLP API) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:52.315988+00:00
---

# Sensitive Data Protection (DLP API)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Sensitive Data Protection (DLP API) Stay organized with collections  Save and categorize content based on your preferences. 

Provides methods for detection of privacy-sensitive fragments in text, images, and Google Cloud Platform storage repositories. The Cloud Data Loss Prevention API (DLP API) is part of [Sensitive Data Protection](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview).

## Service: dlp.googleapis.com

The Service name `dlp.googleapis.com` is needed to create RPC client stubs.

## `[google.privacy.dlp.v2.DlpService](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService)`

Methods  
---  
``[ActivateJobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ActivateJobTrigger)`` |  Activate a job trigger.  
``[CancelDlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.CancelDlpJob)`` |  Starts asynchronous cancellation on a long-running DlpJob.  
``[CreateConnection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.CreateConnection)`` |  Create a Connection to an external data source.  
``[CreateContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.CreateContentPolicy)`` |  Create a ContentPolicy.  
``[CreateDeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.CreateDeidentifyTemplate)`` |  Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage.  
``[CreateDiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.CreateDiscoveryConfig)`` |  Creates a config for discovery to scan and profile storage.  
``[CreateDlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.CreateDlpJob)`` |  Creates a new job to inspect storage or calculate risk metrics.  
``[CreateInspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.CreateInspectTemplate)`` |  Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage.  
``[CreateJobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.CreateJobTrigger)`` |  Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule.  
``[CreateStoredInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.CreateStoredInfoType)`` |  Creates a pre-built stored infoType to be used for inspection.  
``[DeidentifyContent](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeidentifyContent)`` |  De-identifies potentially sensitive info from a ContentItem.  
``[DeleteConnection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteConnection)`` |  Delete a Connection.  
``[DeleteContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteContentPolicy)`` |  Delete a ContentPolicy.  
``[DeleteDeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteDeidentifyTemplate)`` |  Deletes a DeidentifyTemplate.  
``[DeleteDiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteDiscoveryConfig)`` |  Deletes a discovery configuration.  
``[DeleteDlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteDlpJob)`` |  Deletes a long-running DlpJob.  
``[DeleteFileStoreDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteFileStoreDataProfile)`` |  Delete a FileStoreDataProfile.  
``[DeleteInspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteInspectTemplate)`` |  Deletes an InspectTemplate.  
``[DeleteJobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteJobTrigger)`` |  Deletes a job trigger.  
``[DeleteStoredInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteStoredInfoType)`` |  Deletes a stored infoType.  
``[DeleteTableDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.DeleteTableDataProfile)`` |  Delete a TableDataProfile.  
``[FinishDlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.FinishDlpJob)`` |  Finish a running hybrid DlpJob.  
``[GetColumnDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetColumnDataProfile)`` |  Gets a column data profile.  
``[GetConnection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetConnection)`` |  Get a Connection by name.  
``[GetContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetContentPolicy)`` |  Get a ContentPolicy.  
``[GetDeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetDeidentifyTemplate)`` |  Gets a DeidentifyTemplate.  
``[GetDiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetDiscoveryConfig)`` |  Gets a discovery configuration.  
``[GetDlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetDlpJob)`` |  Gets the latest state of a long-running DlpJob.  
``[GetFileStoreDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetFileStoreDataProfile)`` |  Gets a file store data profile.  
``[GetInspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetInspectTemplate)`` |  Gets an InspectTemplate.  
``[GetJobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetJobTrigger)`` |  Gets a job trigger.  
``[GetProjectDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetProjectDataProfile)`` |  Gets a project data profile.  
``[GetStoredInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetStoredInfoType)`` |  Gets a stored infoType.  
``[GetTableDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetTableDataProfile)`` |  Gets a table data profile.  
``[HybridInspectDlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.HybridInspectDlpJob)`` |  Inspect hybrid content and store findings to a job.  
``[HybridInspectJobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.HybridInspectJobTrigger)`` |  Inspect hybrid content and store findings to a trigger.  
``[InspectContent](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.InspectContent)`` |  Finds potentially sensitive info in content.  
``[ListColumnDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListColumnDataProfiles)`` |  Lists column data profiles for an organization.  
``[ListConnections](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListConnections)`` |  Lists Connections in a parent.  
``[ListContentPolicies](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListContentPolicies)`` |  Lists ContentPolicies in a parent.  
``[ListDeidentifyTemplates](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListDeidentifyTemplates)`` |  Lists DeidentifyTemplates.  
``[ListDiscoveryConfigs](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListDiscoveryConfigs)`` |  Lists discovery configurations.  
``[ListDlpJobs](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListDlpJobs)`` |  Lists DlpJobs that match the specified filter in the request.  
``[ListFileStoreDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListFileStoreDataProfiles)`` |  Lists file store data profiles for an organization.  
``[ListInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListInfoTypes)`` |  Returns a list of the sensitive information types that the DLP API supports.  
``[ListInspectTemplates](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListInspectTemplates)`` |  Lists InspectTemplates.  
``[ListJobTriggers](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListJobTriggers)`` |  Lists job triggers.  
``[ListProjectDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListProjectDataProfiles)`` |  Lists project data profiles for an organization.  
``[ListStoredInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListStoredInfoTypes)`` |  Lists stored infoTypes.  
``[ListTableDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ListTableDataProfiles)`` |  Lists table data profiles for an organization.  
``[RedactImage](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.RedactImage)`` |  Redacts potentially sensitive info from an image.  
``[ReidentifyContent](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.ReidentifyContent)`` |  Re-identifies content that has been de-identified.  
``[SearchConnections](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.SearchConnections)`` |  Searches for Connections in a parent.  
``[UpdateConnection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.UpdateConnection)`` |  Update a Connection.  
``[UpdateContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.UpdateContentPolicy)`` |  Update a ContentPolicy.  
``[UpdateDeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.UpdateDeidentifyTemplate)`` |  Updates the DeidentifyTemplate.  
``[UpdateDiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.UpdateDiscoveryConfig)`` |  Updates a discovery configuration.  
``[UpdateInspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.UpdateInspectTemplate)`` |  Updates the InspectTemplate.  
``[UpdateJobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.UpdateJobTrigger)`` |  Updates a job trigger.  
``[UpdateStoredInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.UpdateStoredInfoType)`` |  Updates the stored infoType by creating a new version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
