---
url: https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports/
title: Use inventory reports \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:31.615710+00:00
---

# Use inventory reports  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use inventory reports Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage [inventory reports](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#inventory-reports-overview) lets you generate scheduled CSV or Apache Parquet exports of your object metadata without running resource-intensive list operations. You can configure report schedules, view generated reports, and manage report configurations to audit objects, analyze storage costs, or validate data migrations.

## Before you begin

Before you begin creating and managing inventory reports and inventory report configurations, follow the instructions in the subsequent subsections.

### Get required roles

In order to get the required permissions for creating and managing inventory reports, ask your administrator to grant you the following IAM roles on the project or source and destination buckets with which you'll be managing inventory reports.

  * To create and manage inventory report configurations:

    * `roles/storage.admin` on the source bucket and destination bucket

    * `roles/storageinsights.admin` on the project

  * To read and download inventory reports:

    * `roles/storage.objectViewer` on the destination bucket

    * `roles/storageinsights.viewer` on the project




These predefined roles contain the permissions required to create and manage inventory reports and configurations. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

To create and manage inventory report configurations:

  * `storage.buckets.get` on the source bucket
  * `storage.objects.list` on the source bucket
  * `storage.buckets.getObjectInsights` on the source bucket
  * `storage.buckets.get` on the destination bucket
  * `storage.objects.create` on the destination bucket
  * `storageinsights.reportConfigs.delete` on the project
  * `storageinsights.reportConfigs.get` on the project
  * `storageinsights.reportConfigs.create` on the project
  * `storageinsights.reportConfigs.list` on the project
  * `storageinsights.reportConfigs.update` on the project



To read and download inventory reports:

  * `storage.objects.get` on the destination bucket
  * `storageinsights.reportDetails.get` on the project
  * `storageinsights.reportDetails.list` on the project



You might also be able to get these permissions with other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles). To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

For instructions on using roles to control access to buckets, see [Use IAM](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#command-line). For instructions on using roles to control access to projects, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Enable the Storage Insights API

### Console

Enable the Storage Insights API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=storageinsights.googleapis.com)

### Command line

Enable the Storage Insights API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable storageinsights.googleapis.com

### REST APIs

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To enable the Storage Insights API, use [`cURL`](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/create) to call the [`services.enable`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/enable) method:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           https://serviceusage.googleapis.com/v1/projects/PROJECT_ID/services/storageinsights.googleapis.com:enable
         

Replace:

`PROJECT_ID` with the ID of the project you want to enable the API for.




## Create an inventory report configuration

### Console

