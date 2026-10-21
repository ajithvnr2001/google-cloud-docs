---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-admin-index-get/
title: Get admin index \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:08:44.296044+00:00
---

# Get admin index  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-admin-index-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Get admin index Stay organized with collections  Save and categorize content based on your preferences. 

Get admin index

## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Datastore.Admin.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.html);
    using System;
    using Index = Google.Cloud.Datastore.Admin.V1.Index;
    
    public class GetIndexSample
    {
        public Index GetIndex(
            string projectId = "your-project-id",
            string indexId = "your-index-id")
        {
            // Create client
            [DatastoreAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html) datastoreAdminClient = [DatastoreAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html#Google_Cloud_Datastore_Admin_V1_DatastoreAdminClient_Create)();
    
            // Initialize request argument(s)
            [GetIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.GetIndexRequest.html) getIndexRequest = new [GetIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.GetIndexRequest.html)
            {
                ProjectId = projectId,
                IndexId = indexId
            };
    
            [Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.Index.html) index = datastoreAdminClient.[GetIndex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html#Google_Cloud_Datastore_Admin_V1_DatastoreAdminClient_GetIndex_Google_Cloud_Datastore_Admin_V1_GetIndexRequest_Google_Api_Gax_Grpc_CallSettings_)(getIndexRequest);
    
            Console.WriteLine($"Index Id: {index.[IndexId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.Index.html#Google_Cloud_Datastore_Admin_V1_Index_IndexId)}");
            Console.WriteLine($"Kind: {index.[Kind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.Index.html#Google_Cloud_Datastore_Admin_V1_Index_Kind)}");
            Console.WriteLine("Properties:");
            foreach (var property in index.[Properties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.Index.html#Google_Cloud_Datastore_Admin_V1_Index_Properties))
            {
                Console.WriteLine($"Property: {property.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.Index.Types.IndexedProperty.html#Google_Cloud_Datastore_Admin_V1_Index_Types_IndexedProperty_Name)}");
                Console.WriteLine($"Direction: {property.Direction}");
            }
            return index;
        }
    }

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	admin "cloud.google.com/go/datastore/admin/apiv1"
    	"cloud.google.com/go/datastore/admin/apiv1/adminpb"
    )
    
    // indexGet gets an index.
    func indexGet(w io.Writer, projectID, indexID string) (*adminpb.Index, error) {
    	// projectID := "my-project-id"
    	// indexID := "my-index"
    	ctx := context.Background()
    	client, err := admin.NewDatastoreAdminClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("admin.NewDatastoreAdminClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/admin/apiv1.html#cloud_google_com_go_datastore_admin_apiv1_DatastoreAdminClient_Close)()
    
    	req := &adminpb.GetIndexRequest{
    		ProjectId: projectID,
    		IndexId:   indexID,
    	}
    	index, err := client.GetIndex(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("client.GetIndex: %w", err)
    	}
    
    	fmt.Fprintf(w, "Got index: %v\n", index.IndexId)
    	return index, nil
    }
    

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_index(project_id, index_id):
        """Gets an index."""
        # project_id := "my-project-id"
        # index_id := "my-index"
        client = DatastoreAdminClient()
        index = client.get_index({"project_id": project_id, "index_id": index_id})
    
        print("Got index: %v\n", index.index_id)
        return index
    
    

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "project-id"
    # index_id = "my-index"
    index = client.get_index project_id: project_id, index_id: index_id
    puts "Got index: #{index.index_id}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
