---
url: https://docs.cloud.google.com/bigquery/docs/authentication/getting-started/
title: Get started with authentication \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:51.256627+00:00
---

# Get started with authentication  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/authentication/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with authentication

To authenticate your application to BigQuery resources, you can use Application Default Credentials (ADC). ADC uses service account credentials, providing a consistent authentication method for both local development and deployed environments. This approach removes the need to modify authentication code when you move from development to production. BigQuery doesn't support the use of [API keys](https://docs.cloud.google.com/docs/authentication/api-keys-use) for authentication.

## Before you begin

Select the tab for how you plan to use the samples on this page:

### C#

To use the .NET samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigquery/docs/authentication#local-development). 

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigquery/docs/authentication#local-development). 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigquery/docs/authentication#local-development). 

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigquery/docs/authentication#local-development). 

### PHP

To use the PHP samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigquery/docs/authentication#local-development). 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigquery/docs/authentication#local-development). 

### Ruby

To use the Ruby samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigquery/docs/authentication#local-development). 

For information about setting up authentication for a production environment, see [ Set up Application Default Credentials for code running on Google Cloud ](https://docs.cloud.google.com/bigquery/docs/authentication#on-gcp). 

## Application Default Credentials

Client libraries can use [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to easily authenticate with Google APIs and send requests to those APIs. With Application Default Credentials, you can test your application locally and deploy it without changing the underlying code. For more information, see [ Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

When you create a service object with the [BigQuery API Client Libraries](https://docs.cloud.google.com/bigquery/docs/reference/libraries) and don't pass in explicit credentials, your application authenticates using Application Default Credentials. The following samples show how to authenticate to BigQuery by using ADC.

### C#

Before trying this sample, follow the C# setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    using Google.Apis.Bigquery.v2.Data;
    using [Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html);
    
    public class BigQueryCreateDataset
    {
        public BigQueryDataset CreateDataset(
            string projectId = "your-project-id",
            string location = "US"
        )
        {
            [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html) client = [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_)(projectId);
            var dataset = new Dataset
            {
                // Specify the geographic location where the dataset should reside.
                Location = location
            };
            // Create the dataset
            return client.[CreateDataset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_CreateDataset_Google_Apis_Bigquery_v2_Data_DatasetReference_Google_Apis_Bigquery_v2_Data_Dataset_Google_Cloud_BigQuery_V2_CreateDatasetOptions_)(
                datasetId: "your_new_dataset_id", dataset);
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    // Sample bigquery-quickstart creates a Google BigQuery dataset.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/bigquery"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Sets your Google Cloud Platform project ID.
    	projectID := "YOUR_PROJECT_ID"
    
    	// Creates a client.
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("bigquery.NewClient: %v", err)
    	}
    	defer client.Close()
    
    	// Sets the name for the new dataset.
    	datasetName := "my_new_dataset"
    
    	// Creates the new BigQuery dataset.
    	if err := client.Dataset(datasetName).Create(ctx, &bigquery.[DatasetMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_DatasetMetadata){}); err != nil {
    		log.Fatalf("Failed to create dataset: %v", err)
    	}
    
    	fmt.Printf("Dataset created\n")
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    public static void implicit() {
      // Instantiate a client. If you don't specify credentials when constructing a client, the
      // client library will look for credentials in the environment, such as the
      // GOOGLE_APPLICATION_CREDENTIALS environment variable.
      BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
    
      // Use the client.
      System.out.println("Datasets:");
      for (Dataset dataset : bigquery.listDatasets().iterateAll()) {
        System.out.printf("%s%n", dataset.getDatasetId().getDataset());
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    // Import the Google Cloud client library using default credentials
    const {BigQuery} = require('[@google-cloud/bigquery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/overview.html)');
    const bigquery = new [BigQuery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html)();

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    /** Uncomment and populate these variables in your code */
    //$projectId = 'The Google project ID';
    
    $bigQuery = new BigQueryClient([
        'projectId' => $projectId,
    ]);

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-bigquery/latest/Google/Cloud/Bigquery.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    require "google/cloud/bigquery"
    
    # This uses Application Default Credentials to authenticate.
    # @see https://cloud.google.com/bigquery/docs/authentication/getting-started
    bigquery = Google::Cloud::[Bigquery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_policies-v1beta1/latest/Google-Cloud-Bigquery.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery.html)
    
    sql     = "SELECT " \
              "CONCAT('https://stackoverflow.com/questions/', CAST(id as STRING)) as url, view_count " \
              "FROM `bigquery-public-data.stackoverflow.posts_questions` " \
              "WHERE tags like '%google-bigquery%' " \
              "ORDER BY view_count DESC LIMIT 10"
    results = bigquery.query sql
    
    results.each do |row|
      puts "#{[row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-InsertResponse-InsertError.html)[:url]}: #{[row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-InsertResponse-InsertError.html)[:view_count]} views"
    end

## What's next

  * Learn more about [BigQuery authentication](https://docs.cloud.google.com/bigquery/docs/authentication).
  * Learn how to [authenticate with end-user credentials](https://docs.cloud.google.com/bigquery/docs/authentication/end-user-installed).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
