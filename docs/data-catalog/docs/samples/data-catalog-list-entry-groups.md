---
url: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-list-entry-groups/
title: List entry groups \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:52.273165+00:00
---

# List entry groups  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-list-entry-groups/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/data-catalog/docs/samples)



#  List entry groups Stay organized with collections  Save and categorize content based on your preferences. 

List existing entry groups.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/overview). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datacatalog.v1.[DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html);
    import com.google.cloud.datacatalog.v1.[ListEntryGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListEntryGroupsRequest.html);
    import com.google.cloud.datacatalog.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LocationName.html);
    import java.io.IOException;
    
    // Sample to get list of entry group
    public class ListEntryGroups {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        String location = "MY_LOCATION";
        [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LocationName.html) name = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LocationName.html).of(projectId, location);
        listEntryGroups(name);
      }
    
      public static void listEntryGroups([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LocationName.html) name) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html) client = [DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html).create()) {
          [ListEntryGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListEntryGroupsRequest.html) request =
              [ListEntryGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListEntryGroupsRequest.html).newBuilder().setParent(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LocationName.html#com_google_cloud_datacatalog_v1_LocationName_toString__)()).build();
          [DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html).[ListEntryGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.ListEntryGroupsPagedResponse.html) listEntryGroups =
              client.listEntryGroups(request);
          listEntryGroups
              .iterateAll()
              .forEach(
                  entryGroup -> {
                    System.out.println("Entry group name : " + entryGroup.getName());
                  });
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datacatalog). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
