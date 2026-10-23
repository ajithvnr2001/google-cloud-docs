---
url: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-update-entry/
title: Update entry (with aspect update) \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:52.384198+00:00
---

# Update entry (with aspect update)  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-update-entry/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/knowledge-catalog/docs/samples)



#  Update entry (with aspect update) Stay organized with collections  Save and categorize content based on your preferences. 

Update an entry and its aspects.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage aspects and enrich metadata](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[Aspect](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Aspect.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html);
    import com.google.cloud.dataplex.v1.[EntryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryName.html);
    import com.google.cloud.dataplex.v1.[EntrySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntrySource.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.[Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import java.util.Map;
    
    public class UpdateEntry {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        // Available locations: https://cloud.google.com/dataplex/docs/locations
        String location = "MY_LOCATION";
        String entryGroupId = "MY_ENTRY_GROUP_ID";
        String entryId = "MY_ENTRY_ID";
    
        [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) createdEntry = updateEntry(projectId, location, entryGroupId, entryId);
        System.out.println("Successfully updated entry: " + createdEntry.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html#com_google_cloud_dataplex_v1_Entry_getName__)());
      }
    
      // Method to update Entry located in projectId, location, entryGroupId and with entryId
      public static [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) updateEntry(
          String projectId, String location, String entryGroupId, String entryId) throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) client = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) entry =
              [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html).newBuilder()
                  .setName([EntryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryName.html).of(projectId, location, entryGroupId, entryId).toString())
                  .setEntrySource(
                      [EntrySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntrySource.html).newBuilder()
                          .setDescription("updated description of the entry")
                          .build())
                  .putAllAspects(
                      Map.of(
                          "dataplex-types.global.generic",
                          [Aspect](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Aspect.html).newBuilder()
                              .setAspectType(
                                  "projects/dataplex-types/locations/global/aspectTypes/generic")
                              .setData(
                                  [Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html).newBuilder()
                                      // "Generic" Aspect Type have fields called "type" and "system.
                                      // The values below are a sample of possible options.
                                      .putFields(
                                          "type",
                                          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder()
                                              .setStringValue("updated example value")
                                              .build())
                                      .putFields(
                                          "system",
                                          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder()
                                              .setStringValue("updated example system")
                                              .build())
                                      .build())
                              .build()))
                  .build();
    
          // Update mask specifies which fields will be updated.
          // For more information on update masks, see: https://google.aip.dev/161
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().addPaths("aspects").addPaths("entry_source.description").build();
          return client.updateEntry(entry, updateMask);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    from google.protobuf import struct_pb2
    
    
    def update_entry(
        project_id: str, location: str, entry_group_id: str, entry_id: str
    ) -> dataplex_v1.Entry:
        """Method to update Entry located in project_id, location, entry_group_id and with entry_id"""
    
        # Initialize client that will be used to send requests across threads. This
        # client only needs to be created once, and can be reused for multiple requests.
        # After completing all of your requests, call the "__exit__()" method to safely
        # clean up any remaining background resources. Alternatively, use the client as
        # a context manager.
        with [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)() as client:
            # The resource name of the Entry
            name = f"projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}"
            entry = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entry.html)(
                name=name,
                entry_source=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).EntrySource(
                    description="updated description of the entry"
                ),
                aspects={
                    "dataplex-types.global.generic": [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Aspect](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Aspect.html)(
                        aspect_type="projects/dataplex-types/locations/global/aspectTypes/generic",
                        data=struct_pb2.Struct(
                            fields={
                                # "Generic" Aspect Type have fields called "type" and "system.
                                # The values below are a sample of possible options.
                                "type": struct_pb2.Value(
                                    string_value="updated example value"
                                ),
                                "system": struct_pb2.Value(
                                    string_value="updated example system"
                                ),
                            }
                        ),
                    )
                },
            )
    
            # Update mask specifies which fields will be updated.
            # For more information on update masks, see: https://google.aip.dev/161
            update_mask = {"paths": ["aspects", "entry_source.description"]}
            return client.update_entry(entry=entry, update_mask=update_mask)
    
    
    if __name__ == "__main__":
        # TODO(developer): Replace these variables before running the sample.
        project_id = "MY_PROJECT_ID"
        # Available locations: https://cloud.google.com/dataplex/docs/locations
        location = "MY_LOCATION"
        entry_group_id = "MY_ENTRY_GROUP_ID"
        entry_id = "MY_ENTRY_ID"
    
        updated_entry = update_entry(project_id, location, entry_group_id, entry_id)
        print(f"Successfully updated entry: {updated_entry.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataplex). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
