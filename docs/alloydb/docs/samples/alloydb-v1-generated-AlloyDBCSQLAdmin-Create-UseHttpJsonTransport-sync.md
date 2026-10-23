---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBCSQLAdmin-Create-UseHttpJsonTransport-sync/
title: Create a client with HTTP/JSON transport \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:53.900221+00:00
---

# Create a client with HTTP/JSON transport  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBCSQLAdmin-Create-UseHttpJsonTransport-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Create a client with HTTP/JSON transport Stay organized with collections  Save and categorize content based on your preferences. 

Initialize an Admin client configured to use the HTTP/JSON transport protocol instead of the default gRPC. This is useful for environments where gRPC is not supported or is blocked, such as certain web proxies or firewalls.

## Code sample

### Java

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.alloydb.v1.[AlloyDBCSQLAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBCSQLAdminClient.html);
    import com.google.cloud.alloydb.v1.[AlloyDBCSQLAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBCSQLAdminSettings.html);
    
    public class SyncCreateUseHttpJsonTransport {
    
      public static void main(String[] args) throws Exception {
        syncCreateUseHttpJsonTransport();
      }
    
      public static void syncCreateUseHttpJsonTransport() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        [AlloyDBCSQLAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBCSQLAdminSettings.html) alloyDBCSQLAdminSettings =
            [AlloyDBCSQLAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBCSQLAdminSettings.html).newHttpJsonBuilder().build();
        [AlloyDBCSQLAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBCSQLAdminClient.html) alloyDBCSQLAdminClient =
            [AlloyDBCSQLAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBCSQLAdminClient.html).create(alloyDBCSQLAdminSettings);
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
