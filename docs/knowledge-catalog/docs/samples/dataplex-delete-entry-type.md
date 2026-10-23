---
url: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-delete-entry-type/
title: Delete entry type \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:50.551662+00:00
---

# Delete entry type  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-delete-entry-type/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/knowledge-catalog/docs/samples)



#  Delete entry type Stay organized with collections  Save and categorize content based on your preferences. 

Delete an entry type.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[EntryTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryTypeName.html);
    
    public class DeleteEntryType {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        // Available locations: https://cloud.google.com/dataplex/docs/locations
        String location = "MY_LOCATION";
        String entryTypeId = "MY_ENTRY_TYPE_ID";
    
        deleteEntryType(projectId, location, entryTypeId);
        System.out.println("Successfully deleted entry type");
      }
    
      // Method to delete Entry Type located in projectId, location and with entryTypeId
      public static void deleteEntryType(String projectId, String location, String entryTypeId)
          throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) client = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [EntryTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryTypeName.html) entryTypeName = [EntryTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryTypeName.html).of(projectId, location, entryTypeId);
          client.[deleteEntryTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_deleteEntryTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_EntryTypeName_)(entryTypeName).get();
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def delete_entry_type(project_id: str, location: str, entry_type_id: str) -> None:
        """Method to delete Entry Type located in project_id, location and with entry_type_id"""
    
        # Initialize client that will be used to send requests across threads. This
        # client only needs to be created once, and can be reused for multiple requests.
        # After completing all of your requests, call the "__exit__()" method to safely
        # clean up any remaining background resources. Alternatively, use the client as
        # a context manager.
        with [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)() as client:
            # The resource name of the Entry Type
            name = f"projects/{project_id}/locations/{location}/entryTypes/{entry_type_id}"
            client.delete_entry_type(name=name)
    
    
    if __name__ == "__main__":
        # TODO(developer): Replace these variables before running the sample.
        project_id = "MY_PROJECT_ID"
        # Available locations: https://cloud.google.com/dataplex/docs/locations
        location = "MY_LOCATION"
        entry_type_id = "MY_ENTRY_TYPE_ID"
    
        delete_entry_type(project_id, location, entry_type_id)
        print("Successfully deleted entry type")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataplex). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
