---
url: https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata/
title: Manage aspects and enrich metadata \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:02.884719+00:00
---

# Manage aspects and enrich metadata  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage aspects and enrich metadata Stay organized with collections  Save and categorize content based on your preferences. 

Aspects and aspect types in Knowledge Catalog (formerly Dataplex Universal Catalog) let you add structured metadata to entries and entry links to describe your data assets and their relationships. This context improves data discoverability and helps you classify sensitive information, such as personally identifiable information (PII), to apply data quality or access policies.

For more information about metadata concepts, see [About metadata in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview). If this is your first time working with Knowledge Catalog metadata, see the [Add metadata to a BigQuery table](https://docs.cloud.google.com/knowledge-catalog/docs/add-metadata-quickstart) or [Create and use a business glossary](https://docs.cloud.google.com/knowledge-catalog/docs/quickstart-business-glossary) quickstarts.

## What are aspect types?

Aspect types are reusable resources that provide JSON templates defining related metadata fields for aspects. For example, for compliance information, you might define an aspect type with fields for PII classification and GDPR compliance. When you create a custom aspect type, you must specify an ID that complies with [Knowledge Catalog resource naming guidelines](https://docs.cloud.google.com/knowledge-catalog/docs/guidelines-resources#id).

### Categories of aspect types

Aspect types are categorized into custom and system aspect types:

#### Custom aspect types

Aspect types that you create in Knowledge Catalog are called custom aspect types.

**Note:** Custom aspect types apply to entries but not to entry links.

Custom aspect types can be global or regional:

  * **Global aspect types** : Can be used to create aspects for entries in any region. Choose a `global` aspect type if you need to apply the same structure to entries across multiple regions, as you only need to define it once. Because the definition of a global aspect type is replicated across all regions, this option may not be suitable if the aspect type schema itself contains sensitive information or if strict data residency for all metadata components is required.
  * **Regional aspect types** : Can only be used to create aspects for entries that reside in the same region as the aspect type. For example, an aspect type created in `us-central1` can only be used with entries in `us-central1`. Choose a regional location if an aspect type is only relevant for entries in a specific region, or to ensure that the aspect type definition resides within the selected region, which can help meet data sovereignty and compliance requirements. If you use regional aspect types but need the same structure in multiple regions, you must create and manage separate aspect type definitions in each region.



You can create custom aspect types either in a specific regional location (for example, `us-central1`) or as a `global` resource. The location of an aspect type impacts the scope of its applicability and determines which entries it can be used with.

For more information, see [Project and location constraints](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#project-location-constraints).

#### System aspect types

Aspect types that Knowledge Catalog provides, uses, and manages are called system aspect types. System aspect types are always global, therefore they can be used in any region. System aspect types are stored in a Google-managed project with project number `655216118709`. For example, `projects/655216118709/locations/global/aspectTypes/schema`.

Each system-defined aspect type, entry type, and entry link type has its own IAM permissions. For more information, see [IAM permissions for system aspect types, entry types, and entry link types](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#system-aspect-types-entry-types-entry-link-types).

System aspect types are further categorized into reusable and restricted. The following table describes the categories of system aspect types, and the list of aspect types that Knowledge Catalog provides for each of the categories:

Category of system aspect type | Description | Aspect types that Knowledge Catalog provides  
---|---|---  
Reusable system aspect type | You can use these aspect types to create or modify aspects. | 

  * `contacts`
  * `data-profile`
  * `data-quality-scorecard`
  * `generic`
  * `graph-profile`
  * `guidelines`
  * `overview`
  * `schema-join`
  * `schema`
  * `storage`
  * `usage`

  
Restricted system aspect type | Knowledge Catalog manages these aspect types.  
You can read aspects under these aspect types, but can't create or edit aspects under these aspect types.  |  Including but not limited to: 

  * `analytics-hub`
  * `aspecttype-aspect`
  * `bigquery-dataset`
  * `bigquery-table`
  * `cloudsql-database`
  * `cloudsql-instance`
  * `cloudsql-table`
  * `entrygroup-aspect`
  * `entrytype-aspect`
  * `sensitive-data-protection-profile`
  * `storage-bucket`
  * `storage-folder`

  
  
### Custom aspect types and Gemini in BigQuery

**Gemini Context Retrieval Boundary:** Gemini in BigQuery grounds SQL generation and data reasoning on standard schema definitions, table constraints, and table or column description fields. User-defined custom aspect types in Knowledge Catalog are stored in the catalog plane for governance, search, and API retrieval, but are not dynamically injected into Gemini's contextual prompt retrieval pipeline.

#### Recommended best practice

To ensure business logic, semantic context, or developer notes are visible to Gemini in BigQuery, document them directly in the [table](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_a_tables_description) and [column description](https://docs.cloud.google.com/bigquery/docs/managing-table-schemas#change-column-description) fields, within the standard `overview` aspect, or by using [business glossary terms](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).

For more information, see [Use Knowledge Catalog with BigQuery](https://docs.cloud.google.com/bigquery/docs/use-knowledge-catalog).

## What are aspects?

Aspects let you capture metadata within entries or entry links to provide meaningful context. You can use aspects to store the following types of metadata:

  * **Business metadata** : Information that provides business context, such as data classification. For example, regulated industries need to protect PII—such as names, addresses, and government-issued ID numbers—across distributed data systems. After you catalog your distributed data assets, you can classify data as PII and then apply data quality or access policies to the data.

  * **Technical metadata** : Technical details of entries or entry links, including the following:

    * For entries: details about the data asset itself, for example, its schema.
    * For entry links: details about the relationship between data assets, for example, join details.
  * **Data-derived metadata** : Information generated from the data itself, such as statistics from a BigQuery table.




Aspects are component parts of the parent entry resource rather than separate standalone resources. Modifying an aspect updates the containing entry. To track these modifications, you can subscribe to [Metadata change feeds](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-change-feeds-overview).

### Aspect placement and target levels

Every aspect is an instance of an aspect type template, which defines the fields you must populate—for example, `{"pii_classification": "confidential", "gdpr_compliant": true}`. You can apply an aspect to an entire table, an individual table column, or an entry link. Where you can apply an aspect and how many times it can appear depends on the target resource type:

Target resource | Supported levels | Cardinality limits  
---|---|---  
Entries | Entry-level or column-level | Maximum of one aspect per aspect type at the entry level. Multiple aspects per aspect type are allowed across different columns.  
Entry links | Link-level only | Maximum of one aspect per aspect type per link.  
**Note:** You can't create or use aspects if the parent aspect type and the target entry (or entry link) belong to different Google Cloud organizations.

### Categories of aspects

Aspects are categorized into required aspects and optional aspects:

#### Required aspects

Required aspects are the aspects that are mandatory upon creation of an entry or entry link. Such aspects are defined by the entry type or entry link type. All resources belonging to a specific type must always have all of the required aspects that are defined by that type.

Knowledge Catalog manages the required aspects (for example, schema) for [system entries](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#categories-entries).

Note the following:

  * You can associate required aspects only with entries and not with its columns.

  * You can't delete the required aspects from an entry or entry link.

  * You can read the required aspects of system entries, but can't modify them.

  * Data aspects can't be required aspects.




#### Optional aspects

You can associate optional aspects with entries or with entry columns. You can populate optional aspects either at the time of entry creation, or later by updating the entry.

Note the following:

  * You can delete optional aspects after they have been populated.

  * Entry links support only required aspects.




### Data aspects

Some aspects contain information derived from the underlying data of an entry, rather than metadata about the entry. These are referred to as data aspects. For example, the results of a data profile scan or a data quality scan contain statistics derived from the data itself, and are therefore classified as data aspects.

System aspect types that are data aspects include the following:

  * `data-profile`: Contains results from a data profile scan. For more information, see [About data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profiling).
  * `data-quality-scorecard`: Contains a summary of data quality scores.
  * [`data-rules`](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules#data-rules-fields): Attach data quality rules to an entry.
  * [`data-quality-rule-template`](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules#rule-template-fields): Define a reusable data quality rule template.



## Before you begin

Before you create and manage aspect types and aspects, complete the tasks described in this section.

### Required roles

To get the permissions that you need to create and manage aspect types and aspects, ask your administrator to grant you the following IAM roles on the resource: 

  * Full set of permissions on metadata resources in Knowledge Catalog, including aspect types and data aspects: [**Dataplex Catalog Admin** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) 
  * Create and manage metadata resources in Knowledge Catalog, including aspect types and data aspects: [**Dataplex Catalog Editor** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) 
  * Full set of permissions on custom aspect types (except for permissions to use aspect types to create or edit entries): [**Dataplex Aspect Type Owner** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeOwner) (`roles/dataplex.aspectTypeOwner`) 
  * View aspect types and IAM policies associated with them: [**Dataplex Catalog Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) 
  * Use aspect types to create and modify entries with the corresponding aspects: [**Dataplex Aspect Type User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`) 
  * Add aspects of some of the system aspect types, such as `schema`, `schema-join`, `overview`, `contacts`: [**Dataplex Entry and EntryLink Owner** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information, see [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles).

### Enable the API

Enable the Dataplex API in your Knowledge Catalog project. If you are using a new Google Cloud project or a project in which the BigQuery API is enabled, the Dataplex API is enabled by default.

[Enable the API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com)

## Create a custom aspect type

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog)

  2. Click the **Aspect types > Custom** tab.

  3. Click **Create aspect type**.

  4. In the **Create aspect type** window, enter the following:

     1. Optional: In the **Display name** field, enter a name for the aspect type.
     2. In the **Aspect type ID** field, enter a unique ID for the aspect type.
     3. Optional: In the **Description** field, enter a description for the aspect type.
     4. In the **Location** field, select a location for the aspect type. You can't modify the location of an aspect type after you create it. To understand the impact of choosing a global versus a regional location, see the Custom aspect types section.
  5. Optional: Define a template for your aspect type.

In the **Template** section, click **Add field**. In the **New field** section, enter the following:

     1. In the **Name** field, enter a name.
     2. Optional: In the **Display name** field, enter a display name.
     3. Optional: In the **Description** field, enter a description.
     4. In the **Type** field, select a data type for the field. Based on your selection, the next set of fields and options are displayed:

        * If you selected **Text** as the data type, follow these steps:

          1. In the **Text type** field, select the type of text.
          2. In the **Text values** field, provide a hint for the text field. To do this, click **Add value** and enter the hint. You can add multiple hints for a text field.
          3. Click **Done**.
        * If you selected **Enum** as the data type, add an enum value:

          1. Click **Add an enum value**.
          2. In the **Value** field, enter an enum value. You can add multiple enum values.
          3. Click **Done**.
        * If you selected **Array** as the data type, in the **Array item** section, define the types of items to be present in the array:

          1. Click **Add array item**.
          2. In the **Name** field, enter a name for the array items.
          3. Optional: In the **Display name** field, enter a display name for the array items.
          4. Optional: In the **Description** field, enter a description for the array items.
          5. In the **Type** field, select a data type for the array items.

Based on your selection, the next set of fields and options are displayed. They are similar to the options described for the data types **Text** , **Enum** , **Map** , **Array** , and **Record** elsewhere in this section.

          6. Click **Done**.

        * If you selected **Map** as the data type, in the **Map value** section, define the types of values to be present in the map:

          1. Click **Add map value**.
          2. In the **Name** field, enter a name for the map.
          3. Optional: In the **Display name** field, enter a display name for the map.
          4. Optional: In the **Description** field, enter a description for the map.
          5. In the **Type** field, select a data type for the map.

Based on your selection, the next set of fields and options are displayed. They are similar to the options described for the data types **Text** , **Enum** , **Map** , **Array** , and **Record** elsewhere in this section.

          6. Click **Done**.

        * If you selected **Record** as the data type, enter the following:

          1. In the **Record ID** field, enter a unique ID that other record fields can use to refer to this record. See the Example for using the Record ID and Record reference fields section of this document.
          2. Optional: If you want to add a reference to another record from this template, use the **Record reference** field. You can't modify this after you create the aspect type. See the Example for using the Record ID and Record reference fields section of this document.
          3. In the **Record fields** section, you can define a complex object with multiple nested fields. To do this, click **Add record field item** , and specify the following:

          4. In the **Name** field, enter a name for the record field.

          5. Optional: In the **Display name** field, enter a display name for the record field.

          6. Optional: In the **Description** field, enter a description for the record field.

          7. In the **Type** field, select a data type.

Based on your selection, the next set of fields and options are displayed. They are similar to the options described for the data types **Text** , **Enum** , **Map** , **Array** , and **Record** earlier in this section.

          8. Click **Done**.

     5. To make the field mandatory for an aspect of this type, select **Is required**. For more information about required aspects and optional aspects, see the categories of aspects section of this document.

     6. Click **Done**.

     7. To add multiple fields, click **Add field** and repeat the previous steps.

  6. Optional: In the **Labels** section, add arbitrary labels as key-value pairs to your resources:

     1. Click **Add label**.
     2. In the **Key** field, enter a key.
     3. In the **Value** field, enter a value for the key.
     4. To add more labels, click **Add label** and repeat the steps.
  7. Click **Save**.




###  gcloud 

To create a custom aspect type, use the [`gcloud dataplex aspect-types create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/create).

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for CreateAspectType</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateAspectTypeRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [CreateAspectTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateAspectTypeRequest.html) request = new [CreateAspectTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateAspectTypeRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                AspectTypeId = "",
                AspectType = new [AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html)(),
                ValidateOnly = false,
            };
            // Make the request
            Operation<AspectType, OperationMetadata> response = catalogServiceClient.[CreateAspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_CreateAspectType_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Dataplex_V1_AspectType_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<AspectType, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<AspectType, OperationMetadata> retrievedResponse = catalogServiceClient.[PollOnceCreateAspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_PollOnceCreateAspectType_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.CreateAspectTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#CreateAspectTypeRequest.
    	}
    	op, err := c.CreateAspectType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[CreateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAspectTypeRequest.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    
    public class SyncCreateAspectType {
    
      public static void main(String[] args) throws Exception {
        syncCreateAspectType();
      }
    
      public static void syncCreateAspectType() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [CreateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAspectTypeRequest.html) request =
              [CreateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAspectTypeRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .[setAspectTypeId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAspectTypeRequest.Builder.html#com_google_cloud_dataplex_v1_CreateAspectTypeRequest_Builder_setAspectTypeId_java_lang_String_)("aspectTypeId-423030675")
                  .setAspectType([AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).newBuilder().build())
                  .setValidateOnly(true)
                  .build();
          [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) response = catalogServiceClient.[createAspectTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_createAspectTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_LocationName_com_google_cloud_dataplex_v1_AspectType_java_lang_String_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the AspectType, of the form:
     *  projects/{project_number}/locations/{location_id}
     *  where `location_id` refers to a Google Cloud region.
     */
    // const parent = 'abc123'
    /**
     *  Required. AspectType identifier.
     */
    // const aspectTypeId = 'abc123'
    /**
     *  Required. AspectType Resource.
     */
    // const aspectType = {}
    /**
     *  Optional. The service validates the request without performing any
     *  mutations. The default is false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callCreateAspectType() {
      // Construct request
      const request = {
        parent,
        aspectTypeId,
        aspectType,
      };
    
      // Run request
      const [operation] = await dataplexClient.createAspectType(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateAspectType();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_create_aspect_type():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        aspect_type = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html)()
        aspect_type.metadata_template.name = "name_value"
        aspect_type.metadata_template.type_ = "type__value"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CreateAspectTypeRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.CreateAspectTypeRequest.html)(
            parent="parent_value",
            aspect_type_id="aspect_type_id_value",
            aspect_type=aspect_type,
        )
    
        # Make the request
        operation = client.[create_aspect_type](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_create_aspect_type)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the create_aspect_type call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#create_aspect_type.
    #
    def create_aspect_type
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::CreateAspectTypeRequest.new
    
      # Call the create_aspect_type method.
      result = client.create_aspect_type request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

### REST

To create a custom aspect type, use the [`aspectType.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/create) method.

After you create a custom aspect type, you can add aspects to entries.

### Example for using the Record ID and Record reference fields

You can use the **Record ID** and **Record reference** fields for recursive references. The following example shows how to use these fields:

Consider an aspect type called `Employee`, with the following fields:

  * _Name_ (type: `Text`)
  * _Start date_ (type: `Date & time`)
  * _Designation_ (type: `Text`)
  * _Current address_ (type: `Record`)
  * _Permanent address_ (type: `Record`)



The two address fields _Current address_ and _Permanent address_ are of the same data type `Record`. To avoid duplication, you can set the **Record ID** and **Record reference** values when defining these fields.

When you define the field _Current address_ , you can specify **Record ID** as `address-field`. For _Permanent address_ , you can specify the same value (`address-field`) for **Record reference**. For example:

  * _Name_ (type: `Text`)
  * _Start date_ (type: `Date & time`)
  * _Designation_ (type: `Text`)
  * _Current address_ (type: `Record`, Record ID: `address-field`)
  * _Permanent address_ (type: `Record`, Record reference: `address-field`)



This way, you don't need to duplicate the fields of another address.

## Add aspects to an entry

After you create a custom aspect type, you can create aspects of that type. To add aspects to an entry, you must update the entry, as aspects are stored within entries.

Note the following:

  * You can add aspects to an entry or to the columns of an entry.
  * You can edit the required aspects only for custom entries. You can't delete the required aspects.
  * You can edit and delete the optional aspects for both custom entries and system entries.

**Note:** When you use a [`CREATE OR REPLACE TABLE` statement](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_statement) to replace a BigQuery table, the metadata (including aspects) that was associated with the original table isn't applied to the new table. If you want the metadata to persist, you can [create a BigQuery view](https://docs.cloud.google.com/bigquery/docs/views) for the table and add the metadata to the view.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Search for the entry that you want to add aspects to, and click the entry. The entry details page opens.

  3. To add aspects to the entry, follow these steps:

     1. Click the **Details** tab.
     2. To add required aspects or optional aspects to the entry, in the **Aspects** section, click add **Add** for the respective category.  
You can't add required aspects if the entry type of the selected entry has no required aspects defined.  

     3. Search for and select the aspect you want to add.
     4. In the **Add aspect** window, enter the values for the fields.
     5. Click **Save**.

     6. To add aspects to a column of the entry, follow these steps:

     7. On the entry details page, click the **Schema** tab.

     8. Select the columns to which you want to add aspects.

     9. Click **Add aspect**.

     10. Search for and select the aspect you want to add.

     11. In the **Add aspect** window, enter the values for the fields.

     12. Click **Save**.




###  gcloud 

To add aspects to an entry or to a column of an entry, use the [`gcloud dataplex entries update` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/update).

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for UpdateEntry</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateEntryRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateEntryRequest.html) request = new [UpdateEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateEntryRequest.html)
            {
                Entry = new [Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Entry.html)(),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                AllowMissing = false,
                DeleteMissingAspects = false,
                AspectKeys = { "", },
            };
            // Make the request
            [Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Entry.html) response = catalogServiceClient.[UpdateEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_UpdateEntry_Google_Cloud_Dataplex_V1_Entry_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

To add aspects to the entry object, see [Aspects](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Entry#Google_Cloud_Dataplex_V1_Entry_Aspects).

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.UpdateEntryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#UpdateEntryRequest.
    	}
    	resp, err := c.UpdateEntry(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

To add aspects to the entry object, see [Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1/dataplexpb#cloud_google_com_go_dataplex_apiv1_dataplexpb_Entry).

### Java

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

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. Entry resource.
     */
    // const entry = {}
    /**
     *  Optional. Mask of fields to update. To update Aspects, the update_mask must
     *  contain the value "aspects".
     *  If the update_mask is empty, the service will update all modifiable fields
     *  present in the request.
     */
    // const updateMask = {}
    /**
     *  Optional. If set to true and the entry doesn't exist, the service will
     *  create it.
     */
    // const allowMissing = true
    /**
     *  Optional. If set to true and the aspect_keys specify aspect ranges, the
     *  service deletes any existing aspects from that range that weren't provided
     *  in the request.
     */
    // const deleteMissingAspects = true
    /**
     *  Optional. The map keys of the Aspects which the service should modify. It
     *  supports the following syntaxes:
     *  * `<aspect_type_reference>` - matches an aspect of the given type and empty
     *  path.
     *  * `<aspect_type_reference>@path` - matches an aspect of the given type and
     *  specified path. For example, to attach an aspect to a field that is
     *  specified by the `schema` aspect, the path should have the format
     *  `Schema.<field_name>`.
     *  * `<aspect_type_reference>@*` - matches aspects of the given type for all
     *  paths.
     *  * `*@path` - matches aspects of all types on the given path.
     *  The service will not remove existing aspects matching the syntax unless
     *  `delete_missing_aspects` is set to true.
     *  If this field is left empty, the service treats it as specifying
     *  exactly those Aspects present in the request.
     */
    // const aspectKeys = ['abc','def']
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callUpdateEntry() {
      // Construct request
      const request = {
        entry,
      };
    
      // Run request
      const response = await dataplexClient.updateEntry(request);
      console.log(response);
    }
    
    callUpdateEntry();

### Python

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

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the update_entry call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#update_entry.
    #
    def update_entry
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::UpdateEntryRequest.new
    
      # Call the update_entry method.
      result = client.update_entry request
    
      # The returned object is of type Google::Cloud::Dataplex::V1::Entry.
      p result
    end

To add aspects to the entry object, see [#required_aspects=](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-EntryType#Google__Cloud__Dataplex__V1__EntryType_required_aspects__instance_). 

### REST

To add aspects to an entry or to a column of an entry, use the [`entry.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

Creating and using aspects in an entry where the respective aspect type and the entry are in different Google Cloud organizations isn't supported.

### Attach aspects of reusable system aspect types

You can attach aspects of reusable system aspect types to entries.

You can edit an aspect of a reusable aspect type in the Google Cloud console depending on its structure. Aspect types that contain nested fields are not supported for editing in Google Cloud console. You must use the `gcloud` command-line tool or the REST API to attach or update aspects of this type.

### Data quality scorecard

A data quality scorecard is an aspect that provides a summary of data quality, often based on data quality scans or other processes. You can attach a data quality scorecard to an entry to provide custom data quality information. To do so, attach an aspect of the system-defined type `data-quality-scorecard`.

The `data` field within the `data-quality-scorecard` aspect can include the following fields:

  * `job`: Optional. A record containing details about the job that generated the scorecard.

    * `name`: The resource name of the data quality job.

    * `runTime`: The run time of the data quality job.

  * `score`: Optional. The overall data quality score. The score ranges between [0, 100].

  * `status`: Required. The status of the data quality scorecard, indicating if it passed or failed the quality threshold (`PASS` or `FAIL`).

  * `dimensions`: Optional. An array of dimension results. Each result includes:

    * `name`: The name of the dimension. This can be one of `ACCURACY`, `COMPLETENESS`, `CONSISTENCY`, `FRESHNESS`, `UNIQUENESS`, `VALIDITY`, or `VOLUME`, or a custom dimension name. Custom dimension names must use uppercase letters and be 30 characters or less.

    * `score`: The overall dimension-level score, ranging from [0, 100].

    * `status`: The status of the dimension, indicating if it passed or failed the quality threshold (`PASS` or `FAIL`).

  * `columns`: Optional. An array of column results. Each result includes:

    * `name`: The name of the column.

    * `score`: The overall column-level score, ranging from [0, 100].

    * `status`: The status of the column, indicating if it passed or failed the quality threshold (`PASS` or `FAIL`).

    * `dimensions`: An array of dimension scores for the column. Each dimension score includes:

      * `name`: The name of the dimension.

      * `score`: The score for the dimension, ranging from [0, 100].

      * `status`: The status of the dimension for the column, indicating if it passed or failed the quality threshold (`PASS` or `FAIL`).




When you run the command to attach an aspect, it replaces any existing data for that specific aspect. For example, if you update a scorecard that has a score of `80` with a new file showing a score of `90`, the `80` is overwritten. It does not merge the data.

To attach a data quality scorecard, follow these steps:

###  gcloud 

To update aspects for an entry, use the [`gcloud dataplex entries update-aspects` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/update-aspects).

  1. Create a JSON file (`dq-aspect.json`) with the following content.

**Note:** The key for the aspect map follows the format `dataplex-types.global.<ASPECT-TYPE>`.
         
         {
             "dataplex-types.global.data-quality-scorecard": {
               "data": {
                 "score": 0.8,
                 "status": "PASS",
                 "dimensions": [
                   {
                     "name": "completeness",
                     "score": 0.9,
                     "status": "PASS"
                   },
                   {
                     "name": "uniqueness",
                     "score": 0.7,
                     "status": "FAIL"
                   }
                 ],
                 "columns": [
                   {
                     "name": "col1",
                     "score": 0.85,
                     "status": "PASS"
                   }
                 ]
               }
             }
           }
         }
         

  2. Run the following command:
         
         gcloud dataplex entries update-aspects ENTRY_ID
           --location=LOCATION
           --entry-group=ENTRY_GROUP_ID
           --project=PROJECT_ID
           --aspects=dq-aspect.json
         

Replace the following variables:

     * `ENTRY_ID`: the ID of the entry—for example, `example-entry`
     * `LOCATION`: the location of the entry—for example, `us-central1`
     * `ENTRY_GROUP_ID`: the ID of the entry group—for example, `example-entry-group`
     * `PROJECT_ID`: the ID of the project—for example, `example-project`



### REST

To update aspects for an entry, use the [`entry.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

  1. Create a file named `payload.json` and paste the JSON content from your request into it.
         
           {
             "aspects": {
               "dataplex-types.global.data-quality-scorecard": {
                 "data": {
                   "score": 80,
                   "status": "PASS",
                   "dimensions": [
                     {
                       "name": "completeness",
                       "score": 90,
                       "status": "PASS"
                     },
                     {
                       "name": "uniqueness",
                       "score": 70,
                       "status": "FAIL"
                     }
                   ],
                   "columns": [
                     {
                       "name": "col1",
                       "score": 85,
                       "status": "PASS"
                     }
                   ]
                 }
               }
             }
           }
         

  2. Run this command in your terminal:
         
         curl -X PATCH \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          -d @payload.json \
          "https://dataplex.googleapis.com/v1/projects/<var>PROJECT_ID</var>/locations/<var>LOCATION</var>/entryGroups/<var>ENTRY_GROUP_ID</var>/entries/<var>ENTRY_ID</var>?updateMask=aspects"
         

Replace the following:

     * `PROJECT_ID`: the ID of the project—for example, `example-project`
     * `LOCATION`: the location of the entry—for example, `us-central1`
     * `ENTRY_GROUP_ID`: the ID of the entry group—for example, `example-entry-group`
     * `ENTRY_ID`: the ID of the entry—for example, `example-entry`



### Other reusable aspect types

The following system aspect types are also available for use. You can attach them using the same `gcloud` or REST API methods as shown for the data quality scorecard. For aspect types without nested fields, for example, `generic`, you can use the console.

  * **Contacts.** Use the `contacts` aspect type to assign ownership or stewardship. The fields include the following:

    * `identities` (array): A list of contacts. Each contact includes: 
      * `role` (string): The role of the contact (for example, `owner`, `steward`, `producer`, or `admin`).
      * `name` (string): The name of the contact.
      * `id` (string): The email address or ID of the contact.

Create the `payload.json` file as follows:
    
    {
       "aspects": {
         "dataplex-types.global.contacts": {
           "data": {
             "identities": [
               {
                 "role": "steward",
                 "name": "Jane Doe",
                 "id": "jane.doe@example.com"
               }
             ]
           }
         }
       }
     }
    

  * **Data profile.** Use the `data-profile` aspect type to capture data profiling results. For more information, see [About data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profiling).

The fields include the following:

    * `sourceDataInfo` (record): Information about the source data scanned to generate the profile. 
      * `scope` (enum): The scope of the profile (`PREVIEW`, `SAMPLED`, or `ALL`). The `PREVIEW` value corresponds to results from a [Lightweight profiling scan](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview#configuration-options).
      * `scannedRows` (int): The number of rows scanned.
      * `samplingPercentage` (double): The sampling percentage used.
    * `fields` (map): A map of column names to their data profiles, including metrics such as `uniqueness`, `nullness`, `topN` values, and type-specific statistics for `numeric`, `string`, `datetime`, and `array` columns.

Create the `payload.json` file as follows:
    
    {
       "aspects": {
         "dataplex-types.global.data-profile": {
           "data": {
             "sourceDataInfo": {
             "scope": "ALL",
             "scannedRows": 100
           },
           "fields": {
             "col1": {
               "nullness": 0.0,
               "uniqueness": 0.1,
          "string": {
            "length": {
              "min": 1,
              "max": 20,
              "avg": 12.54
            }
          }
             }
           }
         }
       }
     }}
    

  * **Generic.** Use the `generic` aspect type for generic entry information. The fields include the following:

    * `type` (string): A freeform field to store a user-specified type.
    * `system` (string): The system of the custom entry.

Create the `payload.json` file as follows:
    
    {
      "aspects": {
        "dataplex-types.global.generic": {
          "data": {
            "type": "custom-type",
            "system": "custom-system"
          }
        }
      }
    }
    

  * **Overview.** Use the `overview` aspect type to provide a rich text description. The fields include the following:

    * `content` (string): The entry overview, which supports HTML format.
    * `links` (array): A list of source system links. Each link includes: 
      * `url` (string): The URL of the link.
      * `title` (string): The title of the link.

Create the `payload.json` file as follows:
    
    {
      "aspects": {
        "dataplex-types.global.overview": {
          "data": {
            "content": "This is a <b>rich text</b> description.",
          "links": [
            {
              "url": "https://example.com",
              "title": "Example Link"
            }
          ]
        }
      }
    }}
    

  * **Schema.** Use the `schema` aspect type to describe the structure of data.

    * `fields` (array): A list of schema fields. The fields include the following: 
      * `name` (string): The name of the field.
      * `dataType` (string): The data type of the field.
      * `metadataType` (enum): The metadata type (for example, `STRING`, `BOOLEAN`).
      * `mode` (enum): The mode of the field (`NULLABLE`, `REQUIRED`, `REPEATED`).
      * `description` (string): A description of the field.

Create the `payload.json` file as follows:
    
    {
      "aspects": {
        "dataplex-types.global.schema": {
          "data": {
            "fields": [
            {
              "name": "id",
              "dataType": "string",
              "metadataType": "STRING",
              "mode": "REQUIRED"
            }
          ]
        }
      }
    }}
    

  * **Usage.** Use the `usage` aspect type to track usage metrics. The fields include the following:

    * `metrics` (array): A list of usage metrics. Each metric includes: 
      * `name` (string): The name of the metric (for example, `views`, `reads`).
      * `timeSeries` (array): A list of time series data. Each item includes: 
        * `interval` (string): The aggregation interval (for example, `30d`).
        * `value` (integer): The aggregated value.
    * `refreshTime` (datetime): The time when the metrics were last refreshed.

Create the `payload.json` file as follows:
    
    {
      "aspects": {
        "dataplex-types.global.usage": {
          "data": {
            "metrics": [
            {
              "name": "views",
              "timeSeries": [
                {
                  "interval": "30d",
                  "value": 100
                }
              ]
            }
          ],
          "refreshTime": "2025-01-01T12:00:00Z"
        }
      }
    }}
    




## Create an entry link

You can establish a relationship between two entries by creating an entry link.

An entry link can be symmetric such as a `synonym` or asymmetric such as a `definition`.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for CreateEntryLink</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateEntryLinkRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [CreateEntryLinkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateEntryLinkRequest.html) request = new [CreateEntryLinkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateEntryLinkRequest.html)
            {
                ParentAsEntryGroupName = [EntryGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryGroupName.html).[FromProjectLocationEntryGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryGroupName.html#Google_Cloud_Dataplex_V1_EntryGroupName_FromProjectLocationEntryGroup_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]"),
                EntryLinkId = "",
                EntryLink = new [EntryLink](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryLink.html)(),
            };
            // Make the request
            [EntryLink](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryLink.html) response = catalogServiceClient.[CreateEntryLink](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_CreateEntryLink_Google_Cloud_Dataplex_V1_CreateEntryLinkRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.CreateEntryLinkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#CreateEntryLinkRequest.
    	}
    	resp, err := c.CreateEntryLink(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[CreateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryLinkRequest.html);
    import com.google.cloud.dataplex.v1.[EntryGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroupName.html);
    import com.google.cloud.dataplex.v1.[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink.html);
    
    public class SyncCreateEntryLink {
    
      public static void main(String[] args) throws Exception {
        syncCreateEntryLink();
      }
    
      public static void syncCreateEntryLink() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [CreateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryLinkRequest.html) request =
              [CreateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryLinkRequest.html).newBuilder()
                  .setParent([EntryGroupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroupName.html).of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
                  .[setEntryLinkId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryLinkRequest.Builder.html#com_google_cloud_dataplex_v1_CreateEntryLinkRequest_Builder_setEntryLinkId_java_lang_String_)("entryLinkId-1349584441")
                  .setEntryLink([EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink.html).newBuilder().build())
                  .build();
          [EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink.html) response = catalogServiceClient.createEntryLink(request);
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the parent Entry Group:
     *  `projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}`.
     */
    // const parent = 'abc123'
    /**
     *  Required. Entry Link identifier
     *  * Must contain only lowercase letters, numbers and hyphens.
     *  * Must start with a letter.
     *  * Must be between 1-63 characters.
     *  * Must end with a number or a letter.
     *  * Must be unique within the EntryGroup.
     */
    // const entryLinkId = 'abc123'
    /**
     *  Required. Entry Link resource.
     */
    // const entryLink = {}
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callCreateEntryLink() {
      // Construct request
      const request = {
        parent,
        entryLinkId,
        entryLink,
      };
    
      // Run request
      const response = await dataplexClient.createEntryLink(request);
      console.log(response);
    }
    
    callCreateEntryLink();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_create_entry_link():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        entry_link = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryLink](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryLink.html)()
        entry_link.entry_link_type = "entry_link_type_value"
        entry_link.entry_references.name = "name_value"
        entry_link.entry_references.type_ = "TARGET"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CreateEntryLinkRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.CreateEntryLinkRequest.html)(
            parent="parent_value",
            entry_link_id="entry_link_id_value",
            entry_link=entry_link,
        )
    
        # Make the request
        response = client.[create_entry_link](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_create_entry_link)(request=request)
    
        # Handle the response
        print(response)
    
    

### REST

To create an entry link with the required aspect, use the [`entryLinks.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks/create) method, including the aspect data in the request body.

### Add aspects to an entry link

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To enrich metadata with information about relationships between the entries, add aspects to entry links.

You can configure entry link types to require a specific aspect. When you create an entry link of such type, you must provide the required aspect.

You can add these aspects when you create an entry link, or by updating an existing entry link, as follows:

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for UpdateEntryLink</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateEntryLinkRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateEntryLinkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateEntryLinkRequest.html) request = new [UpdateEntryLinkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateEntryLinkRequest.html)
            {
                EntryLink = new [EntryLink](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryLink.html)(),
                AllowMissing = false,
                AspectKeys = { "", },
            };
            // Make the request
            [EntryLink](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.EntryLink.html) response = catalogServiceClient.[UpdateEntryLink](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_UpdateEntryLink_Google_Cloud_Dataplex_V1_EntryLink_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.UpdateEntryLinkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#UpdateEntryLinkRequest.
    	}
    	resp, err := c.UpdateEntryLink(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink.html);
    import com.google.cloud.dataplex.v1.[UpdateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryLinkRequest.html);
    import java.util.ArrayList;
    
    public class SyncUpdateEntryLink {
    
      public static void main(String[] args) throws Exception {
        syncUpdateEntryLink();
      }
    
      public static void syncUpdateEntryLink() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [UpdateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryLinkRequest.html) request =
              [UpdateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryLinkRequest.html).newBuilder()
                  .setEntryLink([EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink.html).newBuilder().build())
                  .setAllowMissing(true)
                  .addAllAspectKeys(new ArrayList<String>())
                  .build();
          [EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink.html) response = catalogServiceClient.updateEntryLink(request);
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. Entry Link resource.
     */
    // const entryLink = {}
    /**
     *  Optional. If set to true and the entry link doesn't exist, the service will
     *  create it.
     */
    // const allowMissing = true
    /**
     *  Optional. The map keys of the Aspects which the service should modify.
     *  It should be the aspect type reference in the format
     *  `{project_id_or_number}.{location_id}.{aspect_type_id}`.
     *  If this field is left empty, the service treats it as specifying
     *  exactly those Aspects present in the request.
     */
    // const aspectKeys = ['abc','def']
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callUpdateEntryLink() {
      // Construct request
      const request = {
        entryLink,
      };
    
      // Run request
      const response = await dataplexClient.updateEntryLink(request);
      console.log(response);
    }
    
    callUpdateEntryLink();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_update_entry_link():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        entry_link = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryLink](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryLink.html)()
        entry_link.entry_link_type = "entry_link_type_value"
        entry_link.entry_references.name = "name_value"
        entry_link.entry_references.type_ = "TARGET"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[UpdateEntryLinkRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.UpdateEntryLinkRequest.html)(
            entry_link=entry_link,
        )
    
        # Make the request
        response = client.[update_entry_link](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_update_entry_link)(request=request)
    
        # Handle the response
        print(response)
    
    

### REST

To update an entry link, use the [`entryLinks.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks/patch) method, including the aspect data in the [`entryLink`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks#EntryLink) body.

Note the following limitations for using aspects with entry links:

  * Optional aspects aren't supported.
  * [Data aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#data-aspects) are not supported.
  * Aspects of custom types aren't supported.
  * You can only manage required aspects defined by system aspect types, for example, `schema-join`.
  * Searching for entry links based on the content of their aspects isn't supported.
  * Importing or exporting entry link aspects isn't supported.



## Manage existing aspects for an entry

This section describes how to update and delete the existing aspects for an entry.

### Update an aspect

You can edit the optional aspects for both custom entries and system entries. You can edit the required aspects only for custom entries.

For first-party (1P) system entries, such as BigQuery tables, you can update aspects using the `modifyEntry` API. This lets you use the source system's metadata update permissions (for example, **BigQuery Data Editor** (`roles/bigquery.dataEditor`)).

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Search for the entry whose aspects you want to update, and click the entry.




The entry details page opens.

  1. Click the **Details** tab.
  2. In the **Aspects** section, expand the aspect that you want to update, and click edit **Edit**.
  3. In the **Edit aspect** window, update the required fields.
  4. Click **Save**.



###  gcloud 

To update aspects for an entry or a column of an entry, use the [`gcloud dataplex entries update` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/update).

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for UpdateEntry</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateEntryRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateEntryRequest.html) request = new [UpdateEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateEntryRequest.html)
            {
                Entry = new [Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Entry.html)(),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                AllowMissing = false,
                DeleteMissingAspects = false,
                AspectKeys = { "", },
            };
            // Make the request
            [Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Entry.html) response = catalogServiceClient.[UpdateEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_UpdateEntry_Google_Cloud_Dataplex_V1_Entry_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.UpdateEntryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#UpdateEntryRequest.
    	}
    	resp, err := c.UpdateEntry(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html);
    import com.google.cloud.dataplex.v1.[UpdateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.util.ArrayList;
    
    public class SyncUpdateEntry {
    
      public static void main(String[] args) throws Exception {
        syncUpdateEntry();
      }
    
      public static void syncUpdateEntry() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [UpdateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryRequest.html) request =
              [UpdateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryRequest.html).newBuilder()
                  .setEntry([Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html).newBuilder().build())
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .setAllowMissing(true)
                  .setDeleteMissingAspects(true)
                  .addAllAspectKeys(new ArrayList<String>())
                  .build();
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) response = catalogServiceClient.updateEntry(request);
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. Entry resource.
     */
    // const entry = {}
    /**
     *  Optional. Mask of fields to update. To update Aspects, the update_mask must
     *  contain the value "aspects".
     *  If the update_mask is empty, the service will update all modifiable fields
     *  present in the request.
     */
    // const updateMask = {}
    /**
     *  Optional. If set to true and the entry doesn't exist, the service will
     *  create it.
     */
    // const allowMissing = true
    /**
     *  Optional. If set to true and the aspect_keys specify aspect ranges, the
     *  service deletes any existing aspects from that range that weren't provided
     *  in the request.
     */
    // const deleteMissingAspects = true
    /**
     *  Optional. The map keys of the Aspects which the service should modify. It
     *  supports the following syntaxes:
     *  * `<aspect_type_reference>` - matches an aspect of the given type and empty
     *  path.
     *  * `<aspect_type_reference>@path` - matches an aspect of the given type and
     *  specified path. For example, to attach an aspect to a field that is
     *  specified by the `schema` aspect, the path should have the format
     *  `Schema.<field_name>`.
     *  * `<aspect_type_reference>@*` - matches aspects of the given type for all
     *  paths.
     *  * `*@path` - matches aspects of all types on the given path.
     *  The service will not remove existing aspects matching the syntax unless
     *  `delete_missing_aspects` is set to true.
     *  If this field is left empty, the service treats it as specifying
     *  exactly those Aspects present in the request.
     */
    // const aspectKeys = ['abc','def']
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callUpdateEntry() {
      // Construct request
      const request = {
        entry,
      };
    
      // Run request
      const response = await dataplexClient.updateEntry(request);
      console.log(response);
    }
    
    callUpdateEntry();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_update_entry():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        entry = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entry.html)()
        entry.entry_type = "entry_type_value"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[UpdateEntryRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.UpdateEntryRequest.html)(
            entry=entry,
        )
    
        # Make the request
        response = client.[update_entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_update_entry)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the update_entry call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#update_entry.
    #
    def update_entry
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::UpdateEntryRequest.new
    
      # Call the update_entry method.
      result = client.update_entry request
    
      # The returned object is of type Google::Cloud::Dataplex::V1::Entry.
      p result
    end

### REST

To update aspects for an entry or a column of an entry, use the [`entry.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

### Delete an aspect

**Note:** You can delete the optional aspects for an entry, but not the required aspects.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. If your search platform is set to **Data Catalog** , in the **Choose search platform** menu, select **Dataplex Universal Catalog**.

  3. Search for the entry whose aspects you want to delete, and click the entry.




The entry details page opens.

  1. Click the **Details** tab.
  2. In the **Aspects** section, expand the aspect that you want to delete, click delete **Delete**.
  3. Click **Confirm**.



###  gcloud 

To delete an aspect for an entry, use the [`gcloud dataplex entries update` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/update).

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for UpdateEntry</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateEntryRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateEntryRequest.html) request = new [UpdateEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateEntryRequest.html)
            {
                Entry = new [Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Entry.html)(),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                AllowMissing = false,
                DeleteMissingAspects = false,
                AspectKeys = { "", },
            };
            // Make the request
            [Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Entry.html) response = catalogServiceClient.[UpdateEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_UpdateEntry_Google_Cloud_Dataplex_V1_Entry_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.UpdateEntryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#UpdateEntryRequest.
    	}
    	resp, err := c.UpdateEntry(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html);
    import com.google.cloud.dataplex.v1.[UpdateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.util.ArrayList;
    
    public class SyncUpdateEntry {
    
      public static void main(String[] args) throws Exception {
        syncUpdateEntry();
      }
    
      public static void syncUpdateEntry() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [UpdateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryRequest.html) request =
              [UpdateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryRequest.html).newBuilder()
                  .setEntry([Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html).newBuilder().build())
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .setAllowMissing(true)
                  .setDeleteMissingAspects(true)
                  .addAllAspectKeys(new ArrayList<String>())
                  .build();
          [Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry.html) response = catalogServiceClient.updateEntry(request);
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. Entry resource.
     */
    // const entry = {}
    /**
     *  Optional. Mask of fields to update. To update Aspects, the update_mask must
     *  contain the value "aspects".
     *  If the update_mask is empty, the service will update all modifiable fields
     *  present in the request.
     */
    // const updateMask = {}
    /**
     *  Optional. If set to true and the entry doesn't exist, the service will
     *  create it.
     */
    // const allowMissing = true
    /**
     *  Optional. If set to true and the aspect_keys specify aspect ranges, the
     *  service deletes any existing aspects from that range that weren't provided
     *  in the request.
     */
    // const deleteMissingAspects = true
    /**
     *  Optional. The map keys of the Aspects which the service should modify. It
     *  supports the following syntaxes:
     *  * `<aspect_type_reference>` - matches an aspect of the given type and empty
     *  path.
     *  * `<aspect_type_reference>@path` - matches an aspect of the given type and
     *  specified path. For example, to attach an aspect to a field that is
     *  specified by the `schema` aspect, the path should have the format
     *  `Schema.<field_name>`.
     *  * `<aspect_type_reference>@*` - matches aspects of the given type for all
     *  paths.
     *  * `*@path` - matches aspects of all types on the given path.
     *  The service will not remove existing aspects matching the syntax unless
     *  `delete_missing_aspects` is set to true.
     *  If this field is left empty, the service treats it as specifying
     *  exactly those Aspects present in the request.
     */
    // const aspectKeys = ['abc','def']
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callUpdateEntry() {
      // Construct request
      const request = {
        entry,
      };
    
      // Run request
      const response = await dataplexClient.updateEntry(request);
      console.log(response);
    }
    
    callUpdateEntry();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_update_entry():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        entry = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entry.html)()
        entry.entry_type = "entry_type_value"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[UpdateEntryRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.UpdateEntryRequest.html)(
            entry=entry,
        )
    
        # Make the request
        response = client.[update_entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_update_entry)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the update_entry call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#update_entry.
    #
    def update_entry
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::UpdateEntryRequest.new
    
      # Call the update_entry method.
      result = client.update_entry request
    
      # The returned object is of type Google::Cloud::Dataplex::V1::Entry.
      p result
    end

### REST

To delete an aspect for an entry, use the [`entry.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

## Manage existing aspects for an entry link

This section describes how to update the existing aspects for an entry link.

### Update an aspect

For entry links, you can only update required aspects that use reusable system aspect types.

For more information, see [IAM permissions for entry links operations](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#system-aspect-types-entry-types-entry-link-types).

**Note:** Entry links support system aspect types, but not custom aspect types.

### REST

To update an entry link with the required aspect, use the [`entryLinks.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks/patch) method, including the aspect data in the request body.

### Delete an aspect

You can't delete required aspect for an entry link.

## Manage aspect types

This section describes how to view aspect types, and update and delete custom aspect types.

**Note:** You can't edit, delete, or modify permissions for system aspect types.

### View the list of available aspect types

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog)

  2. Click the **Aspect types** tab.




This page lists all the available Knowledge Catalog aspect types.

  1. To view custom aspect types, click the **Custom** tab. In the **Custom** tab, the **Catalog source** column displays where the resource resides in Knowledge Catalog.



To view system aspect types, click the **System** tab.

For more information about custom and system aspect types, see the categories of aspect types section of this document.

  1. Optional: To view the list of aspect types in your selected project, click the **Custom** tab, and then click the **Show from all projects** toggle to the off position.



The **Show from all projects** toggle is on by default, and the list includes Knowledge Catalog resources from your selected organization.

**Note:** If the **Show from all projects** toggle is on, you can't edit or delete an aspect type directly. Instead, click the aspect type to open the **Aspect type details** page, and then edit or delete it.

###  gcloud 

To list all the available aspect types, use the [`gcloud dataplex aspect-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/list).

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using System;
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for ListAspectTypes</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ListAspectTypesRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [ListAspectTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListAspectTypesRequest.html) request = new [ListAspectTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListAspectTypesRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                Filter = "",
                OrderBy = "",
            };
            // Make the request
            PagedEnumerable<ListAspectTypesResponse, AspectType> response = catalogServiceClient.[ListAspectTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_ListAspectTypes_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Iterate over all response items, lazily performing RPCs as required
            foreach ([AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            foreach ([ListAspectTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListAspectTypesResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<AspectType> singlePage = response.ReadPage(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html) item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.ListAspectTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#ListAspectTypesRequest.
    	}
    	it := c.ListAspectTypes(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*dataplexpb.ListAspectTypesResponse)
    	}
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[ListAspectTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAspectTypesRequest.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    
    public class SyncListAspectTypes {
    
      public static void main(String[] args) throws Exception {
        syncListAspectTypes();
      }
    
      public static void syncListAspectTypes() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [ListAspectTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAspectTypesRequest.html) request =
              [ListAspectTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAspectTypesRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .setFilter("filter-1274492040")
                  .setOrderBy("orderBy-1207110587")
                  .build();
          for ([AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) element : catalogServiceClient.listAspectTypes(request).iterateAll()) {
            // doThingsWith(element);
          }
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the AspectType location, of the form:
     *  `projects/{project_number}/locations/{location_id}`
     *  where `location_id` refers to a Google Cloud region.
     */
    // const parent = 'abc123'
    /**
     *  Optional. Maximum number of AspectTypes to return. The service may return
     *  fewer than this value. If unspecified, the service returns at most 10
     *  AspectTypes. The maximum value is 1000; values above 1000 will be coerced
     *  to 1000.
     */
    // const pageSize = 1234
    /**
     *  Optional. Page token received from a previous `ListAspectTypes` call.
     *  Provide this to retrieve the subsequent page. When paginating, all other
     *  parameters you provide to `ListAspectTypes` must match the call that
     *  provided the page token.
     */
    // const pageToken = 'abc123'
    /**
     *  Optional. Filter request. Filters are case-sensitive.
     *  The service supports the following formats:
     *  * labels.key1 = "value1"
     *  * labels:key1
     *  * name = "value"
     *  These restrictions can be conjoined with AND, OR, and NOT conjunctions.
     */
    // const filter = 'abc123'
    /**
     *  Optional. Orders the result by `name` or `create_time` fields.
     *  If not specified, the ordering is undefined.
     */
    // const orderBy = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callListAspectTypes() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const iterable = dataplexClient.[listAspectTypesAsync](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/v1.catalogserviceclient.html)(request);
      for await (const response of iterable) {
          console.log(response);
      }
    }
    
    callListAspectTypes();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_list_aspect_types():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[ListAspectTypesRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListAspectTypesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_aspect_types](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_list_aspect_types)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the list_aspect_types call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#list_aspect_types.
    #
    def list_aspect_types
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::ListAspectTypesRequest.new
    
      # Call the list_aspect_types method.
      result = client.list_aspect_types request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::Dataplex::V1::AspectType.
        p item
      end
    end

### REST

To list all the available aspect types, use the [`aspectTypes.list`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/list) method.

### View details of an aspect type

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog)

  2. Click the **Aspect types** tab.

  3. To view the details of a Knowledge Catalog aspect type, click the aspect type. The aspect type details page opens, where you can access details, such as display name, aspect type ID, description, project ID, location, labels, creation date, and last modified date.

     * To view the structure of the selected aspect type, click the **Template** tab.
     * To view the list of 10 related entries created recently, click the **Sample entries** tab.
     * To search for all related entries, click **Show all related entries in Search**. This button appears only if there's at least one related entry.



###  gcloud 

To get the details of an aspect type, use the [`gcloud dataplex aspect-types describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/describe).

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for GetAspectType</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void GetAspectTypeRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [GetAspectTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetAspectTypeRequest.html) request = new [GetAspectTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetAspectTypeRequest.html)
            {
                AspectTypeName = [AspectTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectTypeName.html).[FromProjectLocationAspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectTypeName.html#Google_Cloud_Dataplex_V1_AspectTypeName_FromProjectLocationAspectType_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]"),
            };
            // Make the request
            [AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html) response = catalogServiceClient.[GetAspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_GetAspectType_Google_Cloud_Dataplex_V1_AspectTypeName_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.GetAspectTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#GetAspectTypeRequest.
    	}
    	resp, err := c.GetAspectType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html);
    import com.google.cloud.dataplex.v1.[AspectTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectTypeName.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[GetAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetAspectTypeRequest.html);
    
    public class SyncGetAspectType {
    
      public static void main(String[] args) throws Exception {
        syncGetAspectType();
      }
    
      public static void syncGetAspectType() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [GetAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetAspectTypeRequest.html) request =
              [GetAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetAspectTypeRequest.html).newBuilder()
                  .setName([AspectTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectTypeName.html).of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
                  .build();
          [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) response = catalogServiceClient.getAspectType(request);
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the AspectType:
     *  `projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}`.
     */
    // const name = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callGetAspectType() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const response = await dataplexClient.getAspectType(request);
      console.log(response);
    }
    
    callGetAspectType();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_get_aspect_type():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[GetAspectTypeRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.GetAspectTypeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_aspect_type](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_get_aspect_type)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the get_aspect_type call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#get_aspect_type.
    #
    def get_aspect_type
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::GetAspectTypeRequest.new
    
      # Call the get_aspect_type method.
      result = client.get_aspect_type request
    
      # The returned object is of type Google::Cloud::Dataplex::V1::AspectType.
      p result
    end

### REST

To get the details of an aspect type, use the [`aspectTypes.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/get) method.

### Update a custom aspect type

You can update the display name, description, template fields, and labels of a custom aspect type. You can't delete an existing field in a template.

You can't update the aspect type ID and location after you create the aspect type.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog)

  2. Click the **Aspect types** tab.

  3. Click the aspect type that you want to update.

  4. On the **Aspect type details** page, click **Edit**.

  5. Edit the display name, description, template fields, and labels, as required.

  6. Optional: To mark a field in the aspect type as deprecated, follow these steps:

     1. In the **Template** section, expand the field.
     2. Select **Is Deprecated**.
     3. In the **Deprecation reason** field, enter a reason for deprecating the selected field.
     4. Click **Done**.

     5. Click **Save**.




###  gcloud 

To update a custom aspect type, use the [`gcloud dataplex aspect-types update` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/update).

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for UpdateAspectType</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateAspectTypeRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateAspectTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateAspectTypeRequest.html) request = new [UpdateAspectTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateAspectTypeRequest.html)
            {
                AspectType = new [AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html)(),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                ValidateOnly = false,
            };
            // Make the request
            Operation<AspectType, OperationMetadata> response = catalogServiceClient.[UpdateAspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_UpdateAspectType_Google_Cloud_Dataplex_V1_AspectType_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<AspectType, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<AspectType, OperationMetadata> retrievedResponse = catalogServiceClient.[PollOnceUpdateAspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_PollOnceUpdateAspectType_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [AspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectType.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.UpdateAspectTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#UpdateAspectTypeRequest.
    	}
    	op, err := c.UpdateAspectType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[UpdateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateAspectTypeRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class SyncUpdateAspectType {
    
      public static void main(String[] args) throws Exception {
        syncUpdateAspectType();
      }
    
      public static void syncUpdateAspectType() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [UpdateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateAspectTypeRequest.html) request =
              [UpdateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateAspectTypeRequest.html).newBuilder()
                  .setAspectType([AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).newBuilder().build())
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .setValidateOnly(true)
                  .build();
          [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) response = catalogServiceClient.[updateAspectTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_updateAspectTypeAsync_com_google_cloud_dataplex_v1_AspectType_com_google_protobuf_FieldMask_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. AspectType Resource
     */
    // const aspectType = {}
    /**
     *  Required. Mask of fields to update.
     */
    // const updateMask = {}
    /**
     *  Optional. Only validate the request, but do not perform mutations.
     *  The default is false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callUpdateAspectType() {
      // Construct request
      const request = {
        aspectType,
        updateMask,
      };
    
      // Run request
      const [operation] = await dataplexClient.updateAspectType(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callUpdateAspectType();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_update_aspect_type():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        aspect_type = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html)()
        aspect_type.metadata_template.name = "name_value"
        aspect_type.metadata_template.type_ = "type__value"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[UpdateAspectTypeRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.UpdateAspectTypeRequest.html)(
            aspect_type=aspect_type,
        )
    
        # Make the request
        operation = client.[update_aspect_type](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_update_aspect_type)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the update_aspect_type call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#update_aspect_type.
    #
    def update_aspect_type
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::UpdateAspectTypeRequest.new
    
      # Call the update_aspect_type method.
      result = client.update_aspect_type request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

### REST

To update a custom aspect type, use the [`aspectTypes.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/patch) method.

### Delete a custom aspect type

**Caution:** Deleting a custom aspect type deletes all aspects related to that aspect type across all entries.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog)

  2. Click the **Aspect types** tab.

  3. Click the aspect type that you want to delete.

  4. On the **Aspect type details** page, click **Delete**. Confirm when prompted.




###  gcloud 

To delete a custom aspect type, use the [`gcloud dataplex aspect-types delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/aspect-types/delete).

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for DeleteAspectType</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void DeleteAspectTypeRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [DeleteAspectTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteAspectTypeRequest.html) request = new [DeleteAspectTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteAspectTypeRequest.html)
            {
                AspectTypeName = [AspectTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectTypeName.html).[FromProjectLocationAspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.AspectTypeName.html#Google_Cloud_Dataplex_V1_AspectTypeName_FromProjectLocationAspectType_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]"),
                Etag = "",
            };
            // Make the request
            Operation<Empty, OperationMetadata> response = catalogServiceClient.[DeleteAspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_DeleteAspectType_Google_Cloud_Dataplex_V1_AspectTypeName_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Empty, OperationMetadata> retrievedResponse = catalogServiceClient.[PollOnceDeleteAspectType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_PollOnceDeleteAspectType_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.DeleteAspectTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#DeleteAspectTypeRequest.
    	}
    	op, err := c.DeleteAspectType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[AspectTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectTypeName.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[DeleteAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteAspectTypeRequest.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncDeleteAspectType {
    
      public static void main(String[] args) throws Exception {
        syncDeleteAspectType();
      }
    
      public static void syncDeleteAspectType() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [DeleteAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteAspectTypeRequest.html) request =
              [DeleteAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteAspectTypeRequest.html).newBuilder()
                  .setName([AspectTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectTypeName.html).of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
                  .setEtag("etag3123477")
                  .build();
          catalogServiceClient.[deleteAspectTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_deleteAspectTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_AspectTypeName_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the AspectType:
     *  `projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}`.
     */
    // const name = 'abc123'
    /**
     *  Optional. If the client provided etag value does not match the current etag
     *  value, the DeleteAspectTypeRequest method returns an ABORTED error
     *  response.
     */
    // const etag = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callDeleteAspectType() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const [operation] = await dataplexClient.deleteAspectType(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callDeleteAspectType();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_delete_aspect_type():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DeleteAspectTypeRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DeleteAspectTypeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_aspect_type](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_delete_aspect_type)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the delete_aspect_type call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#delete_aspect_type.
    #
    def delete_aspect_type
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::DeleteAspectTypeRequest.new
    
      # Call the delete_aspect_type method.
      result = client.delete_aspect_type request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

### REST

To delete an existing custom aspect type, use the [`aspectTypes.delete`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.aspectTypes/delete) method.

## What's next

  * Learn how to [search for resources in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).
  * Learn how to [manage entries and ingest custom sources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources).
  * Learn how to [import metadata into Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview).
  * Learn more about [metadata in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).
  * Learn how to [establish foundational data context](https://docs.cloud.google.com/knowledge-catalog/docs/establish-foundational-data-context).
  * Try [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