To create an inventory report configuration, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you'd like to use as the [source bucket](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#source-and-destination-buckets).

  3. On the **Bucket details** page, click the **Inventory reports** tab.

  4. Click **Create report configuration**.

  5. In the **Identify your report configuration** section, create a display name for the inventory report configuration. The display name can contain up to 256 characters.

  6. In the **Choose metadata fields** section, select the [metadata fields](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#object-metadata-fields) you want to include in your inventory reports.

  7. Click **Continue**.

  8. In the **Choose a file format** section, select the file format in which you'd like to generate inventory reports.

  9. In the **Choose a destination bucket** section, select the bucket you'd like to use as a [destination bucket](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#source-and-destination-buckets).

In the **Enter destination path (optional)** section, you can optionally specify a destination path where inventory reports will be generated.

  10. In the **Scheduling options** section, specify the frequency, start date, and end date for generating reports.

  11. Click **Create**.

The **Report configuration details** page is displayed. The metadata of generated inventory reports will appear on the page.




### Command line

  1. To create an inventory report configuration, run the `gcloud storage insights inventory-reports create` command:
         
         gcloud storage insights inventory-reports create SOURCE_BUCKET_URL \
           --csv-separator=SEPARATOR \
           --csv-delimiter=DELIMITER \
           --[no]-csv-header \
           --parquet \
           --display-name=DISPLAY_NAME \
           --destination=DESTINATION_PATH \
           --metadata-fields=METADATA_FIELD \
           --schedule-starts=START_DATE \
           --schedule-repeats=FREQUENCY \
           --schedule-repeats-until=END_DATE

Replace:

     * `SOURCE_BUCKET_URL` with the URL of the source bucket. For example, `gs://my_example_source_bucket`.

     * `SEPARATOR` with the character used to separate the records in the inventory report CSV file. Must be either `\n` or `\r\n`. Default value is `\n`. Optional. If the `--csv-separator` flag is used, `--parquet` cannot be used.

     * `DELIMITER` with the delimiter that separates the fields in the inventory report CSV file. The value can include one character and cannot be the same value as `SEPARATOR`. Default value is `,`. Optional. If `--csv-delimiter` is used, `--parquet` cannot be used.

     * `--[no]-csv-header` with the flag that indicates whether or not headers are included in the inventory report CSV file. Use `--csv-header` to include headers and `--no-csv-header` to exclude headers. If either flag is used, `--parquet` cannot be used.

     * `DISPLAY_NAME` with the editable name of the inventory report configuration. Optional.

     * `--parquet` with the flag that generates inventory reports in Apache Parquet format instead of CSV. If used, `--csv-delimiter`, `--csv-separator`, and `--[no-]csv-header` cannot be used.

     * `DESTINATION_PATH` with the bucket or folder in the bucket where inventory reports will be generated. For example, `gs://my_example_destination_bucket` or `gs://my_example_destination_bucket/path/to/inventory/report`.

When you specify a path to a folder within a bucket, you can use keywords in the path, which are substituted with their corresponding values when the report is generated. This lets you generate reports in a Hive partitioned format so you can load or query the data in BigQuery without additional processing.

     * `METADATA_FIELD` with a comma-separated list of [metadata fields](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#object-metadata-fields) you want included in the inventory report.

     * `START_DATE` with the UTC date on which you want to start generating inventory reports. For example, `2022-01-15`.

     * `FREQUENCY` with how often you want inventory reports to be generated. Values are `daily` or `weekly`.

     * `END_DATE` with the UTC date after which you want to stop generating inventory reports. Must be a value after the `START_DATE`. For example, if you specify `2022-02-15`, inventory reports will no longer be generated as of February 16, 2022.




### Client libraries

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storageinsights.v1.[CSVOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CSVOptions.html);
    import com.google.cloud.storageinsights.v1.[CloudStorageDestinationOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CloudStorageDestinationOptions.html);
    import com.google.cloud.storageinsights.v1.[CloudStorageFilters](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CloudStorageFilters.html);
    import com.google.cloud.storageinsights.v1.[CreateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CreateReportConfigRequest.html);
    import com.google.cloud.storageinsights.v1.[FrequencyOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.FrequencyOptions.html);
    import com.google.cloud.storageinsights.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.LocationName.html);
    import com.google.cloud.storageinsights.v1.[ObjectMetadataReportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ObjectMetadataReportOptions.html);
    import com.google.cloud.storageinsights.v1.[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html);
    import com.google.cloud.storageinsights.v1.[StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html);
    import com.google.common.collect.ImmutableList;
    import com.google.type.[Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html);
    import java.io.IOException;
    
    public class CreateInventoryReportConfig {
    
      public static void createInventoryReportConfig(
          String projectId, String bucketLocation, String sourceBucket, String destinationBucket)
          throws IOException {
        try ([StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html) storageInsightsClient = [StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html).create()) {
          [ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html) reportConfig =
              [ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html).newBuilder()
                  .[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.Builder.html#com_google_cloud_storageinsights_v1_ReportConfig_Builder_setDisplayName_java_lang_String_)("Example inventory report configuration")
                  .[setFrequencyOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.Builder.html#com_google_cloud_storageinsights_v1_ReportConfig_Builder_setFrequencyOptions_com_google_cloud_storageinsights_v1_FrequencyOptions_)(
                      [FrequencyOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.FrequencyOptions.html).newBuilder()
                          .[setFrequency](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.FrequencyOptions.Builder.html#com_google_cloud_storageinsights_v1_FrequencyOptions_Builder_setFrequency_com_google_cloud_storageinsights_v1_FrequencyOptions_Frequency_)([FrequencyOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.FrequencyOptions.html).Frequency.WEEKLY)
                          .[setStartDate](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.FrequencyOptions.Builder.html#com_google_cloud_storageinsights_v1_FrequencyOptions_Builder_setStartDate_com_google_type_Date_)([Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html).newBuilder().setDay(15).setMonth(8).setYear(3022).build())
                          .[setEndDate](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.FrequencyOptions.Builder.html#com_google_cloud_storageinsights_v1_FrequencyOptions_Builder_setEndDate_com_google_type_Date_)([Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html).newBuilder().setDay(15).setMonth(9).setYear(3022).build())
                          .build())
                  .[setCsvOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.Builder.html#com_google_cloud_storageinsights_v1_ReportConfig_Builder_setCsvOptions_com_google_cloud_storageinsights_v1_CSVOptions_)(
                      [CSVOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CSVOptions.html).newBuilder()
                          .[setDelimiter](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CSVOptions.Builder.html#com_google_cloud_storageinsights_v1_CSVOptions_Builder_setDelimiter_java_lang_String_)(",")
                          .[setRecordSeparator](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CSVOptions.Builder.html#com_google_cloud_storageinsights_v1_CSVOptions_Builder_setRecordSeparator_java_lang_String_)("\n")
                          .[setHeaderRequired](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CSVOptions.Builder.html#com_google_cloud_storageinsights_v1_CSVOptions_Builder_setHeaderRequired_boolean_)(true)
                          .build())
                  .[setObjectMetadataReportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.Builder.html#com_google_cloud_storageinsights_v1_ReportConfig_Builder_setObjectMetadataReportOptions_com_google_cloud_storageinsights_v1_ObjectMetadataReportOptions_)(
                      [ObjectMetadataReportOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ObjectMetadataReportOptions.html).newBuilder()
                          .[addAllMetadataFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ObjectMetadataReportOptions.Builder.html#com_google_cloud_storageinsights_v1_ObjectMetadataReportOptions_Builder_addAllMetadataFields_java_lang_Iterable_java_lang_String__)(ImmutableList.of("project", "name", "bucket"))
                          .[setStorageFilters](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ObjectMetadataReportOptions.Builder.html#com_google_cloud_storageinsights_v1_ObjectMetadataReportOptions_Builder_setStorageFilters_com_google_cloud_storageinsights_v1_CloudStorageFilters_)(
                              [CloudStorageFilters](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CloudStorageFilters.html).newBuilder().setBucket(sourceBucket).build())
                          .[setStorageDestinationOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ObjectMetadataReportOptions.Builder.html#com_google_cloud_storageinsights_v1_ObjectMetadataReportOptions_Builder_setStorageDestinationOptions_com_google_cloud_storageinsights_v1_CloudStorageDestinationOptions_)(
                              [CloudStorageDestinationOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CloudStorageDestinationOptions.html).newBuilder()
                                  .setBucket(destinationBucket)
                                  .build())
                          .build())
                  .build();
          [CreateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CreateReportConfigRequest.html) request =
              [CreateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CreateReportConfigRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.LocationName.html).of(projectId, bucketLocation).toString())
                  .setReportConfig(reportConfig)
                  .build();
          [ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html) response = storageInsightsClient.createReportConfig(request);
          System.out.println("Created inventory report config with name " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html#com_google_cloud_storageinsights_v1_ReportConfig_getName__)());
        }
      }
    }

### REST APIs

### JSON API

To create an inventory report configuration, complete the following steps:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information, where all fields are required unless noted otherwise:
         
         {
           "display_name": "DISPLAY_NAME",
           "frequency_options": {
             "frequency": "FREQUENCY",
             "start_date": "START_DATE",
             "end_date": "END_DATE",
           },
           "csv_options": {
             "record_separator": "RECORD_SEPARATOR",
             "delimiter": "DELIMITER",
             "header_required": HEADER_REQUIRED
           },
           "object_metadata_report_options": {
              "metadata_fields": [
               "METADATA_FIELD",
               ...
             ],
             "storage_filters": {
               "bucket": "SOURCE_BUCKET_NAME"
             },
             "storage_destination_options": {
               "bucket": "DESTINATION_BUCKET_NAME",
               "destination_path": "DESTINATION_PATH"
             }
           }
         }

Replace:

     * `DISPLAY_NAME` with the editable display name of the inventory report configuration. Can contain up to 256 characters.

     * `FREQUENCY` with the frequency for generating inventory reports. Values are `DAILY` or `WEEKLY`.

     * `START_DATE` with the UTC date on which you want to start generating inventory reports. Cannot be the current date or any past date. Value must be an object containing the keys `day`, `month`, and `year`. For example: `{"day": 15, "month": 8, "year": 2022}`.

     * `END_DATE` with the UTC date after which you want to stop generating inventory reports. Value must be an object containing the keys `day`, `month`, and `year`. For example, if you specify `{"day": 15, "month": 9, "year": 2022}`, inventory reports are no longer generated as of September 16, 2022.

     * `RECORD_SEPARATOR` with the character used to separate the records in the inventory report CSV file. Must be either `\n` or `\r\n`. Default value is `\n`. This field is optional.

     * `DELIMITER` with the delimiter that separates the fields in the inventory report CSV file. The value can include one character and cannot be the same as the `RECORD_SEPARATOR`. Default value is `,`. This field is optional.

     * `HEADER_REQUIRED` with the boolean that indicates whether or not headers are included in the CSV file. This field is optional.

     * `SOURCE_BUCKET_NAME` with the name of the [source bucket](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#source-and-destination-buckets) that contains the objects you want to generate inventory reports for. For example, `my_example_bucket`.

     * `METADATA_FIELD` with a comma-separated list of [metadata fields](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#object-metadata-fields) you want included in the inventory report.

     * `DESTINATION_BUCKET_NAME` with the name of the [destination bucket](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#source-and-destination-buckets) where generated inventory reports are generated and stored. For example, `my_example_destination_bucket`.

     * `DESTINATION_PATH` with the path in the destination bucket where generated inventory reports are generated. This field is optional.

When you specify a path to a folder within a bucket, you can use keywords in the path, which are substituted with their corresponding values when the report is generated. This lets you generate reports in a Hive partitioned format so you can load or query the data in BigQuery without additional processing.

**Note:** To generate inventory reports in Apache Parquet format, include `"parquet_options": {}` instead of `"csv_options": {...}` in your inventory report configuration.

For example, the following code sample creates an inventory report configuration named "Example inventory report configuration" that generates reports at a weekly frequency:
    
    {
      "display_name": "Example inventory report configuration",
      "frequency_options": {
        "frequency": "WEEKLY",
        "start_date": {
          "day": 15,
          "month": 8,
          "year": 2022
        },
        "end_date": {
          "day": 15,
          "month": 9,
          "year": 2022
        },
      },
      "csv_options": {
        "record_separator": "\n",
        "delimiter": ",",
        "header_required": true
      },
      "object_metadata_report_options": {
         "metadata_fields": [
          "project",
          "name",
          "bucket"
        ],
        "storage_filters": {
          "bucket": "example_source_bucket"
        },
        "storage_destination_options": {
          "bucket": "example_destination_bucket"
        }
      }
    }

  3. To apply the inventory report configuration, use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Create` ReportConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/create) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
         "https://storageinsights.googleapis.com/v1/projects/YOUR_PROJECT/locations/LOCATION/reportConfigs" \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json" \
         

Replace:

     * `JSON_FILE_NAME` with the path to the JSON file you created in the previous step.

     * `YOUR_PROJECT` with the name of the project in which your source and destination buckets reside.

     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of the source and destination buckets. For example, `us-west1`.




## Grant required roles to the service agent

A project-level [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) is automatically created the first time you set up an inventory report configuration. The service agent follows the naming format `service-PROJECT_NUMBER@gcp-sa-storageinsights.iam.gserviceaccount.com` and appears on the [IAM page of the Google Cloud console](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId) when you select the **Include Google-provided role grants** checkbox.

To enable Storage Insights to generate and write inventory reports, ask your administrator to grant the service agent the following IAM roles: 

  * `roles/storage.insightsCollectorService` on the source bucket, which includes the `storage.buckets.getObjectInsights` and `storage.buckets.get` permissions
  * `roles/storage.objectCreator` on the destination bucket, which includes the `storage.objects.create` permission



For instructions on granting roles, see [Use IAM](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). You can grant the `roles/storage.insightsCollectorService` role by using the Google Cloud console or the Google Cloud CLI. For example: 
    
    
    gcloud storage buckets add-iam-policy-binding SOURCE_BUCKET_URL \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-storageinsights.iam.gserviceaccount.com \
        --role=roles/storage.insightsCollectorService

Once the service agent is granted the required permissions, it takes up to 24 hours to write the first inventory report to the destination bucket.

## Edit an inventory report configuration

Once an inventory report configuration has been created, you can modify [certain properties](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#inventory-reports-overview) of the configuration.

### Console

To edit an inventory report configuration, do the following:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the source bucket that contains the inventory report configuration you want to edit.

  3. In your source bucket's **Bucket details** page, click the **Inventory reports** tab.

  4. Click the configuration name of the inventory report configuration you want to edit.

  5. In the **Report configuration details** page that appears, edit the properties by using the edit **Edit** button.




### Command line

To edit an inventory report configuration, do the following:

  1. To find the name of the inventory report configuration you want to edit, list all the inventory configurations in the source bucket by using the `gcloud storage insights inventory-reports list` command:
         
         gcloud storage insights inventory-reports list \
           --source=SOURCE_BUCKET \
           --filter=EXPRESSION \
           --page-size=SIZE \
           --sort-by=FIELD \
           --format="yaml(name)"

Replace:

     * `SOURCE_BUCKET` with the URL of the source bucket that contains the inventory report configuration.

     * `EXPRESSION` with a boolean filter to apply to each resource item to be listed. If the expression evaluates True, the item is listed. For more details and examples of filter expressions, run `$ gcloud topic filters`.

     * `SIZE` with the maximum number of resources per page. The default is 50.

     * `FIELD` with a comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with `~` for descending order on that field.

     1. Edit the inventory report configuration fields you want to update by using the `gcloud storage insights inventory-reports update` command. The following example updates the inventory report configuration to generate inventory reports daily in Apache Parquet format:
            
            gcloud storage insights inventory-reports update CONFIG_NAME \
            --parquet \
            --schedule-repeats="daily"




### Client libraries

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storageinsights.v1.[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html);
    import com.google.cloud.storageinsights.v1.[ReportConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfigName.html);
    import com.google.cloud.storageinsights.v1.[StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html);
    import com.google.cloud.storageinsights.v1.[UpdateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.UpdateReportConfigRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class EditInventoryReportConfig {
    
    
      public static void editInventoryReportConfig(
              String projectId, String location, String inventoryReportConfigUuid) throws IOException {
        try ([StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html) storageInsightsClient = [StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html).create()) {
          [ReportConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfigName.html) name = [ReportConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfigName.html).of(projectId, location, inventoryReportConfigUuid);
          [ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html) reportConfig = storageInsightsClient.getReportConfig(name);
    
          // Set any other fields you want to update here
          [ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html) updatedReportConfig =
                  reportConfig.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html#com_google_cloud_storageinsights_v1_ReportConfig_toBuilder__)().[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.Builder.html#com_google_cloud_storageinsights_v1_ReportConfig_Builder_setDisplayName_java_lang_String_)("Updated Display Name").build();
    
          storageInsightsClient.updateReportConfig(
                  [UpdateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.UpdateReportConfigRequest.html).newBuilder()
                          // Add any fields that you want to update to the update mask, in snake case
                          .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("display_name")
                                  .build())
                          .setReportConfig(updatedReportConfig).build());
    
          System.out.println("Edited inventory report config with name " + name);
        }
      }
    }
    

### REST APIs

### JSON API

To edit an inventory report configuration, complete the following steps:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Get the name of the inventory report configuration you want to edit by using [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Get` ReportConfig](https://docs.cloud.google.com/storage/docs/insights/v1/reportConfig/get) request:
         
         curl --request GET \
         "https://storageinsights.googleapis.com/v1/projects/YOUR_PROJECT/locations/LOCATION/reportConfigs?" \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json" \
         

Replace:

     * `YOUR_PROJECT` with the name of the project in which your source and destination buckets reside.

     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of the source and destination buckets. For example, `us-west1`.

If you want to retrieve all inventory report configurations in a specific source bucket, append the `filter` query parameter to your request:
    
    curl --request GET \
    "https://storageinsights.googleapis.com/v1/projects/YOUR_PROJECT/locations/LOCATION/reportConfigs?filter=objectMetadataReportOptions.storageFilters.bucket=BUCKET_NAME" \
      --header "Authorization: Bearer $(gcloud auth print-access-token)" \
      --header "Accept: application/json" \
      --header "Content-Type: application/json" \
    

Replace:

     * `YOUR_PROJECT` with the name of the project in which your source and destination buckets reside.
     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of the source and destination buckets. For example, `us-west1`.
     * `BUCKET_NAME` with the name of the source bucket that contains the inventory report configurations you want to edit.
  3. Create a JSON file that includes changes to the properties you want to edit. The following example updates the inventory report configuration to generate inventory reports daily in Apache Parquet format:
         
         {
           "ReportConfig": {
             "frequency_options": {
               "frequency": "DAILY"
             },
             "parquet_options": {
             }
           }

  4. To apply the inventory report configuration, use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Patch` ReportConfig](https://docs.cloud.google.com/storage/docs/insights/v1/reportConfig/patch) request:
         
         curl --request PATCH \
         "https://storageinsights.googleapis.com/v1/projects/YOUR_PROJECT/locations/LOCATION/reportConfigs/REPORT_CONFIG_UUID" \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json" \
           --data-binary "@JSON_FILE_NAME.json" \
         

Replace:

     * `YOUR_PROJECT` with the name of the project in which your source and destination buckets reside.

     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of the source and destination buckets. For example, `us-west1`.

     * `REPORT_CONFIG_UUID` with the auto-generated UUID of the inventory report configuration.




## List inventory report configurations

### Console

To list the inventory report configurations in a source bucket, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the source bucket that contains the inventory report configurations you want to view.

  3. On the **Bucket details** page, click the **Inventory reports** tab.

Inventory report configurations in the source bucket appear.




### Command line

You can list all the inventory configurations in a source bucket by using the `gcloud storage insights inventory-reports list` command:
    
    
    gcloud storage insights inventory-reports list \
      --source=SOURCE_BUCKET \
      --filter=EXPRESSION \
      --page-size=SIZE \
      --sort-by=FIELD \
      --format="yaml(name)"
      

Replace:

  * `SOURCE_BUCKET` with the URL of the source bucket that contains the inventory report configuration.

  * `EXPRESSION` with a boolean filter to apply to each resource item to be listed. If the expression evaluates True, the item is listed. For more details and examples of filter expressions, run `$ gcloud topic filters`.

  * `SIZE` with the maximum number of resources per page. The default is 50.

  * `FIELD` with a comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with `~` for descending order on that field.




### Client libraries

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storageinsights.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.LocationName.html);
    import com.google.cloud.storageinsights.v1.[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html);
    import com.google.cloud.storageinsights.v1.[StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html);
    import java.io.IOException;
    
    public class ListInventoryReportConfigs {
    
    
      public static void listInventoryReportConfigs(String projectId, String location)
          throws IOException {
        try ([StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html) storageInsightsClient = [StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html).create()) {
          System.out.println(
              "Printing inventory report configs in project "
                  + projectId
                  + " and location "
                  + location);
          for ([ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html) config :
              storageInsightsClient
                  .listReportConfigs([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.LocationName.html).of(projectId, location))
                  .iterateAll()) {
            System.out.println(config.getName());
          }
        }
      }
    }
    

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. You can list all inventory report configurations in a project for a given location by using a [request to list inventory report configurations](https://docs.cloud.google.com/storage/docs/insights/v1/reportConfig/list):
         
         curl --request GET \
         "https://storageinsights.googleapis.com/v1/projects/YOUR_PROJECT/locations/LOCATION/reportConfigs?" \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json" \
         

Replace:

     * `YOUR_PROJECT` with the name of the project in which your source and destination buckets reside.

     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of the source and destination buckets. For example, `us-west1`.

If you want to list all inventory report configurations in a specific source bucket, append the `filter` query parameter to your request:
    
    curl --request GET \
    "https://storageinsights.googleapis.com/v1/projects/YOUR_PROJECT/locations/LOCATION/reportConfigs?filter=objectMetadataReportOptions.storageFilters.bucket=BUCKET_NAME" \
      --header "Authorization: Bearer $(gcloud auth print-access-token)" \
      --header "Accept: application/json" \
      --header "Content-Type: application/json" \
    

Replace:

     * `YOUR_PROJECT` with the name of the project in which your source and destination buckets reside.

     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of the source and destination buckets. For example, `us-west1`.

     * `BUCKET_NAME` with the name of the source bucket that contains the inventory report configurations you want to list.




## Download an inventory report

### Console

### Download individual reports

Inventory reports are generated and stored as objects in the destination bucket, so you can download them as you would download a regular object.

To download an inventory report, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the destination bucket that contains the inventory report you want to download.

  3. On the **Bucket details** page, make sure the **Objects** tab is selected.

  4. Click file_download **Download** associated with the inventory report you want to download.




If you don't know the destination bucket, you can also download an inventory report through the inventory report configuration from which it was generated:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the source bucket containing the inventory report configuration that generated the report you want to download.

  3. On the **Bucket details** page, click the configuration name of the inventory report configuration.

  4. On the **Report configuration details** page that appears, navigate to the **Inventory report history** section, then click the destination object path of the inventory report you want to download.

The **Bucket details** page appears for the destination bucket that contains the inventory report.

  5. Click file_download **Download** associated with the inventory report you want to download.




### Download report shards

To download an inventory report that's been split into one or more [shards](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#shards), complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the destination bucket you specified when you created the inventory report configuration.

  3. On the **Bucket details** page, check for the presence of a [manifest file](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#manifest-file). The presence of a manifest file indicates that all the shards of an inventory report have been generated.

An example manifest filename is `fc95c52f-157a-494f-af4a-d4a53a69ba66_2022-11-30T00:00_manifest.json`.

  4. In the destination bucket, click file_download **Download** associated with the manifest file. Note the names of the shard files you want to download from the `report_shards_file_names` field.

  5. In the destination bucket, click file_download **Download** associated with the shard files you want to download.




### Command line

### Download individual reports

To download an inventory report, complete the following steps:

  1. To list all the inventory reports that have been generated by an inventory report configuration and retrieve their `REPORT_DETAIL_ID`, use the `gcloud storage insights inventory-reports details list` command:
         
         gcloud storage insights inventory-reports details list CONFIG_NAME \
           --filter=EXPRESSION \
           --page-size=SIZE \
           --sort-by=FIELD

Replace:

     * `CONFIG_NAME` with the unique name of the inventory report configuration, in the format `projects/PROJECT/locations/LOCATION/reportConfigs/REPORT_CONFIG_UUID`.

     * `EXPRESSION` with a boolean filter to apply to each resource item to be listed. If the expression evaluates True, then that item is listed. For more details and examples of filter expressions, run `$ gcloud topic filters`.

     * `SIZE` with the maximum number of resources per page. The default is 50.

     * `FIELD` with a comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with `~` for descending order on that field.

If successful, the command returns output similar to the following:
    
    REPORT_DETAIL_ID            SNAPSHOT_TIME
    Report_2023-04-10T00-00     2023-04-10T00:53:03Z
    Report_2023-04-12T00-00     2023-04-12T00:52:54Z
    Report_2023-04-05T00-00     2023-04-05T00:53:01Z

  2. To download an inventory report, you need to first retrieve the `reportPathPrefix` property of the ReportDetail object. To get the `reportPathPrefix` of a report, use the `gcloud storage insights inventory-reports details describe` command:
         
         gcloud storage insights inventory-reports details describe REPORT_DETAIL_NAME

Replace `REPORT_DETAIL_NAME` with the name of the inventory report in the format `projects/PROJECT/locations/LOCATION/reportConfigs/REPORT_CONFIG_UUID/reportDetails/REPORT_DETAIL_ID`.




### Download report shards

To download an inventory report that's been split into one or more [shards](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#shards), complete the following steps:

  1. Download the inventory report [manifest file](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#manifest-file) by using the `gcloud storage cp` command:
         
         gcloud storage cp gs://BUCKET_NAME/MANIFEST_FILE_NAME DOWNLOAD_PATH

Replace:

     * `BUCKET_NAME` with the name of the destination bucket.

     * `MANIFEST_FILE_NAME` with the name of the manifest file in the destination bucket, in the following naming convention:
           
           REPORT_CONFIG_UUID_TARGET_DATETIME_manifest.json

Where:

       * `REPORT_CONFIG_UUID` is the auto-generated UUID of the inventory report configuration that generated the report shards you want to download.

       * `TARGET_DATETIME` is the datetime at which the inventory report was generated.

For example, `fc95c52f-157a-494f-af4a-d4a53a69ba66_2022-11-30T00:00_manifest.json`.

     * `DOWNLOAD_PATH` with the path to your file system where you want to save the inventory report to. For example, `./example_report.csv`.

  2. To download a shard file, use the [`gcloud storage cp` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp):
         
         gcloud storage cp gs://BUCKET_NAME/SHARD_FILE_NAME DOWNLOAD_PATH

Replace:

     * `BUCKET_NAME` with the name of the destination bucket.

     * `SHARD_FILE_NAME` with the URL-encoded name of the shard file you want to download. For example, `fc95c52f-157a-494f-af4a-d4a53a69ba66_2022-11-30T00:54_0.csv`.

     * `DOWNLOAD_PATH` with the path to your file system where you want to save the inventory report to. For example, `./example_report.csv`.




### Client libraries

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storageinsights.v1.[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html);
    import com.google.cloud.storageinsights.v1.[ReportConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfigName.html);
    import com.google.cloud.storageinsights.v1.[ReportDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportDetail.html);
    import com.google.cloud.storageinsights.v1.[StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html);
    import java.io.IOException;
    
    public class GetInventoryReportNames {
    
    
      public static void getInventoryReportNames(
          String projectId, String location, String reportConfigUuid) throws IOException {
        try ([StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html) storageInsightsClient = [StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html).create()) {
          [ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html) config =
              storageInsightsClient.getReportConfig(
                  [ReportConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfigName.html).of(projectId, location, reportConfigUuid));
          String extension = config.[hasCsvOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html#com_google_cloud_storageinsights_v1_ReportConfig_hasCsvOptions__)() ? "csv" : "parquet";
          System.out.println(
              "You can use the Google Cloud Storage Client "
                  + "to download the following objects from Google Cloud Storage:");
          for ([ReportDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportDetail.html) reportDetail :
              storageInsightsClient.listReportDetails(config.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig.html#com_google_cloud_storageinsights_v1_ReportConfig_getName__)()).iterateAll()) {
            for (long index = reportDetail.getShardsCount() - 1; index >= 0; index--) {
              System.out.println(reportDetail.getReportPathPrefix() + index + "." + extension);
            }
          }
        }
      }
    }
    

### REST APIs

### JSON API

### Download individual reports

To download an inventory report, complete the following steps:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. List all the inventory reports generated by an inventory report configuration by using [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to list inventory report details](https://docs.cloud.google.com/storage/docs/insights/v1/reportDetail/list):
         
         curl --request GET \
         "https://storageinsights.googleapis.com/v1/projects/YOUR_PROJECT/locations/LOCATION/reportConfigs/REPORT_CONFIG_UUID/reportDetails/" \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json" \
         

Replace:

     * `YOUR_PROJECT` with the name of the project in which your source and destination buckets reside.

     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of the source and destination buckets. For example, `us-west1`.

     * `REPORT_CONFIG_UUID` with the auto-generated UUID of the inventory report configuration that generated the report you want to download.

  3. To get the details of an individual report, use `cURL` to call the JSON API with a [`Get` ReportDetails](https://docs.cloud.google.com/storage/docs/insights/v1/reportDetail/get) request:
         
         curl --request GET \
         "https://storageinsights.googleapis.com/v1/projects/YOUR_PROJECT/locations/LOCATION/reportConfigs/REPORT_CONFIG_UUID/reportDetails/REPORT_DETAIL_ID" \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json" \
         

Replace:

     * `YOUR_PROJECT` with the name of the project in which your source and destination buckets reside.

     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of the source and destination buckets. For example, `us-west1`.

     * `REPORT_CONFIG_UUID` with the auto-generated UUID of the inventory report configuration that generated the report you want to download.

     * `REPORT_DETAIL_ID` with the name of the inventory report you want to download.




### Download report shards

To download an inventory report that's been split into one or more [shards](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#shards), complete the following steps:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To download the [manifest file](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#manifest-file) of the inventory report, use `cURL` to call the JSON API with a [`GET` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) request:
         
         curl -X GET \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/MANIFEST_FILE_NAME?alt=media"

Replace:

     * `BUCKET_NAME` with the name of the destination bucket.

     * `MANIFEST_FILE_NAME` with the name of the manifest file in the destination bucket, in the following naming convention:
           
           REPORT_CONFIG_UUID_TARGET_DATETIME_manifest.json

Where:

       * `REPORT_CONFIG_UUID` is the auto-generated UUID of the inventory report configuration that generated the report shards you want to download.

       * `TARGET_DATETIME` is the date on which the inventory report was generated.

For example, `fc95c52f-157a-494f-af4a-d4a53a69ba66_2022-11-30T00:00_manifest.json`.

The `report_shards_file_names` field of the manifest file contains the names of the inventory report shards you can download.

  3. To download the inventory report shard files, use `curl` to call the Cloud Storage JSON API with a [`Get` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) request:
         
         curl -X GET \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           -o "DOWNLOAD_PATH" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/SHARD_FILE_NAME?alt=media"

Replace:

     * `DOWNLOAD_PATH` with the path to your local file system where you want to save your object. For example, `Desktop/dog.png`.

     * `BUCKET_NAME` with the name of the destination bucket containing the inventory report. For example, `my-bucket`.

     * `SHARD_FILE_NAME` with the URL-encoded name of the shard file you want to download. For example, `fc95c52f-157a-494f-af4a-d4a53a69ba66_2022-11-30T00:54_0.csv`.




## Delete an inventory report configuration

### Console

To delete an inventory report configuration, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the source bucket that contains the inventory report configuration you want to delete.

  3. In your source bucket's **Bucket details** page, click the **Inventory reports** tab.

  4. Click the configuration name of the inventory report configuration you want to delete.

  5. In the **Report configuration details** page that appears, click delete **Delete**.




### Command line

To delete an inventory report configuration, use the `gcloud storage insights inventory-reports delete` command:
    
    
    gcloud storage insights inventory-reports delete CONFIG_NAME
      --force

Replace `CONFIG_NAME` with the unique name of the inventory report configuration, in the format `projects/PROJECT/locations/LOCATION/reportConfigs/REPORT_CONFIG_UUID`.

The `--force` flag deletes the metadata for all inventory reports generated by the given inventory report configuration. The inventory report objects themselves are not deleted.

### Client libraries

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storageinsights.v1.[ReportConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfigName.html);
    import com.google.cloud.storageinsights.v1.[StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html);
    import java.io.IOException;
    
    public class DeleteInventoryReportConfig {
    
    
      public static void deleteInventoryReportConfig(
          String projectId, String location, String inventoryReportConfigUuid) throws IOException {
        try ([StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html) storageInsightsClient = [StorageInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsClient.html).create()) {
          [ReportConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfigName.html) name = [ReportConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfigName.html).of(projectId, location, inventoryReportConfigUuid);
          storageInsightsClient.deleteReportConfig(name);
    
          System.out.println("Deleted inventory report config with name " + name);
        }
      }
    }

### REST APIs

### JSON API

To delete an inventory report configuration, complete the following steps:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To delete an inventory report configuration, use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Delete` ReportConfig](https://docs.cloud.google.com/storage/docs/insights/v1/reportConfig/delete) request:
         
         curl --request DELETE \
         'https://storageinsights.googleapis.com/v1/projects/YOUR_PROJECT/locations/LOCATION/reportConfigs/REPORT_CONFIG_UUID?force=true' \
           --header 'Authorization: Bearer $(gcloud auth print-access-token)' \
           --header 'Accept: application/json' \
           --header 'Content-Type: application/json' \
         

Replace:

     * `YOUR_PROJECT` with the name of the project in which your source and destination buckets reside.

     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of the source and destination buckets. For example, `us-west1`.

     * `REPORT_CONFIG_UUID` with the auto-generated UUID of the inventory report configuration you want to delete.




The `force` query parameter deletes the metadata for all inventory reports generated by the given inventory report configuration. The inventory report objects themselves are not deleted.

## Advanced: Generate inventory reports in a Hive partitioned format

When you create an inventory report configuration, you can specify a destination path, which is a location in your destination bucket where inventory reports will be generated. This lets you generate inventory reports in a [Hive partitioned format](https://sparkbyexamples.com/apache-hive/hive-partitions-explained-with-examples/).

You specify a destination path by using placeholder keywords. Keywords in the destination path are substituted with their corresponding values when the inventory report is generated. For example, the destination path `config={{report-config-id}}/date={{date}}` can resolve to `config=1A34-F2E456-12B456-1C3D/date=2022-05-20`.

### Destination path keywords

You can specify the keywords `report-config-id`, `date`, or `datetime`, enclosed within {{ and }}, where:

  * `report-config-id` is the UUID of the inventory report configuration.

  * `date` is the date on which the inventory report is generated. Follows the ISO 8601 format.

  * `datetime` is the date and time on which the inventory report is generated. Follows the ISO 8601 format.




Keywords can be specified by using any of the following tools:

  * When using the Google Cloud console, specify keywords in the **Enter destination path (optional)** section. This section appears when you create an inventory report configuration.

  * When using the Google Cloud CLI, specify placeholder keywords by using the `--destination` flag.

  * When using the JSON API, specify placeholder keywords in the `storage_destination_options.destination_path` field of the ReportConfig object.




## Access control and security

The following recommendations and considerations relate to the security and usage of inventory reports and configurations:

  * We recommend that users with the `roles/storage.admin` role also have the `storageinsights.reportConfigs.*` permissions so they can maintain control over the usage of all resources in their buckets, such as the reading of objects and their metadata.

  * We recommend that you limit access to your inventory report resources by granting the `storageinsights.reportConfigs.*` permissions only to necessary individuals.

  * Once an inventory report configuration has been created, it continues to generate inventory reports even if the user who created the configuration no longer has the required permissions. To stop generating inventory reports, you can edit the end date in the inventory report configuration or delete the configuration entirely.




## What's next

  * If you encounter issues with generating inventory reports, refer to [Troubleshooting](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting#common-issues) for help.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
