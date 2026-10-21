---
url: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-create-fileset/
title: Create fileset \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:30.677332+00:00
---

# Create fileset  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-create-fileset/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/data-catalog/docs/samples)



#  Create fileset Stay organized with collections  Save and categorize content based on your preferences. 

Create a fileset within an entry group.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Surface files from Cloud Storage with fileset entries](https://docs.cloud.google.com/data-catalog/docs/how-to/filesets)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/overview). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datacatalog.v1.[ColumnSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.html);
    import com.google.cloud.datacatalog.v1.[CreateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryRequest.html);
    import com.google.cloud.datacatalog.v1.[DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html);
    import com.google.cloud.datacatalog.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html);
    import com.google.cloud.datacatalog.v1.[EntryGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroupName.html);
    import com.google.cloud.datacatalog.v1.[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryType.html);
    import com.google.cloud.datacatalog.v1.[GcsFilesetSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.GcsFilesetSpec.html);
    import com.google.cloud.datacatalog.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Schema.html);
    import java.io.IOException;
    
    // Sample to create file set entry
    public class CreateFilesetEntry {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String entryGroupId = "fileset_entry_group";
        String entryId = "fileset_entry_id";
        createFilesetEntry(projectId, entryGroupId, entryId);
      }
    
      // Create Fileset Entry.
      public static void createFilesetEntry(String projectId, String entryGroupId, String entryId)
          throws IOException {
        // Currently, Data Catalog stores metadata in the us-central1 region.
        String location = "us-central1";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html) dataCatalogClient = [DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html).create()) {
          // Construct the Entry for the Entry request.
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html) entry =
              [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html).newBuilder()
                  .setDisplayName("My Fileset")
                  .setDescription("This fileset consists of ....")
                  .[setGcsFilesetSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.Builder.html#com_google_cloud_datacatalog_v1_Entry_Builder_setGcsFilesetSpec_com_google_cloud_datacatalog_v1_GcsFilesetSpec_)(
                      [GcsFilesetSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.GcsFilesetSpec.html).newBuilder().[addFilePatterns](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.GcsFilesetSpec.Builder.html#com_google_cloud_datacatalog_v1_GcsFilesetSpec_Builder_addFilePatterns_java_lang_String_)("gs://cloud-samples-data/*").build())
                  .[setSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.Builder.html#com_google_cloud_datacatalog_v1_Entry_Builder_setSchema_com_google_cloud_datacatalog_v1_Schema_)(
                      [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Schema.html).newBuilder()
                          .[addColumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Schema.Builder.html#com_google_cloud_datacatalog_v1_Schema_Builder_addColumns_com_google_cloud_datacatalog_v1_ColumnSchema_)(
                              [ColumnSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.html).newBuilder()
                                  .setColumn("first_name")
                                  .setDescription("First name")
                                  .setMode("REQUIRED")
                                  .setType("STRING")
                                  .build())
                          .[addColumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Schema.Builder.html#com_google_cloud_datacatalog_v1_Schema_Builder_addColumns_com_google_cloud_datacatalog_v1_ColumnSchema_)(
                              [ColumnSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.html).newBuilder()
                                  .setColumn("last_name")
                                  .setDescription("Last name")
                                  .setMode("REQUIRED")
                                  .setType("STRING")
                                  .build())
                          .[addColumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Schema.Builder.html#com_google_cloud_datacatalog_v1_Schema_Builder_addColumns_com_google_cloud_datacatalog_v1_ColumnSchema_)(
                              [ColumnSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.html).newBuilder()
                                  .setColumn("addresses")
                                  .setDescription("Addresses")
                                  .setMode("REPEATED")
                                  .setType("RECORD")
                                  .[addSubcolumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.Builder.html#com_google_cloud_datacatalog_v1_ColumnSchema_Builder_addSubcolumns_com_google_cloud_datacatalog_v1_ColumnSchema_)(
                                      [ColumnSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.html).newBuilder()
                                          .setColumn("city")
                                          .setDescription("City")
                                          .setMode("NULLABLE")
                                          .setType("STRING")
                                          .build())
                                  .[addSubcolumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.Builder.html#com_google_cloud_datacatalog_v1_ColumnSchema_Builder_addSubcolumns_com_google_cloud_datacatalog_v1_ColumnSchema_)(
                                      [ColumnSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.html).newBuilder()
                                          .setColumn("state")
                                          .setDescription("State")
                                          .setMode("NULLABLE")
                                          .setType("STRING")
                                          .build())
                                  .build())
                          .build())
                  .setType([EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryType.html).FILESET)
                  .build();
    
          // Construct the Entry request to be sent by the client.
          [CreateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryRequest.html) entryRequest =
              [CreateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryRequest.html).newBuilder()
                  .setParent([EntryGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroupName.html).of(projectId, location, entryGroupId).toString())
                  .[setEntryId](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryRequest.Builder.html#com_google_cloud_datacatalog_v1_CreateEntryRequest_Builder_setEntryId_java_lang_String_)(entryId)
                  .setEntry(entry)
                  .build();
    
          // Use the client to send the API request.
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html) entryCreated = dataCatalogClient.createEntry(entryRequest);
          System.out.printf("Entry created with name: %s", entryCreated.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html#com_google_cloud_datacatalog_v1_Entry_getName__)());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Node.js API reference documentation](https://googleapis.dev/nodejs/datacatalog/latest/index.html). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client library.
    const {DataCatalogClient} = require('[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)').v1;
    const datacatalog = new [DataCatalogClient](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)();
    
    async function createFileset() {
      // Create a fileset within an entry group.
    
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'my_project';
      // const entryGroupId = 'my_entry_group';
      // const entryId = 'my_entry';
    
      // Currently, Data Catalog stores metadata in the us-central1 region.
      const location = 'us-central1';
    
      // Delete any pre-existing Entry with the same name that will be used
      // when creating the new Entry.
      try {
        const formattedName = datacatalog.entryPath(
          projectId,
          location,
          entryGroupId,
          entryId
        );
        await datacatalog.deleteEntry({name: formattedName});
      } catch (err) {
        console.log('Entry does not exist.');
      }
    
      // Delete any pre-existing Entry Group with the same name
      // that will be used to create the new Entry Group.
      try {
        const formattedName = datacatalog.entryGroupPath(
          projectId,
          location,
          entryGroupId
        );
        await datacatalog.deleteEntryGroup({name: formattedName});
      } catch (err) {
        console.log('Entry Group does not exist.');
      }
    
      // Construct the Entry Group for the Entry Group request.
      const entryGroup = {
        displayName: 'My Fileset Entry Group',
        description: 'This Entry Group consists of ....',
      };
    
      // Construct the Entry Group request to be sent by the client.
      const entryGroupRequest = {
        parent: datacatalog.locationPath(projectId, location),
        entryGroupId: entryGroupId,
        entryGroup: entryGroup,
      };
    
      // Use the client to send the API request.
      await datacatalog.createEntryGroup(entryGroupRequest);
    
      // Construct the Entry for the Entry request.
      const FILESET_TYPE = 4;
    
      const entry = {
        displayName: 'My Fileset',
        description: 'This fileset consists of ....',
        gcsFilesetSpec: {filePatterns: ['gs://my_bucket/*']},
        schema: {
          columns: [
            {
              column: 'city',
              description: 'City',
              mode: 'NULLABLE',
              type: 'STRING',
            },
            {
              column: 'state',
              description: 'State',
              mode: 'NULLABLE',
              type: 'STRING',
            },
            {
              column: 'addresses',
              description: 'Addresses',
              mode: 'REPEATED',
              subcolumns: [
                {
                  column: 'city',
                  description: 'City',
                  mode: 'NULLABLE',
                  type: 'STRING',
                },
                {
                  column: 'state',
                  description: 'State',
                  mode: 'NULLABLE',
                  type: 'STRING',
                },
              ],
              type: 'RECORD',
            },
          ],
        },
        type: FILESET_TYPE,
      };
    
      // Construct the Entry request to be sent by the client.
      const request = {
        parent: datacatalog.entryGroupPath(projectId, location, entryGroupId),
        entryId: entryId,
        entry: entry,
      };
    
      // Use the client to send the API request.
      const [response] = await datacatalog.createEntry(request);
    
      console.log(`Name: ${response.name}`);
      console.log(`Display name: ${response.displayName}`);
      console.log(`Type: ${response.type}`);
    }
    createFileset();

### Python

Before trying this sample, follow the Python setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Import required modules.
    from google.cloud import [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest)
    
    # TODO: Set these values before running the sample.
    project_id = "project_id"
    fileset_entry_group_id = "entry_group_id"
    fileset_entry_id = "entry_id"
    
    # For all regions available, see:
    # https://cloud.google.com/data-catalog/docs/concepts/regions
    location = "us-central1"
    
    datacatalog = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[DataCatalogClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html)()
    
    # Create an Entry Group.
    entry_group_obj = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[EntryGroup](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.EntryGroup.html)()
    entry_group_obj.display_name = "My Fileset Entry Group"
    entry_group_obj.description = "This Entry Group consists of ...."
    
    entry_group = datacatalog.[create_entry_group](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_create_entry_group)(
        parent=[datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[DataCatalogClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html).common_location_path(
            project_id, location
        ),
        entry_group_id=fileset_entry_group_id,
        entry_group=entry_group_obj,
    )
    print(f"Created entry group: {entry_group.name}")
    
    # Create a Fileset Entry.
    entry = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[Entry](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.Entry.html)()
    entry.display_name = "My Fileset"
    entry.description = "This fileset consists of ...."
    entry.gcs_fileset_spec.file_patterns.append("gs://my_bucket/*.csv")
    entry.type_ = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[EntryType](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.EntryType.html).FILESET
    
    # Create the Schema, for example when you have a csv file.
    entry.schema.columns.append(
        [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[ColumnSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.ColumnSchema.html)(
            column="first_name",
            description="First name",
            mode="REQUIRED",
            type_="STRING",
        )
    )
    
    entry.schema.columns.append(
        [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[ColumnSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.ColumnSchema.html)(
            column="last_name", description="Last name", mode="REQUIRED", type_="STRING"
        )
    )
    
    # Create the addresses parent column
    addresses_column = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[ColumnSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.ColumnSchema.html)(
        column="addresses", description="Addresses", mode="REPEATED", type_="RECORD"
    )
    
    # Create sub columns for the addresses parent column
    addresses_column.subcolumns.append(
        [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[ColumnSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.ColumnSchema.html)(
            column="city", description="City", mode="NULLABLE", type_="STRING"
        )
    )
    
    addresses_column.subcolumns.append(
        [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[ColumnSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.ColumnSchema.html)(
            column="state", description="State", mode="NULLABLE", type_="STRING"
        )
    )
    
    entry.schema.columns.append(addresses_column)
    
    entry = datacatalog.[create_entry](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_create_entry)(
        parent=entry_group.name, entry_id=fileset_entry_id, entry=entry
    )
    print(f"Created fileset entry: {entry.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datacatalog). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
