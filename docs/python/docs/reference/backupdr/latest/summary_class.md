---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/summary_class/
title: Package Classes (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:31.657798+00:00
---

# Package Classes (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 

Summary of entries of Classes for backupdr.

## Classes 

### [BackupDRAsyncClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient)

The BackupDR Service

### [BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient)

The BackupDR Service

### [FetchBackupPlanAssociationsForResourceTypeAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager)

A pager for iterating through `fetch_backup_plan_associations_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__aiter__` method will make additional `FetchBackupPlanAssociationsForResourceType` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchBackupPlanAssociationsForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager)

A pager for iterating through `fetch_backup_plan_associations_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse) object, and provides an `__iter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__iter__` method will make additional `FetchBackupPlanAssociationsForResourceType` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchBackupsForResourceTypeAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager)

A pager for iterating through `fetch_backups_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `FetchBackupsForResourceType` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchBackupsForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypePager)

A pager for iterating through `fetch_backups_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `FetchBackupsForResourceType` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchDataSourceReferencesForResourceTypeAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager)

A pager for iterating through `fetch_data_source_references_for_resource_type` requests.

This class thinly wraps an initial [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__aiter__` method will make additional `FetchDataSourceReferencesForResourceType` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchDataSourceReferencesForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager)

A pager for iterating through `fetch_data_source_references_for_resource_type` requests.

This class thinly wraps an initial [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse) object, and provides an `__iter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__iter__` method will make additional `FetchDataSourceReferencesForResourceType` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchUsableBackupVaultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager)

A pager for iterating through `fetch_usable_backup_vaults` requests.

This class thinly wraps an initial [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse) object, and provides an `__aiter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__aiter__` method will make additional `FetchUsableBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchUsableBackupVaultsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsPager)

A pager for iterating through `fetch_usable_backup_vaults` requests.

This class thinly wraps an initial [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse) object, and provides an `__iter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__iter__` method will make additional `FetchUsableBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanAssociationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager)

A pager for iterating through `list_backup_plan_associations` requests.

This class thinly wraps an initial [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse) object, and provides an `__aiter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPlanAssociations` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanAssociationsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsPager)

A pager for iterating through `list_backup_plan_associations` requests.

This class thinly wraps an initial [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse) object, and provides an `__iter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPlanAssociations` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager)

A pager for iterating through `list_backup_plan_revisions` requests.

This class thinly wraps an initial [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse) object, and provides an `__aiter__` method to iterate through its `backup_plan_revisions` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPlanRevisions` requests and continue to iterate through the `backup_plan_revisions` field on the corresponding responses.

All the usual [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanRevisionsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsPager)

A pager for iterating through `list_backup_plan_revisions` requests.

This class thinly wraps an initial [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse) object, and provides an `__iter__` method to iterate through its `backup_plan_revisions` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPlanRevisions` requests and continue to iterate through the `backup_plan_revisions` field on the corresponding responses.

All the usual [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlansAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansAsyncPager)

A pager for iterating through `list_backup_plans` requests.

This class thinly wraps an initial [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse) object, and provides an `__aiter__` method to iterate through its `backup_plans` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPlans` requests and continue to iterate through the `backup_plans` field on the corresponding responses.

All the usual [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlansPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansPager)

A pager for iterating through `list_backup_plans` requests.

This class thinly wraps an initial [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse) object, and provides an `__iter__` method to iterate through its `backup_plans` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPlans` requests and continue to iterate through the `backup_plans` field on the corresponding responses.

All the usual [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupVaultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsAsyncPager)

A pager for iterating through `list_backup_vaults` requests.

This class thinly wraps an initial [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse) object, and provides an `__aiter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupVaultsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsPager)

A pager for iterating through `list_backup_vaults` requests.

This class thinly wraps an initial [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse) object, and provides an `__iter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__iter__` method will make additional `ListBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsAsyncPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourceReferencesAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager)

A pager for iterating through `list_data_source_references` requests.

This class thinly wraps an initial [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse) object, and provides an `__aiter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__aiter__` method will make additional `ListDataSourceReferences` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourceReferencesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesPager)

A pager for iterating through `list_data_source_references` requests.

This class thinly wraps an initial [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse) object, and provides an `__iter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__iter__` method will make additional `ListDataSourceReferences` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesAsyncPager)

A pager for iterating through `list_data_sources` requests.

This class thinly wraps an initial [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse) object, and provides an `__aiter__` method to iterate through its `data_sources` field.

If there are more pages, the `__aiter__` method will make additional `ListDataSources` requests and continue to iterate through the `data_sources` field on the corresponding responses.

All the usual [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourcesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesPager)

A pager for iterating through `list_data_sources` requests.

This class thinly wraps an initial [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse) object, and provides an `__iter__` method to iterate through its `data_sources` field.

If there are more pages, the `__iter__` method will make additional `ListDataSources` requests and continue to iterate through the `data_sources` field on the corresponding responses.

All the usual [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListManagementServersAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersAsyncPager)

A pager for iterating through `list_management_servers` requests.

This class thinly wraps an initial [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse) object, and provides an `__aiter__` method to iterate through its `management_servers` field.

If there are more pages, the `__aiter__` method will make additional `ListManagementServers` requests and continue to iterate through the `management_servers` field on the corresponding responses.

All the usual [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListManagementServersPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersPager)

A pager for iterating through `list_management_servers` requests.

This class thinly wraps an initial [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse) object, and provides an `__iter__` method to iterate through its `management_servers` field.

If there are more pages, the `__iter__` method will make additional `ListManagementServers` requests and continue to iterate through the `management_servers` field on the corresponding responses.

All the usual [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [BackupDrProtectionSummaryAsyncClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient)

The Protection Summary service.

### [BackupDrProtectionSummaryClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient)

The Protection Summary service.

### [ListResourceBackupConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager)

A pager for iterating through `list_resource_backup_configs` requests.

This class thinly wraps an initial [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListResourceBackupConfigsResponse) object, and provides an `__aiter__` method to iterate through its `resource_backup_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListResourceBackupConfigs` requests and continue to iterate through the `resource_backup_configs` field on the corresponding responses.

All the usual [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListResourceBackupConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceBackupConfigsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager)

A pager for iterating through `list_resource_backup_configs` requests.

This class thinly wraps an initial [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListResourceBackupConfigsResponse) object, and provides an `__iter__` method to iterate through its `resource_backup_configs` field.

If there are more pages, the `__iter__` method will make additional `ListResourceBackupConfigs` requests and continue to iterate through the `resource_backup_configs` field on the corresponding responses.

All the usual [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListResourceBackupConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AcceleratorConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AcceleratorConfig)

A specification of the type and number of accelerator cards attached to the instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AccessConfig)

An access configuration attached to an instance's network interface. Only one access config per instance is supported.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AccessConfig.AccessType)

The type of configuration.

### [NetworkTier](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AccessConfig.NetworkTier)

Network tier property used by addresses, instances and forwarding rules.

### [AdvancedMachineFeatures](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AdvancedMachineFeatures)

Specifies options for controlling advanced machine features.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AliasIpRange](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AliasIpRange)

An alias IP range attached to an instance's network interface.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AllocationAffinity](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AllocationAffinity)

Specifies the reservations that this instance can consume from.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AllocationAffinity.Type)

Indicates whether to consume from a reservation or not.

### [AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AlloyDBClusterBackupPlanAssociationProperties)

Properties for an AlloyDB cluster backup plan association.

### [AlloyDBClusterDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AlloyDBClusterDataSourceProperties)

