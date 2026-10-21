---
url: https://docs.cloud.google.com/data-catalog/docs/how-to/custom-entries/
title: Create custom Data Catalog entries for your data sources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:53.973037+00:00
---

# Create custom Data Catalog entries for your data sources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/how-to/custom-entries/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/data-catalog/docs/concepts/overview)



Send feedback 

#  Create custom Data Catalog entries for your data sources Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create custom Data Catalog entries. To integrate your custom data sources, call Data Catalog APIs that allow you to create and manage Data Catalog entries with custom data resource types. In this document, an entry for a custom data resource type is referred to as a "custom entry".

**Note:** To automatically integrate with the supported Google Cloud data sources as well as a number of on-premises ones using the community-contributed connectors, follow the steps in [Integrate data sources](https://docs.cloud.google.com/data-catalog/docs/integrate-data-sources).

## Create entry groups and custom entries

Custom entries must be placed within a user-created entry group. You create the entry group, then create the custom entry within the entry group. For more information, see [Entries and entry groups](https://docs.cloud.google.com/data-catalog/docs/entries-and-entry-groups).

After creating an entry, you can [set IAM policies](https://docs.cloud.google.com/data-catalog/docs/how-to/filesets#iam_roles_permissions_and_policies) on the entry group to define who has access to the entry group and the entries inside.

###  Java 

Before trying this sample, follow the Java setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/overview). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datacatalog.v1.[ColumnSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.html);
    import com.google.cloud.datacatalog.v1.[CreateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryGroupRequest.html);
    import com.google.cloud.datacatalog.v1.[CreateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryRequest.html);
    import com.google.cloud.datacatalog.v1.[DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html);
    import com.google.cloud.datacatalog.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html);
    import com.google.cloud.datacatalog.v1.[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroup.html);
    import com.google.cloud.datacatalog.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LocationName.html);
    import com.google.cloud.datacatalog.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Schema.html);
    import java.io.IOException;
    
    // Sample to create custom entry
    public class CreateCustomEntry {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String entryGroupId = "onprem_entry_group";
        String entryId = "onprem_entry_id";
        createCustomEntry(projectId, entryGroupId, entryId);
      }
    
      public static void createCustomEntry(String projectId, String entryGroupId, String entryId)
          throws IOException {
        // Currently, Data Catalog stores metadata in the us-central1 region.
        String location = "us-central1";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html) dataCatalogClient = [DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html).create()) {
          // Construct the EntryGroup for the EntryGroup request.
          [EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroup.html) entryGroup =
              [EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroup.html).newBuilder()
                  .setDisplayName("My awesome Entry Group")
                  .setDescription("This Entry Group represents an external system")
                  .build();
    
          // Construct the EntryGroup request to be sent by the client.
          [CreateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryGroupRequest.html) entryGroupRequest =
              [CreateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryGroupRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LocationName.html).of(projectId, location).toString())
                  .[setEntryGroupId](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryGroupRequest.Builder.html#com_google_cloud_datacatalog_v1_CreateEntryGroupRequest_Builder_setEntryGroupId_java_lang_String_)(entryGroupId)
                  .setEntryGroup(entryGroup)
                  .build();
    
          // Use the client to send the API request.
          [EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroup.html) createdEntryGroup = dataCatalogClient.createEntryGroup(entryGroupRequest);
    
          // Construct the Entry for the Entry request.
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html) entry =
              [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html).newBuilder()
                  .setUserSpecifiedSystem("onprem_data_system")
                  .[setUserSpecifiedType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.Builder.html#com_google_cloud_datacatalog_v1_Entry_Builder_setUserSpecifiedType_java_lang_String_)("onprem_data_asset")
                  .setDisplayName("My awesome data asset")
                  .setDescription("This data asset is managed by an external system.")
                  .setLinkedResource("//my-onprem-server.com/dataAssets/my-awesome-data-asset")
                  .[setSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.Builder.html#com_google_cloud_datacatalog_v1_Entry_Builder_setSchema_com_google_cloud_datacatalog_v1_Schema_)(
                      [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Schema.html).newBuilder()
                          .[addColumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Schema.Builder.html#com_google_cloud_datacatalog_v1_Schema_Builder_addColumns_com_google_cloud_datacatalog_v1_ColumnSchema_)(
                              [ColumnSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.html).newBuilder()
                                  .setColumn("first_column")
                                  .setDescription("This columns consists of ....")
                                  .setMode("NULLABLE")
                                  .setType("DOUBLE")
                                  .build())
                          .[addColumns](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Schema.Builder.html#com_google_cloud_datacatalog_v1_Schema_Builder_addColumns_com_google_cloud_datacatalog_v1_ColumnSchema_)(
                              [ColumnSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ColumnSchema.html).newBuilder()
                                  .setColumn("second_column")
                                  .setDescription("This columns consists of ....")
                                  .setMode("REQUIRED")
                                  .setType("STRING")
                                  .build())
                          .build())
                  .build();
    
          // Construct the Entry request to be sent by the client.
          [CreateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryRequest.html) entryRequest =
              [CreateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryRequest.html).newBuilder()
                  .setParent(createdEntryGroup.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroup.html#com_google_cloud_datacatalog_v1_EntryGroup_getName__)())
                  .[setEntryId](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryRequest.Builder.html#com_google_cloud_datacatalog_v1_CreateEntryRequest_Builder_setEntryId_java_lang_String_)(entryId)
                  .setEntry(entry)
                  .build();
    
          // Use the client to send the API request.
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html) createdEntry = dataCatalogClient.createEntry(entryRequest);
          System.out.printf("Custom entry created with name: %s", createdEntry.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry.html#com_google_cloud_datacatalog_v1_Entry_getName__)());
        }
      }
    }

