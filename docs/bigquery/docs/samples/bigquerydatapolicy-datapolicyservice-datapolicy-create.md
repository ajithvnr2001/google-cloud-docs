---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicy-create/
title: Create a data masking policy \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:44.428430+00:00
---

# Create a data masking policy  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicy-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a data masking policy Stay organized with collections  Save and categorize content based on your preferences. 

Creates a data policy to apply a data masking rule to a specific BigQuery table column. This is a primary mechanism for implementing column-level security in BigQuery.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Mask column data](https://docs.cloud.google.com/bigquery/docs/column-data-masking)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.datapolicies.v2.[CreateDataPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.CreateDataPolicyRequest.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.html).[PredefinedExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.PredefinedExpression.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html).[DataPolicyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.DataPolicyType.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html);
    import com.google.cloud.bigquery.datapolicies.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.LocationName.html);
    import java.io.IOException;
    
    public class CreateDataPolicy {
    
      /**
       * Creates a data policy to apply a data masking rule to a specific BigQuery table column.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the data policy (for example, "us-central1").
       * @param dataPolicyId The user-assigned ID for the new data policy (for example,
       *     "example_data_policy").
       */
      public static void createDataPolicy(String projectId, String location, String dataPolicyId) {
        [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.LocationName.html).of(projectId, location);
    
        [DataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.html) dataMaskingPolicy =
            [DataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.html).newBuilder()
                .[setPredefinedExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.Builder.html#com_google_cloud_bigquery_datapolicies_v2_DataMaskingPolicy_Builder_setPredefinedExpression_com_google_cloud_bigquery_datapolicies_v2_DataMaskingPolicy_PredefinedExpression_)([PredefinedExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.PredefinedExpression.html).SHA256)
                .build();
    
        [DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html) dataPolicy =
            [DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html).newBuilder()
                .[setDataPolicyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.Builder.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_Builder_setDataPolicyType_com_google_cloud_bigquery_datapolicies_v2_DataPolicy_DataPolicyType_)([DataPolicyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.DataPolicyType.html).DATA_MASKING_POLICY)
                .[setDataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.Builder.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_Builder_setDataMaskingPolicy_com_google_cloud_bigquery_datapolicies_v2_DataMaskingPolicy_)(dataMaskingPolicy)
                .build();
    
        [CreateDataPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.CreateDataPolicyRequest.html) request =
            [CreateDataPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.CreateDataPolicyRequest.html).newBuilder()
                .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.LocationName.html#com_google_cloud_bigquery_datapolicies_v2_LocationName_toString__)())
                .setDataPolicyId(dataPolicyId)
                .setDataPolicy(dataPolicy)
                .build();
    
        try ([DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html) client = [DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html).create()) {
          [DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html) response = client.createDataPolicy(request);
    
          System.out.printf("Successfully created data policy: %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_getName__)());
          System.out.printf("Data Policy ID: %s%n", response.[getDataPolicyId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_getDataPolicyId__)());
          System.out.printf("Data Policy Type: %s%n", response.[getDataPolicyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_getDataPolicyType__)());
          if (response.[hasDataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_hasDataMaskingPolicy__)()) {
            System.out.printf(
                "Data Masking Predefined Expression: %s%n",
                response.[getDataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_getDataMaskingPolicy__)().getPredefinedExpression());
          }
        } catch ([AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html) err) {
          System.err.printf(
              "error: data policy '%s' already exists in location '%s' for project '%s': %s%n",
              dataPolicyId, location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf(
              "error: project '%s' or location '%s' was not found: %s%n",
              projectId, location, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to create data policy '%s' in location '%s' for project '%s': %s%n",
              dataPolicyId, location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const datapolicy = require('[@google-cloud/bigquery-datapolicies](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-datapolicies/latest/overview.html)');
    const {DataPolicyServiceClient} = datapolicy.v2;
    const protos = datapolicy.protos.google.cloud.bigquery.datapolicies.v2;
    const {status} = require('@grpc/grpc-js');
    
    const dataPolicyServiceClient = new [DataPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-datapolicies/latest/overview.html)();
    
    /**
     * Creates a data policy to apply a data masking rule to a specific BigQuery table column.
     * This is a primary mechanism for implementing column-level security in BigQuery.
     *
     * @param {string} projectId The Google Cloud project ID (for example, 'example-project-id')
     * @param {string} location The Google Cloud location. Example: 'us'
     * @param {string} dataPolicyId The user-assigned ID of the data policy. Example: 'example-data-policy-id'
     */
    async function createDataPolicy(projectId, location, dataPolicyId) {
      const parent = `projects/${projectId}/locations/${location}`;
    
      const dataPolicy = {
        dataPolicyType: protos.DataPolicy.DataPolicyType.DATA_MASKING_POLICY,
        dataMaskingPolicy: {
          predefinedExpression:
            protos.DataMaskingPolicy.PredefinedExpression.SHA256,
        },
      };
    
      const request = {
        parent,
        dataPolicyId,
        dataPolicy,
      };
    
      try {
        const [response] = await dataPolicyServiceClient.createDataPolicy(request);
        console.log(`Successfully created data policy: ${response.name}`);
        console.log(`Data policy ID: ${response.dataPolicyId}`);
        console.log(`Data policy type: ${response.dataPolicyType}`);
        if (response.dataMaskingPolicy) {
          console.log(
            `Data masking expression: ${response.dataMaskingPolicy.predefinedExpression}`,
          );
        }
      } catch (err) {
        if (err.code === status.ALREADY_EXISTS) {
          console.log(
            `Data policy '${dataPolicyId}' already exists in location '${location}' of project '${projectId}'.`,
          );
          console.log(
            'Consider updating the existing data policy or using a different dataPolicyId.',
          );
        } else {
          console.error('Error creating data policy:', err.message);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import bigquery_datapolicies_v2
    
    client = bigquery_datapolicies_v2.DataPolicyServiceClient()
    
    
    def create_data_policy(project_id: str, location: str, data_policy_id: str) -> None:
        """Creates a data policy to apply a data masking rule to a specific BigQuery table column.
        This is a primary mechanism for implementing column-level security in BigQuery.
    
        Args:
            project_id (str): The Google Cloud project ID.
            location (str): The geographic location of the data policy (for example, "us-central1").
            data_policy_id (str): The ID for the new data policy.
        """
    
        parent = f"projects/{project_id}/locations/{location}"
    
        # Define the data masking policy.
        # Here, we specify a SHA-256 predefined expression for data masking.
        data_masking_policy = bigquery_datapolicies_v2.DataMaskingPolicy(
            predefined_expression=bigquery_datapolicies_v2.DataMaskingPolicy.PredefinedExpression.SHA256
        )
    
        # Create the DataPolicy object.
        # We set the type to DATA_MASKING_POLICY and assign the defined masking policy.
        data_policy = bigquery_datapolicies_v2.DataPolicy(
            data_policy_type=bigquery_datapolicies_v2.DataPolicy.DataPolicyType.DATA_MASKING_POLICY,
            data_masking_policy=data_masking_policy,
        )
    
        request = bigquery_datapolicies_v2.CreateDataPolicyRequest(
            parent=parent,
            data_policy_id=data_policy_id,
            data_policy=data_policy,
        )
    
        try:
            response = client.[create_data_policy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_create_data_policy)(request=request)
            print(f"Successfully created data policy: {response.name}")
            print(f"Data Policy ID: {response.data_policy_id}")
            print(f"Data Policy Type: {response.data_policy_type.name}")
            print(
                "Data Masking Predefined Expression:"
                f" {response.data_masking_policy.predefined_expression.name}"
            )
        except exceptions.AlreadyExists as e:
            print(
                f"Error: Data policy '{data_policy_id}' already exists in project"
                f" '{project_id}' in location '{location}'. Use a unique ID or"
                " update the existing policy if needed."
            )
    
        except exceptions.NotFound as e:
            print(
                f"Error: The specified project '{project_id}' or location '{location}'"
                " was not found or is inaccessible. Make sure the project ID and"
                " location are correct and you have the necessary permissions."
            )
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
