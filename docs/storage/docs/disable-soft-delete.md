---
url: https://docs.cloud.google.com/storage/docs/disable-soft-delete/
title: Disable soft delete \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:30.346280+00:00
---

# Disable soft delete  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/disable-soft-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Disable soft delete Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/soft-delete) [Usage](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects)

This page describes how to disable the soft delete feature on new and existing buckets across your organization.

Soft delete is enabled on new buckets by default to prevent data loss. If needed, you can disable soft delete for existing buckets by modifying the soft delete policy, and you can disable soft delete by default for new buckets by setting an organization-wide default tag. Note that once you disable soft delete, your deleted data cannot be recovered, including accidental or malicious deletions.

## Required roles

To get the permissions that you need to disable soft delete, ask your administrator to grant you the following IAM roles on the organization level: 

  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`)
  * [Organization Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`)



These predefined roles contain the permissions required to disable soft delete. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to disable soft delete:

  * `storage.buckets.get`
  * `storage.buckets.update`
  * `storage.buckets.list` (this permission is only required if you plan to use the Google Cloud console to perform the instructions on this page)

For required permissions that are included as part of the Tag Admin(`roles/resourcemanager.tagAdmin`) role, see[Required permissions for administering tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#required-permissions-administer). 




For information about granting roles, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) or [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Disable soft delete for a specific bucket

Before you begin, consider the following:

  * If you disable a soft delete policy from your bucket that has soft-deleted objects in it during the time of disablement, the existing soft-deleted objects are retained until the previously applied retention duration expires.

  * After disabling a soft delete policy on your bucket, Cloud Storage doesn't retain newly deleted objects.

  * When you disable a soft delete policy on your bucket, the change isn't instantaneous across Cloud Storage due to metadata caching. Therefore, we recommend waiting at least thirty seconds before initiating any other delete operations, such as bulk delete, after you disable a soft delete policy. This ensures that your data is deleted permanently rather than soft-deleted. For more information about consistency in Cloud Storage operations, see [Cloud Storage consistency](https://docs.cloud.google.com/storage/docs/consistency).




Use the following instructions to disable soft delete for a specific bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket whose soft delete policy you want to disable.

  3. Click the **Protection** tab.

  4. In the **Soft delete policy** section, click **Disable** to disable the soft delete policy.

  5. Click **Confirm**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Run the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets#update) command with the `--clear-soft-delete` flag:
    
    
    gcloud storage buckets update --clear-soft-delete gs://BUCKET_NAME
    

Where:

  * `BUCKET_NAME` is the name of the bucket. For example, `my-bucket`.



### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "softDeletePolicy": {
             "retentionDurationSeconds": "0"
           }
         }

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



**Note:** You can also disable soft delete policies on multiple buckets in bulk. To learn more, see Disable soft delete in bulk.

## Disable soft delete for the 100 largest buckets in a project

Using the Google Cloud console you can disable soft delete for up to 100 buckets at once, with buckets sorted by the most soft-deleted bytes or the highest ratio of soft-deleted bytes to live bytes, allowing you to manage buckets with the greatest impact to your soft delete costs.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the Cloud Storage page, click **Settings**.

  3. Click the **Soft delete** tab.

  4. From the **Top buckets by deleted bytes** list, select the buckets you want to disable soft delete for.

  5. Click **Turn off soft delete**.

Soft delete is disabled on the buckets you selected.




## Disable soft delete for multiple or all buckets within a project

Using the Google Cloud CLI, run the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets#update) command with the `--project` flag and the [`*` wildcard](https://docs.cloud.google.com/storage/docs/wildcards#surprising-behavior) to bulk disable soft delete for multiple or all buckets within a project:
    
    
    gcloud storage buckets update --project=PROJECT_ID --clear-soft-delete gs://*
    

Where:

  * `PROJECT_ID` is the ID of the project. For example, `my-project`.



## Disable soft delete across all buckets within a folder