AlloyDBClusterDataSourceProperties represents the properties of a AlloyDB cluster resource that are stored in the DataSource. .

### [AlloyDbClusterBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AlloyDbClusterBackupProperties)

AlloyDbClusterBackupProperties represents AlloyDB cluster backup properties. .

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AttachedDisk](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk)

An instance-attached disk resource.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DiskInterface](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.DiskInterface)

List of the Disk Interfaces.

### [DiskMode](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.DiskMode)

List of the Disk Modes.

### [DiskSavedState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.DiskSavedState)

List of the states of the Disk.

### [DiskType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.DiskType)

List of the Disk Types.

### [InitializeParams](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.InitializeParams)

Specifies the parameters to initialize this disk.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup)

Message describing a Backup object.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup.BackupType)

Type of the backup, scheduled or ondemand.

### [GCPBackupPlanInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup.GCPBackupPlanInfo)

GCPBackupPlanInfo captures the plan configuration details of Google Cloud resources at the time of backup.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup.State)

Holds the state of the backup resource.

### [BackupApplianceBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupApplianceBackupConfig)

BackupApplianceBackupConfig captures the backup configuration for applications that are protected by Backup Appliances.

### [BackupApplianceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupApplianceBackupProperties)

BackupApplianceBackupProperties represents BackupDR backup appliance's properties.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupApplianceLockInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupApplianceLockInfo)

BackupApplianceLockInfo contains metadata about the backupappliance that created the lock.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupConfigDetails](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigDetails)

BackupConfigDetails has information about how the resource is configured for backups and about the most recent backup taken for this configuration.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigDetails.State)

The state tells whether the backup config is active or not.

### [Type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigDetails.Type)

Type of the backup configuration. This enum may receive new values in the future.

### [BackupConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigInfo)

BackupConfigInfo has information about how the resource is configured for Backup and about the most recent backup to this vault.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LastBackupState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigInfo.LastBackupState)

LastBackupstate tracks whether the last backup was not yet started, successful, failed, or could not be run because of the lack of permissions.

### [BackupConfigState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigState)

Backup configuration state. Is the resource configured for backup?

### [BackupDrPlanConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupDrPlanConfig)

BackupDrPlanConfig has additional information about Google Cloud Backup and DR's Plan backup configuration.

### [BackupDrPlanRule](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupDrPlanRule)

BackupDrPlanRule has rule specific information of the backup plan resource.

### [BackupDrTemplateConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupDrTemplateConfig)

Provides additional information about Google Cloud Backup and DR's Template backup configuration.

### [BackupGcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupGcpResource)

Minimum details to identify a Google Cloud resource for a backup.

### [BackupLocation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupLocation)

BackupLocation represents a cloud location where a backup can be stored.

### [Type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupLocation.Type)

The type of the location.

### [BackupLock](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupLock)

BackupLock represents a single lock on a Backup resource. An unexpired lock on a Backup prevents the Backup from being deleted.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan)

A `BackupPlan` specifies some common fields, such as `description` as well as one or more `BackupRule` messages. Each `BackupRule` has a retention policy and defines a schedule by which the system is to perform backup workloads.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan.State)

`State` enumerates the possible states for a `BackupPlan`.

### [BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation)

A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation.State)

Enum for State of BackupPlan Association

### [BackupPlanRevision](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanRevision)

`BackupPlanRevision` represents a snapshot of a `BackupPlan` at a point in time.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanRevision.State)

The state of the `BackupPlanRevision`.

### [BackupRule](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupRule)

`BackupRule` binds the backup schedule to a retention policy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupVault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault)

Message describing a BackupVault object.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessRestriction](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault.AccessRestriction)

Holds the access restriction for the backup vault.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault.AnnotationsEntry)

The abstract base class for a message.

### [BackupRetentionInheritance](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault.BackupRetentionInheritance)

How a backup's enforced retention end time is inherited.
    
    
        This is the default behavior.
    MATCH_BACKUP_EXPIRE_TIME (2):
        The enforced retention end time of a backup
        will always match the expire time of the backup.
    
        If this is set, the backup's enforced retention
        end time will be set to match the expire time
        during creation of the backup. When updating,
        the ERET and expire time must be updated
        together and have the same value. Invalid update
        requests will be rejected by the server.
    

### [EncryptionConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault.EncryptionConfig)

Message describing the EncryptionConfig of backup vault. This determines how data within the vault is encrypted at rest.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault.State)

Holds the state of the backup vault resource.

### [BackupVaultView](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVaultView)

BackupVaultView contains enum options for Partial and Full view.

### [BackupView](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupView)

BackupView contains enum options for Partial and Full view.

### [BackupWindow](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupWindow)

`BackupWindow` defines a window of the day during which backup jobs will run.

### [CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceBackupPlanAssociationProperties)

Cloud SQL instance's BPA properties.

### [CloudSqlInstanceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceBackupProperties)

CloudSqlInstanceBackupProperties represents Cloud SQL Instance Backup properties.

### [CloudSqlInstanceDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceDataSourceProperties)

CloudSqlInstanceDataSourceProperties represents the properties of a Cloud SQL resource that are stored in the DataSource.

### [CloudSqlInstanceDataSourceReferenceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceDataSourceReferenceProperties)

CloudSqlInstanceDataSourceReferenceProperties represents the properties of a Cloud SQL resource that are stored in the DataSourceReference.

### [CloudSqlInstanceInitializationConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceInitializationConfig)

CloudSqlInstanceInitializationConfig contains the configuration for initializing a Cloud SQL instance.

### [Edition](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceInitializationConfig.Edition)

The edition of the Cloud SQL instance. For details, see <https://cloud.google.com/sql/docs/editions-intro>.

### [ComputeInstanceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceBackupProperties)

ComputeInstanceBackupProperties represents Compute Engine instance backup properties.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceBackupProperties.LabelsEntry)

The abstract base class for a message.

### [ComputeInstanceDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceDataSourceProperties)

ComputeInstanceDataSourceProperties represents the properties of a ComputeEngine resource that are stored in the DataSource.

### [ComputeInstanceRestoreProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties)

ComputeInstanceRestoreProperties represents Compute Engine instance properties to be overridden during restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InstancePrivateIpv6GoogleAccess](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess)

The private IPv6 google access type for the VMs.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties.LabelsEntry)

The abstract base class for a message.

### [ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceTargetEnvironment)

ComputeInstanceTargetEnvironment represents Compute Engine target environment to be used during restore.

### [ConfidentialInstanceConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ConfidentialInstanceConfig)

A set of Confidential Instance options.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupPlanAssociationRequest)

Request message for creating a backup plan.

### [CreateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupPlanRequest)

The request message for creating a `BackupPlan`.

### [CreateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupVaultRequest)

Message for creating a BackupVault.

### [CreateManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateManagementServerRequest)

Request message for creating a management server instance.

### [CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CustomerEncryptionKey)

A customer-supplied encryption key.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource)

Message describing a DataSource object. Datasource object used to represent Datasource details for both admin and basic view.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource.State)

Holds the state of the data source resource.

### [DataSourceBackupApplianceApplication](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceBackupApplianceApplication)

BackupApplianceApplication describes a Source Resource when it is an application backed up by a BackupAppliance.

### [DataSourceBackupConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceBackupConfigInfo)

Information of backup configuration on the DataSource.

### [DataSourceGcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceGcpResource)

