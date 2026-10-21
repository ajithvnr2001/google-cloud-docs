---
url: https://docs.cloud.google.com/compute/docs/logging/usage-export/
title: Viewing usage reports \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:50:15.663406+00:00
---

# Viewing usage reports  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/logging/usage-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Viewing usage reports Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine lets you export detailed reports of your Compute Engine usage to a [Cloud Storage](https://docs.cloud.google.com/storage) bucket using the usage export feature.

**Caution:** The usage export feature is deprecated and was discontinued on March 30, 2026. We recommend using [Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) as an alternative. For more information about this deprecation, including migration examples, see [Compute Engine usage report deprecation](https://docs.cloud.google.com/compute/docs/deprecations/usage-export).

Usage reports provide information about the lifetime of your resources. For example, you can see how many VM instances in your project are running an `n2-standard-4` machine type and how long each instance has been running. You can also review the storage space of a persistent disk, and information about other Compute Engine features.

Usage reports don't provide billing or activity information, such as information about API requests. For billing information, see [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). For a record of administrative activities and accesses within your Google Cloud resources, see [Audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * If you're using a local shell, then create local authentication credentials for your user account: 
        
        gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 




## Overview

When you enable usage reports, Compute Engine delivers two types of reports to the Cloud Storage bucket you specify:

  1. **Daily usage reports**

These reports are delivered daily and include usage data from the preceding day. Each report is a separate file that contains data from the last period. Data in these reports are immutable, meaning that Compute Engine does not update or rewrite the log file if there are inaccuracies. Instead, the data is corrected in the next new report that is delivered to the bucket.

Daily usage reports have the following name format:
         
         <bucket>/<report _prefix_ ><numeric_project _id_ ><YYYYMMDD>.csv
          

  2. **Monthly rollup report**

A single monthly rollup report is delivered daily, which contains monthly usage data for that project up to, but not including, that day. The monthly usage report is overwritten each day with new data that reflects the monthly usage of resources up to that date. There is only one monthly usage data file per project, per month.

Monthly rollup reports have following name format:
         
         <bucket>/<report _prefix_ ><numeric_project _id_ ><YYYYMM>.csv
          

The daily and monthly report files look very similar, except for the difference in date format, where the monthly rollup reports are dated using the year and month (`YYYYMM`), and the daily usage reports are dated using the year, month, and date (`YYYYMMDD`).




All usage reports are delivered in [comma-separated values (CSV)](https://www.ietf.org/rfc/rfc4180.txt) format and usage report files are prefixed using `<report_prefix>`. The `<report_prefix>` is a customizable value chosen by the user. If you don't specify a report prefix, the prefix `usage_gce` is used by default. All times are given in Pacific time (PST).

## Prerequisites

Before you can start using Compute Engine usage export:

  * You must have already [created a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store usage logs.



## Setting up usage export

**Note:** You can no longer enable the usage export feature through the Google Cloud console or Google Cloud CLI. We recommend using [Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) instead of enabling usage export.

When you first enable the usage export feature, the first report is sent the following day, detailing the previous day's usage. Afterwards, you receive reports in 24 hour intervals.

When you enable this feature, you must define two properties:

  1. **The Cloud Storage[bucket](https://docs.cloud.google.com/storage/docs/buckets) where you would like your reports to be delivered.**

You can select any Cloud Storage bucket for which you are an owner, including buckets that are from different projects. This bucket must exist before you can start exporting reports and you must have owner access to the bucket. Cloud Storage charges for usage, so you should review [Cloud Storage pricing](https://cloud.google.com/storage/pricing) for information on how you might incur charges for the service.

Any user who has read access to the Cloud Storage bucket can view the usage reports in the bucket. Any user who has write access to the bucket can create, view, and modify existing files in the bucket. For more information, see the Access control section.

  2. **The report prefix for your files.**

You can specify the report prefix to use for your usage reports. Your usage reports then have filenames that contain this prefix. For example, specifying "my-cool-project-report" as your report prefix results in a filename similar to the format `my-cool-project-report_1234567890_20131230.csv`. If you don't specify a report prefix, the default prefix `usage_gce` is used.




After you decide on these two properties, you can enable the usage export feature in the following ways:

###  Python 

To enable usage exports, use the `set_usage_export_bucket()` method in the `Projects` collection. The following example uses the Cloud Client Libraries for Python:
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def set_usage_export_bucket(
        project_id: str, bucket_name: str, report_name_prefix: str = ""
    ) -> None:
        """
        Set Compute Engine usage export bucket for the Cloud project.
        This sample presents how to interpret the default value for the
        report name prefix parameter.
    
        Args:
            project_id: project ID or project number of the project to update.
            bucket_name: Google Cloud Storage bucket used to store Compute Engine
                usage reports. An existing Google Cloud Storage bucket is required.
            report_name_prefix: Prefix of the usage report name which defaults to an empty string
                to showcase default values behaviour.
        """
        usage_export_location = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[UsageExportLocation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UsageExportLocation.html)()
        usage_export_location.bucket_name = bucket_name
        usage_export_location.report_name_prefix = report_name_prefix
    
        if not report_name_prefix:
            # Sending an empty value for report_name_prefix results in the
            # next usage report being generated with the default prefix value
            # "usage_gce". (ref: https://cloud.google.com/compute/docs/reference/rest/v1/projects/setUsageExportBucket)
            print(
                "Setting report_name_prefix to empty value causes the report "
                "to have the default prefix of `usage_gce`."
            )
    
        projects_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.projects.ProjectsClient.html)()
        operation = projects_client.[set_usage_export_bucket](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.projects.ProjectsClient.html#google_cloud_compute_v1_services_projects_ProjectsClient_set_usage_export_bucket)(
            project=project_id, usage_export_location_resource=usage_export_location
        )
    
        wait_for_extended_operation(operation, "setting GCE usage bucket")
    
    

For more information, see the REST reference documentation for [`projects.setUsageExportBucket`](https://docs.cloud.google.com/compute/docs/reference/latest/projects/setUsageExportBucket)

## Downloading usage export reports

After you start receiving usage reports in your bucket, download your reports like you would download other objects from Cloud Storage. For more information, see [Download objects](https://docs.cloud.google.com/storage/docs/downloading-objects).

## Supported metrics

Daily usage reports provide usage information about the following resources:

  * Virtual machines
  * Persistent disks
  * Images
  * Snapshots
  * Static IP addresses
  * Load balancers
  * Reservations



Each resource is described using the following metrics:

Metric Name | Metric Properties  
---|---  
Report Date | 

  * Metric Type: string
  * Description: The date of the usage.
  * Example: 2019-08-15

  
MeasurementId | 

  * Metric Type: string
  * Description: The ID of the type of resource that is being measured.  
For example, `VmimageN2StandardCore_Uswest2` to represent an `n2-standard` [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) in `us-west2`. 
  * Example: `com.google.cloud/services/compute‑engine/VmimageN2StandardCore_Uswest2`
  * Example: `com.google.cloud/services/compute‑engine/VmimageN2StandardRam_Uswest2`

  
Quantity | 

  * Metric Type: integer
  * Description: The amount of usage for the specified date.
  * Example: 86400

  
Unit | 

  * Metric Type: string
  * Description: The unit type, such as count, seconds, or hours. 
  * Example: seconds

  
Resource URI | 

  * Metric Type: string
  * Description: The URI of the specified resource.
  * Example: `https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-n2-vm`

  
ResourceId | 

  * Metric Type: integer
  * Description: A numeric ID that identifies the specific resource. 
  * Example: 16557630484925648021

  
Location | 

  * Metric Type: string
  * Description: The location of the resource. Either a zone or region name, or `GLOBAL` for global resources. 
  * Example: `us-central1-a`

  
**Note:** If you are using the billing export feature, you can also match the `MeasurementId` fields to find the charges for a particular resource.

An example entry in the report would look like the following:

Report Date | MeasurementId | Quantity | Unit | Resource URI | Resource ID | Location  
---|---|---|---|---|---|---  
02/13/2019 |  `com.google.cloud/services/compute-engine/VmimageE2Standard_2` | 86400 | seconds |  `https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/my-instance` | 16557630484 | us-central1-a  
  
## Access control

When you enable the usage export feature for a Cloud Storage bucket, Compute Engine automatically adds itself to the bucket with write access in order to deliver usage reports. As long as Compute Engine has access to the bucket and the usage export feature is enabled, Compute Engine continues to export usage reports to the specified Cloud Storage bucket.

You can identify that Compute Engine has access to a bucket if you see the following identity added to the bucket IAM policy:
    
    
    cloud-cluster-analytics-export@google.com
    

Any user who is an owner of the project has full access to the Cloud Storage bucket. Other users, such as writers and readers, have different degrees of access to the bucket. To learn about IAM for a bucket, read [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

If you disable the usage export feature, Compute Engine automatically removes write access from Compute Engine to the bucket. If you modify the permissions on the `cloud-cluster-analytics-export@google.com` account and then disable the usage export feature, Compute Engine disables the usage export feature but doesn't remove the account from the project access list. You can remove the account manually.

## Checking if usage reports are enabled

You can check on a project's usage export settings by getting information about the project:
    
    
    gcloud compute project-info describe
    

Look for the `usageExportLocation` field:
    
    
    +-------------------------+----------------------------------------------------+
    | name                    | myproject                                          |
    | description             |                                                    |
    | creation-time           | 2019-10-18T16:31:52.308-07:00                      |
    | usage                   |                                                    |
    |   snapshots             | 1.0/1000.0                                         |
    |   networks              | 2.0/2.0                                            |
    |   firewalls             | 3.0/10.0                                           |
    |...                      |                                                    |
    | usageExportLocation     |                                                    |
    |   bucketName            | https://storage.googleapis.com/usage-export-sample |
    |   reportNamePrefix      |                                                    |
    +-------------------------+----------------------------------------------------+
    

## Disabling usage reports

When you disable usage reports, Compute Engine automatically removes write access for Compute Engine to your Cloud Storage bucket and stops sending new reports.

###  Python 

To disable usage exports, use the `set_usage_export_bucket()` method in the `Projects` collection with `usage_export_location_resource` set to `None`. The following example uses the Cloud Client Libraries for Python:
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def disable_usage_export(project_id: str) -> None:
        """
        Disable Compute Engine usage export bucket for the Cloud Project.
    
        Args:
            project_id: project ID or project number of the project to update.
        """
        projects_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.projects.ProjectsClient.html)()
    
        # Setting `usage_export_location_resource` to an
        # empty object will disable the usage report generation.
        operation = projects_client.[set_usage_export_bucket](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.projects.ProjectsClient.html#google_cloud_compute_v1_services_projects_ProjectsClient_set_usage_export_bucket)(
            project=project_id, usage_export_location_resource={}
        )
    
        wait_for_extended_operation(operation, "disabling GCE usage bucket")
    
    

## What's next

  * Turn on the [Export Cloud Billing data to BigQuery feature](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) to view your billing logs.
  * Track the activity in your project using [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).
  * Learn more about [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets).
  * Use the [pricing calculator](https://cloud.google.com/products/calculator) to get an estimated price.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