Using the Google Cloud CLI, run the [`gcloud projects list`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/list) and [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets#update) commands to disable soft delete on buckets across all the projects in a specified [folder](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).

**Note:** Make sure you confirm which projects' buckets you want to disable soft delete for before running the command.

Run the [`gcloud projects list`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/list) and [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets#update) commands to list all the buckets under a specified folder and then disable soft delete for all buckets within the folder:
    
    
    gcloud projects list --filter="parent.id: FOLDER_ID" --format="value(projectId)" | while read project
    do
      gcloud storage buckets update --project=$project --clear-soft-delete gs://*
    done
    

Where:

  * `FOLDER_ID` is the name of the folder. For example, `123456`.



## Disable soft delete at the organization level

Using the Google Cloud CLI, run the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets#update) command with the `--clear-soft-delete` flag and the [`*` wildcard](https://docs.cloud.google.com/storage/docs/wildcards#surprising-behavior) to disable soft delete at the organization level:

**Note:** Make sure you confirm which projects you want to disable soft delete for before running the command.

Run the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the `--clear-soft-delete` flag and the [`*` wildcard](https://docs.cloud.google.com/storage/docs/wildcards#surprising-behavior) to disable soft delete for all buckets within your organization:
    
    
    gcloud projects list --format="value(projectId)" | while read project
    do
      gcloud storage buckets update --project=$project --clear-soft-delete gs://*
    done
    

Cloud Storage disables soft delete on existing buckets. Objects that have already been soft deleted will remain in the buckets until their soft delete retention duration completes, after which, they are permanently deleted.

**Note:** Some shells such as bash and zsh can attempt to expand wildcards before passing the arguments to Google Cloud CLI. To avoid this, we recommend surrounding the argument with single quotes (on Linux) or double quotes (on Windows). For more information about URI wildcards, see [URI wildcards behavior considerations](https://docs.cloud.google.com/storage/docs/wildcards#surprising-behavior).

## Disable soft delete for new buckets

While soft delete is enabled by default on new buckets, you can prevent soft delete from default enablement using tags. Tags use the `storage.defaultSoftDeletePolicy` key to apply a `0d` (zero days) soft delete policy at the organization level, which disables the feature and prevents future retention of deleted data.

Use the following instructions to disable soft delete by default when you create new buckets. Note that the following instructions aren't equivalent to setting an organization policy that mandates a particular soft delete policy, meaning you can still enable soft delete on specific buckets by specifying a policy if needed.

  1. Using the Google Cloud CLI, create the `storage.defaultSoftDeletePolicy` tag which is used to change the default soft delete retention duration on new buckets. Note that only the `storage.defaultSoftDeletePolicy` tag name updates the default soft delete retention duration.

Create a tag key using the [`gcloud resource-manager tags keys create`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create) command:
         
         gcloud resource-manager tags keys create storage.defaultSoftDeletePolicy \
          --parent=organizations/ORGANIZATION_ID \
          --description="Configures the default softDeletePolicy for new Storage buckets."
         

Where:

     * `ORGANIZATION_ID` is the numeric ID of the organization you want to set a default soft delete retention duration for. For example, `12345678901`. To learn how to find the organization ID, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  2. Create a tag value for `0d` (zero days) to disable the soft delete retention period by default on new buckets using the [`gcloud resource-manager tags values create`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create) command:
         
         gcloud resource-manager tags values create 0d \
           --parent=ORGANIZATION_ID/storage.defaultSoftDeletePolicy \
           --description="Disables soft delete for new Storage buckets."
         

Where:

     * `ORGANIZATION_ID` is the numeric ID of the organization you want to set the default soft delete retention duration for. For example, `12345678901`.
**Note:** The command fails if you've previously created a `storage.defaultSoftDeletePolicy` tag. To create a tag value for `0d` and disable soft delete, you'll need to update the existing `storage.defaultSoftDeletePolicy` tag to use the `0d` tag value. For more information about updating tags, see [Update existing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#updating).
  3. Attach the tag to your resource using the [`gcloud resource-manager tags bindings create`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create) command:
         
         gcloud resource-manager tags bindings create \
          --tag-value=ORGANIZATION_ID/storage.defaultSoftDeletePolicy/0d \
          --parent=RESOURCE_ID
         

Where:

     * `ORGANIZATION_ID` is the numeric ID of the organization under which the tag was created. For example, `12345678901`.

     * `RESOURCE_ID` is the full name of the organization you want to create the tag binding for. For example, to attach a tag to `organizations/7890123456`, enter `//cloudresourcemanager.googleapis.com/organizations/7890123456`.




## Disable soft delete for buckets that exceed a specified cost threshold

Using the Cloud Client Libraries for Python, you can disable soft delete for buckets that exceed a specified relative cost threshold with a Python client library sample. The sample does the following:

  1. Calculates the relative cost of storage for each storage class.

  2. Assesses the soft delete cost accumulated by your buckets.

  3. Sets a cost threshold for soft delete usage and lists the buckets that exceed the threshold you set and lets you disable soft delete for the buckets that exceed the threshold.




To learn more about setting up the Python client library and using the sample, see the [Cloud Storage soft delete cost analyzer `README.md` page](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/storage/cost-analysis/README.md).

The following sample disables soft delete for buckets that exceed a specified cost threshold:
    
    
    from __future__ import annotations
    
    import argparse
    import json
    import google.cloud.monitoring_v3 as monitoring_client
    
    
    def get_relative_cost(storage_class: str) -> float:
        """Retrieves the relative cost for a given storage class and location.
    
        Args:
            storage_class: The storage class (e.g., 'standard', 'nearline').
    
        Returns:
            The price per GB from the https://cloud.google.com/storage/pricing,
            divided by the standard storage class.
        """
        relative_cost = {
            "STANDARD": 0.023 / 0.023,
            "NEARLINE": 0.013 / 0.023,
            "COLDLINE": 0.007 / 0.023,
            "ARCHIVE": 0.0025 / 0.023,
        }
    
        return relative_cost.get(storage_class, 1.0)
    
    
    def get_soft_delete_cost(
        project_name: str,
        soft_delete_window: float,
        agg_days: int,
        lookback_days: int,
    ) -> dict[str, list[dict[str, float]]]:
        """Calculates soft delete costs for buckets in a Google Cloud project.
    
        Args:
            project_name: The name of the Google Cloud project.
            soft_delete_window: The time window in seconds for considering
              soft-deleted objects (default is 7 days).
            agg_days: Aggregate results over a time period, defaults to 30-day period
            lookback_days: Look back up to upto days, defaults to 360 days
    
        Returns:
            A dictionary with bucket names as keys and cost data for each bucket,
            broken down by storage class.
        """
    
        query_client = monitoring_client.QueryServiceClient()
    
        # Step 1: Get storage class ratios for each bucket.
        storage_ratios_by_bucket = get_storage_class_ratio(
            project_name, query_client, agg_days, lookback_days
        )
    
        # Step 2: Fetch soft-deleted bytes and calculate costs using Monitoring API.
        soft_deleted_costs = calculate_soft_delete_costs(
            project_name,
            query_client,
            soft_delete_window,
            storage_ratios_by_bucket,
            agg_days,
            lookback_days,
        )
    
        return soft_deleted_costs
    
    
    def calculate_soft_delete_costs(
        project_name: str,
        query_client: monitoring_client.QueryServiceClient,
        soft_delete_window: float,
        storage_ratios_by_bucket: dict[str, float],
        agg_days: int,
        lookback_days: int,
    ) -> dict[str, list[dict[str, float]]]:
        """Calculates the relative cost of enabling soft delete for each bucket in a
           project for certain time frame in secs.
    
        Args:
            project_name: The name of the Google Cloud project.
            query_client: A Monitoring API query client.
            soft_delete_window: The time window in seconds for considering
              soft-deleted objects (default is 7 days).
            storage_ratios_by_bucket: A dictionary of storage class ratios per bucket.
            agg_days: Aggregate results over a time period, defaults to 30-day period
            lookback_days: Look back up to upto days, defaults to 360 days
    
        Returns:
            A dictionary with bucket names as keys and a list of cost data
            dictionaries
            for each bucket, broken down by storage class.
        """
        soft_deleted_bytes_time = query_client.query_time_series(
            monitoring_client.QueryTimeSeriesRequest(
                name=f"projects/{project_name}",
                query=f"""
                        {{  # Fetch 1: Soft-deleted (bytes seconds)
                            fetch gcs_bucket :: storage.googleapis.com/storage/v2/deleted_bytes
                            | value val(0) * {soft_delete_window}\'s\'  # Multiply by soft delete window
                            | group_by [resource.bucket_name, metric.storage_class], window(), .sum;
    
                            # Fetch 2: Total byte-seconds (active objects)
                            fetch gcs_bucket :: storage.googleapis.com/storage/v2/total_byte_seconds
                            | filter metric.type != 'soft-deleted-object'
                            | group_by [resource.bucket_name, metric.storage_class], window(1d), .mean  # Daily average
                            | group_by [resource.bucket_name, metric.storage_class], window(), .sum  # Total over window
    
                        }}  # End query definition
                        | every {agg_days}d  # Aggregate over larger time intervals
                        | within {lookback_days}d  # Limit data range for analysis
                        | ratio  # Calculate ratio (soft-deleted (bytes seconds)/ total (bytes seconds))
                        """,
            )
        )
    
        buckets: dict[str, list[dict[str, float]]] = {}
        missing_distribution_storage_class = []
        for data_point in soft_deleted_bytes_time.time_series_data:
            bucket_name = data_point.label_values[0].string_value
            storage_class = data_point.label_values[1].string_value
            # To include location-based cost analysis:
            # 1. Uncomment the line below:
            # location = data_point.label_values[2].string_value
            # 2. Update how you calculate 'relative_storage_class_cost' to factor in location
            soft_delete_ratio = data_point.point_data[0].values[0].double_value
            distribution_storage_class = bucket_name + " - " + storage_class
            storage_class_ratio = storage_ratios_by_bucket.get(
                distribution_storage_class
            )
            if storage_class_ratio is None:
                missing_distribution_storage_class.append(
                    distribution_storage_class)
            buckets.setdefault(bucket_name, []).append({
                # Include storage class and location data for additional plotting dimensions.
                # "storage_class": storage_class,
                # 'location': location,
                "soft_delete_ratio": soft_delete_ratio,
                "storage_class_ratio": storage_class_ratio,
                "relative_storage_class_cost": get_relative_cost(storage_class),
            })
    
        if missing_distribution_storage_class:
            print(
                "Missing storage class for following buckets:",
                missing_distribution_storage_class,
            )
            raise ValueError("Cannot proceed with missing storage class ratios.")
    
        return buckets
    
    
    def get_storage_class_ratio(
        project_name: str,
        query_client: monitoring_client.QueryServiceClient,
        agg_days: int,
        lookback_days: int,
    ) -> dict[str, float]:
        """Calculates storage class ratios for each bucket in a project.
    
        This information helps determine the relative cost contribution of each
        storage class to the overall soft-delete cost.
    
        Args:
            project_name: The Google Cloud project name.
            query_client: Google Cloud's Monitoring Client's QueryServiceClient.
            agg_days: Aggregate results over a time period, defaults to 30-day period
            lookback_days: Look back up to upto days, defaults to 360 days
    
        Returns:
            Ratio of Storage classes within a bucket.
        """
        request = monitoring_client.QueryTimeSeriesRequest(
            name=f"projects/{project_name}",
            query=f"""
                {{
                # Fetch total byte-seconds for each bucket and storage class
                fetch gcs_bucket :: storage.googleapis.com/storage/v2/total_byte_seconds
                | group_by [resource.bucket_name, metric.storage_class], window(), .sum;
                # Fetch total byte-seconds for each bucket (regardless of class)
                fetch gcs_bucket :: storage.googleapis.com/storage/v2/total_byte_seconds
                | group_by [resource.bucket_name], window(), .sum
                }}
                | ratio  # Calculate ratios of storage class size to total size
                | every {agg_days}d
                | within {lookback_days}d
                """,
        )
    
        storage_class_ratio = query_client.query_time_series(request)
    
        storage_ratios_by_bucket = {}
        for time_series in storage_class_ratio.time_series_data:
            bucket_name = time_series.label_values[0].string_value
            storage_class = time_series.label_values[1].string_value
            ratio = time_series.point_data[0].values[0].double_value
    
            # Create a descriptive key for the dictionary
            key = f"{bucket_name} - {storage_class}"
            storage_ratios_by_bucket[key] = ratio
    
        return storage_ratios_by_bucket
    
    
    def soft_delete_relative_cost_analyzer(
        project_name: str,
        cost_threshold: float = 0.0,
        soft_delete_window: float = 604800,
        agg_days: int = 30,
        lookback_days: int = 360,
        list_buckets: bool = False,
        ) -> str | dict[str, float]: # Note potential string output
        """Identifies buckets exceeding the relative cost threshold for enabling soft delete.
    
        Args:
            project_name: The Google Cloud project name.
            cost_threshold: Threshold above which to consider removing soft delete.
            soft_delete_window: Time window for calculating soft-delete costs (in
              seconds).
            agg_days: Aggregate results over this time period (in days).
            lookback_days: Look back up to this many days.
            list_buckets: Return a list of bucket names (True) or JSON (False,
              default).
    
        Returns:
            JSON formatted results of buckets exceeding the threshold and costs
            *or* a space-separated string of bucket names.
        """
    
        buckets: dict[str, float] = {}
        for bucket_name, storage_sources in get_soft_delete_cost(
            project_name, soft_delete_window, agg_days, lookback_days
        ).items():
            bucket_cost = 0.0
            for storage_source in storage_sources:
                bucket_cost += (
                    storage_source["soft_delete_ratio"]
                    * storage_source["storage_class_ratio"]
                    * storage_source["relative_storage_class_cost"]
                )
            if bucket_cost > cost_threshold:
                buckets[bucket_name] = round(bucket_cost, 4)
    
        if list_buckets:
            return " ".join(buckets.keys())  # Space-separated bucket names
        else:
            return json.dumps(buckets, indent=2)  # JSON output
    
    
    def soft_delete_relative_cost_analyzer_main() -> None:
        # Sample run: python storage_soft_delete_relative_cost_analyzer.py <Project Name>
        parser = argparse.ArgumentParser(
            description="Analyze and manage Google Cloud Storage soft-delete costs."
        )
        parser.add_argument(
            "project_name", help="The name of the Google Cloud project to analyze."
        )
        parser.add_argument(
            "--cost_threshold",
            type=float,
            default=0.0,
            help="Relative Cost threshold.",
        )
        parser.add_argument(
            "--soft_delete_window",
            type=float,
            default=604800.0,
            help="Time window (in seconds) for considering soft-deleted objects.",
        )
        parser.add_argument(
            "--agg_days",
            type=int,
            default=30,
            help=(
                "Time window (in days) for aggregating results over a time period,"
                " defaults to 30-day period"
            ),
        )
        parser.add_argument(
            "--lookback_days",
            type=int,
            default=360,
            help=(
                "Time window (in days) for considering the how old the bucket to be."
            ),
        )
        parser.add_argument(
            "--list",
            type=bool,
            default=False,
            help="Return the list of bucketnames seperated by space.",
        )
    
        args = parser.parse_args()
    
        response = soft_delete_relative_cost_analyzer(
            args.project_name,
            args.cost_threshold,
            args.soft_delete_window,
            args.agg_days,
            args.lookback_days,
            args.list,
        )
        if not args.list:
            print(
                "To remove soft-delete policy from the listed buckets run:\n"
                # Capture output
                "python storage_soft_delete_relative_cost_analyzer.py"
                " [your-project-name] --[OTHER_OPTIONS] --list > list_of_buckets.txt \n"
                "cat list_of_buckets.txt | gcloud storage buckets update -I "
                "--clear-soft-delete",
                response,
            )
            return
        print(response)
    
    
    if __name__ == "__main__":
        soft_delete_relative_cost_analyzer_main()

## What's next

  * Review [considerations](https://docs.cloud.google.com/storage/docs/soft-delete#soft-delete-policy) before re-enabling soft delete.

  * Learn about [how soft delete interacts with other Cloud Storage features](https://docs.cloud.google.com/storage/docs/soft-delete#soft-delete-considerations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