DataSourceGcpResource is used for protected resources that are Google Cloud Resources. This name is easeier to understand than GcpResourceDataSource or GcpDataSourceResource

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSourceGcpResourceInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceGcpResourceInfo)

The GCP resource that the DataSource is associated with.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSourceReference](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceReference)

DataSourceReference is a reference to a DataSource resource.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupPlanAssociationRequest)

Request message for deleting a backup plan association.

### [DeleteBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupPlanRequest)

The request message for deleting a `BackupPlan`.

### [DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupRequest)

Message for deleting a Backup.

### [DeleteBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupVaultRequest)

Message for deleting a BackupVault.

### [DeleteManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteManagementServerRequest)

Request message for deleting a management server instance.

### [DiskBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskBackupProperties)

DiskBackupProperties represents the properties of a Disk backup.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Architecture](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskBackupProperties.Architecture)

Architecture of the source disk.

### [DiskDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskDataSourceProperties)

DiskDataSourceProperties represents the properties of a Disk resource that are stored in the DataSource. .

### [DiskRestoreProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties)

DiskRestoreProperties represents the properties of a Disk restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessMode](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties.AccessMode)

The supported access modes of the disk.

### [Architecture](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties.Architecture)

Architecture of the source disk.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties.LabelsEntry)

The abstract base class for a message.

### [ResourceManagerTagsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties.ResourceManagerTagsEntry)

The abstract base class for a message.

### [DiskTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskTargetEnvironment)

DiskTargetEnvironment represents the target environment for the disk.

### [DisplayDevice](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DisplayDevice)

A set of Display Device options

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Entry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Entry)

A key/value pair to be used for storing metadata.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeRequest)

Request for the FetchBackupPlanAssociationsForResourceType method.

### [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse)

Response for the FetchBackupPlanAssociationsForResourceType method.

### [FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest)

Request for the FetchBackupsForResourceType method.

### [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse)

Response for the FetchBackupsForResourceType method.

### [FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest)

Request for the FetchDataSourceReferencesForResourceType method.

### [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse)

Response for the FetchDataSourceReferencesForResourceType method.

### [FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsRequest)

Request message for fetching usable BackupVaults.

### [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse)

Response message for fetching usable BackupVaults.

### [GcpBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GcpBackupConfig)

GcpBackupConfig captures the Backup configuration details for Google Cloud resources. All Google Cloud resources regardless of type are protected with backup plan associations.

### [GcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GcpResource)

Minimum details to identify a Google Cloud resource

### [GetBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanAssociationRequest)

Request message for getting a BackupPlanAssociation resource.

### [GetBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanRequest)

The request message for getting a `BackupPlan`.

### [GetBackupPlanRevisionRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanRevisionRequest)

The request message for getting a `BackupPlanRevision`.

### [GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupRequest)

Request message for getting a Backup.

### [GetBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupVaultRequest)

Request message for getting a BackupVault.

### [GetDataSourceReferenceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetDataSourceReferenceRequest)

Request for the GetDataSourceReference method.

### [GetDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetDataSourceRequest)

Request message for getting a DataSource instance.

### [GetManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetManagementServerRequest)

Request message for getting a management server instance.

### [GuestOsFeature](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GuestOsFeature)

Feature type of the Guest OS.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FeatureType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GuestOsFeature.FeatureType)

List of the Feature Types.

### [InitializeServiceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InitializeServiceRequest)

Request message for initializing the service.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InitializeServiceResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InitializeServiceResponse)

Response message for initializing the service.

### [InstanceParams](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InstanceParams)

Additional instance params.

### [ResourceManagerTagsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InstanceParams.ResourceManagerTagsEntry)

The abstract base class for a message.

### [KeyRevocationActionType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.KeyRevocationActionType)

Specifies whether the virtual machine instance will be shut down on key revocation. It is currently used in instance, instance properties and GMI protos

### [ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsRequest)

Request message for List BackupPlanAssociation

### [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse)

Response message for List BackupPlanAssociation

### [ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsRequest)

The request message for getting a list of `BackupPlanRevision`.

### [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse)

The response message for getting a list of `BackupPlanRevision`.

### [ListBackupPlansRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansRequest)

The request message for getting a list `BackupPlan`.

### [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse)

The response message for getting a list of `BackupPlan`.

### [ListBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsRequest)

Request message for listing backupvault stores.

### [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse)

Response message for listing BackupVaults.

### [ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsRequest)

Request message for listing Backups.

### [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse)

Response message for listing Backups.

### [ListDataSourceReferencesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesRequest)

Request for the ListDataSourceReferences method.

### [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse)

Response for the ListDataSourceReferences method.

### [ListDataSourcesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesRequest)

Request message for listing DataSources.

### [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse)

Response message for listing DataSources.

### [ListManagementServersRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersRequest)

Request message for listing management servers.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse)

Response message for listing management servers.

### [ListResourceBackupConfigsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListResourceBackupConfigsRequest)

Request for ListResourceBackupConfigs.

### [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListResourceBackupConfigsResponse)

Response for ListResourceBackupConfigs.

### [ManagementServer](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer)

ManagementServer describes a single BackupDR ManagementServer instance.

### [InstanceState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer.InstanceState)

State of Management server instance.

### [InstanceType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer.InstanceType)

Type of backup service resource.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer.LabelsEntry)

The abstract base class for a message.

### [ManagementURI](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementURI)

ManagementURI for the Management Server resource.

### [Metadata](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Metadata)

A metadata key/value entry.

### [NetworkConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkConfig)

Network configuration for ManagementServer instance.

### [PeeringMode](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkConfig.PeeringMode)

VPC peering modes supported by Cloud BackupDR.

### [NetworkInterface](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkInterface)

A network interface resource attached to an instance. s

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Ipv6AccessType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkInterface.Ipv6AccessType)

IPv6 access type for this network interface.

### [NicType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkInterface.NicType)

Nic type for this network interface.

### [StackType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkInterface.StackType)

Stack type for this network interface.

### [NetworkPerformanceConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkPerformanceConfig)

Network performance configuration.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Tier](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkPerformanceConfig.Tier)

Network performance tier.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [AdditionalInfoEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.OperationMetadata.AdditionalInfoEntry)

The abstract base class for a message.

### [PitrSettings](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.PitrSettings)

Point in time recovery settings of the backup configuration resource.

### [RegionDiskTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RegionDiskTargetEnvironment)

RegionDiskTargetEnvironment represents the target environment for the disk.

### [ResourceBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ResourceBackupConfig)

ResourceBackupConfig represents a resource along with its backup configurations.

### [ResourceType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ResourceBackupConfig.ResourceType)

The type of the cloud resource.

### [TargetResourceLabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ResourceBackupConfig.TargetResourceLabelsEntry)

The abstract base class for a message.

### [RestoreBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RestoreBackupRequest)

Request message for restoring from a Backup.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreBackupResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RestoreBackupResponse)

Response message for restoring from a Backup.

### [RuleConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RuleConfigInfo)

Message for rules config info.

### [LastBackupState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RuleConfigInfo.LastBackupState)

Enum for LastBackupState

### [Scheduling](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling)

Sets the scheduling options for an Instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InstanceTerminationAction](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling.InstanceTerminationAction)

Defines the supported termination actions for an instance.

### [NodeAffinity](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling.NodeAffinity)

Node Affinity: the configuration of desired nodes onto which this Instance could be scheduled.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Operator](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling.NodeAffinity.Operator)

Defines the type of node selections.

### [OnHostMaintenance](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling.OnHostMaintenance)

Defines the maintenance behavior for this instance=

### [ProvisioningModel](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling.ProvisioningModel)

