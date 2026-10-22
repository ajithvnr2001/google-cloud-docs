---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-quickstart/
title: List data sources \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:04.381580+00:00
---

# List data sources  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  List data sources Stay organized with collections  Save and categorize content based on your preferences. 

Lists all supported data sources for the BigQuery Data Transfer Service.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [BigQuery Data Transfer Service API Client Libraries](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/libraries)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.BigQuery.DataTransfer.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.html);
    using System;
    
    namespace GoogleCloudSamples
    {
        public class QuickStart
        {
            public static void Main(string[] args)
            {
                // Instantiates a client
                [DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.DataTransferServiceClient.html) client = [DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.DataTransferServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.DataTransferServiceClient.html#Google_Cloud_BigQuery_DataTransfer_V1_DataTransferServiceClient_Create)();
    
                // Your Google Cloud Platform project ID
                string projectId = "YOUR-PROJECT-ID";
    
                [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) project = [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html).[FromProject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_)(projectId);
                var sources = client.[ListDataSources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.DataTransferServiceClient.html#Google_Cloud_BigQuery_DataTransfer_V1_DataTransferServiceClient_ListDataSources_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(project);
                Console.WriteLine("Supported Data Sources:");
                foreach ([DataSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataTransfer.V1/latest/Google.Cloud.BigQuery.DataTransfer.V1.DataSource.html) source in sources)
                {
                    Console.WriteLine(
                        $"{source.DataSourceId}: " +
                        $"{source.DisplayName} ({source.Description})");
                }
            }
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // Sample bigquery-quickstart creates a Google BigQuery dataset.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"google.golang.org/api/iterator"
    
    	// Imports the BigQuery Data Transfer client package.
    	datatransfer "cloud.google.com/go/bigquery/datatransfer/apiv1"
    	"cloud.google.com/go/bigquery/datatransfer/apiv1/datatransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Sets your Google Cloud Platform project ID.
    	projectID := "YOUR_PROJECT_ID"
    
    	// Creates a client.
    	client, err := datatransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/datatransfer/apiv1.html#cloud_google_com_go_bigquery_datatransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/datatransfer/apiv1.html#cloud_google_com_go_bigquery_datatransfer_apiv1_Client_Close)()
    
    	req := &datatransferpb.ListDataSourcesRequest{
    		Parent: fmt.Sprintf("projects/%s", projectID),
    	}
    	it := client.ListDataSources(ctx, req)
    	fmt.Println("Supported Data Sources:")
    	for {
    		ds, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			log.Fatalf("Failed to list sources: %v", err)
    		}
    		fmt.Println(ds.DisplayName)
    		fmt.Println("\tID: ", ds.DataSourceId)
    		fmt.Println("\tFull path: ", ds.Name)
    		fmt.Println("\tDescription: ", ds.Description)
    	}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // Imports the Google Cloud client library
    
    import com.google.cloud.bigquery.datatransfer.v1.[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataSource.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html);
    import com.google.cloud.bigquery.datatransfer.v1.[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).[ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.ListDataSourcesPagedResponse.html);
    import com.google.cloud.bigquery.datatransfer.v1.[ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ListDataSourcesRequest.html);
    
    public class QuickstartSample {
      /** List available data sources for the BigQuery Data Transfer service. */
      public static void main(String... args) throws Exception {
        // Sets your Google Cloud Platform project ID.
        // String projectId = "YOUR_PROJECT_ID";
        String projectId = args[0];
    
        // Instantiate a client. If you don't specify credentials when constructing a client, the
        // client library will look for credentials in the environment, such as the
        // GOOGLE_APPLICATION_CREDENTIALS environment variable.
        try ([DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html) client = [DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.html).create()) {
          // Request the list of available data sources.
          String parent = String.format("projects/%s", projectId);
          [ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ListDataSourcesRequest.html) request =
              [ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.ListDataSourcesRequest.html).newBuilder().setParent(parent).build();
          [ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataTransferServiceClient.ListDataSourcesPagedResponse.html) response = client.listDataSources(request);
    
          // Print the results.
          System.out.println("Supported Data Sources:");
          for ([DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatatransfer/latest/com.google.cloud.bigquery.datatransfer.v1.DataSource.html) dataSource : response.iterateAll()) {
            System.out.println(dataSource.getDisplayName());
            System.out.printf("\tID: %s%n", dataSource.getDataSourceId());
            System.out.printf("\tFull path: %s%n", dataSource.getName());
            System.out.printf("\tDescription: %s%n", dataSource.getDescription());
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {
      DataTransferServiceClient,
    } = require('[@google-cloud/bigquery-data-transfer](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)');
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)();
    
    /**
     * Lists all available data sources for a project.
     * Data sources are the services that can be used to create data transfers into BigQuery.
     *
     * @param {string} projectId The Google Cloud project ID, for example 'example-project-id'.
     */
    async function listDataSources(projectId) {
      const request = {
        parent: `projects/${projectId}`,
      };
    
      try {
        const [dataSources] = await client.listDataSources(request);
    
        if (dataSources.length === 0) {
          console.log(`No data sources found in project ${projectId}.`);
          return;
        }
    
        console.log('Supported data sources:');
        for (const dataSource of dataSources) {
          console.log(`\nData source: ${dataSource.name}`);
          console.log(`  ID: ${dataSource.dataSourceId}`);
          console.log(`  Display Name: ${dataSource.displayName}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(`Project ${projectId} not found.`);
        } else {
          console.error('An error occurred:', err);
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    # Includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    # Imports the Google Cloud client library
    use Google\Cloud\BigQuery\DataTransfer\V1\Client\DataTransferServiceClient;
    use Google\Cloud\BigQuery\DataTransfer\V1\ListDataSourcesRequest;
    
    # Instantiates a client
    $bqdtsClient = new DataTransferServiceClient();
    
    # Your Google Cloud Platform project ID
    $projectId = 'YOUR_PROJECT_ID';
    $parent = sprintf('projects/%s/locations/us', $projectId);
    
    try {
        echo 'Supported Data Sources:', PHP_EOL;
        $listDataSourcesRequest = (new ListDataSourcesRequest())
            ->setParent($parent);
        $pagedResponse = $bqdtsClient->listDataSources($listDataSourcesRequest);
        foreach ($pagedResponse->iterateAllElements() as $dataSource) {
            echo 'Data source: ', $dataSource->getDisplayName(), PHP_EOL;
            echo 'ID: ', $dataSource->getDataSourceId(), PHP_EOL;
            echo 'Full path: ', $dataSource->getName(), PHP_EOL;
            echo 'Description: ', $dataSource->getDescription(), PHP_EOL;
        }
    } finally {
        $bqdtsClient->close();
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import bigquery_datatransfer
    
    client = bigquery_datatransfer.[DataTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html)()
    
    # TODO: Update to your project ID.
    project_id = "my-project"
    
    # Get the full path to your project.
    parent = client.[common_project_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_common_project_path)(project_id)
    
    print("Supported Data Sources:")
    
    # Iterate over all possible data sources.
    for data_source in client.[list_data_sources](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.DataTransferServiceClient.html#google_cloud_bigquery_datatransfer_v1_services_data_transfer_service_DataTransferServiceClient_list_data_sources)(parent=parent):
        print("{}:".format(data_source.display_name))
        print("\tID: {}".format(data_source.data_source_id))
        print("\tFull path: {}".format(data_source.name))
        print("\tDescription: {}".format(data_source.description))

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-bigquery/latest/Google/Cloud/Bigquery.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    # Imports the Google Cloud client library
    require "google/cloud/bigquery/data_transfer"
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    # Instantiate a client
    data_transfer = Google::Cloud::Bigquery::DataTransfer.data_transfer_service
    
    # Get the full path to your project.
    project_path = data_transfer.project_path project: project_id
    
    puts "Supported Data Sources:"
    
    # Iterate over all possible data sources.
    data_transfer.list_data_sources(parent: project_path).each do |data_source|
      puts "Data source: #{data_source.display_name}"
      puts "ID: #{data_source.data_source_id}"
      puts "Full path: #{data_source.name}"
      puts "Description: #{data_source.description}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquerydatatransferservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
