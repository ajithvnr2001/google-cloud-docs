---
url: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-lookup-entry/
title: Lookup entry \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:58.935023+00:00
---

# Lookup entry  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-lookup-entry/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/knowledge-catalog/docs/samples)



#  Lookup entry Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve an existing entry.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html);
    import com.google.cloud.dataplex.v1.[EntryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryName.html);
    import com.google.cloud.dataplex.v1.[EntryView](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryView.html);
    import com.google.cloud.dataplex.v1.[LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryRequest.html);
    import java.io.IOException;
    
    public class LookupEntry {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        // Available locations: https://cloud.google.com/dataplex/docs/locations
        String location = "MY_LOCATION";
        String entryGroupId = "MY_ENTRY_GROUP_ID";
        String entryId = "MY_ENTRY_ID";
    
        [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) entry = lookupEntry(projectId, location, entryGroupId, entryId);
        System.out.println("Entry retrieved successfully: " + entry.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html#com_google_cloud_dataplex_v1_Entry_getName__)());
        entry
            .getAspectsMap()
            .keySet()
            .forEach(aspectKey -> System.out.println("Retrieved aspect for entry: " + aspectKey));
      }
    
      // Method to retrieve Entry located in projectId, location, entryGroupId and with entryId
      // When Entry is created in Dataplex for example for BigQuery table,
      // access permissions might differ between Dataplex and source system.
      // "Lookup" method checks permissions in source system.
      // Please also refer how to get an Entry, which checks permissions in Dataplex.
      public static [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) lookupEntry(
          String projectId, String location, String entryGroupId, String entryId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) client = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          String projectLocation = String.format("projects/%s/locations/%s", projectId, location);
          [LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryRequest.html) lookupEntryRequest =
              [LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryRequest.html).newBuilder()
                  // The project to which the request should be attributed
                  .setName(projectLocation)
                  // The resource name of the Entry
                  .setEntry([EntryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryName.html).of(projectId, location, entryGroupId, entryId).toString())
                  // View determines which Aspects are returned with the Entry.
                  // For all available options, see:
                  // https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/lookup#--view
                  .setView([EntryView](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryView.html).FULL)
                  // Following 2 lines will be ignored, because "View" is set to FULL.
                  // Their purpose is to demonstrate how to filter the Aspects returned for Entry
                  // when "View" is set to CUSTOM.
                  .addAspectTypes("projects/dataplex-types/locations/global/aspectTypes/generic")
                  .addPaths("my_path")
                  .build();
          return client.lookupEntry(lookupEntryRequest);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def lookup_entry(
        project_id: str, location: str, entry_group_id: str, entry_id: str
    ) -> dataplex_v1.Entry:
        """Method to retrieve Entry located in project_id, location, entry_group_id and with entry_id
    
        When Entry is created in Dataplex for example for BigQuery table,
        access permissions might differ between Dataplex and source system.
        "Lookup" method checks permissions in source system.
        Please also refer how to get an Entry, which checks permissions in Dataplex.
        """
    
        # Initialize client that will be used to send requests across threads. This
        # client only needs to be created once, and can be reused for multiple requests.
        # After completing all of your requests, call the "__exit__()" method to safely
        # clean up any remaining background resources. Alternatively, use the client as
        # a context manager.
        with [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)() as client:
            lookup_entry_request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[LookupEntryRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.LookupEntryRequest.html)(
                # The project to which the request should be attributed
                name=f"projects/{project_id}/locations/{location}",
                # The resource name of the Entry
                entry=f"projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}",
                # View determines which Aspects are returned with the Entry.
                # For all available options, see:
                # https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/lookup#--view
                view=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryView](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryView.html).FULL,
                # Following 2 lines will be ignored, because "View" is set to FULL.
                # Their purpose is to demonstrate how to filter the Aspects returned for Entry
                # when "View" is set to CUSTOM.
                aspect_types=[
                    "projects/dataplex-types/locations/global/aspectTypes/generic"
                ],
                paths=["my_path"],
            )
            return client.lookup_entry(request=lookup_entry_request)
    
    
    if __name__ == "__main__":
        # TODO(developer): Replace these variables before running the sample.
        project_id = "MY_PROJECT_ID"
        # Available locations: https://cloud.google.com/dataplex/docs/locations
        location = "MY_LOCATION"
        entry_group_id = "MY_ENTRY_GROUP_ID"
        entry_id = "MY_ENTRY_ID"
    
        entry = lookup_entry(project_id, location, entry_group_id, entry_id)
        print(f"Entry retrieved successfully: {entry.name}")
        for aspect_key in entry.aspects.keys():
            print(f"Retrieved aspect for entry: {aspect_key}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataplex). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
