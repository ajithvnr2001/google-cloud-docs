---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-bigquery-export/
title: Update a BigQuery export configuration \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:37.165339+00:00
---

# Update a BigQuery export configuration  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-bigquery-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Update a BigQuery export configuration Stay organized with collections  Save and categorize content based on your preferences. 

Update an existing BigQuery export configuration

## Code sample

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v1.[UpdateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.UpdateBigQueryExportRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateBigQueryExport {
    
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
    
        // bigQueryExportId: Unique identifier provided by the client.
        // For more info, see:
        // https://cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query#export_findings_from_to
        String bigQueryExportId = "big-query-export-id";
    
        updateBigQueryExport(parent, filter, bigQueryExportId);
      }
    
      // Updates an existing BigQuery export.
      public static void updateBigQueryExport(String parent, String filter, String bigQueryExportId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          //  Set the new values for export configuration.
          [BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html) bigQueryExport =
              [BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html).newBuilder()
                  .setName(String.format("%s/bigQueryExports/%s", parent, bigQueryExportId))
                  .setFilter(filter)
                  .build();
    
          [UpdateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.UpdateBigQueryExportRequest.html) request =
              [UpdateBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.UpdateBigQueryExportRequest.html).newBuilder()
                  .setBigQueryExport(bigQueryExport)
                  // Set the update mask to specify which properties should be updated.
                  // If empty, all mutable fields will be updated.
                  // For more info on constructing field mask path, see the proto or:
                  // https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("filter").build())
                  .build();
    
          [BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html) response = client.updateBigQueryExport(request);
          if (!response.[getFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html#com_google_cloud_securitycenter_v1_BigQueryExport_getFilter__)().equalsIgnoreCase(filter)) {
            System.out.println("Failed to update BigQueryExport!");
            return;
          }
          System.out.println("BigQueryExport updated successfully!");
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_bigquery_export(parent: str, export_filter: str, bigquery_export_id: str):
        """
        Updates an existing BigQuery export.
        Args:
            parent: Use any one of the following resource paths:
                     - organizations/{organization_id}
                     - folders/{folder_id}
                     - projects/{project_id}
            export_filter: Expression that defines the filter to apply across create/update events of findings.
            bigquery_export_id: Unique identifier provided by the client.
            For more info, see:
            https://cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query#export_findings_from_to
        """
        from google.cloud import securitycenter
        from google.protobuf import field_mask_pb2
    
        client = securitycenter.SecurityCenterClient()
    
        # Set the new values for export configuration.
        bigquery_export = securitycenter.[BigQueryExport](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BigQueryExport.html)()
        bigquery_export.name = f"{parent}/bigQueryExports/{bigquery_export_id}"
        bigquery_export.filter = export_filter
    
        # Field mask to only update the export filter.
        # Set the update mask to specify which properties should be updated.
        # If empty, all mutable fields will be updated.
        # For more info on constructing field mask path, see the proto or:
        # https://googleapis.dev/python/protobuf/latest/google/protobuf/field_mask_pb2.html
        field_mask = field_mask_pb2.FieldMask(paths=["filter"])
    
        request = securitycenter.[UpdateBigQueryExportRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateBigQueryExportRequest.html)()
        request.big_query_export = bigquery_export
        request.update_mask = field_mask
    
        response = client.[update_big_query_export](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_big_query_export)(request)
    
        if response.filter != export_filter:
            print("Failed to update BigQueryExport!")
            return
        print("BigQueryExport updated successfully!")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
