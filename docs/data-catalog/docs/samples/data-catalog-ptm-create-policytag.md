---
url: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-ptm-create-policytag/
title: Create policy tag \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:30.731170+00:00
---

# Create policy tag  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-ptm-create-policytag/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/data-catalog/docs/samples)



#  Create policy tag Stay organized with collections  Save and categorize content based on your preferences. 

Create a new policy tag.

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
    
    // createPolicyTag creates a policy tag resource under a given parent taxonomy.
    //
    // It optionally accepts a parent ID, which can be used to create a hierarchical
    // relationship between tags.
    func createPolicyTag(w io.Writer, parent, displayName, parentPolicyTag string) (string, error) {
    	// parent := "projects/myproject/locations/us/taxonomies/1234"
    	// displayName := "Example Policy Tag"
    	// parentPolicyTag := "projects/myproject/locations/us/taxonomies/1234/policyTags/5678"
    	ctx := context.Background()
    	policyClient, err := datacatalog.NewPolicyTagManagerClient(ctx)
    	if err != nil {
    		return "", fmt.Errorf("datacatalog.NewPolicyTagManagerClient: %w", err)
    	}
    	defer policyClient.Close()
    
    	req := &datacatalogpb.CreatePolicyTagRequest{
    		Parent: parent,
    		PolicyTag: &datacatalogpb.PolicyTag{
    			DisplayName: displayName,
    			Description: "Example description for the policy tag",
    		},
    	}
    	if parentPolicyTag != "" {
    		req.PolicyTag.ParentPolicyTag = parentPolicyTag
    	}
    	resp, err := policyClient.CreatePolicyTag(ctx, req)
    	if err != nil {
    		return "", fmt.Errorf("CreatePolicyTag: %w", err)
    	}
    
    	fmt.Fprintf(w, "PolicyTag %s was created.\n", resp.Name)
    	return resp.Name, nil
    }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Node.js API reference documentation](https://googleapis.dev/nodejs/datacatalog/latest/index.html). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Create a policy tag resource under a given parent taxonomy.
    
    // Import the Google Cloud client library.
    const {PolicyTagManagerClient} = require('[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)').v1;
    const policyClient = new [PolicyTagManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)();
    
    async function createPolicyTag() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'my_project'; // Google Cloud Platform project
      // const location = 'us';
      // const taxonomy = 'my_existing_taxonomy';
      // const parent = `projects/${projectId}/locations/${location}/taxonomies/${taxonomy}`;
    
      const request = {
        parent,
        policyTag: {
          displayName: 'nodejs_samples_tag',
          //   // It optionally accepts a parent ID, which can be used to create a hierarchical
          //   // relationship between tags.
          //   parentPolicyTag: `projects/${projectId}/locations/${location}/taxonomies/${taxonomy}/policyTags/my_existing_policy_tag`
        },
      };
    
      try {
        const [metadata] = await policyClient.createPolicyTag(request);
        console.log(`Created policy tag: ${metadata.name}`);
      } catch (e) {
        console.error(e);
        process.exitCode = 1;
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datacatalog). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
