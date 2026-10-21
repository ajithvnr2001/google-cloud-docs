---
url: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-ptm-create-taxonomy/
title: Create taxonomy \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:30.978937+00:00
---

# Create taxonomy  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-ptm-create-taxonomy/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/data-catalog/docs/samples)



#  Create taxonomy Stay organized with collections  Save and categorize content based on your preferences. 

Create a new taxonomy.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Go API reference documentation](https://godoc.org/cloud.google.com/go/datacatalog). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	datacatalog "cloud.google.com/go/datacatalog/apiv1beta1"
    	"cloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb"
    )
    
    // createTaxonomy creates a taxonomy resource, which holds the collection of policy tags.
    //
    // This example marks the taxonomy as valid for defining fine grained access control, also
    // known as column-level access control when used in conjunction with BigQuery.
    func createTaxonomy(w io.Writer, projectID, location, displayName string) (string, error) {
    	// projectID := "my-project-id"
    	// location := "us"
    	// displayName := "example-taxonomy"
    	ctx := context.Background()
    	policyClient, err := datacatalog.NewPolicyTagManagerClient(ctx)
    	if err != nil {
    		return "", fmt.Errorf("datacatalog.NewPolicyTagManagerClient: %w", err)
    	}
    	defer policyClient.Close()
    
    	req := &datacatalogpb.CreateTaxonomyRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		Taxonomy: &datacatalogpb.Taxonomy{
    			DisplayName: displayName,
    			Description: "Taxonomy created via basic snippet testing",
    			ActivatedPolicyTypes: []datacatalogpb.Taxonomy_PolicyType{
    				datacatalogpb.[Taxonomy_FINE_GRAINED_ACCESS_CONTROL](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/apiv1beta1/datacatalogpb.html#cloud_google_com_go_datacatalog_apiv1beta1_datacatalogpb_Taxonomy_POLICY_TYPE_UNSPECIFIED_Taxonomy_FINE_GRAINED_ACCESS_CONTROL),
    			},
    		},
    	}
    	resp, err := policyClient.CreateTaxonomy(ctx, req)
    	if err != nil {
    		return "", fmt.Errorf("CreateTaxonomy: %w", err)
    	}
    
    	fmt.Fprintf(w, "Taxonomy %s was created.\n", resp.Name)
    	return resp.Name, nil
    }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Node.js API reference documentation](https://googleapis.dev/nodejs/datacatalog/latest/index.html). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client library.
    const {DataCatalogClient, PolicyTagManagerClient} =
      require('[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)').v1;
    const dataCatalog = new [DataCatalogClient](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)();
    const policyTagManager = new [PolicyTagManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)();
    
    async function createTaxonomy() {
      // const location = 'us';
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'my_project'; // Google Cloud Platform project
      // const location = 'us'
      // const displayName = 'my_display_name'; // Display name for new taxonomy.
    
      // Parent project location format is `projects/${projectId}/locations/${location}`
      const parent = dataCatalog.locationPath(projectId, location);
    
      const request = {
        parent: parent,
        taxonomy: {
          displayName: displayName,
          activatedPolicyTypes: ['FINE_GRAINED_ACCESS_CONTROL'],
        },
      };
    
      try {
        const [metadata] = await policyTagManager.createTaxonomy(request);
        console.log(`Created taxonomy: ${metadata.name}`);
      } catch (e) {
        console.error(e);
        process.exitCode = 1;
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest)
    
    
    def create_taxonomy(
        # TODO(developer): Set project_id to the ID of the project the
        #  taxonomy will belong to.
        project_id: str = "your-project-id",
        # TODO(developer): Specify the geographic location where the
        #  taxonomy should reside.
        location_id: str = "us",
        # TODO(developer): Set the display name of the taxonomy.
        display_name: str = "example-taxonomy",
    ):
        # TODO(developer): Construct a Policy Tag Manager client object. To avoid
        # extra delays due to authentication, create a single client for your
        # program and share it across operations.
        client = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[PolicyTagManagerClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.policy_tag_manager.PolicyTagManagerClient.html)()
    
        # Construct a full location path to be the parent of the taxonomy.
        parent = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[PolicyTagManagerClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.policy_tag_manager.PolicyTagManagerClient.html).common_location_path(
            project_id, location_id
        )
    
        # TODO(developer): Construct a full Taxonomy object to send to the API.
        taxonomy = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[Taxonomy](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.Taxonomy.html)()
        taxonomy.display_name = display_name
        taxonomy.description = "This Taxonomy represents ..."
    
        # Send the taxonomy to the API for creation.
        taxonomy = client.[create_taxonomy](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.policy_tag_manager.PolicyTagManagerClient.html#google_cloud_datacatalog_v1_services_policy_tag_manager_PolicyTagManagerClient_create_taxonomy)(parent=parent, taxonomy=taxonomy)
        print(f"Created taxonomy {taxonomy.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datacatalog). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