Defines the provisioning model for an instance.

### [SchedulingDuration](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.SchedulingDuration)

A SchedulingDuration represents a fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". Range is approximately 10,000 years.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceAccount](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ServiceAccount)

A service account.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceLockInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ServiceLockInfo)

ServiceLockInfo represents the details of a lock taken by the service on a Backup resource.

### [StandardSchedule](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.StandardSchedule)

`StandardSchedule` defines a schedule that run within the confines of a defined window of days. We can define recurrence type for schedule as HOURLY, DAILY, WEEKLY, MONTHLY or YEARLY.

### [RecurrenceType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.StandardSchedule.RecurrenceType)

`RecurrenceTypes` enumerates the applicable periodicity for the schedule.

### [Tags](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Tags)

A set of instance tags.

### [TargetResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.TargetResource)

Details of the target resource created/modified as part of restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TriggerBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.TriggerBackupRequest)

Request message for triggering a backup.

### [UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupPlanAssociationRequest)

Request message for updating a backup plan association.

### [UpdateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupPlanRequest)

Request message for updating a backup plan.

### [UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupRequest)

Request message for updating a Backup.

### [UpdateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupVaultRequest)

Request message for updating a BackupVault.

### [UpdateDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateDataSourceRequest)

Request message for updating a data source instance.

### [WeekDayOfMonth](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.WeekDayOfMonth)

`WeekDayOfMonth` defines the week day of the month on which the backups will run. The message combines a `WeekOfMonth` and `DayOfWeek` to produce values like `FIRST`/`MONDAY` or `LAST`/`FRIDAY`.

### [WeekOfMonth](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.WeekDayOfMonth.WeekOfMonth)

`WeekOfMonth` enumerates possible weeks in the month, e.g. the first, third, or last week of the month.

### [WorkforceIdentityBasedManagementURI](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.WorkforceIdentityBasedManagementURI)

ManagementURI depending on the Workforce Identity i.e. either 1p or 3p.

### [WorkforceIdentityBasedOAuth2ClientID](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.WorkforceIdentityBasedOAuth2ClientID)

OAuth Client ID depending on the Workforce Identity i.e. either 1p or 3p,

### [BackupDRAsyncClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient)

The BackupDR Service

### [BackupDRClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient)

The BackupDR Service

### [FetchBackupPlanAssociationsForResourceTypeAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager)

A pager for iterating through `fetch_backup_plan_associations_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupPlanAssociationsForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__aiter__` method will make additional `FetchBackupPlanAssociationsForResourceType` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupPlanAssociationsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchBackupPlanAssociationsForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager)

A pager for iterating through `fetch_backup_plan_associations_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupPlanAssociationsForResourceTypeResponse) object, and provides an `__iter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__iter__` method will make additional `FetchBackupPlanAssociationsForResourceType` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupPlanAssociationsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchBackupsForResourceTypeAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager)

A pager for iterating through `fetch_backups_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupsForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `FetchBackupsForResourceType` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchBackupsForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypePager)

A pager for iterating through `fetch_backups_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupsForResourceTypeResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `FetchBackupsForResourceType` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchDataSourceReferencesForResourceTypeAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager)

A pager for iterating through `fetch_data_source_references_for_resource_type` requests.

This class thinly wraps an initial [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchDataSourceReferencesForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__aiter__` method will make additional `FetchDataSourceReferencesForResourceType` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchDataSourceReferencesForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchDataSourceReferencesForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager)

A pager for iterating through `fetch_data_source_references_for_resource_type` requests.

This class thinly wraps an initial [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchDataSourceReferencesForResourceTypeResponse) object, and provides an `__iter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__iter__` method will make additional `FetchDataSourceReferencesForResourceType` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchDataSourceReferencesForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchUsableBackupVaultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager)

A pager for iterating through `fetch_usable_backup_vaults` requests.

This class thinly wraps an initial [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchUsableBackupVaultsResponse) object, and provides an `__aiter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__aiter__` method will make additional `FetchUsableBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchUsableBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchUsableBackupVaultsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsPager)

A pager for iterating through `fetch_usable_backup_vaults` requests.

This class thinly wraps an initial [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchUsableBackupVaultsResponse) object, and provides an `__iter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__iter__` method will make additional `FetchUsableBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchUsableBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAppliedAutoProtectionPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesAsyncPager)

A pager for iterating through `list_applied_auto_protection_policies` requests.

This class thinly wraps an initial [ListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAppliedAutoProtectionPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `applied_auto_protection_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListAppliedAutoProtectionPolicies` requests and continue to iterate through the `applied_auto_protection_policies` field on the corresponding responses.

All the usual [ListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAppliedAutoProtectionPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAppliedAutoProtectionPoliciesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesPager)

A pager for iterating through `list_applied_auto_protection_policies` requests.

This class thinly wraps an initial [ListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAppliedAutoProtectionPoliciesResponse) object, and provides an `__iter__` method to iterate through its `applied_auto_protection_policies` field.

If there are more pages, the `__iter__` method will make additional `ListAppliedAutoProtectionPolicies` requests and continue to iterate through the `applied_auto_protection_policies` field on the corresponding responses.

All the usual [ListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAppliedAutoProtectionPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutoProtectionPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesAsyncPager)

A pager for iterating through `list_auto_protection_policies` requests.

This class thinly wraps an initial [ListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `auto_protection_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListAutoProtectionPolicies` requests and continue to iterate through the `auto_protection_policies` field on the corresponding responses.

All the usual [ListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutoProtectionPoliciesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesPager)

A pager for iterating through `list_auto_protection_policies` requests.

This class thinly wraps an initial [ListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPoliciesResponse) object, and provides an `__iter__` method to iterate through its `auto_protection_policies` field.

If there are more pages, the `__iter__` method will make additional `ListAutoProtectionPolicies` requests and continue to iterate through the `auto_protection_policies` field on the corresponding responses.

All the usual [ListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutoProtectionPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsAsyncPager)

A pager for iterating through `list_auto_protection_policy_bindings` requests.

This class thinly wraps an initial [ListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `auto_protection_policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `ListAutoProtectionPolicyBindings` requests and continue to iterate through the `auto_protection_policy_bindings` field on the corresponding responses.

All the usual [ListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutoProtectionPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsPager)

A pager for iterating through `list_auto_protection_policy_bindings` requests.

This class thinly wraps an initial [ListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `auto_protection_policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `ListAutoProtectionPolicyBindings` requests and continue to iterate through the `auto_protection_policy_bindings` field on the corresponding responses.

All the usual [ListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanAssociationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager)

A pager for iterating through `list_backup_plan_associations` requests.

This class thinly wraps an initial [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanAssociationsResponse) object, and provides an `__aiter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPlanAssociations` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanAssociationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanAssociationsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsPager)

A pager for iterating through `list_backup_plan_associations` requests.

This class thinly wraps an initial [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanAssociationsResponse) object, and provides an `__iter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPlanAssociations` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanAssociationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager)

A pager for iterating through `list_backup_plan_revisions` requests.

This class thinly wraps an initial [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanRevisionsResponse) object, and provides an `__aiter__` method to iterate through its `backup_plan_revisions` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPlanRevisions` requests and continue to iterate through the `backup_plan_revisions` field on the corresponding responses.

All the usual [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanRevisionsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsPager)

A pager for iterating through `list_backup_plan_revisions` requests.

This class thinly wraps an initial [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanRevisionsResponse) object, and provides an `__iter__` method to iterate through its `backup_plan_revisions` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPlanRevisions` requests and continue to iterate through the `backup_plan_revisions` field on the corresponding responses.

All the usual [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlansAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansAsyncPager)

A pager for iterating through `list_backup_plans` requests.

This class thinly wraps an initial [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlansResponse) object, and provides an `__aiter__` method to iterate through its `backup_plans` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPlans` requests and continue to iterate through the `backup_plans` field on the corresponding responses.

All the usual [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlansResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlansPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansPager)

A pager for iterating through `list_backup_plans` requests.

This class thinly wraps an initial [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlansResponse) object, and provides an `__iter__` method to iterate through its `backup_plans` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPlans` requests and continue to iterate through the `backup_plans` field on the corresponding responses.

All the usual [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlansResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupVaultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsAsyncPager)

A pager for iterating through `list_backup_vaults` requests.

This class thinly wraps an initial [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupVaultsResponse) object, and provides an `__aiter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupVaultsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsPager)

A pager for iterating through `list_backup_vaults` requests.

This class thinly wraps an initial [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupVaultsResponse) object, and provides an `__iter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__iter__` method will make additional `ListBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsAsyncPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupsResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupsResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBindingMatchingResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesAsyncPager)

