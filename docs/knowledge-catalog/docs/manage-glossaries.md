---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries/
title: Manage a business glossary \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:02.524411+00:00
---

# Manage a business glossary  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage a business glossary Stay organized with collections  Save and categorize content based on your preferences. 

Business glossaries in Knowledge Catalog (formerly Dataplex Universal Catalog) let you establish a standardized vocabulary for your data assets across your organization. You can create and manage categories and terms to help reduce ambiguity and improve data discovery and governance. If this is your first time creating a business glossary, see the [Create and use a business glossary](https://docs.cloud.google.com/knowledge-catalog/docs/quickstart-business-glossary) quickstart.

## Knowledge Catalog business glossary use cases

By creating a common language for data using Knowledge Catalog business glossary, you can achieve the following:

  * Define a clear hierarchy of business categories and terms.
  * Link concepts using synonyms and show relationships between terms.
  * Search for data resources based on business concepts, not only technical names.



Knowledge Catalog business glossary helps streamline data discovery and reduce ambiguity, resulting in better governance, more accurate analysis, and faster insights.

## Elements of a business glossary

This section describes the key elements that you can use to structure a business glossary.

### Glossary

A _glossary_ has the following properties:

  * **Overview**. Describes the purpose and contents of the business glossary. You can add images, links, and tables. While HTML formatting isn't supported, you can include HTML code formatted as code or add a link to an HTML page. You can also use rich text formatting options such as bold, italics, underline, bulleted lists, paragraphs, headings, and code blocks. The maximum supported size is 120 KB.

  * **Description**. Describes the glossary. The text in this field is indexed for search. The maximum supported size is 1 KB.

  * **Region**. Specifies the [region](https://docs.cloud.google.com/knowledge-catalog/docs/locations) where the glossary is located.




### Category

A _category_ lets you organize and structure various categories and terms. Categories are defined within a business glossary. You can nest categories up to three levels.

A category has the properties of a glossary as well as the following properties:

  * **Contacts**. Specifies the person responsible for maintaining the category. This property is descriptive and doesn't affect the permissions of the category.
  * **Parent**. Specifies a relationship that is used to establish the parent of the current category. You can nest up to three categories.



The region of a category is the same as the region of the glossary that contains it.

### Term

A _term_ (short for "glossary term") describes a concept that's used in a particular branch of business within your company. For example, the marketing department of a company might create a term that describes cost per click. Terms are defined within a business glossary, either in the glossary directly or within any category found in the glossary.

A term has the properties of a category as well as the following properties:

  * **Synonyms**. Specifies links between terms that have the same meaning. See Synonym terms.
  * **Related terms**. Specifies links between terms that are conceptually related to each other, but that have different meanings. See Related terms.
  * **Related entries**. Specifies links between terms and data assets, or between terms and columns within data assets.
  * **Data quality rules**. Specifies data quality requirements for the term. For more information, see [Reuse data quality rules](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules#attach-glossary).
  * **Contacts**. Specifies the person responsible for maintaining the term. Terms don't inherit the contacts that are defined in categories.



The region of a term is the same as the region of the glossary that contains it.

### Synonym terms

A synonym is a relationship that indicates equivalence between two different terms. Use synonyms when two terms with the same meaning are defined by different teams in different glossaries. For example, you can create a synonym to link the terms "profit" and "earnings."

### Related terms

A related term is a relationship that indicates that two terms are associated with each other, but have different meanings. For example, you can create a related term to link the terms "revenue" and "profit."

## Limitations

  * Business glossaries are housed within projects and locations; the [limitations for projects and locations](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#project-location-constraints) apply to glossaries.
  * When you use a business glossary with a BigQuery data agent, the data agent can import a maximum of 10 glossary terms per table. If you attach more than 10 terms to a table, the data agent ignores the additional terms. For optimal data agent performance, ensure that you also provide comprehensive table-level and column-level descriptions on your tables.



## Required roles

To get the permissions that you need to create and manage glossaries, ask your administrator to grant you the following IAM roles on your project: 

  * For data administrators, get full access to glossaries, categories, terms, synonyms, and related terms, and to set IAM policies: [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) 
  * For data stewards or data owners, get access to creating, editing or deleting glossaries, categories, terms, links between terms, links between terms and [data assets](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#metamodel-overview), and search: [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) 
  * For data analysts or data consumers, get read-only access to glossaries, categories, terms, links between terms and between terms and data assets, and search: [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and manage glossaries. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage glossaries:

  * Create, read, update, and delete a business glossary, category, and terms in your project: 
    * `dataplex.glossaries.list` on unknown

    * `dataplex.glossaries.create`
    * `dataplex.glossaries.get`
    * `dataplex.glossaries.update`
    * `dataplex.glossaries.delete`
    * `dataplex.glossaryCategories.create`
    * `dataplex.glossaryCategories.list`
    * `dataplex.glossaryCategories.get`
    * `dataplex.glossaryCategories.update`
    * `dataplex.glossaryCategories.delete`
    * `dataplex.glossaryTerms.create`
    * `dataplex.glossaryTerms.list`
    * `dataplex.glossaryTerms.get`
    * `dataplex.glossaryTerms.update`
    * `dataplex.glossaryTerms.delete` on unknown
      * Create, look up, and delete synonym term-to-term links in your project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information, see [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles).

## Create and manage business glossaries

The following sections describe how to create, view, edit, and delete a business glossary. When you create business glossaries, categories, or terms, ensure that their IDs comply with the [Knowledge Catalog resource naming guidelines](https://docs.cloud.google.com/knowledge-catalog/docs/guidelines-resources).

**Note:** Requesting metadata changes to business glossaries and Knowledge Catalog entries with [governance workflows](https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows) is available in **private preview**. To request access to the feature, fill in the following [access form](https://forms.gle/eFMGqsaKTUJ62mrR7).

### Create a business glossary

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Click **Create business glossary**.

  3. On the **Create business glossary** page, specify a name and location for the business glossary. After you create the glossary, you can't change the location.

  4. Click **Create**. The glossary is created under the current project.

  5. Optional: Add a short description in **Description** (up to 1024 characters) or a long description in **Overview** (up to 120 KB).




### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedBusinessGlossaryServiceClientSnippets
    {
        /// <summary>Snippet for CreateGlossary</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateGlossaryRequestObject()
        {
            // Create client
            [BusinessGlossaryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html) businessGlossaryServiceClient = [BusinessGlossaryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html#Google_Cloud_Dataplex_V1_BusinessGlossaryServiceClient_Create)();
            // Initialize request argument(s)
            [CreateGlossaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateGlossaryRequest.html) request = new [CreateGlossaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateGlossaryRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                GlossaryId = "",
                Glossary = new [Glossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Glossary.html)(),
                ValidateOnly = false,
            };
            // Make the request
            Operation<Glossary, OperationMetadata> response = businessGlossaryServiceClient.[CreateGlossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html#Google_Cloud_Dataplex_V1_BusinessGlossaryServiceClient_CreateGlossary_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Dataplex_V1_Glossary_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Glossary, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Glossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Glossary.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Glossary, OperationMetadata> retrievedResponse = businessGlossaryServiceClient.[PollOnceCreateGlossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html#Google_Cloud_Dataplex_V1_BusinessGlossaryServiceClient_PollOnceCreateGlossary_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Glossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Glossary.html) retrievedResult = retrievedResponse.Result;
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
    	c, err := dataplex.[NewBusinessGlossaryClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_BusinessGlossaryClient_NewBusinessGlossaryClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.CreateGlossaryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#CreateGlossaryRequest.
    	}
    	op, err := c.CreateGlossary(ctx, req)
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
    
    
    import com.google.cloud.dataplex.v1.[BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html);
    import com.google.cloud.dataplex.v1.[CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryRequest.html);
    import com.google.cloud.dataplex.v1.[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    
    public class SyncCreateGlossary {
    
      public static void main(String[] args) throws Exception {
        syncCreateGlossary();
      }
    
      public static void syncCreateGlossary() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html) businessGlossaryServiceClient =
            [BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html).create()) {
          [CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryRequest.html) request =
              [CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .[setGlossaryId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryRequest.Builder.html#com_google_cloud_dataplex_v1_CreateGlossaryRequest_Builder_setGlossaryId_java_lang_String_)("glossaryId1849967577")
                  .setGlossary([Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary.html).newBuilder().build())
                  .setValidateOnly(true)
                  .build();
          [Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary.html) response = businessGlossaryServiceClient.[createGlossaryAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html#com_google_cloud_dataplex_v1_BusinessGlossaryServiceClient_createGlossaryAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_LocationName_com_google_cloud_dataplex_v1_Glossary_java_lang_String_)(request).get();
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
     *  Required. The parent resource where this Glossary will be created.
     *  Format: projects/{project_id_or_number}/locations/{location_id}
     *  where `location_id` refers to a Google Cloud region.
     */
    // const parent = 'abc123'
    /**
     *  Required. Glossary ID: Glossary identifier.
     */
    // const glossaryId = 'abc123'
    /**
     *  Required. The Glossary to create.
     */
    // const glossary = {}
    /**
     *  Optional. Validates the request without actually creating the Glossary.
     *  Default: false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {BusinessGlossaryServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [BusinessGlossaryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callCreateGlossary() {
      // Construct request
      const request = {
        parent,
        glossaryId,
        glossary,
      };
    
      // Run request
      const [operation] = await dataplexClient.createGlossary(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateGlossary();

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
    
    
    def sample_create_glossary():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[BusinessGlossaryServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.business_glossary_service.BusinessGlossaryServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CreateGlossaryRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.CreateGlossaryRequest.html)(
            parent="parent_value",
            glossary_id="glossary_id_value",
        )
    
        # Make the request
        operation = client.[create_glossary](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.business_glossary_service.BusinessGlossaryServiceClient.html#google_cloud_dataplex_v1_services_business_glossary_service_BusinessGlossaryServiceClient_create_glossary)(request=request)
    
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
    # Snippet for the create_glossary call in the BusinessGlossaryService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client#create_glossary.
    #
    def create_glossary
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::CreateGlossaryRequest.new
    
      # Call the create_glossary method.
      result = client.create_glossary request
    
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

When you create a glossary, Knowledge Catalog creates an [entry](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entries) to represent the glossary.

  1. Create the glossary.
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         
         gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries?glossary_id=GLOSSARY_ID --data @- << EOF
         {
         "displayName": "DISPLAY_NAME",
         "description": "DESCRIPTION"
         }
         EOF

Replace the following:

     * `PROJECT_ID`: the ID of the project in which you want to create the glossary
     * `LOCATION_ID`: the ID of the location where you want to create the glossary
     * `GLOSSARY_ID`: the ID of the glossary
     * `DISPLAY_NAME`: the display name of the glossary
     * `DESCRIPTION`: the description of the glossary, up to a maximum of 1024 characters
  2. Optional: Add an overview to the glossary.

     1. Look up the entry for your glossary:
            
            gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID
            :lookupEntry\
            ?entry=projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID
            \
            \&view=ALL

Replace `PROJECT_NUMBER` with the number of the project where your glossary is created.

     2. Add an overview to your glossary:
            
            gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID\
            ?update_mask=aspects\
            \&deleteMissingAspects=false\
            \&aspect_keys=projects/dataplex-types/locations/global/aspectTypes/overview \
            --data @- << EOF
            {
            "aspects": {
               "dataplex-types.global.overview": {
                  "aspect_type": "projects/dataplex-types/locations/global/aspectTypes/overview",
                  "data": {
                  "content": "OVERVIEW",
                  "links": []
                  },
               }
            }
            }
            EOF

Replace `OVERVIEW` with plaintext or HTML to describe your glossary category or term.




### View the available glossaries

### Console

  * In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

The **My glossaries** pane displays all the organization's glossaries you have permission to view, along with their descriptions and last modified timestamps.




### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using System;
    
    public sealed partial class GeneratedBusinessGlossaryServiceClientSnippets
    {
        /// <summary>Snippet for ListGlossaries</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ListGlossariesRequestObject()
        {
            // Create client
            [BusinessGlossaryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html) businessGlossaryServiceClient = [BusinessGlossaryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html#Google_Cloud_Dataplex_V1_BusinessGlossaryServiceClient_Create)();
            // Initialize request argument(s)
            [ListGlossariesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListGlossariesRequest.html) request = new [ListGlossariesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListGlossariesRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                Filter = "",
                OrderBy = "",
            };
            // Make the request
            PagedEnumerable<ListGlossariesResponse, Glossary> response = businessGlossaryServiceClient.[ListGlossaries](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html#Google_Cloud_Dataplex_V1_BusinessGlossaryServiceClient_ListGlossaries_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Iterate over all response items, lazily performing RPCs as required
            foreach ([Glossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Glossary.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            foreach ([ListGlossariesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListGlossariesResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([Glossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Glossary.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<Glossary> singlePage = response.ReadPage(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([Glossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Glossary.html) item in singlePage)
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
    	c, err := dataplex.[NewBusinessGlossaryClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_BusinessGlossaryClient_NewBusinessGlossaryClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.ListGlossariesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#ListGlossariesRequest.
    	}
    	it := c.ListGlossaries(ctx, req)
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
    		_ = it.Response.(*dataplexpb.ListGlossariesResponse)
    	}
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html);
    import com.google.cloud.dataplex.v1.[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary.html);
    import com.google.cloud.dataplex.v1.[ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossariesRequest.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    
    public class SyncListGlossaries {
    
      public static void main(String[] args) throws Exception {
        syncListGlossaries();
      }
    
      public static void syncListGlossaries() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html) businessGlossaryServiceClient =
            [BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html).create()) {
          [ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossariesRequest.html) request =
              [ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossariesRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .setFilter("filter-1274492040")
                  .setOrderBy("orderBy-1207110587")
                  .build();
          for ([Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary.html) element : businessGlossaryServiceClient.listGlossaries(request).iterateAll()) {
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
     *  Required. The parent, which has this collection of Glossaries.
     *  Format: projects/{project_id_or_number}/locations/{location_id}
     *  where `location_id` refers to a Google Cloud region.
     */
    // const parent = 'abc123'
    /**
     *  Optional. The maximum number of Glossaries to return. The service may
     *  return fewer than this value. If unspecified, at most 50 Glossaries will be
     *  returned. The maximum value is 1000; values above 1000 will be coerced to
     *  1000.
     */
    // const pageSize = 1234
    /**
     *  Optional. A page token, received from a previous `ListGlossaries` call.
     *  Provide this to retrieve the subsequent page.
     *  When paginating, all other parameters provided to `ListGlossaries` must
     *  match the call that provided the page token.
     */
    // const pageToken = 'abc123'
    /**
     *  Optional. Filter expression that filters Glossaries listed in the response.
     *  Filters on proto fields of Glossary are supported.
     *  Examples of using a filter are:
     *    - `display_name="my-glossary"`
     *    - `categoryCount=1`
     *    - `termCount=0`
     */
    // const filter = 'abc123'
    /**
     *  Optional. Order by expression that orders Glossaries listed in the
     *  response. Order by fields are: `name` or `create_time` for the result. If
     *  not specified, the ordering is undefined.
     */
    // const orderBy = 'abc123'
    
    // Imports the Dataplex library
    const {BusinessGlossaryServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [BusinessGlossaryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callListGlossaries() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const iterable = dataplexClient.[listGlossariesAsync](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/v1.businessglossaryserviceclient.html)(request);
      for await (const response of iterable) {
          console.log(response);
      }
    }
    
    callListGlossaries();

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
    
    
    def sample_list_glossaries():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[BusinessGlossaryServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.business_glossary_service.BusinessGlossaryServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[ListGlossariesRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListGlossariesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_glossaries](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.business_glossary_service.BusinessGlossaryServiceClient.html#google_cloud_dataplex_v1_services_business_glossary_service_BusinessGlossaryServiceClient_list_glossaries)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the list_glossaries call in the BusinessGlossaryService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client#list_glossaries.
    #
    def list_glossaries
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::ListGlossariesRequest.new
    
      # Call the list_glossaries method.
      result = client.list_glossaries request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::Dataplex::V1::Glossary.
        p item
      end
    end

### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries

### Edit a glossary

You can edit the name and description of a glossary.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Click the glossary that you want to edit.

  3. Click **Edit** next to the name, description, or overview, and then make your change.

  4. Click **Save**.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID?update_mask=displayName,description --data @- << EOF
    {
    "displayName": "DISPLAY_NAME",
    "description": "DESCRIPTION"
    }
    EOF

### Delete a glossary

Before you can delete a glossary, you first need to delete all the categories and terms in the glossary.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Click the glossary that you want to delete.

  3. Click **Delete** , and then confirm when prompted.




### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedBusinessGlossaryServiceClientSnippets
    {
        /// <summary>Snippet for DeleteGlossary</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void DeleteGlossaryRequestObject()
        {
            // Create client
            [BusinessGlossaryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html) businessGlossaryServiceClient = [BusinessGlossaryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html#Google_Cloud_Dataplex_V1_BusinessGlossaryServiceClient_Create)();
            // Initialize request argument(s)
            [DeleteGlossaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteGlossaryRequest.html) request = new [DeleteGlossaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteGlossaryRequest.html)
            {
                GlossaryName = [GlossaryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GlossaryName.html).[FromProjectLocationGlossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GlossaryName.html#Google_Cloud_Dataplex_V1_GlossaryName_FromProjectLocationGlossary_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[GLOSSARY]"),
                Etag = "",
            };
            // Make the request
            Operation<Empty, OperationMetadata> response = businessGlossaryServiceClient.[DeleteGlossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html#Google_Cloud_Dataplex_V1_BusinessGlossaryServiceClient_DeleteGlossary_Google_Cloud_Dataplex_V1_DeleteGlossaryRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Empty, OperationMetadata> retrievedResponse = businessGlossaryServiceClient.[PollOnceDeleteGlossary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.BusinessGlossaryServiceClient.html#Google_Cloud_Dataplex_V1_BusinessGlossaryServiceClient_PollOnceDeleteGlossary_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
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
    	c, err := dataplex.[NewBusinessGlossaryClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_BusinessGlossaryClient_NewBusinessGlossaryClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.DeleteGlossaryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#DeleteGlossaryRequest.
    	}
    	op, err := c.DeleteGlossary(ctx, req)
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
    
    
    import com.google.cloud.dataplex.v1.[BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html);
    import com.google.cloud.dataplex.v1.[DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryRequest.html);
    import com.google.cloud.dataplex.v1.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryName.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncDeleteGlossary {
    
      public static void main(String[] args) throws Exception {
        syncDeleteGlossary();
      }
    
      public static void syncDeleteGlossary() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html) businessGlossaryServiceClient =
            [BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html).create()) {
          [DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryRequest.html) request =
              [DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryRequest.html).newBuilder()
                  .setName([GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryName.html).of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
                  .setEtag("etag3123477")
                  .build();
          businessGlossaryServiceClient.[deleteGlossaryAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.html#com_google_cloud_dataplex_v1_BusinessGlossaryServiceClient_deleteGlossaryAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_GlossaryName_)(request).get();
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
     *  Required. The name of the Glossary to delete.
     *  Format:
     *  projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
     */
    // const name = 'abc123'
    /**
     *  Optional. The etag of the Glossary.
     *  If this is provided, it must match the server's etag.
     *  If the etag is provided and does not match the server-computed etag,
     *  the request must fail with a ABORTED error code.
     */
    // const etag = 'abc123'
    
    // Imports the Dataplex library
    const {BusinessGlossaryServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [BusinessGlossaryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callDeleteGlossary() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const [operation] = await dataplexClient.deleteGlossary(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callDeleteGlossary();

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
    
    
    def sample_delete_glossary():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[BusinessGlossaryServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.business_glossary_service.BusinessGlossaryServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DeleteGlossaryRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DeleteGlossaryRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_glossary](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.business_glossary_service.BusinessGlossaryServiceClient.html#google_cloud_dataplex_v1_services_business_glossary_service_BusinessGlossaryServiceClient_delete_glossary)(request=request)
    
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
    # Snippet for the delete_glossary call in the BusinessGlossaryService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client#delete_glossary.
    #
    def delete_glossary
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::BusinessGlossaryService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::DeleteGlossaryRequest.new
    
      # Call the delete_glossary method.
      result = client.delete_glossary request
    
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
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X DELETE https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID

## Create and manage categories

The following sections describe how to create, view, update, and delete categories.

### Create a category under a glossary

A business glossary can have a maximum of 200 categories.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Select the glossary in which you want to create a category, and then click **Create category**.

  3. Enter a name for the category.

  4. Click **Create**.

  5. Optional: Add a short description in **Description** (up to 1024 characters) or a long description in **Overview** (up to 120 KB).




### REST

When you create a category, Knowledge Catalog creates an [entry](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entries) to represent the category.

  1. Create the category.
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         
         gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories?category_id=CATEGORY_ID --data @- << EOF
         {
         "displayName": "CATEGORY_DISPLAY_NAME",
         "description": "CATEGORY_DESCRIPTION",
         "parent": "projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID"
         }
         EOF

Replace the following:

     * `CATEGORY_ID`: the category ID
     * `CATEGORY_DISPLAY_NAME`: the category display name
     * `CATEGORY_DESCRIPTION`: the category description
  2. Optional: Add an overview to the category.

     1. Look up the entry for your category:
            
            gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID
            :lookupEntry\
            ?entry=projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID
            \
            \&view=ALL

     2. Add an overview to your category:
            
            gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID\
            ?update_mask=aspects\
            \&deleteMissingAspects=false\
            \&aspect_keys=projects/dataplex-types/locations/global/aspectTypes/overview
            \
            --data @- << EOF
            {
            "aspects": {
               "dataplex-types.global.overview": {
                  "aspect_type":"projects/dataplex-types/locations/global/aspectTypes/overview
            ",
                  "data": {
                  "content": "OVERVIEW",
                  "links": []
                  },
               }
            }
            }
            EOF

Replace `OVERVIEW` with plaintext or HTML to describe your glossary category or term.

  3. Optional: Add contacts

     1. Look up the entry for your category:
            
            gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID
            :lookupEntry\
            ?entry=projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID
            \
            \&view=ALL

     2. Update the entry for your category with contacts:
            
            gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID\
            ?update_mask=aspects\
            \&deleteMissingAspects=false\
            \&aspect_keys=projects/dataplex-types/locations/global/aspectTypes/contacts \
            --data @- << EOF
            {
            "aspects": {
               "dataplex-types.global.contacts": {
                  "aspect_type": "projects/dataplex-types/locations/global/aspectTypes/contacts",
                  "data": {
                  "identities": [
                     {
                        "role": "steward",
                        "name": "CONTACT_NAME",
                        "id": "CONTACT_EMAIL"
                     }
                  ]
                  },
               }
            }
            }
            EOF




### Create a nested category

A business glossary can have a maximum of three nested category levels, excluding the root glossary level.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Expand the glossary in which you want to create a category.

  3. Select the parent category in which you want to create another category, and click **Create category**.

  4. Enter a name for the category.

  5. Click **Create**.

  6. Optional: Add a short description in **Description** (up to 1024 characters) or a long description in **Overview** (up to 120 KB).




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories?category_id=CATEGORY_ID --data @- << EOF
    {
       "displayName": "CATEGORY_DISPLAY_NAME",
       "description": "CATEGORY_DESCRIPTION",
       "parent": "projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/PARENT_CATEGORY_ID"
    }
    EOF

Replace `PARENT_CATEGORY_ID` with the ID of the parent category.

### View the categories that belong to a glossary

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. To view the categories in a glossary, expand the glossary.

  3. To view the nested categories in a category, expand the category.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories

### Edit a category

You can edit the name, description, and contacts for a category. For nested categories, you can also edit the parent category.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Expand the glossary and click the category you want to edit.

  3. Click edit **Edit** next to the name, description, or overview, and then make your change.

  4. Click **Save**.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID?update_mask=displayName,description --data @- << EOF
    {
    "displayName": "CATEGORY_DISPLAY_NAME",
    "description": "DESCRIPTION"
    }
    EOF

### Delete a category

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Expand the glossary and click the category that you want to delete.

  3. Click **Delete** , and then confirm when prompted.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X DELETE https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID

## Create and manage terms

The following sections describe how to create, view, access, edit, and delete terms.

### Create a term under a business glossary

A business glossary can have a maximum of 5,000 terms.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/bigquery/governance/metadata-curation/business-glossary)

  2. To create a term at the glossary level, select the glossary where you want to create a term, and then click **Create term**.

  3. Enter a name for the term.

  4. Click **Create**.

  5. Optional: Add a short description in **Description** (up to 1024 characters) or a long description in **Overview** (up to 120 KB).

  6. Optional: To add contacts, click **Edit** , and then provide a list of email addresses for the data stewards, data owners, or data domain owners. Then click **Save**.




### REST

When you create a term, Knowledge Catalog creates an [entry](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entries) to represent the term.

  1. Create the term.
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         
         gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms?term_id=TERM_ID --data @- << EOF
         {
         "displayName": "TERM_DISPLAY_NAME",
         "description": "TERM_DESCRIPTION",
         "parent": "projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID"
         }
         EOF

Replace the following:

     * TERM_ID: the ID of the term you're creating
     * TERM_DISPLAY_NAME: the display name for the term you're creating
     * TERM_DESCRIPTION: the description for the term you're creating
  2. Optional: Add an overview to the term.

     1. Look up the entry for your term:
            
            gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID
            :lookupEntry\
            ?entry=projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID
            \
            \&view=ALL

     2. Add an overview to your term:
            
            gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID
            \
            ?update_mask=aspects\
            \&deleteMissingAspects=false\
            \&aspect_keys=projects/dataplex-types/locations/global/aspectTypes/overview
            \
            --data @- << EOF
            {
            "aspects": {
               "dataplex-types.global.overview": {
                  "aspect_type":"projects/dataplex-types/locations/global/aspectTypes/overview
            ",
                  "data": {
                  "content": "OVERVIEW",
                  "links": []
                  },
               }
            }
            }
            EOF

Replace `OVERVIEW` with plaintext or HTML to describe your glossary category or term.

  3. Optional: Add contacts.

     1. Look up the entry for your term:
            
            gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID
            :lookupEntry\
            ?entry=projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID
            \
            \&view=ALL

     2. Update the entry for your term with contacts:
            
            gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID
            ?update_mask=aspects\
            \&deleteMissingAspects=false\
            \&aspect_keys=projects/dataplex-types/locations/global/aspectTypes/contacts \
            --data @- << EOF
            {
            "aspects": {
               "dataplex-types.global.contacts": {
                  "aspect_type": "projects/dataplex-types/locations/global/aspectTypes/contacts",
                  "data": {
                  "identities": [
                     {
                        "role": "steward",
                        "name": "CONTACT_NAME",
                        "id": "CONTACT_EMAIL"
                     }
                  ]
                  },
               }
            }
            }
            EOF




### Create a term under a category

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/bigquery/governance/metadata-curation/business-glossary)

  2. To create a term in a category, select the category where you want to create a term, and then click **Add term**.

  3. Enter a name for the term.

  4. Click **Create**.

  5. Optional: Add a short description in **Description** (up to 1024 characters) or a long description in **Overview** (up to 120 KB).

  6. Optional: To add contacts, click **Edit** , and then provide a list of email addresses for the data stewards, data owners, or data domain owners. Then click **Save**.




### REST

When you create a term, Knowledge Catalog creates an [entry](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entries) to represent the term.

  1. Create a term.
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         
         gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms?term_id=TERM_ID --data @- << EOF
         {
         "displayName": "TERM_DISPLAY_NAME",
         "description": "TERM_DESCRIPTION",
         "parent": "projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/PARENT_CATEGORY_ID"
         }
         EOF

Replace the following:

     * TERM_ID: the ID of the term you're creating
     * TERM_DISPLAY_NAME: the display name for the term you're creating
     * TERM_DESCRIPTION: the description for the term you're creating
  2. Optional: Add an overview to the term.

     1. Look up the entry for your term:
            
            gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID
            :lookupEntry\
            ?entry=projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID
            \
            \&view=ALL

     2. Add an overview to your term:
            
            gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID
            \
            ?update_mask=aspects\
            \&deleteMissingAspects=false\
            \&aspect_keys=projects/dataplex-types/locations/global/aspectTypes/overview
            \
            --data @- << EOF
            {
            "aspects": {
               "dataplex-types.global.overview": {
                  "aspect_type":"projects/dataplex-types/locations/global/aspectTypes/overview
            ",
                  "data": {
                  "content": "OVERVIEW",
                  "links": []
                  },
               }
            }
            }
            EOF

Replace `OVERVIEW` with plaintext or HTML to describe your glossary category or term.

  3. Optional: Add contacts.

     1. Look up the entry for your term:
            
            gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID
            :lookupEntry\
            ?entry=projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID
            \
            \&view=ALL

     2. Update the entry for your term with contacts:
            
            gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID
            ?update_mask=aspects\
            \&deleteMissingAspects=false\
            \&aspect_keys=projects/dataplex-types/locations/global/aspectTypes/contacts \
            --data @- << EOF
            {
            "aspects": {
               "dataplex-types.global.contacts": {
                  "aspect_type": "projects/dataplex-types/locations/global/aspectTypes/contacts",
                  "data": {
                  "identities": [
                     {
                        "role": "steward",
                        "name": "CONTACT_NAME",
                        "id": "CONTACT_EMAIL"
                     }
                  ]
                  },
               }
            }
            }
            EOF




### Add an aspect to a term

You can add aspects to terms to provide additional context or metadata.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Expand the glossary and click the term that you want to add an aspect to.

  3. In the **Aspects** section, click **Add**.

  4. Search for the aspect, provide details for the aspect, and then click **Save**.




### REST

Glossary terms are entries. To attach an aspect, patch the entry resource. The entry group for glossaries is `@dataplex`.
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID?update_mask=aspects\&aspect_keys=ASPECT_PROJECT_ID.ASPECT_LOCATION_ID.ASPECT_TYPE_ID --data @- << EOF
    {
      "aspects": {
        "ASPECT_PROJECT_ID.ASPECT_LOCATION_ID.ASPECT_TYPE_ID": {
          "aspect_type": "projects/ASPECT_PROJECT_ID/locations/ASPECT_LOCATION_ID/aspectTypes/ASPECT_TYPE_ID",
          "data": {
            "sensitivity": "HIGH",
            "data_owner": "achalg@google.com"
          }
        }
      }
    }
    EOF

Replace the following:

  * `PROJECT_NUMBER`: the number of the project containing the glossary term.
  * `LOCATION_ID`: the location of the glossary term.
  * `GLOSSARY_ID`: the ID of the glossary containing the term.
  * `TERM_ID`: the ID of the term to attach aspect to.
  * `ASPECT_PROJECT_ID`: the ID of the project containing the aspect type.
  * `ASPECT_LOCATION_ID`: the location of the aspect type.
  * `ASPECT_TYPE_ID`: the ID of the aspect type.



### View the terms in a glossary or category

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. To view the terms in a glossary, expand the glossary. To view terms in a category within this glossary, expand the category. To view terms within a nested category, expand the nested category.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms

### View the details of a term

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. To view the list of terms in a glossary, expand the glossary.

  3. Click a term. The **Term details** page displays the term name, description, related terms, synonyms, and related entries.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID

### Edit a term

You can edit the name, description, overview, contacts, and parent for a term.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Expand the glossary and click the term that you want to edit.

  3. Click **Edit**.

  4. Edit any of the fields and click **Save**.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID?update_mask=displayName,description --data @- << EOF
    {
       "displayName": "TERM_DISPLAY_NAME",
       "description": "TERM_DESCRIPTION"
    }
    EOF

### Delete a term

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Expand the glossary and click the term that you want to delete.

  3. Click **Delete** , and then confirm when prompted.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X DELETE https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM_ID

## Manage synonyms and related terms

You can add relationships between terms by linking them as synonyms or related terms.

Term relationships are bi-directional. For example, when you link `profit` as a synonym of `earnings`, `earnings` also becomes a synonym of `profit`.

### Create synonym links between terms

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Expand the glossary and click the term that you want to create links with.

  3. Click edit**Edit** next to **Synonym terms**.

  4. Search for and then select the terms to link to.

The term gets linked immediately when you select it.

  5. Click **Close**.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/TERM1_PROJECT_ID/locations/TERM1_LOCATION_ID/entryGroups/@dataplex/entryLinks?entry_link_id=ENTRY_LINK_ID -d "$(cat<<EOF
    {
       "entry_link_type": "projects/dataplex-types/locations/global/entryLinkTypes/synonym",
    "entry_references": [{
          "name": "projects/TERM1_PROJECT_NUMBER/locations/TERM1_LOCATION_ID/entryGroups/@dataplex/entries/projects/TERM1_PROJECT_NUMBER/locations/TERM1_LOCATION_ID/glossaries/TERM1_GLOSSARY_ID/terms/TERM1_ID",
          "type": "UNSPECIFIED"
       }, {
          "name": "projects/TERM2_PROJECT_NUMBER/locations/TERM2_LOCATION_ID/entryGroups/@dataplex/entries/projects/TERM2_PROJECT_NUMBER/locations/TERM2_LOCATION_ID/glossaries/TERM2_GLOSSARY_ID/terms/TERM2_ID",
          "type": "UNSPECIFIED"
       }
       ]
    
    }
    EOF
    )"

Replace the following:

  * `TERM1_PROJECT_NUMBER`: the project number for the first term being linked.
  * `TERM1_LOCATION_ID`: the location ID of the glossary that contains the first term.
  * `TERM1_GLOSSARY_ID`: the ID of the glossary that contains the first term.
  * `TERM1_ID`: the ID of the first term.
  * `TERM2_PROJECT_NUMBER`: the project number for the second term that you want to link to as a synonym term. If both terms are in the same project, then this value is the same as the project number for the first term.
  * `TERM2_LOCATION_ID`: the location ID of the glossary that contains the second term. If both terms are in the same location, then this value is the same as the location ID for the first term.
  * `TERM2_GLOSSARY_ID`: the ID of the glossary that contains the second term. If both terms are in the same glossary, then this value is the same as the glossary ID for the first term.
  * `TERM2_ID`: the ID of the second term.
  * `ENTRY_LINK_ID`: an ID for the link between the two terms. Each term is represented as a Knowledge Catalog entry. The entry link is the relationship between synonym terms.



### Create related links between terms

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Expand the glossary and click the term that you want to create links with.

  3. Click edit**Edit** next to **Related terms**.

  4. Search for and then select the terms to link to.

The term gets linked immediately when you select it.

  5. Click **Close**.




### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/TERM1_PROJECT_ID/locations/TERM1_LOCATION_ID/entryGroups/@dataplex/entryLinks?entry_link_id=ENTRY_LINK_ID -d "$(cat<<EOF
    {
       "entry_link_type": "projects/dataplex-types/locations/global/entryLinkTypes/related",
    "entry_references": [{
          "name": "projects/TERM1_PROJECT_NUMBER/locations/TERM1_LOCATION_ID/entryGroups/@dataplex/entries/projects/TERM1_PROJECT_NUMBER/locations/TERM1_LOCATION_ID/glossaries/TERM1_GLOSSARY_ID/terms/TERM1_ID",
          "type": "UNSPECIFIED"
       }, {
          "name": "projects/TERM2_PROJECT_NUMBER/locations/TERM2_LOCATION_ID/entryGroups/@dataplex/entries/projects/TERM2_PROJECT_NUMBER/locations/TERM2_LOCATION_ID/glossaries/TERM2_GLOSSARY_ID/terms/TERM2_ID",
          "type": "UNSPECIFIED"
       }
       ]
    
    }
    EOF
    )"

Replace the following:

  * `TERM1_PROJECT_NUMBER`: the project number for the first term being linked.
  * `TERM1_LOCATION_ID`: the location ID of the glossary that contains the first term.
  * `TERM1_GLOSSARY_ID`: the ID of the glossary that contains the first term.
  * `TERM1_ID`: the ID of the first term.
  * `TERM2_PROJECT_NUMBER`: the project number for the second term that you want to link to as a related term. If both terms are in the same project, then this value is the same as the project number for the first term.
  * `TERM2_LOCATION_ID`: the location ID of the glossary that contains the second term. If both terms are in the same location, then this value is the same as the location ID for the first term.
  * `TERM2_GLOSSARY_ID`: the ID of the glossary that contains the second term. If both terms are in the same glossary, then this value is the same as the glossary ID for the first term.
  * `TERM2_ID`: the ID of the second term.
  * `ENTRY_LINK_ID`: an ID for the link between the two terms. Each term is represented as a Knowledge Catalog entry. The entry link is the relationship between related terms.



### Look up synonym links for a term

### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/TERM_PROJECT_ID/locations/SYNONYM_LINKS_LOCATION_ID:lookupEntryLinks?entry=projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/entryGroups/@dataplex/entries/projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/glossaries/TERM_GLOSSARY_ID/terms/TERM_ID&entry_link_types=projects/dataplex-types/locations/global/entryLinkTypes/synonym&page_size=10

Replace the following:

  * `TERM_PROJECT_ID`: the project ID of the term whose synonym links you are looking up.
  * `TERM_PROJECT_NUMBER`: the project number of the term whose synonym links you are looking up.
  * `SYNONYM_LINKS_LOCATION_ID`: the location ID where you are looking up the synonym links.
  * `TERM_LOCATION_ID`: the location ID of the term.
  * `TERM_GLOSSARY_ID`: the ID of the glossary that contains the term.
  * `TERM_ID`: the ID of the term.

**Note:** To fetch subsequent pages, append `&page_token=PAGE_TOKEN` to the request. Replace `PAGE_TOKEN` with the value of the page token you received from the earlier `lookupEntryLinks` response.

### Look up related links for a term

### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/TERM_PROJECT_ID/locations/RELATED_LINKS_LOCATION_ID:lookupEntryLinks?entry=projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/entryGroups/@dataplex/entries/projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/glossaries/TERM_GLOSSARY_ID/terms/TERM_ID&entry_link_types=projects/dataplex-types/locations/global/entryLinkTypes/related&page_size=10

Replace the following:

  * `TERM_PROJECT_ID`: the project ID of the term whose related links you are looking up.
  * `TERM_PROJECT_NUMBER`: the project number of the term whose related links you are looking up.
  * `RELATED_LINKS_LOCATION_ID`: the location ID where you are looking up the related links.
  * `TERM_LOCATION_ID`: the location ID of the term.
  * `TERM_GLOSSARY_ID`: the ID of the glossary that contains the term.
  * `TERM_ID`: the ID of the term.

**Note:** To fetch subsequent pages, append `&page_token=PAGE_TOKEN` to the request. Replace `PAGE_TOKEN` with the value of the page token you received from the earlier `lookupEntryLinks` response.

### Remove links between synonyms and related terms

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Expand the glossary and click the term whose synonyms or related terms you want to remove.

  3. To delete links between related terms, click edit**Edit** next to **Related terms**. Delete the related terms, and then click **Close**.

  4. To delete links between synonyms, click edit**Edit** next to **Synonym terms**. Delete the synonyms, and then click **Close**.




### REST

  1. Look up entry links to find the entry link ID of the link you want to delete. For more information, see Look up synonym links for a term or Look up related links for a term.

  2. Delete the link by sending the following `DELETE` request:
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         
         gcurl -X DELETE https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/entryGroups/ENTRY_GROUP_ID/entryLinks/ENTRY_LINK_ID




## Manage links between terms and data assets

You can attach terms to data assets or data asset columns. For example, you can attach terms to BigQuery datasets and Iceberg REST Catalog tables.

### Attach terms to a data asset

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Search for the data asset (such as a dataset, file, or table) that you want to link a term to, and then click it.

  3. On the data asset page, do one of the following:

     * To link terms to an asset, on the **Details** tab, in the **Glossary terms** section, click **Add**. Search for and then select the terms, and then click **Close.**
     * If the asset has a schema, you can link terms to a column. On the **Schema** tab, select a column to link terms to, and then click **Add business term**. Search for and then select the terms, and then click **Close.**



### Python
    
    
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    def attach_term_to_asset(
        project_id: str,
        location: str,
        entry_group_id: str,
        entry_link_id: str,
        source_entry_name: str,
        target_term_name: str,
    ) -> dataplex_v1.EntryLink:
        """Creates an entry link attaching a glossary term to a data asset."""
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
        parent_group = (
            f"projects/{project_id}/locations/{location}/"
            f"entryGroups/{entry_group_id}"
        )
    
        entry_link = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryLink](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryLink.html)(
            entry_link_type=(
                "projects/dataplex-types/locations/global/"
                "entryLinkTypes/definition"
            ),
            entry_references=[
                [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryLink](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryLink.html).[EntryReference](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryLink.EntryReference.html)(
                    name=source_entry_name, type_="SOURCE"
                ),
                [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[EntryLink](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryLink.html).[EntryReference](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryLink.EntryReference.html)(
                    name=target_term_name, type_="TARGET"
                ),
            ],
        )
    
        return client.[create_entry_link](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_create_entry_link)(
            parent=parent_group,
            entry_link_id=entry_link_id,
            entry_link=entry_link,
        )
    

### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/ENTRY_LOCATION_ID/entryGroups/ENTRY_GROUP_ID/entryLinks?entry_link_id=ENTRY_LINK_ID -d "$(cat<<EOF
    {
       "entry_link_type": "projects/dataplex-types/locations/global/entryLinkTypes/definition",
       "entry_references": [{
          "name": "projects/PROJECT_NUMBER/locations/ENTRY_LOCATION_ID/entryGroups/ENTRY_GROUP_ID/entries/ENTRY_ID",
          "type": "SOURCE"
       }, {
          "name": "projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/entryGroups/@dataplex/entries/projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/glossaries/TERM_GLOSSARY_ID/terms/TERM_ID",
          "type": "TARGET"
       }
       ]
    }
    EOF
    )"

Replace the following:

  * `PROJECT_NUMBER`: the project number of the data asset being linked to
  * `ENTRY_LOCATION_ID`: the location ID of the data asset being linked to
  * `ENTRY_GROUP_ID`: the entry group of the data asset being linked to
  * `ENTRY_LINK_ID`: an ID for the link between the term and the Knowledge Catalog entry that represents the data asset.
  * `TERM_PROJECT_NUMBER`: the project number for the term being linked.



### Attach terms to a column in an entry schema

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Search for the data asset (such as a dataset, file, or table) that has a schema with a column you want to link a term to. Click the data asset.

  3. On the data asset page, do one of the following:

     * To link terms to a column in the data asset, on the **Schema** tab, select the columns you want to attach the term to.
     * Click **Add business term**. Search for the term you want to attach and click the term to attach.



### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_NUMBER/locations/ENTRY_LOCATION_ID/entryGroups/ENTRY_GROUP_ID/entryLinks?entry_link_id=ENTRY_LINK_ID -d "$(cat<<EOF
    {
      "entry_link_type": "projects/dataplex-types/locations/global/entryLinkTypes/definition",
      "entry_references": [
        {
          "name": "projects/PROJECT_NUMBER/locations/ENTRY_LOCATION_ID/entryGroups/ENTRY_GROUP_ID/entries/ENTRY_ID",
          "path": "Schema.COLUMN_NAME",
          "type": "SOURCE"
        },
        {
          "name": "projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/entryGroups/@dataplex/entries/projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/glossaries/TERM_GLOSSARY_ID/terms/TERM_ID",
          "type": "TARGET"
        }
      ]
    }
    EOF
    )"

Replace the following:

  * `PROJECT_NUMBER`: the project number of the data asset being linked to
  * `ENTRY_LOCATION_ID`: the location ID of the data asset being linked to
  * `ENTRY_GROUP_ID`: the entry group of the data asset being linked to
  * `ENTRY_LINK_ID`: an ID for the link between the term and the Knowledge Catalog entry that represents the data asset
  * `TERM_PROJECT_NUMBER`: the project number for the term being linked
  * `COLUMN_NAME`: the column to which you want to attach the term



### Attach a term to multiple data assets or columns

You can attach a single glossary term to multiple data assets or columns simultaneously. You can select up to 20 resources or columns in a single operation.

### Console

To attach a term to multiple resources, follow these steps:

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. In the **Glossaries** list, expand the glossary that contains the term you want to link.

  3. Click the term.

  4. In the **Related entries** section, click add **Add**.

  5. In the **Attach related entries** dialog, complete the following steps:

     1. Find the resources or columns you want to link. To narrow your search results, use **Filter** to search by resource name, resource type, or column name.

For example, to find a column named `sample-column` in a BigQuery table named `sample-table` within a project with the ID `sample-project`, use the following query:
            
            project id:sample-project
            Resource Name:sample-table
            Column Name:sample-column
            

You can enter partial strings to find matching assets.

     2. Select the data assets and columns you want to attach.

     3. To review your selections before adding, click the **Show selected resources** toggle.

     4. Click **Add**.

  6. To verify the newly attached resources and columns, go to the **Related entries** section of the term's details page.




### Look up data assets linked to a term

### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/TERM_PROJECT_ID/locations/DEFINITION_LINKS_LOCATION_ID:lookupEntryLinks?entry=projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/entryGroups/@dataplex/entries/projects/TERM_PROJECT_NUMBER/locations/TERM_LOCATION_ID/glossaries/TERM_GLOSSARY_ID/terms/TERM_ID&entry_link_types=projects/dataplex-types/locations/global/entryLinkTypes/definition&entry_mode=TARGET&page_size=10

Replace the following:

  * `TERM_PROJECT_ID`: the project ID of the term whose definition links you are looking up.
  * `TERM_PROJECT_NUMBER`: the project number of the term whose definition links you are looking up.
  * `DEFINITION_LINKS_LOCATION_ID`: the location ID where you are looking up the definition links.
  * `TERM_LOCATION_ID`: the location ID of the term.
  * `TERM_GLOSSARY_ID`: the ID of the glossary that contains the term.
  * `TERM_ID`: the ID of the term.

**Note:** Columns linked to the term are returned in the `path` field. 

To fetch subsequent pages, append `&page_token=PAGE_TOKEN` to the request. Replace `PAGE_TOKEN` with the value of the page token you received from the earlier `lookupEntryLinks` response.

### Look up terms linked to a data asset

### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/DEFINITION_LINKS_LOCATION_ID:lookupEntryLinks?entry=projects/PROJECT_NUMBER/locations/ENTRY_LOCATION_ID/entryGroups/ENTRY_GROUP_ID/entries/ENTRY_ID&entry_link_types=projects/dataplex-types/locations/global/entryLinkTypes/definition&entry_mode=SOURCE&page_size=10

Replace the following:

  * `PROJECT_ID`: the project ID of the data asset whose definition links you are looking up.
  * `PROJECT_NUMBER`: the project number of the data asset whose definition links you are looking up.
  * `DEFINITION_LINKS_LOCATION_ID`: the location ID where you are looking up the definition links.
  * `ENTRY_LOCATION_ID`: the location ID of the data asset.
  * `ENTRY_GROUP_ID`: the ID of the entry group for the data asset.
  * `ENTRY_ID`: the ID of the data asset.

**Note:** Columns linked to the term within a data asset are returned in the `path` field. 

To fetch subsequent pages, append `&page_token=PAGE_TOKEN` to the request. Replace `PAGE_TOKEN` with the value of the page token you received from the earlier `lookupEntryLinks` response.

### Remove terms from a data asset

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Search for the data asset (such as a dataset, file, or table) that you want to remove the terms from, and click it.

  3. On the data asset page, do one of the following:

     * To remove a term from an asset, on the **Details** tab, in the **Glossary terms** section, click the term. Then click close.
     * To remove a term from a column, on the **Schema** tab, click clear next to the term.



### REST
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X DELETE https://dataplex.googleapis.com/v1/projects/ENTRY_PROJECT_ID/locations/ENTRY_LOCATION_ID/entryGroups/ENTRY_GROUP_ID/entryLinks/ENTRY_LINK_ID

## Find glossaries, terms, and linked data assets

### Console

To navigate across your business glossary content, use the glossary and terms tree on the **Glossaries** page.

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. On the **Glossaries** page, use the filter bar to find categories. The following filters are available:

     * **Name** : returns the glossaries, categories, and terms whose name contains the text that you provide.
     * **Parent** : returns the terms whose parent glossary name or description matches the text that you provide. For example, `parent:Finance` returns the terms that are connected with the parent glossary whose name or description contains the phrase `Finance`.
     * **Synonym** : returns the list of terms with a synonym whose name or ID contains the text that you provide. For example, `synonym:Profit` returns the terms which have a synonym term whose name or ID contains the phrase `profit`.
     * **Contact** : returns the terms where the data steward is listed as a contact. For example, `contact:alex@example.com` returns the entries that are connected to terms with a data steward matching `alex@example.com`.



### REST

To find glossaries, terms, and linked data assets by using the REST API, see [`projects.locations.searchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries).

## Search for data assets linked to terms

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. On the **Glossaries** page, use the filter bar to enter a free-form text search query. This returns a list of corresponding matches in the glossary, category, and term names.

  3. Click a matched term.

  4. On the **Term details** page, see the linked terms (synonyms and related terms) and linked entries (data assets) to this term.

  5. If you want to see the details for an entry in Knowledge Catalog, click the entry.




### REST

To find glossaries, terms, and linked data assets by using the REST API, see [`projects.locations.searchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries).

## Import glossaries and links between terms and terms or data assets

To import glossaries and links from another cataloging tool or to update your glossaries in Knowledge Catalog, you can bulk import glossaries, categories, terms, links between terms, links between terms and data assets, or columns, using the REST API.

  1. Create the target glossary.

### REST
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         
         gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries?glossary_id=GLOSSARY_ID -d "$(cat<<EOF
         
         {
            "displayName": "DISPLAY_NAME",
            "description": "DESCRIPTION"
         }
         EOF
         )"

Replace the following:

     * `PROJECT_ID`: the project ID in which you're creating the glossary
     * `LOCATION_ID`: the location in which we want to create the glossary
     * `GLOSSARY_ID`: the glossary ID
     * `DISPLAY_NAME`: the display name of the glossary
     * `DESCRIPTION`: the description of the glossary

  2. To import categories, terms, and links between terms and data assets in the target glossary created, upload files for each of these into a Cloud Storage bucket. These files are of the following format:

     * Sample format for terms and categories of a glossary
           
           {"entry":{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID","entryType":"projects/dataplex-types/locations/global/entryTypes/glossary-category","aspects":{"dataplex-types.global.glossary-category-aspect":{"data":{}},"dataplex-types.global.overview":{"data":{"content":"CONTENT"}},"dataplex-types.global.contacts":{"data":{"identities":[{role: "steward", name: "CONTACT_DISPLAY_NAME", id: "CONTACT_EMAIL"}]}}},"parentEntry":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","entrySource":{"resource":"projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID","displayName":"CATEGORY_NAME","description":"CATEGORY_DESCRIPTION","ancestors":[{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary"}]}}}
           {"entry":{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM1_ID","entryType":"projects/dataplex-types/locations/global/entryTypes/glossary-term","aspects":{"dataplex-types.global.glossary-term-aspect":{"data":{}},"dataplex-types.global.overview":{"data":{"content":"TERM1_CONTENT"}},"dataplex-types.global.contacts":{"data":{"identities":[{role: "steward", name: "CONTACT_DISPLAY_NAME", id: "CONTACT_EMAIL"}]}}},"parentEntry":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","entrySource":{"resource":"projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM1_ID","displayName":"TERM1_DISPLAY_NAME","description":"TERM1_DESCRIPTION","ancestors":[{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary"},{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary-category"}]}}}
           {"entry":{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM2_ID","entryType":"projects/dataplex-types/locations/global/entryTypes/glossary-term","aspects":{"dataplex-types.global.glossary-term-aspect":{"data":{}},"dataplex-types.global.overview":{"data":{"content":"TERM1_CONTENT"}},"dataplex-types.global.contacts":{"data":{"identities":[{role: "steward", name: "CONTACT_DISPLAY_NAME", id: "CONTACT_EMAIL"}]}}},"parentEntry":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","entrySource":{"resource":"projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM2_ID","displayName":"TERM2_DISPLAY_NAME","description":"TERM2_DESCRIPTION","ancestors":[{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary"},{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary-category"}]}}}

     * Sample format for links between terms
           
           {"entryLink":{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entryLinks/el-import-0606e3f2-8206-4f3a-aba9-32c6196f6048","entryLinkType":"projects/dataplex-types/locations/global/entryLinkTypes/synonym","entryReferences":[{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-1"},{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-2"}]}}
           {"entryLink":{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entryLinks/el-import-2f7408e3-af3d-405d-81bb-861cf9ec5146","entryLinkType":"projects/dataplex-types/locations/global/entryLinkTypes/related","entryReferences":[{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-1"},{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-2"}]}}

     * Sample format for links between terms and data assets
           
           projects/PROJECT_NUMBER/locations/us-central1/entryGroups/entry-group-1/entries/entry-1 and term projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-1
           {"entryLink":{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entryLinks/el-import-0606e3f2-8206-4f3a-aba9-32c6196f6048","entryLinkType":"projects/dataplex-types/locations/global/entryLinkTypes/definition","entryReferences":[{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-1"},{"name":"projects/PROJECT_NUMBER/locations/us-central1/entryGroups/entry-group-1/entries/entry-1"}]}}
    
    # Set GCURL alias
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl https://DATAPLEX_API/metadataJobs?metadata_job_id=JOB_ID -d "$(cat<<EOF
    {
       "type":"IMPORT",
       "import_spec":{
          "log_level":"DEBUG",
          "source_storage_uri":"gs://STORAGE_BUCKET/",
          "entry_sync_mode":"FULL",
          "aspect_sync_mode":"INCREMENTAL",
          "scope":{
             "glossaries": "GLOSSARY_NAME"
          }
       }
    }
    EOF
    )"

Replace `DATAPLEX_API` with the Dataplex API endpoint of the format `dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID`.

  3. Optional: Get the status of the operation.
         
         gcurl https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/operations/operation-OPERATION_ID

Replace `OPERATION_ID` with the ID of the operation.

  4. Optional: Get the status of the metadata job.
         
         gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/metadataJobs/JOB_ID

  5. Import links between terms as synonym or related terms.
         
         gcurl https://DATAPLEX_API/metadataJobs?metadata_job_id=JOB_ID -d "$(cat<<EOF
         {
            "type":"IMPORT",
            "import_spec":{
               "log_level":"DEBUG",
               "source_storage_uri":"gs://STORAGE_BUCKET/",
               "entry_sync_mode":"FULL",
               "aspect_sync_mode":"INCREMENTAL",
               "scope":{
                  "entry_groups":[  "projects/PROJECT_ID/locations/LOCATION_ID/entryGroups/@dataplex"
                  ],
                  "entry_link_types":[
                     "projects/dataplex-types/locations/global/entryLinkTypes/synonym",
                     "projects/dataplex-types/locations/global/entryLinkTypes/related"
                  ],
                  "referenced_entry_scopes":[
                     "PROJECT_IDS"
                  ]
               }
            }
         }
         EOF
         )"

Replace `DATAPLEX_API` with `dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID`.

  6. Import links between terms and data assets or columns.

To create a link between glossary terms and data assets, run the import job for each entry group to which the entry for the data asset belongs. All definition entry links are created in this entry group.

**Note:** Make sure that the import file in the Cloud Storage bucket contains a file for links in one entry group. To create a link between a term and entry for the data asset in another entry group, provide a new file in the Cloud Storage bucket.
         
         gcurl https://DATAPLEX_API/metadataJobs?metadata_job_id=JOB_ID -d "$(cat<<EOF
         {
         "type":"IMPORT",
         "import_spec":{
            "log_level":"DEBUG",
            "source_storage_uri":"gs://STORAGE_BUCKET/",
            "entry_sync_mode":"FULL",
            "aspect_sync_mode":"INCREMENTAL",
            "scope":{
               "entry_groups":[  "projects/PROJECT_ID/locations/ENTRY_GROUP_LOCATION_ID/entryGroups/@dataplex"
               ],
               "entry_link_types":[
                  "projects/dataplex-types/locations/global/entryLinkTypes/definition"
               ],
               "referenced_entry_scopes":[
                  "PROJECT_IDS"
               ]
            }
         }
         }
         EOF
         )"

Replace `DATAPLEX_API` with `dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID`.




## Pricing

Starting in July 2025, Knowledge Catalog business glossary will be billed the same as the metadata storage pricing. See [Knowledge Catalog metadata storage pricing](https://cloud.google.com/products/knowledge-catalog/pricing#metadata-storage).

## What's next

  * Learn how to [establish foundational data context](https://docs.cloud.google.com/knowledge-catalog/docs/establish-foundational-data-context).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
