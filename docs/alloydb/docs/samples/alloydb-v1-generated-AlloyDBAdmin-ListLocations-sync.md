---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-ListLocations-sync/
title: List available locations \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:35.619258+00:00
---

# List available locations  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-ListLocations-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  List available locations Stay organized with collections  Save and categorize content based on your preferences. 

This snippet lists all available Google Cloud locations where resources can be created. Use this to identify valid regions and zones for provisioning new clusters or other resources.

## Code sample

### Go

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	alloydb "cloud.google.com/go/alloydb/apiv1"
    	"google.golang.org/api/iterator"
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := alloydb.NewAlloyDBAdminClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
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
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

### Java

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.alloydb.v1.[AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html);
    import com.google.cloud.location.[ListLocationsRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.cloud.location.ListLocationsRequest.html);
    import com.google.cloud.location.[Location](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.cloud.location.Location.html);
    
    public class SyncListLocations {
    
      public static void main(String[] args) throws Exception {
        syncListLocations();
      }
    
      public static void syncListLocations() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html) alloyDBAdminClient = [AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html).create()) {
          [ListLocationsRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.cloud.location.ListLocationsRequest.html) request =
              [ListLocationsRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.cloud.location.ListLocationsRequest.html).newBuilder()
                  .setName("name3373707")
                  .setFilter("filter-1274492040")
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .build();
          for ([Location](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.cloud.location.Location.html) element : alloyDBAdminClient.listLocations(request).iterateAll()) {
            // doThingsWith(element);
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
