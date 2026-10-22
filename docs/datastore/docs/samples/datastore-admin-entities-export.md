---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-admin-entities-export/
title: Export a copy of all or a subset of entities \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:00.982632+00:00
---

# Export a copy of all or a subset of entities  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-admin-entities-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Export a copy of all or a subset of entities Stay organized with collections  Save and categorize content based on your preferences. 

Exports a copy of all or a subset of entities from Datastore to another storage system, such as Cloud Storage.

## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Datastore.Admin.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class ExportEntitiesSample
    {
        public string ExportEntities(
            string projectId = "your-project-id",
            string outputUrlPrefix = "gs://your-bucket-name",
            string kind = "Task",
            string namespaceId = "default")
        {
            // Create client
            [DatastoreAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html) datastoreAdminClient = [DatastoreAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html#Google_Cloud_Datastore_Admin_V1_DatastoreAdminClient_Create)();
    
            IDictionary<string, string> labels = new Dictionary<string, string> { { "cloud_datastore_samples", "true" }, };
            [EntityFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.EntityFilter.html) entityFilter = new [EntityFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.EntityFilter.html)
            {
                Kinds = { kind },
                NamespaceIds = { namespaceId }
            };
    
            var response = datastoreAdminClient.[ExportEntities](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.DatastoreAdminClient.html#Google_Cloud_Datastore_Admin_V1_DatastoreAdminClient_ExportEntities_Google_Cloud_Datastore_Admin_V1_ExportEntitiesRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, labels, entityFilter, outputUrlPrefix);
    
            // Poll until the returned long-running operation is complete
            var completedResponse = response.PollUntilCompleted();
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while Exporting Entities: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            Console.WriteLine($"Entities exported successfully.");
    
            [ExportEntitiesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.ExportEntitiesResponse.html) result = completedResponse.Result;
    
            return result.[OutputUrl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.Admin.V1/latest/Google.Cloud.Datastore.Admin.V1.ExportEntitiesResponse.html#Google_Cloud_Datastore_Admin_V1_ExportEntitiesResponse_OutputUrl);
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
    
    // entitiesExport exports a copy of all or a subset of entities from
    // Datastore to another storage system, such as Cloud Storage.
    func entitiesExport(w io.Writer, projectID, outputURLPrefix string) (*adminpb.ExportEntitiesResponse, error) {
    	// projectID := "project-id"
    	// outputURLPrefix := "gs://bucket-name"
    	ctx := context.Background()
    	client, err := admin.NewDatastoreAdminClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("admin.NewDatastoreAdminClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest/admin/apiv1.html#cloud_google_com_go_datastore_admin_apiv1_DatastoreAdminClient_Close)()
    
    	req := &adminpb.ExportEntitiesRequest{
    		ProjectId:       projectID,
    		OutputUrlPrefix: outputURLPrefix,
    	}
    	op, err := client.ExportEntities(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("ExportEntities: %w", err)
    	}
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("Wait: %w", err)
    	}
    	fmt.Fprintln(w, "Entities were exported")
    	return resp, nil
    }
    

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def export_entities(project_id, output_url_prefix):
        """
        Exports a copy of all or a subset of entities from
        Datastore to another storage system, such as Cloud Storage.
        """
        # project_id = "project-id"
        # output_url_prefix = "gs://bucket-name"
        client = DatastoreAdminClient()
    
        op = client.export_entities(
            {"project_id": project_id, "output_url_prefix": output_url_prefix}
        )
        response = op.result(timeout=300)
    
        print("Entities were exported\n")
        return response
    
    

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "project-id"
    # output_url_prefix = "gs://bucket-name"
    op = client.export_entities project_id: project_id, output_url_prefix: output_url_prefix
    
    op.wait_until_done!
    raise op.error.message if op.error?
    
    response = op.response
    # Process the response.
    
    metadata = op.metadata
    # Process the metadata.
    
    puts "Entities were exported"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
