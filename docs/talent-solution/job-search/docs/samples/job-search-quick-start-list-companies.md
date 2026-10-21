---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-quick-start-list-companies/
title: List companies using client (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:07.718012+00:00
---

# List companies using client (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-quick-start-list-companies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  List companies using client (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

List companies using client.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries)
  * [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries)



## Code sample

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"os"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	"cloud.google.com/go/talent/apiv4beta1/talentpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    
    	// Initialize job search client.
    	ctx := context.Background()
    	c, err := talent.[NewCompanyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_CompanyClient_NewCompanyClient)(ctx)
    	if err != nil {
    		fmt.Printf("talent.NewCompanyClient: %v", err)
    		return
    	}
    	defer c.Close()
    
    	// Construct a listCompany request.
    	req := &talentpb.ListCompaniesRequest{
    		Parent: "projects/" + projectID,
    	}
    
    	it := c.ListCompanies(ctx, req)
    
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			fmt.Printf("Done.\n")
    			break
    		}
    		if err != nil {
    			fmt.Printf("it.Next: %v", err)
    			return
    		}
    		fmt.Printf("Company: %v\n", resp.GetName())
    	}
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