A pager for iterating through `list_binding_matching_resources` requests.

This class thinly wraps an initial [ListBindingMatchingResourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBindingMatchingResourcesResponse) object, and provides an `__aiter__` method to iterate through its `matching_resources` field.

If there are more pages, the `__aiter__` method will make additional `ListBindingMatchingResources` requests and continue to iterate through the `matching_resources` field on the corresponding responses.

All the usual [ListBindingMatchingResourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBindingMatchingResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBindingMatchingResourcesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesPager)

A pager for iterating through `list_binding_matching_resources` requests.

This class thinly wraps an initial [ListBindingMatchingResourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBindingMatchingResourcesResponse) object, and provides an `__iter__` method to iterate through its `matching_resources` field.

If there are more pages, the `__iter__` method will make additional `ListBindingMatchingResources` requests and continue to iterate through the `matching_resources` field on the corresponding responses.

All the usual [ListBindingMatchingResourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBindingMatchingResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourceReferencesAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager)

A pager for iterating through `list_data_source_references` requests.

This class thinly wraps an initial [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourceReferencesResponse) object, and provides an `__aiter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__aiter__` method will make additional `ListDataSourceReferences` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourceReferencesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourceReferencesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesPager)

A pager for iterating through `list_data_source_references` requests.

This class thinly wraps an initial [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourceReferencesResponse) object, and provides an `__iter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__iter__` method will make additional `ListDataSourceReferences` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourceReferencesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesAsyncPager)

A pager for iterating through `list_data_sources` requests.

This class thinly wraps an initial [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourcesResponse) object, and provides an `__aiter__` method to iterate through its `data_sources` field.

If there are more pages, the `__aiter__` method will make additional `ListDataSources` requests and continue to iterate through the `data_sources` field on the corresponding responses.

All the usual [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourcesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesPager)

A pager for iterating through `list_data_sources` requests.

This class thinly wraps an initial [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourcesResponse) object, and provides an `__iter__` method to iterate through its `data_sources` field.

If there are more pages, the `__iter__` method will make additional `ListDataSources` requests and continue to iterate through the `data_sources` field on the corresponding responses.

All the usual [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListManagementServersAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersAsyncPager)

A pager for iterating through `list_management_servers` requests.

This class thinly wraps an initial [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListManagementServersResponse) object, and provides an `__aiter__` method to iterate through its `management_servers` field.

If there are more pages, the `__aiter__` method will make additional `ListManagementServers` requests and continue to iterate through the `management_servers` field on the corresponding responses.

All the usual [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListManagementServersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListManagementServersPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersPager)

A pager for iterating through `list_management_servers` requests.

This class thinly wraps an initial [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListManagementServersResponse) object, and provides an `__iter__` method to iterate through its `management_servers` field.

If there are more pages, the `__iter__` method will make additional `ListManagementServers` requests and continue to iterate through the `management_servers` field on the corresponding responses.

All the usual [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListManagementServersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [BackupDrProtectionSummaryAsyncClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient)

The Protection Summary service.

### [BackupDrProtectionSummaryClient](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient)

The Protection Summary service.

### [ListResourceBackupConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager)

A pager for iterating through `list_resource_backup_configs` requests.

This class thinly wraps an initial [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListResourceBackupConfigsResponse) object, and provides an `__aiter__` method to iterate through its `resource_backup_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListResourceBackupConfigs` requests and continue to iterate through the `resource_backup_configs` field on the corresponding responses.

All the usual [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListResourceBackupConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceBackupConfigsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager)

A pager for iterating through `list_resource_backup_configs` requests.

This class thinly wraps an initial [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListResourceBackupConfigsResponse) object, and provides an `__iter__` method to iterate through its `resource_backup_configs` field.

If there are more pages, the `__iter__` method will make additional `ListResourceBackupConfigs` requests and continue to iterate through the `resource_backup_configs` field on the corresponding responses.

All the usual [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListResourceBackupConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AcceleratorConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AcceleratorConfig)

A specification of the type and number of accelerator cards attached to the instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AccessConfig)

An access configuration attached to an instance's network interface. Only one access config per instance is supported.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AccessConfig.AccessType)

The type of configuration.

### [NetworkTier](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AccessConfig.NetworkTier)

Network tier property used by addresses, instances and forwarding rules.

### [AdvancedMachineFeatures](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AdvancedMachineFeatures)

Specifies options for controlling advanced machine features.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AliasIpRange](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AliasIpRange)

An alias IP range attached to an instance's network interface.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AllocationAffinity](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AllocationAffinity)

Specifies the reservations that this instance can consume from.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AllocationAffinity.Type)

Indicates whether to consume from a reservation or not.

### [AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AlloyDBClusterBackupPlanAssociationProperties)

Properties for an AlloyDB cluster backup plan association.

### [AlloyDBClusterDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AlloyDBClusterDataSourceProperties)

AlloyDBClusterDataSourceProperties represents the properties of a AlloyDB cluster resource that are stored in the DataSource. .

### [AlloyDBClusterDataSourceReferenceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AlloyDBClusterDataSourceReferenceProperties)

AlloyDBClusterDataSourceReferenceProperties represents the properties of an AlloyDB cluster that are stored in the DataSourceReference.

### [AlloyDbClusterBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AlloyDbClusterBackupProperties)

AlloyDbClusterBackupProperties represents AlloyDB cluster backup properties. .

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AlloyDbPitrWindow](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AlloyDbPitrWindow)

Point in time recovery window for an AlloyDB cluster.

### [AppliedAutoProtectionPolicy](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AppliedAutoProtectionPolicy)

AppliedAutoProtectionPolicy is a read-only view of AutoProtectionPolicy and AutoProtectionPolicyBinding resources that apply to a given workload project.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AppliedAutoProtectionPolicy.State)

Represents the various states an applied auto protection policy can be in.

### [AttachedDisk](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AttachedDisk)

An instance-attached disk resource.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DiskInterface](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AttachedDisk.DiskInterface)

List of the Disk Interfaces.

### [DiskMode](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AttachedDisk.DiskMode)

List of the Disk Modes.

### [DiskSavedState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AttachedDisk.DiskSavedState)

List of the states of the Disk.

### [DiskType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AttachedDisk.DiskType)

List of the Disk Types.

### [InitializeParams](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AttachedDisk.InitializeParams)

Specifies the parameters to initialize this disk.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AutoProtectionDetails](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AutoProtectionDetails)

