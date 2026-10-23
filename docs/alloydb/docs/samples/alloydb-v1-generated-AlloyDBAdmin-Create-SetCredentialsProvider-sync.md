---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-Create-SetCredentialsProvider-sync/
title: Create a client with custom credentials \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:04.879124+00:00
---

# Create a client with custom credentials  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-Create-SetCredentialsProvider-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Create a client with custom credentials Stay organized with collections  Save and categorize content based on your preferences. 

This snippet shows how to create an administration client using a fixed credentials provider. Use this method when you need to provide credentials explicitly instead of relying on default application credentials.

## Code sample

### Java

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.core.[FixedCredentialsProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.FixedCredentialsProvider.html);
    import com.google.cloud.alloydb.v1.[AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html);
    import com.google.cloud.alloydb.v1.[AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminSettings.html);
    import com.google.cloud.alloydb.v1.myCredentials;
    
    public class SyncCreateSetCredentialsProvider {
    
      public static void main(String[] args) throws Exception {
        syncCreateSetCredentialsProvider();
      }
    
      public static void syncCreateSetCredentialsProvider() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        [AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminSettings.html) alloyDBAdminSettings =
            [AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminSettings.html).newBuilder()
                .setCredentialsProvider([FixedCredentialsProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.FixedCredentialsProvider.html).create(myCredentials))
                .build();
        [AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html) alloyDBAdminClient = [AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html).create(alloyDBAdminSettings);
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
