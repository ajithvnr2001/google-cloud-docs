---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-create-clients/
title: Create clients \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:20.904690+00:00
---

# Create clients  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-create-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Create clients Stay organized with collections  Save and categorize content based on your preferences. 

Create a client that can read, write, and run transactions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting started with Spanner in Go](https://docs.cloud.google.com/spanner/docs/getting-started/go)



## Code sample

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"io"
    
    	"cloud.google.com/go/spanner"
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    )
    
    func createClients(w io.Writer, db string) error {
    	ctx := context.Background()
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer adminClient.Close()
    
    	dataClient, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer dataClient.Close()
    
    	_ = adminClient
    	_ = dataClient
    
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
