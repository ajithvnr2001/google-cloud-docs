---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicy-update/
title: Update a data policy \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:46.039495+00:00
---

# Update a data policy  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-datapolicy-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Update a data policy Stay organized with collections  Save and categorize content based on your preferences. 

Updates the data masking configuration of an existing data policy. This example demonstrates how to use a FieldMask to selectively update the `data_masking_policy` (for example, changing the masking expression from ALWAYS_NULL to SHA256) without affecting other fields or recreating the policy.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Mask column data](https://docs.cloud.google.com/bigquery/docs/column-data-masking)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.html).[PredefinedExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.PredefinedExpression.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataPolicyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html);
    import com.google.cloud.bigquery.datapolicies.v2.[DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html);
    import com.google.cloud.bigquery.datapolicies.v2.[UpdateDataPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.UpdateDataPolicyRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateDataPolicy {
    
      /**
       * Updates the data masking configuration of an existing data policy.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the data policy (for example, "us-central1").
       * @param dataPolicyId The ID of the data policy to update (for example, "example_data_policy").
       */
      public static void updateDataPolicy(String projectId, String location, String dataPolicyId) {
        [DataPolicyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html) dataPolicyName = [DataPolicyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html).of(projectId, location, dataPolicyId);
    
        try ([DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html) client = [DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html).create()) {
          // Retrieve the existing policy so its etag can be used to prevent race conditions.
          [DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html) existingPolicy = client.getDataPolicy(dataPolicyName);
    
          [DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html) updatedDataPolicy =
              [DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html).newBuilder()
                  .setName(dataPolicyName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicyName_toString__)())
                  .[setDataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.Builder.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_Builder_setDataMaskingPolicy_com_google_cloud_bigquery_datapolicies_v2_DataMaskingPolicy_)(
                      [DataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.html).newBuilder()
                          .[setPredefinedExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.Builder.html#com_google_cloud_bigquery_datapolicies_v2_DataMaskingPolicy_Builder_setPredefinedExpression_com_google_cloud_bigquery_datapolicies_v2_DataMaskingPolicy_PredefinedExpression_)([PredefinedExpression](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.PredefinedExpression.html).SHA256)
                          .build())
                  .[setEtag](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.Builder.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_Builder_setEtag_java_lang_String_)(existingPolicy.[getEtag](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_getEtag__)())
                  .build();
    
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("data_masking_policy").build();
    
          [UpdateDataPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.UpdateDataPolicyRequest.html) request =
              [UpdateDataPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.UpdateDataPolicyRequest.html).newBuilder()
                  .setDataPolicy(updatedDataPolicy)
                  .[setUpdateMask](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.UpdateDataPolicyRequest.Builder.html#com_google_cloud_bigquery_datapolicies_v2_UpdateDataPolicyRequest_Builder_setUpdateMask_com_google_protobuf_FieldMask_)(updateMask)
                  .build();
    
          [DataPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html) response = client.updateDataPolicy(request);
    
          System.out.printf("Successfully updated data policy: %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_getName__)());
          System.out.printf("New data policy type: %s%n", response.[getDataPolicyType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_getDataPolicyType__)());
          if (response.[hasDataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_hasDataMaskingPolicy__)()) {
            System.out.printf(
                "New masking expression: %s%n",
                response.[getDataMaskingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicy.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicy_getDataMaskingPolicy__)().getPredefinedExpression());
          }
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf(
              "error: data policy '%s' not found: %s%n", dataPolicyName, err.getMessage());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to update data policy '%s': %s%n", dataPolicyName, err.getMessage());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const datapolicy = require('[@google-cloud/bigquery-datapolicies](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-datapolicies/latest/overview.html)');
    const {DataPolicyServiceClient} = datapolicy.v2;
    const protos = datapolicy.protos.google.cloud.bigquery.datapolicies.v2;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [DataPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-datapolicies/latest/overview.html)();
    
    /**
     * Updates the data masking configuration of an existing data policy.
     * This example demonstrates how to use a FieldMask to selectively update the
     * `data_masking_policy` (for example, changing the masking expression from
     * ALWAYS_NULL to SHA256) without affecting other fields or recreating the policy.
     *
     * @param {string} projectId The Google Cloud project ID (For example, 'example-project-id').
     * @param {string} location The location of the data policy (For example, 'us').
     * @param {string} dataPolicyId The ID of the data policy to update (For example, 'example-data-policy-id').
     */
    async function updateDataPolicy(projectId, location, dataPolicyId) {
      const resourceName = client.dataPolicyPath(projectId, location, dataPolicyId);
    
      const getRequest = {
        name: resourceName,
      };
    
      try {
        // To prevent race conditions, use the policy's etag in the update.
        const [currentDataPolicy] = await client.getDataPolicy(getRequest);
        const currentETag = currentDataPolicy.etag;
    
        // This example transitions a masking rule from ALWAYS_NULL to SHA256.
        const dataPolicy = {
          name: resourceName,
          etag: currentETag,
          dataMaskingPolicy: {
            predefinedExpression:
              protos.DataMaskingPolicy.PredefinedExpression.SHA256,
          },
        };
    
        // Use a field mask to selectively update only the data masking policy.
        const updateMask = {
          paths: ['data_masking_policy'],
        };
    
        const request = {
          dataPolicy,
          updateMask,
        };
    
        const [response] = await client.updateDataPolicy(request);
        console.log(`Successfully updated data policy: ${response.name}`);
        console.log(
          `New masking expression: ${response.dataMaskingPolicy.predefinedExpression}`,
        );
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Error: Data policy '${resourceName}' not found. ` +
              'Make sure the data policy exists and the project, location, and data policy ID are correct.',
          );
        } else {
          console.error('Error updating data policy:', err.message, err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import bigquery_datapolicies_v2
    from google.protobuf import field_mask_pb2
    
    client = bigquery_datapolicies_v2.DataPolicyServiceClient()
    
    
    def update_data_policy(project_id: str, location: str, data_policy_id: str) -> None:
        """Updates the data masking configuration of an existing data policy.
    
        This example demonstrates how to use a FieldMask to selectively update the
        `data_masking_policy` (for example, changing the masking expression from
        ALWAYS_NULL to SHA256) without affecting other fields or recreating the policy.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location (for example, "us") of the data policy.
            data_policy_id: The ID of the data policy to update.
        """
    
        data_policy_name = client.[data_policy_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_data_policy_path)(
            project=project_id,
            location=location,
            data_policy=data_policy_id,
        )
    
        # To prevent race conditions, use the policy's etag in the update.
        existing_policy = client.[get_data_policy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_get_data_policy)(name=data_policy_name)
    
        # This example transitions a masking rule from ALWAYS_NULL to SHA256.
        updated_data_policy = bigquery_datapolicies_v2.DataPolicy(
            name=data_policy_name,
            data_masking_policy=bigquery_datapolicies_v2.DataMaskingPolicy(
                predefined_expression=bigquery_datapolicies_v2.DataMaskingPolicy.PredefinedExpression.SHA256
            ),
            etag=existing_policy.etag,
        )
    
        # Use a field mask to selectively update only the data masking policy.
        update_mask = field_mask_pb2.FieldMask(paths=["data_masking_policy"])
        request = bigquery_datapolicies_v2.UpdateDataPolicyRequest(
            data_policy=updated_data_policy,
            update_mask=update_mask,
        )
    
        try:
            response = client.[update_data_policy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_update_data_policy)(request=request)
            print(f"Successfully updated data policy: {response.name}")
            print(f"New data policy type: {response.data_policy_type.name}")
            if response.data_masking_policy:
                print(
                    f"New masking expression: {response.data_masking_policy.predefined_expression.name}"
                )
        except exceptions.NotFound:
            print(f"Error: Data policy '{data_policy_name}' not found.")
            print("Make sure the data policy ID and location are correct.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