###  Node.js 

Before trying this sample, follow the Node.js setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Node.js API reference documentation](https://googleapis.dev/nodejs/datacatalog/latest/index.html). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client library.
    const {DataCatalogClient} = require('[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)').v1;
    const datacatalog = new [DataCatalogClient](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)();
    
    async function createCustomEntry() {
      // Create a custom entry within an entry group.
    
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'my_project';
      // const entryGroupId = 'my_entry_group';
      // const entryId =  'my_entry';
      // const tagTemplateId = 'my_tag_template';
    
      // Currently, Data Catalog stores metadata in the us-central1 region.
      const location = 'us-central1';
    
      // Delete any pre-existing Entry with the same name
      // that will be used to create the new Entry.
      try {
        const entryName = datacatalog.entryPath(
          projectId,
          location,
          entryGroupId,
          entryId
        );
        await datacatalog.deleteEntry({name: entryName});
        console.log(`Deleted Entry: ${entryName}`);
      } catch (err) {
        console.log('Entry does not exist.');
      }
    
      // Delete any pre-existing Entry Group with the same name
      // that will be used to construct the new EntryGroup.
      try {
        const entryGroupName = datacatalog.entryGroupPath(
          projectId,
          location,
          entryGroupId
        );
        await datacatalog.deleteEntryGroup({name: entryGroupName});
        console.log(`Deleted Entry Group: ${entryGroupName}`);
      } catch (err) {
        console.log('Entry Group does not exist.');
      }
    
      // Delete any pre-existing Template with the same name
      // that will be used to create a new Template.
      const tagTemplateName = datacatalog.tagTemplatePath(
        projectId,
        location,
        tagTemplateId
      );
    
      let tagTemplateRequest = {
        name: tagTemplateName,
        force: true,
      };
    
      try {
        await datacatalog.deleteTagTemplate(tagTemplateRequest);
        console.log(`Deleted template: ${tagTemplateName}`);
      } catch (error) {
        console.log(`Cannot delete template: ${tagTemplateName}`);
      }
    
      // Construct the EntryGroup for the EntryGroup request.
      const entryGroup = {
        displayName: 'My awesome Entry Group',
        description: 'This Entry Group represents an external system',
      };
    
      // Construct the EntryGroup request to be sent by the client.
      const entryGroupRequest = {
        parent: datacatalog.locationPath(projectId, location),
        entryGroupId: entryGroupId,
        entryGroup: entryGroup,
      };
    
      // Use the client to send the API request.
      const [createdEntryGroup] =
        await datacatalog.createEntryGroup(entryGroupRequest);
      console.log(`Created entry group: ${createdEntryGroup.name}`);
    
      // Construct the Entry for the Entry request.
      const entry = {
        userSpecifiedSystem: 'onprem_data_system',
        userSpecifiedType: 'onprem_data_asset',
        displayName: 'My awesome data asset',
        description: 'This data asset is managed by an external system.',
        linkedResource: '//my-onprem-server.com/dataAssets/my-awesome-data-asset',
        schema: {
          columns: [
            {
              column: 'first_column',
              description: 'This columns consists of ....',
              mode: 'NULLABLE',
              type: 'STRING',
            },
            {
              column: 'second_column',
              description: 'This columns consists of ....',
              mode: 'NULLABLE',
              type: 'DOUBLE',
            },
          ],
        },
      };
    
      // Construct the Entry request to be sent by the client.
      const entryRequest = {
        parent: datacatalog.entryGroupPath(projectId, location, entryGroupId),
        entryId: entryId,
        entry: entry,
      };
    
      // Use the client to send the API request.
      const [createdEntry] = await datacatalog.createEntry(entryRequest);
      console.log(`Created entry: ${createdEntry.name}`);
    
      // Create a Tag Template.
      // For more field types, including ENUM, please refer to
      // https://cloud.google.com/data-catalog/docs/quickstarts/quickstart-search-tag#data-catalog-quickstart-nodejs.
      const fieldSource = {
        displayName: 'Source of data asset',
        type: {
          primitiveType: 'STRING',
        },
      };
    
      const tagTemplate = {
        displayName: 'Demo Tag Template',
        fields: {
          source: fieldSource,
        },
      };
    
      tagTemplateRequest = {
        parent: datacatalog.locationPath(projectId, location),
        tagTemplateId: tagTemplateId,
        tagTemplate: tagTemplate,
      };
    
      // Use the client to send the API request.
      const [createdTagTemplate] =
        await datacatalog.createTagTemplate(tagTemplateRequest);
      console.log(`Created template: ${createdTagTemplate.name}`);
    
      // Attach a Tag to the custom Entry.
      const tag = {
        template: createdTagTemplate.name,
        fields: {
          source: {
            stringValue: 'On-premises system name',
          },
        },
      };
    
      const tagRequest = {
        parent: createdEntry.name,
        tag: tag,
      };
    
      // Use the client to send the API request.
      const [createdTag] = await datacatalog.createTag(tagRequest);
      console.log(`Created tag: ${createdTag.name}`);
    }
    createCustomEntry();

###  Python 

Before trying this sample, follow the Python setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Import required modules.
    from google.cloud import [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest)
    
    # Google Cloud Platform project.
    project_id = "my-project"
    # Entry Group to be created.
    entry_group_id = "my_new_entry_group_id"
    # Entry to be created.
    entry_id = "my_new_entry_id"
    # Currently, Data Catalog stores metadata in the us-central1 region.
    location = "us-central1"
    
    datacatalog = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[DataCatalogClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html)()
    
    # Create an Entry Group.
    entry_group_obj = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[EntryGroup](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.EntryGroup.html)()
    entry_group_obj.display_name = "My awesome Entry Group"
    entry_group_obj.description = "This Entry Group represents an external system"
    
    entry_group = datacatalog.[create_entry_group](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_create_entry_group)(
        parent=[datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[DataCatalogClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html).common_location_path(
            project_id, location
        ),
        entry_group_id=entry_group_id,
        entry_group=entry_group_obj,
    )
    entry_group_name = entry_group.name
    print("Created entry group: {}".format(entry_group_name))
    
    # Create an Entry.
    entry = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[Entry](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.Entry.html)()
    entry.user_specified_system = "onprem_data_system"
    entry.user_specified_type = "onprem_data_asset"
    entry.display_name = "My awesome data asset"
    entry.description = "This data asset is managed by an external system."
    entry.linked_resource = "//my-onprem-server.com/dataAssets/my-awesome-data-asset"
    
    # Create the Schema, this is optional.
    entry.schema.columns.append(
        [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[ColumnSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.ColumnSchema.html)(
            column="first_column",
            type_="STRING",
            description="This columns consists of ....",
            mode=None,
        )
    )
    
    entry.schema.columns.append(
        [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).types.[ColumnSchema](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.ColumnSchema.html)(
            column="second_column",
            type_="DOUBLE",
            description="This columns consists of ....",
            mode=None,
        )
    )
    
    entry = datacatalog.[create_entry](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_create_entry)(
        parent=entry_group_name, entry_id=entry_id, entry=entry
    )
    print("Created entry: {}".format(entry.name))

###  REST & CMD LINE 

### REST

See the following examples and refer to the Data Catalog REST API [entryGroups.create](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups/create) and [entryGroups.entries.create](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/create) documentation.

### 1\. Create an entry group

Before using any of the request data, make the following replacements: 

  * project-id: Your Google Cloud project ID
  * [entryGroupId](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups/create#body.QUERY_PARAMETERS.entry_group_id): The ID must begin with a letter or underscore, contain only English letters, numbers and underscores, and be at most 64 characters. 
  * [displayName](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups#EntryGroup.FIELDS.display_name): The textual name for the entry group. 



HTTP method and URL: 
    
    
    POST https://datacatalog.googleapis.com/v1/projects/project-id/locations/region/entryGroups?entryGroupId=entryGroupId

Request JSON body: 
    
    
    {
      "displayName": "Entry Group display name"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datacatalog.googleapis.com/v1/projects/project-id/locations/region/entryGroups?entryGroupId=entryGroupId"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datacatalog.googleapis.com/v1/projects/project-id/locations/region/entryGroups?entryGroupId=entryGroupId" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my_projectid/locations/us-central1/entryGroups/my_entry_group",
      "displayName": "Entry Group display name",
      "dataCatalogTimestamps": {
        "createTime": "2019-10-19T16:35:50.135Z",
        "updateTime": "2019-10-19T16:35:50.135Z"
      }
    }
    

### 2\. Create a custom entry within the entry group

Before using any of the request data, make the following replacements: 

  * project_id: Your Google Cloud project ID.
  * [entryGroupId](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups/create#body.QUERY_PARAMETERS.entry_group_id): ID of the existing entryGroup. The entry will be created in this EntryGroup.
  * [entryId](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/create#body.QUERY_PARAMETERS.entry_id): ID of the new entry. The ID must begin with a letter or underscore, contain only English letters, numbers and underscores, and have at most 64 characters.
  * [description](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#Entry.FIELDS.description): Optional entry description
  * [displayName](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#Entry.FIELDS.display_name): Optional textual name for the entry.
  * [userSpecifiedType](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#Entry.FIELDS.user_specified_type): Custom type name. The type name must begin with a letter or underscore, must only contain letters, numbers, and underscores, and must have at most 64 characters.
  * [userSpecifiedSystem](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#Entry.FIELDS.user_specified_system): The entry's non-Google Cloud source system, which is not [integrated with Data Catalog](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#Entry.FIELDS.integrated_system). The source system name must begin with a letter or underscore, must only contain letters, numbers, and underscores, and must have at most 64 characters.
  * [linkedResource](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#Entry.FIELDS.linked_resource): Optional fullname of the resource the entry refers to.
  * [schema](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries#Schema): Optional data schema.

**Example JSON schema:**
        
        { ...
          "schema": {
            "columns": [
              {
                "column": "first_name",
                "description": "First name",
                "mode": "REQUIRED",
                "type": "STRING"
              },
              {
                "column": "last_name",
                "description": "Last name",
                "mode": "REQUIRED",
                "type": "STRING"
              },
              {
                "column": "address",
                "description": "Address",
                "mode": "REPEATED",
                "subcolumns": [
                  {
                    "column": "city",
                    "description": "City",
                    "mode": "NULLABLE",
                    "type": "STRING"
                  },
                  {
                    "column": "state",
                    "description": "State",
                    "mode": "NULLABLE",
                    "type": "STRING"
                  }
                ],
                "type": "RECORD"
              }
            ]
          }
        ...
        }
        




HTTP method and URL: 
    
    
    POST https://datacatalog.googleapis.com/v1/projects/project_id/locations/region/entryGroups/entryGroupId/entries?entryId=entryId

Request JSON body: 
    
    
    {
      "description": "Description",
      "displayName": "Display name",
      "userSpecifiedType": "my_type",
      "userSpecifiedSystem": "my_system",
      "linkedResource": "example.com/def",
      "schema": { schema }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project_id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datacatalog.googleapis.com/v1/projects/project_id/locations/region/entryGroups/entryGroupId/entries?entryId=entryId"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project_id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datacatalog.googleapis.com/v1/projects/project_id/locations/region/entryGroups/entryGroupId/entries?entryId=entryId" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my_project_id/locations/us-central1/entryGroups/my_entryGroup_id/entries/my_entry_id",
      "userSpecifiedType": "my-type",
      "userSpecifiedSystem": "my_system",
      "displayName": "On-prem entry",
      "description": "My entry description.",
      "schema": {
        "columns": [
          {
            "type": "STRING",
            "description": "First name",
            "mode": "REQUIRED",
            "column": "first_name"
          },
          {
            "type": "STRING",
            "description": "Last name",
            "mode": "REQUIRED",
            "column": "last_name"
          },
          {
            "type": "RECORD",
            "description": "Address",
            "mode": "REPEATED",
            "column": "address",
            "subcolumns": [
              {
                "type": "STRING",
                "description": "City",
                "mode": "NULLABLE",
                "column": "city"
              },
              {
                "type": "STRING",
                "description": "State",
                "mode": "NULLABLE",
                "column": "state"
              }
            ]
          }
        ]
      },
      "sourceSystemTimestamps": {
        "createTime": "2019-10-23T23:11:26.326Z",
        "updateTime": "2019-10-23T23:11:26.326Z"
      },
    "linkedResource": "example.com/def"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-30 UTC."],[],[]] 
