---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-bigquery-export/
title: List BigQuery export configurations \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:12.000344+00:00
---

# List BigQuery export configurations  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-bigquery-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List BigQuery export configurations Stay organized with collections  Save and categorize content based on your preferences. 

List all the BigQuery export configurations in a given Google Cloud resource

## Code sample

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html);
    import com.google.cloud.securitycenter.v1.[ListBigQueryExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ListBigQueryExportsRequest.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).[ListBigQueryExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.ListBigQueryExportsPagedResponse.html);
    import java.io.IOException;
    
    public class ListBigQueryExports {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Modify the following variable values.
    
        // parent: The parent, which owns the collection of BigQuery exports.
        //         Use any one of the following resource paths:
        //              - organizations/{organization_id}
        //              - folders/{folder_id}
        //              - projects/{project_id}
        String parent = String.format("projects/%s", "your-google-cloud-project-id");
    
        listBigQueryExports(parent);
      }
    
      // List BigQuery exports in the given parent.
      public static void listBigQueryExports(String parent) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          [ListBigQueryExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ListBigQueryExportsRequest.html) request =
              [ListBigQueryExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ListBigQueryExportsRequest.html).newBuilder().setParent(parent).build();
    
          [ListBigQueryExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.ListBigQueryExportsPagedResponse.html) response = client.listBigQueryExports(request);
    
          System.out.println("Listing BigQuery exports:");
          for ([BigQueryExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BigQueryExport.html) bigQueryExport : response.iterateAll()) {
            System.out.println(bigQueryExport.getName());
          }
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_bigquery_exports(parent: str):
        from google.cloud import securitycenter
    
        """
        List BigQuery exports in the given parent.
        Args:
             parent: The parent which owns the collection of BigQuery exports.
                 Use any one of the following resource paths:
                     - organizations/{organization_id}
                     - folders/{folder_id}
                     - projects/{project_id}
        """
    
        client = securitycenter.SecurityCenterClient()
    
        request = securitycenter.[ListBigQueryExportsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListBigQueryExportsRequest.html)()
        request.parent = parent
    
        response = client.[list_big_query_exports](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_big_query_exports)(request)
    
        print("Listing BigQuery exports:")
        for bigquery_export in response:
            print(bigquery_export.name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
