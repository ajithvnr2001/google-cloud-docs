---
url: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-quickstart/
title: Quickstart: manage metadata \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:12.118227+00:00
---

# Quickstart: manage metadata  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-quickstart/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/knowledge-catalog/docs/samples)



#  Quickstart: manage metadata Stay organized with collections  Save and categorize content based on your preferences. 

Code sample to demonstrate lifecycle of different metadata management resources and their interactions. Create aspect type, entry type, entry group and entry, retrieve entry and clean up created resources.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[Aspect](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Aspect.html);
    import com.google.cloud.dataplex.v1.[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html);
    import com.google.cloud.dataplex.v1.[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup.html);
    import com.google.cloud.dataplex.v1.[EntryGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroupName.html);
    import com.google.cloud.dataplex.v1.[EntryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryName.html);
    import com.google.cloud.dataplex.v1.[EntrySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntrySource.html);
    import com.google.cloud.dataplex.v1.[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType.html);
    import com.google.cloud.dataplex.v1.[EntryView](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryView.html);
    import com.google.cloud.dataplex.v1.[GetEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryRequest.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    import com.google.cloud.dataplex.v1.[SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.html);
    import com.google.cloud.dataplex.v1.[SearchEntriesResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesResult.html);
    import com.google.protobuf.[Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    import java.util.stream.Collectors;
    
    public class Quickstart {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        // Available locations: https://cloud.google.com/dataplex/docs/locations
        String location = "MY_LOCATION";
        // Variables below can be replaced with custom values or defaults can be kept
        String aspectTypeId = "dataplex-quickstart-aspect-type";
        String entryTypeId = "dataplex-quickstart-entry-type";
        String entryGroupId = "dataplex-quickstart-entry-group";
        String entryId = "dataplex-quickstart-entry";
    
        quickstart(projectId, location, aspectTypeId, entryTypeId, entryGroupId, entryId);
      }
    
      // Method to demonstrate lifecycle of different Dataplex resources and their interactions.
      // Method creates Aspect Type, Entry Type, Entry Group and Entry, retrieves Entry
      // and cleans up created resources.
      public static void quickstart(
          String projectId,
          String location,
          String aspectTypeId,
          String entryTypeId,
          String entryGroupId,
          String entryId) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) client = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          // 0) Prepare variables used in following steps
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html) globalLocationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of(projectId, "global");
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html) specificLocationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of(projectId, location);
    
          // 1) Create Aspect Type that will be attached to Entry Type
          [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.html) aspectField =
              [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.newBuilder()
                  // The name must follow regex ^(([a-zA-Z]{1})([\\w\\-_]{0,62}))$
                  // That means name must only contain alphanumeric character or dashes or underscores,
                  // start with an alphabet, and must be less than 63 characters.
                  .setName("example_field")
                  // Metadata Template is recursive structure,
                  // primitive types such as "string" or "integer" indicate leaf node,
                  // complex types such as "record" or "array" would require nested Metadata Template
                  .setType("string")
                  .setIndex(1)
                  .[setAnnotations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Builder_setAnnotations_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Annotations_)(
                      [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.Annotations.newBuilder()
                          .setDescription("example field to be filled during entry creation")
                          .build())
                  .[setConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Builder_setConstraints_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Constraints_)(
                      [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.Constraints.newBuilder()
                          // Specifies if field will be required in Aspect Type.
                          .[setRequired](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Constraints.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Constraints_Builder_setRequired_boolean_)(true)
                          .build())
                  .build();
          [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) aspectType =
              [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).newBuilder()
                  .setDescription("aspect type for dataplex quickstart")
                  .[setMetadataTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.Builder.html#com_google_cloud_dataplex_v1_AspectType_Builder_setMetadataTemplate_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_)(
                      [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.newBuilder()
                          .setName("example_template")
                          .setType("record")
                          // Aspect Type fields, that themselves are Metadata Templates
                          .[addAllRecordFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Builder_addAllRecordFields_java_lang_Iterable___extends_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate__)(List.of(aspectField))
                          .build())
                  .build();
          [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) createdAspectType =
              client
                  .[createAspectTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_createAspectTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_LocationName_com_google_cloud_dataplex_v1_AspectType_java_lang_String_)(
                      // Aspect Type is created in "global" location to highlight, that resources from
                      // "global" region can be attached to Entry created in specific location
                      globalLocationName, aspectType, aspectTypeId)
                  .get();
          System.out.println("Step 1: Created aspect type -> " + createdAspectType.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html#com_google_cloud_dataplex_v1_AspectType_getName__)());
    
          // 2) Create Entry Type, of which type Entry will be created
          [EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType.html) entryType =
              [EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType.html).newBuilder()
                  .setDescription("entry type for dataplex quickstart")
                  .[addRequiredAspects](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType.Builder.html#com_google_cloud_dataplex_v1_EntryType_Builder_addRequiredAspects_com_google_cloud_dataplex_v1_EntryType_AspectInfo_)(
                      [EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType.html).AspectInfo.newBuilder()
                          // Aspect Type created in step 1
                          .setType(
                              String.format(
                                  "projects/%s/locations/global/aspectTypes/%s",
                                  projectId, aspectTypeId))
                          .build())
                  .build();
          [EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType.html) createdEntryType =
              client
                  // Entry Type is created in "global" location to highlight, that resources from
                  // "global" region can be attached to Entry created in specific location
                  .[createEntryTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_createEntryTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_LocationName_com_google_cloud_dataplex_v1_EntryType_java_lang_String_)(globalLocationName, entryType, entryTypeId)
                  .get();
          System.out.println("Step 2: Created entry type -> " + createdEntryType.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType.html#com_google_cloud_dataplex_v1_EntryType_getName__)());
    
          // 3) Create Entry Group in which Entry will be located
          [EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup.html) entryGroup =
              [EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup.html).newBuilder().setDescription("entry group for dataplex quickstart").build();
          [EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup.html) createdEntryGroup =
              client
                  // Entry Group is created for specific location
                  .[createEntryGroupAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_createEntryGroupAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_LocationName_com_google_cloud_dataplex_v1_EntryGroup_java_lang_String_)(specificLocationName, entryGroup, entryGroupId)
                  .get();
          System.out.println("Step 3: Created entry group -> " + createdEntryGroup.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup.html#com_google_cloud_dataplex_v1_EntryGroup_getName__)());
    
          // 4) Create Entry
          // Wait 30 seconds to allow previously created resources to propagate
          Thread.sleep(30000);
          String aspectKey = String.format("%s.global.%s", projectId, aspectTypeId);
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) entry =
              [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html).newBuilder()
                  .setEntryType(
                      // Entry is an instance of Entry Type created in step 2
                      String.format(
                          "projects/%s/locations/global/entryTypes/%s", projectId, entryTypeId))
                  .setEntrySource(
                      [EntrySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntrySource.html).newBuilder().setDescription("entry for dataplex quickstart").build())
                  .putAllAspects(
                      Map.of(
                          // Attach Aspect that is an instance of Aspect Type created in step 1
                          aspectKey,
                          [Aspect](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Aspect.html).newBuilder()
                              .setAspectType(
                                  String.format(
                                      "projects/%s/locations/global/aspectTypes/%s",
                                      projectId, aspectTypeId))
                              .setData(
                                  [Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html).newBuilder()
                                      .putFields(
                                          "example_field",
                                          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder()
                                              .setStringValue("example value for the field")
                                              .build())
                                      .build())
                              .build()))
                  .build();
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) createdEntry =
              client.createEntry(
                  // Entry is created in specific location, but it is still possible to link it with
                  // resources (Aspect Type and Entry Type) from "global" location
                  [EntryGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroupName.html).of(projectId, location, entryGroupId), entry, entryId);
          System.out.println("Step 4: Created entry -> " + createdEntry.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html#com_google_cloud_dataplex_v1_Entry_getName__)());
    
          // 5) Retrieve created Entry
          [GetEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryRequest.html) getEntryRequest =
              [GetEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryRequest.html).newBuilder()
                  .setName([EntryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryName.html).of(projectId, location, entryGroupId, entryId).toString())
                  .setView([EntryView](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryView.html).FULL)
                  .build();
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) retrievedEntry = client.getEntry(getEntryRequest);
          System.out.println("Step 5: Retrieved entry -> " + retrievedEntry.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html#com_google_cloud_dataplex_v1_Entry_getName__)());
          retrievedEntry
              .getAspectsMap()
              .values()
              .forEach(
                  retrievedAspect -> {
                    System.out.println("Retrieved aspect for entry:");
                    System.out.println(" * aspect type -> " + retrievedAspect.getAspectType());
                    System.out.println(
                        " * aspect field value -> "
                            + retrievedAspect
                                .getData()
                                .getFieldsMap()
                                .get("example_field")
                                .getStringValue());
                  });
    
          // 6) Use Search capabilities to find Entry
          // Wait 30 seconds to allow resources to propagate to Search
          System.out.println("Step 6: Waiting for resources to propagate to Search...");
          Thread.sleep(30000);
          [SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.html) searchEntriesRequest =
              [SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest.html).newBuilder()
                  .setName(globalLocationName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html#com_google_cloud_dataplex_v1_LocationName_toString__)())
                  .setQuery("name:dataplex-quickstart-entry")
                  .build();
          [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).[SearchEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.SearchEntriesPagedResponse.html) searchEntriesResponse =
              client.searchEntries(searchEntriesRequest);
          List<Entry> entriesFromSearch =
              searchEntriesResponse.getPage().getResponse().getResultsList().stream()
                  .map(SearchEntriesResult::getDataplexEntry)
                  .collect(Collectors.toList());
          System.out.println("Entries found in Search:");
          // Please note in output that Entry Group and Entry Type are also represented as Entries
          entriesFromSearch.forEach(
              entryFromSearch -> System.out.println(" * " + entryFromSearch.getName()));
    
          // 7) Clean created resources
          client
              .[deleteEntryGroupAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_deleteEntryGroupAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_EntryGroupName_)(
                  String.format(
                      "projects/%s/locations/%s/entryGroups/%s", projectId, location, entryGroupId))
              .get();
          client
              .[deleteEntryTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_deleteEntryTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_EntryTypeName_)(
                  String.format("projects/%s/locations/global/entryTypes/%s", projectId, entryTypeId))
              .get();
          client
              .[deleteAspectTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_deleteAspectTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_AspectTypeName_)(
                  String.format("projects/%s/locations/global/aspectTypes/%s", projectId, aspectTypeId))
              .get();
          System.out.println("Step 7: Successfully cleaned up resources");
    
        } catch (IOException | InterruptedException | ExecutionException e) {
          System.err.println("Error during quickstart execution: " + e);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    from google.protobuf import struct_pb2
    
    
    # Method to demonstrate lifecycle of different Dataplex resources and their interactions.
    # Method creates Aspect Type, Entry Type, Entry Group and Entry, retrieves Entry
    # and cleans up created resources.
    def quickstart(
        project_id: str,
        location: str,
        aspect_type_id: str,
        entry_type_id: str,
        entry_group_id: str,
        entry_id: str,
    ) -> None:
        # Initialize client that will be used to send requests across threads. This
        # client only needs to be created once, and can be reused for multiple requests.
        # After completing all of your requests, call the "__exit__()" method to safely
        # clean up any remaining background resources. Alternatively, use the client as
        # a context manager.
        with [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)() as client:
            # 0) Prepare variables used in following steps
            global_parent = f"projects/{project_id}/locations/global"
            specific_location_parent = f"projects/{project_id}/locations/{location}"
    
            # 1) Create Aspect Type that will be attached to Entry Type
            aspect_field = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html)(
                # The name must follow regex ^(([a-zA-Z]{1})([\\w\\-_]{0,62}))$
                # That means name must only contain alphanumeric character or dashes or underscores,
                # start with an alphabet, and must be less than 63 characters.
                name="example_field",
                # Metadata Template is recursive structure,
                # primitive types such as "string" or "integer" indicate leaf node,
                # complex types such as "record" or "array" would require nested Metadata Template
                type="string",
                index=1,
                annotations=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html).[Annotations](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.Annotations.html)(
                    description="example field to be filled during entry creation"
                ),
                constraints=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html).[Constraints](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.Constraints.html)(
                    # Specifies if field will be required in Aspect Type.
                    required=True
                ),
            )
            aspect_type = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html)(
                description="aspect type for dataplex quickstart",
                metadata_template=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html)(
                    name="example_template",
                    type="record",
                    # Aspect Type fields, that themselves are Metadata Templates.
                    record_fields=[aspect_field],
                ),
            )
            aspect_type_create_operation = client.create_aspect_type(
                # Aspect Type is created in "global" location to highlight, that resources from
                # "global" region can be attached to Entry created in specific location
                parent=global_parent,
                aspect_type=aspect_type,
                aspect_type_id=aspect_type_id,
            )
            created_aspect_type = aspect_type_create_operation.result(60)
            print(f"Step 1: Created aspect type -> {created_aspect_type.name}")
    
            # 2) Create Entry Type, of which type Entry will be created
            entry_type = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryType.html)(
                description="entry type for dataplex quickstart",
                required_aspects=[
                    [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryType.html).[AspectInfo](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryType.AspectInfo.html)(
                        # Aspect Type created in step 1
                        type=f"projects/{project_id}/locations/global/aspectTypes/{aspect_type_id}"
                    )
                ],
            )
            entry_type_create_operation = client.create_entry_type(
                # Entry Type is created in "global" location to highlight, that resources from
                # "global" region can be attached to Entry created in specific location
                parent=global_parent,
                entry_type=entry_type,
                entry_type_id=entry_type_id,
            )
            created_entry_type = entry_type_create_operation.result(60)
            print(f"Step 2: Created entry type -> {created_entry_type.name}")
    
            # 3) Create Entry Group in which Entry will be located
            entry_group = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryGroup](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryGroup.html)(
                description="entry group for dataplex quickstart"
            )
            entry_group_create_operation = client.create_entry_group(
                # Entry Group is created for specific location
                parent=specific_location_parent,
                entry_group=entry_group,
                entry_group_id=entry_group_id,
            )
            created_entry_group = entry_group_create_operation.result(60)
            print(f"Step 3: Created entry group -> {created_entry_group.name}")
    
            # 4) Create Entry
            # Wait 10 second to allow previously created resources to propagate
            time.sleep(10)
            aspect_key = f"{project_id}.global.{aspect_type_id}"
            entry = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entry.html)(
                # Entry is an instance of Entry Type created in step 2
                entry_type=f"projects/{project_id}/locations/global/entryTypes/{entry_type_id}",
                entry_source=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).EntrySource(
                    description="entry for dataplex quickstart"
                ),
                aspects={
                    # Attach Aspect that is an instance of Aspect Type created in step 1
                    aspect_key: [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Aspect](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Aspect.html)(
                        aspect_type=f"projects/{project_id}/locations/global/aspectTypes/{aspect_type_id}",
                        data=struct_pb2.Struct(
                            fields={
                                "example_field": struct_pb2.Value(
                                    string_value="example value for the field"
                                ),
                            }
                        ),
                    )
                },
            )
            created_entry = client.create_entry(
                # Entry is created in specific location, but it is still possible to link it with
                # resources (Aspect Type and Entry Type) from "global" location
                parent=f"projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}",
                entry=entry,
                entry_id=entry_id,
            )
            print(f"Step 4: Created entry -> {created_entry.name}")
    
            # 5) Retrieve created Entry
            get_entry_request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[GetEntryRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.GetEntryRequest.html)(
                name=f"projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}",
                view=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryView](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryView.html).FULL,
            )
            retrieved_entry = client.get_entry(request=get_entry_request)
            print(f"Step 5: Retrieved entry -> {retrieved_entry.name}")
            for retrieved_aspect in retrieved_entry.aspects.values():
                print("Retrieved aspect for entry:")
                print(f" * aspect type -> {retrieved_aspect.aspect_type}")
                print(f" * aspect field value -> {retrieved_aspect.data['example_field']}")
    
            # 6) Use Search capabilities to find Entry
            # Wait 30 second to allow resources to propagate to Search
            print("Step 6: Waiting for resources to propagate to Search...")
            time.sleep(30)
            search_entries_request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[SearchEntriesRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.SearchEntriesRequest.html)(
                name=global_parent, query="name:dataplex-quickstart-entry"
            )
            results = client.search_entries(search_entries_request)
            search_entries_response = results._response
            entries_from_search = [
                result.dataplex_entry for result in search_entries_response.results
            ]
            print("Entries found in Search:")
            # Please note in output that Entry Group and Entry Type are also represented as Entries
            for entry_from_search in entries_from_search:
                print(f" * {entry_from_search.name}")
    
            # 7) Clean created resources
            client.delete_entry_group(
                name=f"projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}"
            )
            client.delete_entry_type(
                name=f"projects/{project_id}/locations/global/entryTypes/{entry_type_id}"
            )
            client.delete_aspect_type(
                name=f"projects/{project_id}/locations/global/aspectTypes/{aspect_type_id}"
            )
            print("Step 7: Successfully cleaned up resources")
    
    
    if __name__ == "__main__":
        # TODO(developer): Replace these variables before running the sample.
        project_id = "MY_PROJECT_ID"
        # Available locations: https://cloud.google.com/dataplex/docs/locations
        location = "MY_LOCATION"
        # Variables below can be replaced with custom values or defaults can be kept
        aspect_type_id = "dataplex-quickstart-aspect-type"
        entry_type_id = "dataplex-quickstart-entry-type"
        entry_group_id = "dataplex-quickstart-entry-group"
        entry_id = "dataplex-quickstart-entry"
    
        quickstart(
            project_id, location, aspect_type_id, entry_type_id, entry_group_id, entry_id
        )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataplex). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
