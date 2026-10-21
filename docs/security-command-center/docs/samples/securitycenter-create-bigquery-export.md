---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-bigquery-export/
title: Create a BigQuery export configuration \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:34.266297+00:00
---

# Create a BigQuery export configuration  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-bigquery-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Create a BigQuery export configuration Stay organized with collections  Save and categorize content based on your preferences. 

Export findings from a project to a BigQuery dataset by creating an export configuration

## Code sample

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html);
    import com.google.cloud.securitycenter.v1.[CreateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.CreateBigQueryExportRequest.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import java.io.IOException;
    import java.util.UUID;
    
    public class CreateBigQueryExport {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Modify the following variable values.
    
        // parent: Use any one of the following resource paths:
        //              - organizations/{organization_id}
        //              - folders/{folder_id}
        //              - projects/{project_id}
        String parent = String.format("projects/%s", "your-google-cloud-project-id");
    
        // filter: Expression that defines the filter to apply across create/update events of findings.
        String filter =
            "severity=\"LOW\" OR severity=\"MEDIUM\" AND "
                + "category=\"Persistence: IAM Anomalous Grant\" AND "
                + "-resource.type:\"compute\"";
    
        // bigQueryDatasetId: The BigQuery dataset to write findings' updates to.
        String bigQueryDatasetId = "your-bigquery-dataset-id";
    
        // bigQueryExportId: Unique identifier provided by the client.
        // For more info, see:
        // https://cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query#export_findings_from_to
        String bigQueryExportId = "default-" + UUID.randomUUID().toString().split("-")[0];
    
        createBigQueryExport(parent, filter, bigQueryDatasetId, bigQueryExportId);
      }
    
      // Create export configuration to export findings from a project to a BigQuery dataset.
      // Optionally specify filter to export certain findings only.
      public static void createBigQueryExport(
          String parent, String filter, String bigQueryDatasetId, String bigQueryExportId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          // Create the BigQuery export configuration.
          [BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html) bigQueryExport =
              [BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html).newBuilder()
                  .setDescription(
                      "Export low and medium findings if the compute resource "
                          + "has an IAM anomalous grant")
                  .setFilter(filter)
                  .[setDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.Builder.html#com_google_cloud_securitycenter_v1_BigQueryExport_Builder_setDataset_java_lang_String_)(String.format("%s/datasets/%s", parent, bigQueryDatasetId))
                  .build();
    
          [CreateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.CreateBigQueryExportRequest.html) bigQueryExportRequest =
              [CreateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.CreateBigQueryExportRequest.html).newBuilder()
                  .setParent(parent)
                  .setBigQueryExport(bigQueryExport)
                  .[setBigQueryExportId](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.CreateBigQueryExportRequest.Builder.html#com_google_cloud_securitycenter_v1_CreateBigQueryExportRequest_Builder_setBigQueryExportId_java_lang_String_)(bigQueryExportId)
                  .build();
    
          // Create the export request.
          [BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html) response = client.createBigQueryExport(bigQueryExportRequest);
    
          System.out.printf("BigQuery export request created successfully: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html#com_google_cloud_securitycenter_v1_BigQueryExport_getName__)());
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    
    def create_bigquery_export(
        parent: str, export_filter: str, bigquery_dataset_id: str, bigquery_export_id: str
    ):
        from google.cloud import securitycenter
    
        """
        Create export configuration to export findings from a project to a BigQuery dataset.
        Optionally specify filter to export certain findings only.
    
        Args:
            parent: Use any one of the following resource paths:
                 - organizations/{organization_id}
                 - folders/{folder_id}
                 - projects/{project_id}
            export_filter: Expression that defines the filter to apply across create/update events of findings.
            bigquery_dataset_id: The BigQuery dataset to write findings' updates to.
            bigquery_export_id: Unique identifier provided by the client.
                 - example id: f"default-{str(uuid.uuid4()).split('-')[0]}"
            For more info, see:
            https://cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query#export_findings_from_to
        """
        client = securitycenter.SecurityCenterClient()
    
        # Create the BigQuery export configuration.
        bigquery_export = securitycenter.[BigQueryExport](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BigQueryExport.html)()
        bigquery_export.description = "Export low and medium findings if the compute resource has an IAM anomalous grant"
        bigquery_export.filter = export_filter
        bigquery_export.dataset = f"{parent}/datasets/{bigquery_dataset_id}"
    
        request = securitycenter.[CreateBigQueryExportRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateBigQueryExportRequest.html)()
        request.parent = parent
        request.big_query_export = bigquery_export
        request.big_query_export_id = bigquery_export_id
    
        # Create the export request.
        response = client.[create_big_query_export](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_big_query_export)(request)
    
        print(f"BigQuery export request created successfully: {response.name}\n")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