AutoProtectionDetails contains the protection details of a resource from the current binding's perspective.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AutoProtectionDetails.State)

Enum for protection state of the resource.

### [AutoProtectionPolicy](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AutoProtectionPolicy)

An AutoprotectionPolicy is a policy resource designed to automate backup management, moving from manual per-resource protection to a bulk approach. The policy dynamically discovers and applies a specified backup plan to all eligible resources that match its defined scope and criteria.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AutoProtectionPolicy.State)

The state of an AutoprotectionPolicy.

### [AutoProtectionPolicyBinding](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AutoProtectionPolicyBinding)

An AutoprotectionPolicyBinding (APPA) acts as the bridge between an AutoprotectionPolicy and the scope (Project, Folder, or Organization) where the policy should be applied.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AutoProtectionPolicyBinding.State)

The state of an AutoProtectionPolicyBinding.

### [Backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup)

Message describing a Backup object.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup.BackupType)

Type of the backup, scheduled or ondemand.

### [GCPBackupPlanInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup.GCPBackupPlanInfo)

GCPBackupPlanInfo captures the plan configuration details of Google Cloud resources at the time of backup.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup.State)

Holds the state of the backup resource.

### [BackupApplianceBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupApplianceBackupConfig)

BackupApplianceBackupConfig captures the backup configuration for applications that are protected by Backup Appliances.

### [BackupApplianceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupApplianceBackupProperties)

BackupApplianceBackupProperties represents BackupDR backup appliance's properties.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupApplianceLockInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupApplianceLockInfo)

BackupApplianceLockInfo contains metadata about the backupappliance that created the lock.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupConfigDetails](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupConfigDetails)

BackupConfigDetails has information about how the resource is configured for backups and about the most recent backup taken for this configuration.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupConfigDetails.State)

The state tells whether the backup config is active or not.

### [Type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupConfigDetails.Type)

Type of the backup configuration. This enum may receive new values in the future.

### [BackupConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupConfigInfo)

BackupConfigInfo has information about how the resource is configured for Backup and about the most recent backup to this vault.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LastBackupState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupConfigInfo.LastBackupState)

LastBackupstate tracks whether the last backup was not yet started, successful, failed, or could not be run because of the lack of permissions.

### [BackupConfigState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupConfigState)

Backup configuration state. Is the resource configured for backup?

### [BackupDrPlanConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupDrPlanConfig)

BackupDrPlanConfig has additional information about Google Cloud Backup and DR's Plan backup configuration.

### [BackupDrPlanRule](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupDrPlanRule)

BackupDrPlanRule has rule specific information of the backup plan resource.

### [BackupDrTemplateConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupDrTemplateConfig)

Provides additional information about Google Cloud Backup and DR's Template backup configuration.

### [BackupGcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupGcpResource)

Minimum details to identify a Google Cloud resource for a backup.

### [BackupLocation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupLocation)

BackupLocation represents a cloud location where a backup can be stored.

### [Type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupLocation.Type)

The type of the location.

### [BackupLock](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupLock)

BackupLock represents a single lock on a Backup resource. An unexpired lock on a Backup prevents the Backup from being deleted.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupPlan)

A `BackupPlan` specifies some common fields, such as `description` as well as one or more `BackupRule` messages. Each `BackupRule` has a retention policy and defines a schedule by which the system is to perform backup workloads.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupPlan.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupPlan.State)

`State` enumerates the possible states for a `BackupPlan`.

### [BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupPlanAssociation)

A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupPlanAssociation.State)

Enum for State of BackupPlan Association

### [BackupPlanDetail](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupPlanDetail)

BackupPlanDetail defines configuration of protection.

### [BackupPlanRevision](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupPlanRevision)

`BackupPlanRevision` represents a snapshot of a `BackupPlan` at a point in time.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupPlanRevision.State)

The state of the `BackupPlanRevision`.

### [BackupRule](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupRule)

`BackupRule` binds the backup schedule to a retention policy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupVault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault)

Message describing a BackupVault object.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessRestriction](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.AccessRestriction)

Holds the access restriction for the backup vault.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.AnnotationsEntry)

The abstract base class for a message.

### [BackupRetentionInheritance](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.BackupRetentionInheritance)

How a backup's enforced retention end time is inherited.
    
    
        This is the default behavior.
    MATCH_BACKUP_EXPIRE_TIME (2):
        The enforced retention end time of a backup
        will always match the expire time of the backup.
    
        If this is set, the backup's enforced retention
        end time will be set to match the expire time
        during creation of the backup. When updating,
        the ERET and expire time must be updated
        together and have the same value. Invalid update
        requests will be rejected by the server.
    

### [EncryptionConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.EncryptionConfig)

Message describing the EncryptionConfig of backup vault. This determines how data within the vault is encrypted at rest.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.State)

Holds the state of the backup vault resource.

### [BackupVaultView](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVaultView)

BackupVaultView contains enum options for Partial and Full view.

### [BackupView](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupView)

BackupView contains enum options for Partial and Full view.

### [BackupWindow](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupWindow)

`BackupWindow` defines a window of the day during which backup jobs will run.

### [BindingEvaluationSummary](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BindingEvaluationSummary)

BindingEvaluationSummary contains the summary of the last run of job that applies policy to matching resources for a given binding.

### [BindingMatchingResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BindingMatchingResource)

BindingMatchingResource contains the details of a resource that matches the criteria of a binding.

### [BindingSummary](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BindingSummary)

BindingSummary contains count of different containers covered through this policy.

### [CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CloudSqlInstanceBackupPlanAssociationProperties)

Cloud SQL instance's BPA properties.

### [CloudSqlInstanceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CloudSqlInstanceBackupProperties)

CloudSqlInstanceBackupProperties represents Cloud SQL Instance Backup properties.

### [CloudSqlInstanceDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CloudSqlInstanceDataSourceProperties)

CloudSqlInstanceDataSourceProperties represents the properties of a Cloud SQL resource that are stored in the DataSource.

### [CloudSqlInstanceDataSourceReferenceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CloudSqlInstanceDataSourceReferenceProperties)

CloudSqlInstanceDataSourceReferenceProperties represents the properties of a Cloud SQL resource that are stored in the DataSourceReference.

### [CloudSqlInstanceInitializationConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CloudSqlInstanceInitializationConfig)

CloudSqlInstanceInitializationConfig contains the configuration for initializing a Cloud SQL instance.

### [Edition](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CloudSqlInstanceInitializationConfig.Edition)

The edition of the Cloud SQL instance. For details, see <https://cloud.google.com/sql/docs/editions-intro>.

### [ComputeInstanceBackupPlanProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ComputeInstanceBackupPlanProperties)

Properties for a compute instance backup plan.

### [ComputeInstanceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ComputeInstanceBackupProperties)

ComputeInstanceBackupProperties represents Compute Engine instance backup properties.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ComputeInstanceBackupProperties.LabelsEntry)

The abstract base class for a message.

### [ComputeInstanceDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ComputeInstanceDataSourceProperties)

ComputeInstanceDataSourceProperties represents the properties of a ComputeEngine resource that are stored in the DataSource.

### [ComputeInstanceRestoreProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ComputeInstanceRestoreProperties)

ComputeInstanceRestoreProperties represents Compute Engine instance properties to be overridden during restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InstancePrivateIpv6GoogleAccess](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess)

The private IPv6 google access type for the VMs.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ComputeInstanceRestoreProperties.LabelsEntry)

The abstract base class for a message.

### [ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ComputeInstanceTargetEnvironment)

