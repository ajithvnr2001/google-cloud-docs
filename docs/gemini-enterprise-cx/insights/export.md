---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/export/
title: Export conversations to BigQuery \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:09.451328+00:00
---

# Export conversations to BigQuery  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Export conversations to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

Customer Experience Insights (CX Insights) lets you export your CX Insights conversation and analysis data to BigQuery so that you can perform your own raw queries. The export process writes a [schema](https://docs.cloud.google.com/gemini-enterprise-cx/insights/bigquery-all-schemas) that is similar to the speech analysis framework. This guide details the export process.

## Create a new BigQuery table and dataset

The CX Insights exporter requires a BigQuery table in order for the operation to be successful. If you don't have a target table, use this sample to create a new table and dataset using the [bq command-line tool](https://docs.cloud.google.com/bigquery/docs/quickstarts/load-data-bq).

You don't need to specify a schema for your table because the export process writes one. However, if you do specify a schema, you must explicitly define the version. The `EXPORT_VERSION_LATEST_AVAILABLE` command doesn't reliably provide the most recent version and might remove columns from your table. Sending a query with a schema but no version provides an early version by default. See the [BigQuery schema documentation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/bigquery-all-schemas) for the output schema and column definitions.

BigQuery has some restrictions on the location of its data source. See [Location considerations](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#data-locations). Restrictions that apply to Cloud Storage buckets also apply to CX Insights. For example, if your BigQuery dataset is in the `EU` multi-region location, you can only export CX Insights data from one of the `europe-*` locations.

**Warning:** CX Insights export will [truncate](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#truncate_table_statement) any data in the provided table before writing.
    
    
    bq mk --dataset --location=LOCATION PROJECT:DATASET
    
    bq mk --table PROJECT:DATASET.TABLE
    

## Export conversation data to BigQuery

The export tool supports both filtering and writing data to [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption)-protected tables. If you don't want to enable this feature, you can skip ahead and [export your data to BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/insights/export#export_your_data_to_bigquery).

### Add filtering to the request (Optional)

Export to BigQuery is compatible with all combinations of filters that can be applied to [conversation queries](https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-ui). For example, the following sample will export all conversations with 10 or more turns handled by `agent_id` "007" between January 1st 2021 and January 2nd 2021 PST:

`FILTER='create_time>"2021-01-01T00:00:00-08:00" create_time<"2021-01-02T00:00:00-08:00" agent_id="007" turn_count>="10"'`

### Export data to a CMEK-protected table (Optional)

Provide your CX Insights service account with the [_Cloud KMS CryptoKey Encrypter/Decrypter_ role](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption#assign_role). See the [known issues documentation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/known-issues) about service account format. Once you have provided the correct role to your service account, add the fully-qualified name of the KMS key protecting the table to the export request:

`KMS_KEY='projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<key_name>'`

### Specify write disposition option in the request (Optional)

CCAI Insights export supports the following [write disposition options from BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationquery):

  * `WRITE_TRUNCATE`: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result. This is the default option.
  * `WRITE_APPEND`: If the table already exists, BigQuery appends the data to the table.



For example, the following sample will append the exported data to an existing destination table:

`WRITE_DISPOSITION='WRITE_APPEND'`

### Export your data to BigQuery

The following code sample demonstrates how to export your data. See the [export reference documentation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.insightsdata/export) for complete details.

The export creates a long-running `Operation` object. You can [poll the operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/long-running-operations) to check its status.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.conversations.list` on the parent resource



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * DATASET: the name of the BigQuery dataset that the data should be exported to.
  * TABLE: the BigQuery table name that your CX Insights data should be written to.
  * FILTER_QUERY: a query that CX Insights uses to export only conversations that have specific properties. For example, entering the value "agent_id=\"007\"" will result in only conversations associated with agent 007 being exported.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/insightsdata:export

Request JSON body: 
    
    
    {
      "bigQueryDestination": {
        "projectId": "PROJECT_ID",
        "dataset": "DATASET",
        "table": "TABLE",
      },
      "filter": "FILTER_QUERY"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/insightsdata:export"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/insightsdata:export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID"
    }
    

### Python

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest)
    
    
    def export_to_bigquery(
        project_id: str,
        bigquery_project_id: str,
        bigquery_dataset_id: str,
        bigquery_table_id: str,
    ) -> None:
        """Exports data to BigQuery.
    
        Args:
            project_id:
                The project identifier that owns the data source to be exported.
                For example, 'my-project'.
            bigquery_project_id:
                The project identifier that owns the BigQuery sink to export data to.
                For example, 'my-project'.
            bigquery_dataset_id:
                The BigQuery dataset identifier. For example, 'my-dataset'.
            bigquery_table_id:
                The BigQuery table identifier. For example, 'my-table'.
    
        Returns:
            None.
        """
        # Construct an export request.
        request = [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[ExportInsightsDataRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ExportInsightsDataRequest.html)()
        request.parent = (
            [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[ContactCenterInsightsClient](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html).common_location_path(
                project_id, "us-central1"
            )
        )
        request.big_query_destination.project_id = bigquery_project_id
        request.big_query_destination.dataset = bigquery_dataset_id
        request.big_query_destination.table = bigquery_table_id
        request.filter = 'agent_id="007"'
    
        # Call the Insights client to export data to BigQuery.
        insights_client = [contact_center_insights_v1](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest).[ContactCenterInsightsClient](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html)()
        export_operation = insights_client.[export_insights_data](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.services.contact_center_insights.ContactCenterInsightsClient.html#google_cloud_contact_center_insights_v1_services_contact_center_insights_ContactCenterInsightsClient_export_insights_data)(request=request)
        export_operation.result(timeout=600000)
        print("Exported data to BigQuery")
    
    

### Java

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.contactcenterinsights.v1.[ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html);
    import com.google.cloud.contactcenterinsights.v1.[ContactCenterInsightsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsSettings.html);
    import com.google.cloud.contactcenterinsights.v1.[ExportInsightsDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataRequest.html);
    import com.google.cloud.contactcenterinsights.v1.[ExportInsightsDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataResponse.html);
    import com.google.cloud.contactcenterinsights.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html);
    import java.io.IOException;
    import org.threeten.bp.Duration;
    
    public class ExportToBigquery {
    
      public static void main(String[] args) throws Exception, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my_project_id";
        String bigqueryProjectId = "my_bigquery_project_id";
        String bigqueryDataset = "my_bigquery_dataset";
        String bigqueryTable = "my_bigquery_table";
    
        exportToBigquery(projectId, bigqueryProjectId, bigqueryDataset, bigqueryTable);
      }
    
      public static void exportToBigquery(
          String projectId, String bigqueryProjectId, String bigqueryDataset, String bigqueryTable)
          throws Exception, IOException {
        // Set the operation total polling timeout to 24 hours instead of the 5-minute default.
        // Other values are copied from the default values of {@link ContactCenterInsightsStubSettings}.
        [ContactCenterInsightsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsSettings.html).Builder clientSettings =
            [ContactCenterInsightsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsSettings.html).newBuilder();
        clientSettings
            .exportInsightsDataOperationSettings()
            .setPollingAlgorithm(
                [OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html).create(
                    [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                        .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(5000L))
                        .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(1.5)
                        .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(45000L))
                        .[setInitialRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRpcTimeout_org_threeten_bp_Duration_)(Duration.ZERO)
                        .[setRpcTimeoutMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRpcTimeoutMultiplier_double_)(1.0)
                        .[setMaxRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRpcTimeout_org_threeten_bp_Duration_)(Duration.ZERO)
                        .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(Duration.ofHours(24L))
                        .build()));
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html) client =
            [ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html).create(clientSettings.build())) {
          // Construct an export request.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html).of(projectId, "us-central1");
          [ExportInsightsDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataRequest.html) request =
              [ExportInsightsDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html#com_google_cloud_contactcenterinsights_v1_LocationName_toString__)())
                  .[setBigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataRequest.Builder.html#com_google_cloud_contactcenterinsights_v1_ExportInsightsDataRequest_Builder_setBigQueryDestination_com_google_cloud_contactcenterinsights_v1_ExportInsightsDataRequest_BigQueryDestination_)(
                      [ExportInsightsDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataRequest.html).BigQueryDestination.newBuilder()
                          .[setProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataRequest.BigQueryDestination.Builder.html#com_google_cloud_contactcenterinsights_v1_ExportInsightsDataRequest_BigQueryDestination_Builder_setProjectId_java_lang_String_)(bigqueryProjectId)
                          .[setDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataRequest.BigQueryDestination.Builder.html#com_google_cloud_contactcenterinsights_v1_ExportInsightsDataRequest_BigQueryDestination_Builder_setDataset_java_lang_String_)(bigqueryDataset)
                          .[setTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataRequest.BigQueryDestination.Builder.html#com_google_cloud_contactcenterinsights_v1_ExportInsightsDataRequest_BigQueryDestination_Builder_setTable_java_lang_String_)(bigqueryTable)
                          .build())
                  .setFilter("agent_id=\"007\"")
                  .build();
    
          // Call the Insights client to export data to BigQuery.
          [ExportInsightsDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataResponse.html) response = client.[exportInsightsDataAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html#com_google_cloud_contactcenterinsights_v1_ContactCenterInsightsClient_exportInsightsDataAsync__org_jspecify_annotations_Nullable_com_google_cloud_contactcenterinsights_v1_LocationName_)(request).[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          System.out.printf("Exported data to BigQuery");
        }
      }
    }
    

### Node.js

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my_project_id';
    // const bigqueryProjectId = 'my_bigquery_project_id';
    // const bigqueryDataset = 'my_bigquery_dataset';
    // const bigqueryTable = 'my_bigquery_table';
    
    // Imports the Contact Center Insights client.
    const {
      ContactCenterInsightsClient,
    } = require('[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [ContactCenterInsightsClient](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)();
    
    async function exportToBigquery() {
      const [operation] = await client.exportInsightsData({
        parent: client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/v1.contactcenterinsightsclient.html)(projectId, 'us-central1'),
        bigQueryDestination: {
          projectId: bigqueryProjectId,
          dataset: bigqueryDataset,
          table: bigqueryTable,
        },
        filter: 'agent_id="007"',
      });
    
      // Wait for the operation to complete.
      await operation.promise();
      console.info('Exported data to BigQuery');
    }
    exportToBigquery();

#### Export data to another project (Optional)

By default, CX Insights BigQuery export writes data to the same project that owns the CX Insights data. However, you can also export to BigQuery in another project.

Ensure that your CX Insights service account has BigQuery access to the recipient project using either the Identity and Access Management (IAM) console or with `gcloud`:
    
    
    gcloud projects add-iam-policy-binding RECEIVER_PROJECT \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-contactcenterinsights.iam.gserviceaccount.com \
        --role=roles/bigquery.admin
    

**Note:** If you want to restrict access further, you can also grant the service account access to a specific BigQuery dataset.

To export your data to a specific project, input the recipient project's ID number in the `project_id` field in the [`BigQueryDestination`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.insightsdata/export#BigQueryDestination) object.

## Query the data in BigQuery

Run this command to query the data in BigQuery. See the [BigQuery Quickstart](https://docs.cloud.google.com/bigquery/docs/quickstarts/load-data-bq) documentation for more query options:
    
    
    gcloud config set project PROJECT
    bq show DATASET.TABLE
    

Querying exported conversations:
    
    
    bq query --use_legacy_sql=false \
       "SELECT conversationName FROM DATASET.TABLE"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
