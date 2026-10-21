---
url: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-ptm-list-policytags/
title: List policy tags \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:13.268317+00:00
---

# List policy tags  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-ptm-list-policytags/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/data-catalog/docs/samples)



#  List policy tags Stay organized with collections  Save and categorize content based on your preferences. 

List existing policy tags.

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
    	"google.golang.org/api/iterator"
    )
    
    // listPolicyTags prints information about the policy tags within a given taxonomy
    // resource.
    func listPolicyTags(w io.Writer, parentTaxonomyID string) error {
    	// parentTaxonomyID := projects/myproject/locations/us/taxonomies/1234"
    	ctx := context.Background()
    	policyClient, err := datacatalog.NewPolicyTagManagerClient(ctx)
    	if err != nil {
    		return fmt.Errorf("datacatalog.NewPolicyTagManagerClient: %w", err)
    	}
    	defer policyClient.Close()
    
    	req := &datacatalogpb.ListPolicyTagsRequest{
    		Parent: parentTaxonomyID,
    	}
    	it := policyClient.ListPolicyTags(ctx, req)
    	fmt.Fprintf(w, "listing policy tags in taxonomy %s\n", parentTaxonomyID)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListPolicyTags iteration error: %w", err)
    		}
    
    		fmt.Fprintf(w, "\t- %s (%s)", resp.Name, resp.DisplayName)
    		if resp.ParentPolicyTag != "" {
    			fmt.Fprintf(w, " has parent Tag %s", resp.ParentPolicyTag)
    		}
    		fmt.Fprintln(w)
    	}
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datacatalog). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
