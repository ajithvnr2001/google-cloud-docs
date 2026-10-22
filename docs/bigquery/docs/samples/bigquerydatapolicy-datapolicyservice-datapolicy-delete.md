---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicy-delete/
title: Delete a data policy \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:44.323239+00:00
---

# Delete a data policy  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicy-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Delete a data policy Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a data policy from the BigQuery Data Policy API, which is identified by its project ID, location, and data policy ID.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Mask column data](https://docs.cloud.google.com/bigquery/docs/column-data-masking)
  * [Restrict access with column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataPolicyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html);
    import java.io.IOException;
    
    public class DeleteDataPolicy {
    
      /**
       * Deletes a data policy from the BigQuery Data Policy API.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the data policy (for example, "us-central1").
       * @param dataPolicyId The ID of the data policy to delete (for example, "example_data_policy").
       */
      public static void deleteDataPolicy(String projectId, String location, String dataPolicyId) {
        [DataPolicyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html) name = [DataPolicyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html).of(projectId, location, dataPolicyId);
    
        try ([DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html) client = [DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html).create()) {
          client.deleteDataPolicy(name);
          System.out.printf("Successfully deleted data policy: %s%n", name);
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf(
              "error: data policy '%s' not found: %s%n", name, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to delete data policy '%s': %s%n", name, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {DataPolicyServiceClient} =
      require('[@google-cloud/bigquery-datapolicies](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-datapolicies/latest/overview.html)').v2;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-datapolicies/latest/overview.html)();
    
    /**
     * Deletes a data policy from the BigQuery Data Policy API, which is identified by its project ID, location, and data policy ID.
     *
     * @param {string} projectId The Google Cloud project ID.
     * @param {string} location The Google Cloud location (For example, 'us').
     * @param {string} dataPolicyId The ID of the data policy to delete (For example, 'example-data-policy').
     */
    async function deleteDataPolicy(projectId, location, dataPolicyId) {
      const name = client.dataPolicyPath(projectId, location, dataPolicyId);
    
      const request = {
        name,
      };
    
      try {
        await client.deleteDataPolicy(request);
        console.log(`Successfully deleted data policy: ${name}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Data policy ${name} not found. Make sure the data policy ID and location are correct.`,
          );
        } else {
          console.error(`Error deleting data policy ${name}:`, err.message);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions as core_exceptions
    from google.cloud import bigquery_datapolicies_v2
    
    client = bigquery_datapolicies_v2.DataPolicyServiceClient()
    
    
    def delete_data_policy(project_id: str, location: str, data_policy_id: str) -> None:
        """Deletes a data policy from the BigQuery Data Policy APIs.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The location of the data policy (for example, "us").
            data_policy_id: The ID of the data policy to delete.
        """
    
        name = client.[data_policy_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_data_policy_path)(
            project=project_id, location=location, data_policy=data_policy_id
        )
    
        try:
            client.[delete_data_policy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_delete_data_policy)(name=name)
            print(f"Successfully deleted data policy: {name}")
        except core_exceptions.NotFound:
            print(f"Data policy '{name}' not found. It may have already been deleted.")
        except Exception as e:
            print(f"Error deleting data policy '{name}': {e}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