ComputeInstanceTargetEnvironment represents Compute Engine target environment to be used during restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConfidentialInstanceConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ConfidentialInstanceConfig)

A set of Confidential Instance options.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CreateAutoProtectionPolicyBindingRequest)

Request message for creating an AutoProtectionPolicyBinding.

### [CreateAutoProtectionPolicyRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CreateAutoProtectionPolicyRequest)

Request message for creating an AutoProtectionPolicy.

### [CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CreateBackupPlanAssociationRequest)

Request message for creating a backup plan.

### [CreateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CreateBackupPlanRequest)

The request message for creating a `BackupPlan`.

### [CreateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CreateBackupVaultRequest)

Message for creating a BackupVault.

### [CreateManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CreateManagementServerRequest)

Request message for creating a management server instance.

### [Criteria](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Criteria)

Criteria specifies a set of criteria for matching resources.

### [CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CustomerEncryptionKey)

A customer-supplied encryption key.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DataSource)

Message describing a DataSource object. Datasource object used to represent Datasource details for both admin and basic view.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DataSource.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DataSource.State)

Holds the state of the data source resource.

### [DataSourceBackupApplianceApplication](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DataSourceBackupApplianceApplication)

BackupApplianceApplication describes a Source Resource when it is an application backed up by a BackupAppliance.

### [DataSourceBackupConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DataSourceBackupConfigInfo)

Information of backup configuration on the DataSource.

### [DataSourceGcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DataSourceGcpResource)

DataSourceGcpResource is used for protected resources that are Google Cloud Resources. This name is easeier to understand than GcpResourceDataSource or GcpDataSourceResource

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSourceGcpResourceInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DataSourceGcpResourceInfo)

The Google Cloud resource that the DataSource is associated with.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSourceReference](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DataSourceReference)

DataSourceReference is a reference to a DataSource resource.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeleteAutoProtectionPolicyRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DeleteAutoProtectionPolicyRequest)

Request message for deleting an AutoProtectionPolicy.

### [DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DeleteBackupPlanAssociationRequest)

Request message for deleting a backup plan association.

### [DeleteBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DeleteBackupPlanRequest)

The request message for deleting a `BackupPlan`.

### [DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DeleteBackupRequest)

Message for deleting a Backup.

### [DeleteBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DeleteBackupVaultRequest)

Message for deleting a BackupVault.

### [DeleteManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DeleteManagementServerRequest)

Request message for deleting a management server instance.

### [DiskBackupPlanProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskBackupPlanProperties)

Properties for a disk backup plan.

### [DiskBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskBackupProperties)

DiskBackupProperties represents the properties of a Disk backup.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Architecture](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskBackupProperties.Architecture)

Architecture of the source disk.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskBackupProperties.LabelsEntry)

The abstract base class for a message.

### [DiskDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskDataSourceProperties)

DiskDataSourceProperties represents the properties of a Disk resource that are stored in the DataSource. .

### [DiskRestoreProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskRestoreProperties)

DiskRestoreProperties represents the properties of a Disk restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessMode](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskRestoreProperties.AccessMode)

The supported access modes of the disk.

### [Architecture](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskRestoreProperties.Architecture)

Architecture of the source disk.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskRestoreProperties.LabelsEntry)

The abstract base class for a message.

### [ResourceManagerTagsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskRestoreProperties.ResourceManagerTagsEntry)

The abstract base class for a message.

### [DiskTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskTargetEnvironment)

DiskTargetEnvironment represents the target environment for the disk.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DisplayDevice](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DisplayDevice)

A set of Display Device options

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Entry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Entry)

A key/value pair to be used for storing metadata.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupPlanAssociationsForResourceTypeRequest)

Request for the FetchBackupPlanAssociationsForResourceType method.

### [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupPlanAssociationsForResourceTypeResponse)

Response for the FetchBackupPlanAssociationsForResourceType method.

### [FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupsForResourceTypeRequest)

Request for the FetchBackupsForResourceType method.

### [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchBackupsForResourceTypeResponse)

Response for the FetchBackupsForResourceType method.

### [FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchDataSourceReferencesForResourceTypeRequest)

Request for the FetchDataSourceReferencesForResourceType method.

### [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchDataSourceReferencesForResourceTypeResponse)

Response for the FetchDataSourceReferencesForResourceType method.

### [FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchUsableBackupVaultsRequest)

Request message for fetching usable BackupVaults.

### [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.FetchUsableBackupVaultsResponse)

Response message for fetching usable BackupVaults.

### [GcpBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GcpBackupConfig)

GcpBackupConfig captures the Backup configuration details for Google Cloud resources. All Google Cloud resources regardless of type are protected with backup plan associations.

### [GcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GcpResource)

Minimum details to identify a Google Cloud resource

### [GetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetAutoProtectionPolicyBindingRequest)

Request message for getting an AutoProtectionPolicyBinding.

### [GetAutoProtectionPolicyRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetAutoProtectionPolicyRequest)

Request message for getting an AutoProtectionPolicy.

### [GetBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetBackupPlanAssociationRequest)

Request message for getting a BackupPlanAssociation resource.

### [GetBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetBackupPlanRequest)

The request message for getting a `BackupPlan`.

### [GetBackupPlanRevisionRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetBackupPlanRevisionRequest)

The request message for getting a `BackupPlanRevision`.

### [GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetBackupRequest)

Request message for getting a Backup.

### [GetBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetBackupVaultRequest)

Request message for getting a BackupVault.

### [GetBindingMatchingResourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetBindingMatchingResourceRequest)

Request message for getting a BindingMatchingResource.

### [GetDataSourceReferenceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetDataSourceReferenceRequest)

Request for the GetDataSourceReference method.

### [GetDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetDataSourceRequest)

Request message for getting a DataSource instance.

### [GetManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GetManagementServerRequest)

Request message for getting a management server instance.

### [GuestOsFeature](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GuestOsFeature)

Feature type of the Guest OS.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FeatureType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.GuestOsFeature.FeatureType)

List of the Feature Types.

### [InitializeServiceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.InitializeServiceRequest)

Request message for initializing the service.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InitializeServiceResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.InitializeServiceResponse)

Response message for initializing the service.

### [InitiateDeleteAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.InitiateDeleteAutoProtectionPolicyBindingRequest)

Request message for initiating delete of an AutoProtectionPolicyBinding.

### [InstanceParams](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.InstanceParams)

Additional instance params.

### [ResourceManagerTagsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.InstanceParams.ResourceManagerTagsEntry)

The abstract base class for a message.

### [KeyRevocationActionType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.KeyRevocationActionType)

Specifies whether the virtual machine instance will be shut down on key revocation. It is currently used in instance, instance properties and GMI protos

### [KeyValuePair](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.KeyValuePair)

KeyValuePair defines a key-value pair for matching resource labels.

### [ListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAppliedAutoProtectionPoliciesRequest)

Request message for listing AppliedAutoProtectionPolicies.

### [ListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAppliedAutoProtectionPoliciesResponse)

Response message for ListAppliedAutoProtectionPolicies.

### [ListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPoliciesRequest)

Request message for ListAutoProtectionPolicies.

### [ListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPoliciesResponse)

Response message for ListAutoProtectionPolicies.

### [ListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPolicyBindingsRequest)

Request message for ListAutoProtectionPolicyBindings.

### [ListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListAutoProtectionPolicyBindingsResponse)

Response message for ListAutoProtectionPolicyBindings.

### [ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanAssociationsRequest)

Request message for List BackupPlanAssociation

### [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanAssociationsResponse)

