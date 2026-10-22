---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-admin-entities-import/
title: Import admin entities to Datastore \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:02.211176+00:00
---

# Import admin entities to Datastore  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-admin-entities-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Import admin entities to Datastore Stay organized with collections  Save and categorize content based on your preferences. 

Import admin entities to Datastore

## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Datastore.Admin.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Collections.Generic;
    
    public class ImportEntitiesSample
    {
        public bool ImportEntities(
            string projectId = "your-project-id",
            // For information on accepted input URL formats, see
            // https://cloud.google.com/datastore/docs/reference/admin/rpc/google.datastore.admin.v1#google.datastore.admin.v1.ImportEntitiesRequest
            string inputUrl = "[URL to file containing data]",
            string kind = "Task",
            string namespaceId = "default")
        {
            // Create client
            [DatastoreAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html) datastoreAdminClient = [DatastoreAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html#Google_Cloud_Datastore_Admin_V1_DatastoreAdminClient_Create)();
    
            IDictionary<string, string> labels = new Dictionary<string, string> { { "cloud_datastore_samples", "true" }, };
            [EntityFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.EntityFilter.html) entityFilter = new [EntityFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.EntityFilter.html)()
            {
                Kinds = { kind },
                NamespaceIds = { namespaceId }
            };
    
            Operation<Empty, ImportEntitiesMetadata> response = datastoreAdminClient.[ImportEntities](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html#Google_Cloud_Datastore_Admin_V1_DatastoreAdminClient_ImportEntities_Google_Cloud_Datastore_Admin_V1_ImportEntitiesRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, labels, inputUrl, entityFilter);
    
            // Poll until the returned long-running operation is complete
            Operation<Empty, ImportEntitiesMetadata> completedResponse = response.PollUntilCompleted();
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while Importing Entities: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            Console.WriteLine($"Entities imported successfully.");
    
            return completedResponse.IsCompleted;
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
    
    // entitiesImport imports entities into Datastore.
    func entitiesImport(w io.Writer, projectID, inputURL string) error {
    	// projectID := "project-id"
    	// inputURL := "gs://bucket-name/overall-export-metadata-file"
    	ctx := context.Background()
    	client, err := admin.NewDatastoreAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("admin.NewDatastoreAdminClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/admin/apiv1.html#cloud_google_com_go_datastore_admin_apiv1_DatastoreAdminClient_Close)()
    
    	req := &adminpb.ImportEntitiesRequest{
    		ProjectId: projectID,
    		InputUrl:  inputURL,
    	}
    	op, err := client.ImportEntities(ctx, req)
    	if err != nil {
    		return fmt.Errorf("ImportEntities: %w", err)
    	}
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    	fmt.Fprintf(w, "Entities were imported\n")
    	return nil
    }
    

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def import_entities(project_id, input_url):
        """Imports entities into Datastore."""
        # project_id := "project-id"
        # input_url := "gs://bucket-name/overall-export-metadata-file"
        client = DatastoreAdminClient()
    
        op = client.import_entities({"project_id": project_id, "input_url": input_url})
        response = op.result(timeout=300)
    
        print("Entities were imported\n")
        return response
    
    

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "project-id"
    # input_url = "gs://bucket-name/overall-export-metadata-file"
    op = client.import_entities project_id: project_id, input_url: input_url
    
    op.wait_until_done!
    raise op.error.message if op.error?
    
    response = op.response
    # Process the response.
    
    metadata = op.metadata
    # Process the metadata.
    
    puts "Entities were imported"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
