---
url: https://docs.cloud.google.com/compute/docs/samples/compute-instances-verify-default-value/
title: Set and retrieve Compute Engine usage export bucket \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:05.149009+00:00
---

# Set and retrieve Compute Engine usage export bucket  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-instances-verify-default-value/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Set and retrieve Compute Engine usage export bucket Stay organized with collections  Save and categorize content based on your preferences. 

This sample shows you how to set and retrieve the Compute Engine usage export bucket for a project. The usage export bucket is a Google Cloud Storage bucket where Compute Engine usage reports are stored. The usage reports can be used for billing and cost management purposes.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
    
    
    
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
        usage_export_location = compute_v1.UsageExportLocation()
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
    
        projects_client = compute_v1.ProjectsClient()
        operation = projects_client.set_usage_export_bucket(
            project=project_id, usage_export_location_resource=usage_export_location
        )
    
        wait_for_extended_operation(operation, "setting GCE usage bucket")
    
    
    
    
    def get_usage_export_bucket(project_id: str) -> compute_v1.UsageExportLocation:
        """
        Retrieve Compute Engine usage export bucket for the Cloud project.
        Replaces the empty value returned by the API with the default value used
        to generate report file names.
    
        Args:
            project_id: project ID or project number of the project to update.
        Returns:
            UsageExportLocation object describing the current usage export settings
            for project project_id.
        """
        projects_client = compute_v1.ProjectsClient()
        project_data = projects_client.get(project=project_id)
    
        uel = project_data.usage_export_location
    
        if not uel.bucket_name:
            # The usage reports are disabled.
            return uel
    
        if not uel.report_name_prefix:
            # Although the server sent the empty string value, the next usage report
            # generated with these settings still has the default prefix value
            # "usage_gce". (see https://cloud.google.com/compute/docs/reference/rest/v1/projects/get)
            print(
                "Report name prefix not set, replacing with default value of "
                "`usage_gce`."
            )
            uel.report_name_prefix = "usage_gce"
        return uel
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
