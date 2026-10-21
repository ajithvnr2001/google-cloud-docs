---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-bigquery-export/
title: Get a BigQuery export configuration \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:59.236927+00:00
---

# Get a BigQuery export configuration  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-bigquery-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Get a BigQuery export configuration Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve an existing BigQuery export configuration

## Code sample

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html);
    import com.google.cloud.securitycenter.v1.[GetBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.GetBigQueryExportRequest.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class GetBigQueryExport {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Modify the following variable values.
    
        // parent: Use any one of the following resource paths:
        //              - organizations/{organization_id}
        //              - folders/{folder_id}
        //              - projects/{project_id}
        String parent = String.format("projects/%s", "your-google-cloud-project-id");
    
        // bigQueryExportId: Unique identifier that is used to identify the export.
        String bigQueryExportId = "export-id";
    
        getBigQueryExport(parent, bigQueryExportId);
      }
    
      // Retrieve an existing BigQuery export.
      public static void getBigQueryExport(String parent, String bigQueryExportId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          [GetBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.GetBigQueryExportRequest.html) bigQueryExportRequest =
              [GetBigQueryExportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.GetBigQueryExportRequest.html).newBuilder()
                  .setName(String.format("%s/bigQueryExports/%s", parent, bigQueryExportId))
                  .build();
    
          [BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html) response = client.getBigQueryExport(bigQueryExportRequest);
          System.out.printf("Retrieved the BigQuery export: %s", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html#com_google_cloud_securitycenter_v1_BigQueryExport_getName__)());
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_bigquery_export(parent: str, bigquery_export_id: str):
        from google.cloud import securitycenter
    
        """
        Retrieve an existing BigQuery export.
        Args:
            parent: Use any one of the following resource paths:
                     - organizations/{organization_id}
                     - folders/{folder_id}
                     - projects/{project_id}
            bigquery_export_id: Unique identifier that is used to identify the export.
        """
    
        client = securitycenter.SecurityCenterClient()
    
        request = securitycenter.[GetBigQueryExportRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetBigQueryExportRequest.html)()
        request.name = f"{parent}/bigQueryExports/{bigquery_export_id}"
    
        response = client.[get_big_query_export](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_big_query_export)(request)
        print(f"Retrieved the BigQuery export: {response.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
