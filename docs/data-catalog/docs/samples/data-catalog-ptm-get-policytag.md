---
url: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-ptm-get-policytag/
title: Get policy tag \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:32.104428+00:00
---

# Get policy tag  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-ptm-get-policytag/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/data-catalog/docs/samples)



#  Get policy tag Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve existing policy tag.

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
    
    // getPolicyTag prints information about a given policy tag.
    func getPolicyTag(w io.Writer, policyTagID string) error {
    	// policyTagID := "projects/myproject/locations/us/taxonomies/1234/policyTags/5678"
    	ctx := context.Background()
    	policyClient, err := datacatalog.NewPolicyTagManagerClient(ctx)
    	if err != nil {
    		return fmt.Errorf("datacatalog.NewPolicyTagManagerClient: %w", err)
    	}
    	defer policyClient.Close()
    
    	req := &datacatalogpb.GetPolicyTagRequest{
    		Name: policyTagID,
    	}
    	resp, err := policyClient.GetPolicyTag(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetPolicyTag: %w", err)
    	}
    	fmt.Fprintf(w, "PolicyTag %s has Display Name %s", resp.Name, resp.DisplayName)
    	if resp.ParentPolicyTag != "" {
    		fmt.Fprintf(w, " and is a child of Policy Tag %s", resp.ParentPolicyTag)
    	}
    	if len(resp.ChildPolicyTags) > 0 {
    		fmt.Fprintf(w, ", with %d child tags", len(resp.ChildPolicyTags))
    	}
    	fmt.Fprintln(w)
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datacatalog). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
