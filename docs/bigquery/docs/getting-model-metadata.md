---
url: https://docs.cloud.google.com/bigquery/docs/getting-model-metadata/
title: Get model metadata \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:56.080847+00:00
---

# Get model metadata  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/getting-model-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get model metadata

This page shows you how to get information or metadata about BigQuery ML models. You can get model metadata by:

  * Using the Google Cloud console
  * Using the `bq show` CLI command
  * Calling the [`models.get`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/models/get) API method directly or by using the client libraries

**Note:** Getting information about models by querying the `INFORMATION_SCHEMA` views is unsupported.

## Required permissions

To get model metadata, you must be assigned the [`READER`](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam#grant_access_to_a_dataset) role on the dataset, or you must be assigned a project-level Identity and Access Management (IAM) role that includes `bigquery.models.getMetadata` permissions. If you are granted `bigquery.models.getMetadata` permissions at the project level, you can get metadata on models in any dataset in the project. The following predefined, project-level IAM roles include `bigquery.models.getMetadata` permissions:

  * `bigquery.dataViewer`
  * `bigquery.dataEditor`
  * `bigquery.dataOwner`
  * `bigquery.metadataViewer`
  * `bigquery.admin`



For more information on IAM roles and permissions in BigQuery ML, see [Access control](https://docs.cloud.google.com/bigquery/docs/access-control).

## Get model metadata

To get metadata about models:

###  Console 

  1. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  2. In the **Explorer** pane, expand the project, click **Datasets** , and then select the dataset.

  3. Click the **Models** tab, and then click a model name to select the model.

  4. Click the **Details** tab. This tab displays the model's metadata, including the description, labels, model type, and training options.




###  bq 

Issue the `bq show` command with the `--model` or `-m` flag to display model metadata. The [`--format`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#global_flags) flag can be used to control the output.

To see only the feature columns for your model, use the `--schema` flag with the `--model` flag. When you use the `--schema` flag, `--format` must be set to either `json` or `prettyjson`.

If you are getting information about a model in a project other than your default project, add the project ID to the dataset in the following format: `[PROJECT_ID]:[DATASET]`.
    
    
    bq show --model --format=prettyjson PROJECT_ID:DATASET.MODEL
    

Replace the following:

  * `PROJECT_ID` is your project ID.
  * `DATASET` is the name of the dataset.
  * `MODEL` is the name of the model.



The command output looks like the following when the `--format=pretty` flag is used. To see full details, use the `--format=prettyjson` format. The sample output shows metadata for a logistic regression model.
    
    
    +--------------+---------------------+---------------------+---------------------------+--------+-----------------+-----------------+
    |      Id      |     Model Type      |   Feature Columns   |       Label Columns       | Labels |  Creation Time  | Expiration Time |
    +--------------+---------------------+---------------------+---------------------------+--------+-----------------+-----------------+
    | sample_model | LOGISTIC_REGRESSION | |- column1: string  | |- label_column: int64    |        | 03 May 23:14:42 |                 |
    |              |                     | |- column2: bool    |                           |        |                 |                 |
    |              |                     | |- column3: string  |                           |        |                 |                 |
    |              |                     | |- column4: int64   |                           |        |                 |                 |
    +--------------+---------------------+---------------------+---------------------------+--------+-----------------+-----------------+
    

Examples:

Enter the following command to display all information about `mymodel` in `mydataset`. `mydataset` is in your default project.
    
    
    bq show --model --format=prettyjson mydataset.mymodel
    

Enter the following command to display all information about `mymodel` in `mydataset`. `mydataset` is in `myotherproject`, not your default project.
    
    
    bq show --model --format=prettyjson myotherproject:mydataset.mymodel
    

Enter the following command to display only the feature columns for `mymodel` in `mydataset`. `mydataset` is in `myotherproject`, not your default project.
    
    
    bq show --model --schema --format=prettyjson \
    myotherproject:mydataset.mymodel
    

###  API 

To get model metadata by using the API, call the [`models.get`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/models/get) method and provide the `projectId`, `datasetId`, and `modelId`.

###  Go 

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // printModelInfo demonstrates fetching metadata about a BigQuery ML model and printing some of
    // it to an io.Writer.
    func printModelInfo(w io.Writer, projectID, datasetID, modelID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "mydataset"
    	// modelID := "mymodel"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	meta, err := client.Dataset(datasetID).Model(modelID).Metadata(ctx)
    	if err != nil {
    		return fmt.Errorf("couldn't retrieve metadata: %w", err)
    	}
    	fmt.Fprintf(w, "Got model '%q' with friendly name '%q'\n", modelID, meta.Name)
    	return nil
    }
    

###  Java 

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Model.html);
    import com.google.cloud.bigquery.[ModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ModelId.html);
    
    public class GetModel {
    
      public static void runGetModel() {
        // TODO(developer): Replace these variables before running the sample.
        String datasetName = "MY_DATASET_NAME";
        String modelName = "MY_MODEL_ID";
        getModel(datasetName, modelName);
      }
    
      public static void getModel(String datasetName, String modelName) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [ModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ModelId.html) modelId = [ModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ModelId.html).of(datasetName, modelName);
          [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Model.html) model = bigquery.[getModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_getModel_com_google_cloud_bigquery_ModelId_com_google_cloud_bigquery_BigQuery_ModelOption____)(modelId);
          System.out.println("Model: " + model.getDescription());
    
          System.out.println("Successfully retrieved model");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e) {
          System.out.println("Cannot retrieve model \n" + e.toString());
        }
      }
    }

###  Node.js 

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // Import the Google Cloud client library
    const {BigQuery} = require('[@google-cloud/bigquery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/overview.html)');
    const bigquery = new [BigQuery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html)();
    
    async function getModel() {
      // Retrieves model named "my_existing_model" in "my_dataset".
    
      /**
       * TODO(developer): Uncomment the following lines before running the sample
       */
      // const datasetId = "my_dataset";
      // const modelId = "my_existing_model";
    
      const dataset = bigquery.dataset(datasetId);
      const [model] = await dataset.[model](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/dataset.html)(modelId).get();
    
      console.log('Model:');
      console.log([model](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/dataset.html).metadata.modelReference);
    }

###  Python 

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # TODO(developer): Set model_id to the ID of the model to fetch.
    # model_id = 'your-project.your_dataset.your_model'
    
    model = client.[get_model](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_model)(model_id)  # Make an API request.
    
    full_model_id = "{}.{}.{}".format(model.project, model.dataset_id, model.model_id)
    friendly_name = model.friendly_name
    print(
        "Got model '{}' with friendly_name '{}'.".format(full_model_id, friendly_name)
    )

## What's next

  * For an overview of BigQuery ML, see [Introduction to BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction).
  * To get started using BigQuery ML, see [Create machine learning models in BigQuery ML](https://docs.cloud.google.com/bigquery/docs/create-machine-learning-model).
  * To learn more about working with models, see: 
    * [List models](https://docs.cloud.google.com/bigquery/docs/listing-models)
    * [Update model metadata](https://docs.cloud.google.com/bigquery/docs/updating-model-metadata)
    * [Manage models](https://docs.cloud.google.com/bigquery/docs/managing-models)
    * [Delete models](https://docs.cloud.google.com/bigquery/docs/deleting-models)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