Response message for List BackupPlanAssociation

### [ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanRevisionsRequest)

The request message for getting a list of `BackupPlanRevision`.

### [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlanRevisionsResponse)

The response message for getting a list of `BackupPlanRevision`.

### [ListBackupPlansRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlansRequest)

The request message for getting a list `BackupPlan`.

### [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupPlansResponse)

The response message for getting a list of `BackupPlan`.

### [ListBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupVaultsRequest)

Request message for listing backupvault stores.

### [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupVaultsResponse)

Response message for listing BackupVaults.

### [ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupsRequest)

Request message for listing Backups.

### [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBackupsResponse)

Response message for listing Backups.

### [ListBindingMatchingResourcesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBindingMatchingResourcesRequest)

Request message for List BindingMatchingResources.

### [ListBindingMatchingResourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListBindingMatchingResourcesResponse)

The response message for getting a list of `BindingMatchingResources`.

### [ListDataSourceReferencesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourceReferencesRequest)

Request for the ListDataSourceReferences method.

### [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourceReferencesResponse)

Response for the ListDataSourceReferences method.

### [ListDataSourcesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourcesRequest)

Request message for listing DataSources.

### [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListDataSourcesResponse)

Response message for listing DataSources.

### [ListManagementServersRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListManagementServersRequest)

Request message for listing management servers.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListManagementServersResponse)

Response message for listing management servers.

### [ListResourceBackupConfigsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListResourceBackupConfigsRequest)

Request for ListResourceBackupConfigs.

### [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ListResourceBackupConfigsResponse)

Response for ListResourceBackupConfigs.

### [ManagementServer](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ManagementServer)

ManagementServer describes a single BackupDR ManagementServer instance.

### [InstanceState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ManagementServer.InstanceState)

State of Management server instance.

### [InstanceType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ManagementServer.InstanceType)

Type of backup service resource.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ManagementServer.LabelsEntry)

The abstract base class for a message.

### [ManagementURI](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ManagementURI)

ManagementURI for the Management Server resource.

### [MatchingCondition](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.MatchingCondition)

MatchingCondition specifies a set of conditions for matching resources.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Metadata](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Metadata)

A metadata key/value entry.

### [NetworkConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.NetworkConfig)

Network configuration for ManagementServer instance.

### [PeeringMode](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.NetworkConfig.PeeringMode)

VPC peering modes supported by Google Cloud Backup and DR.

### [NetworkInterface](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.NetworkInterface)

A network interface resource attached to an instance. s

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Ipv6AccessType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.NetworkInterface.Ipv6AccessType)

IPv6 access type for this network interface.

### [NicType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.NetworkInterface.NicType)

Nic type for this network interface.

### [StackType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.NetworkInterface.StackType)

Stack type for this network interface.

### [NetworkPerformanceConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.NetworkPerformanceConfig)

Network performance configuration.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Tier](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.NetworkPerformanceConfig.Tier)

Network performance tier.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [AdditionalInfoEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.OperationMetadata.AdditionalInfoEntry)

The abstract base class for a message.

### [PitrSettings](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.PitrSettings)

Point in time recovery settings of the backup configuration resource.

### [PolicyEvaluationSummary](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.PolicyEvaluationSummary)

PolicyEvaluationSummary contains the summary of the last run of job that applies policy to matching resources.

### [RegionDiskTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.RegionDiskTargetEnvironment)

RegionDiskTargetEnvironment represents the target environment for the disk.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ResourceBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ResourceBackupConfig)

ResourceBackupConfig represents a resource along with its backup configurations.

### [ResourceType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ResourceBackupConfig.ResourceType)

The type of the cloud resource.

### [TargetResourceLabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ResourceBackupConfig.TargetResourceLabelsEntry)

The abstract base class for a message.

### [RestoreBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.RestoreBackupRequest)

Request message for restoring from a Backup.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreBackupResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.RestoreBackupResponse)

Response message for restoring from a Backup.

### [RestoreDiskFromInstanceOptions](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.RestoreDiskFromInstanceOptions)

Options for creating a disk from a source Compute Instance backup.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RuleConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.RuleConfigInfo)

Message for rules config info.

### [LastBackupState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.RuleConfigInfo.LastBackupState)

Enum for LastBackupState

### [Scheduling](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Scheduling)

Sets the scheduling options for an Instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InstanceTerminationAction](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Scheduling.InstanceTerminationAction)

Defines the supported termination actions for an instance.

### [NodeAffinity](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Scheduling.NodeAffinity)

Node Affinity: the configuration of desired nodes onto which this Instance could be scheduled.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Operator](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Scheduling.NodeAffinity.Operator)

Defines the type of node selections.

### [OnHostMaintenance](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Scheduling.OnHostMaintenance)

Defines the maintenance behavior for this instance=

### [ProvisioningModel](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Scheduling.ProvisioningModel)

Defines the provisioning model for an instance.

### [SchedulingDuration](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.SchedulingDuration)

A SchedulingDuration represents a fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". Range is approximately 10,000 years.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceAccount](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ServiceAccount)

A service account.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceLockInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ServiceLockInfo)

ServiceLockInfo represents the details of a lock taken by the service on a Backup resource.

### [StandardSchedule](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.StandardSchedule)

`StandardSchedule` defines a schedule that run within the confines of a defined window of days. We can define recurrence type for schedule as HOURLY, DAILY, WEEKLY, MONTHLY or YEARLY.

### [RecurrenceType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.StandardSchedule.RecurrenceType)

`RecurrenceTypes` enumerates the applicable periodicity for the schedule.

### [Tags](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Tags)

A set of instance tags.

### [TargetResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.TargetResource)

Details of the target resource created/modified as part of restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TriggerBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.TriggerBackupRequest)

Request message for triggering a backup.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.TriggerBackupRequest.LabelsEntry)

The abstract base class for a message.

### [UpdateAutoProtectionPolicyRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.UpdateAutoProtectionPolicyRequest)

Request message for updating an AutoProtectionPolicy.

### [UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.UpdateBackupPlanAssociationRequest)

Request message for updating a backup plan association.

### [UpdateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.UpdateBackupPlanRequest)

Request message for updating a backup plan.

### [UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.UpdateBackupRequest)

Request message for updating a Backup.

### [UpdateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.UpdateBackupVaultRequest)

Request message for updating a BackupVault.

### [UpdateDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.UpdateDataSourceRequest)

Request message for updating a data source instance.

### [WeekDayOfMonth](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.WeekDayOfMonth)

`WeekDayOfMonth` defines the week day of the month on which the backups will run. The message combines a `WeekOfMonth` and `DayOfWeek` to produce values like `FIRST`/`MONDAY` or `LAST`/`FRIDAY`.

### [WeekOfMonth](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.WeekDayOfMonth.WeekOfMonth)

`WeekOfMonth` enumerates possible weeks in the month, e.g. the first, third, or last week of the month.

### [WorkforceIdentityBasedManagementURI](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.WorkforceIdentityBasedManagementURI)

ManagementURI depending on the Workforce Identity i.e. either 1p or 3p.

### [WorkforceIdentityBasedOAuth2ClientID](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.WorkforceIdentityBasedOAuth2ClientID)

OAuth Client ID depending on the Workforce Identity i.e. either 1p or 3p,

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers)

API documentation for `backupdr_v1.services.backup_dr.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers)

API documentation for `backupdr_v1.services.backup_dr_protection_summary.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers)

API documentation for `backupdr_v1beta.services.backup_dr.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers)

API documentation for `backupdr_v1beta.services.backup_dr_protection_summary.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
