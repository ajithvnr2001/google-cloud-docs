---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdminSettings-GetCluster-sync/
title: Configure API call retry settings \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:39.903230+00:00
---

# Configure API call retry settings  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdminSettings-GetCluster-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Configure API call retry settings Stay organized with collections  Save and categorize content based on your preferences. 

Customize the retry and timeout settings for a `getCluster` request. This allows you to fine-tune how the application handles transient errors when retrieving cluster information, improving its resilience.

## Code sample

### Java

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.alloydb.v1.[AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminSettings.html);
    import java.time.Duration;
    
    public class SyncGetCluster {
    
      public static void main(String[] args) throws Exception {
        syncGetCluster();
      }
    
      public static void syncGetCluster() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        [AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminSettings.html).Builder alloyDBAdminSettingsBuilder = [AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminSettings.html).newBuilder();
        alloyDBAdminSettingsBuilder
            .getClusterSettings()
            .setRetrySettings(
                alloyDBAdminSettingsBuilder
                    .getClusterSettings()
                    .getRetrySettings()
                    .toBuilder()
                    .setInitialRetryDelayDuration(Duration.ofSeconds(1))
                    .setInitialRpcTimeoutDuration(Duration.ofSeconds(5))
                    .setMaxAttempts(5)
                    .setMaxRetryDelayDuration(Duration.ofSeconds(30))
                    .setMaxRpcTimeoutDuration(Duration.ofSeconds(60))
                    .setRetryDelayMultiplier(1.3)
                    .setRpcTimeoutMultiplier(1.5)
                    .setTotalTimeoutDuration(Duration.ofSeconds(300))
                    .build());
        [AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminSettings.html) alloyDBAdminSettings = alloyDBAdminSettingsBuilder.build();
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
