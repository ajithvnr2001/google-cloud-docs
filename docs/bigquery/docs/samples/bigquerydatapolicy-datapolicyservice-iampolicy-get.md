---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-iampolicy-get/
title: Get the IAM policy for a data policy \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:44.658170+00:00
---

# Get the IAM policy for a data policy  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerydatapolicy-datapolicyservice-iampolicy-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get the IAM policy for a data policy Stay organized with collections  Save and categorize content based on your preferences. 

Get the IAM policy for a specified data policy resource from the BigQuery Data Policy API. This is useful for auditing which members have which roles on the policy.

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
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class GetIamPolicy {
    
      /**
       * Gets the IAM policy for a specified data policy resource from the BigQuery Data Policy API.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the data policy (for example, "us-central1").
       * @param dataPolicyId The ID of the data policy (for example, "example_data_policy").
       */
      public static void getIamPolicy(String projectId, String location, String dataPolicyId) {
        [DataPolicyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html) resourceName = [DataPolicyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html).of(projectId, location, dataPolicyId);
    
        [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request =
            [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder().setResource(resourceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyName.html#com_google_cloud_bigquery_datapolicies_v2_DataPolicyName_toString__)()).build();
    
        try ([DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html) client = [DataPolicyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerydatapolicy/latest/com.google.cloud.bigquery.datapolicies.v2.DataPolicyServiceClient.html).create()) {
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = client.getIamPolicy(request);
    
          System.out.printf("Successfully retrieved IAM policy for data policy: %s%n", resourceName);
          System.out.printf("Policy Version: %d%n", policy.[getVersion](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getVersion__)());
          if (policy.[getBindingsCount](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsCount__)() > 0) {
            System.out.println("Policy Bindings:");
            for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
              System.out.printf("  Role: %s%n", binding.getRole());
              System.out.printf("  Members: %s%n", String.join(", ", binding.getMembersList()));
              if (binding.hasCondition() && !binding.getCondition().getExpression().[isEmpty](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html#com_google_api_gax_rpc_LibraryMetadata_isEmpty__)()) {
                System.out.printf("  Condition: %s%n", binding.getCondition().getExpression());
              }
            }
          } else {
            System.out.println("No bindings found in the policy.");
          }
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf("error: data policy '%s' not found: %s%n", resourceName, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to get IAM policy for data policy '%s': %s%n",
              resourceName, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
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
     * Get the IAM policy for a specified data policy resource from the BigQuery Data Policy API.
     * This is useful for auditing which members have which roles on the policy.
     *
     *
     * @param {string} projectId Google Cloud Project ID (For example, 'example-project-id')
     * @param {string} location Google Cloud Location (For example, 'us-central1')
     * @param {string} dataPolicyId The ID of the data policy (For example, 'example-data-policy-id')
     */
    async function getIamPolicy(projectId, location, dataPolicyId) {
      const resourceName = client.dataPolicyPath(projectId, location, dataPolicyId);
    
      const request = {
        resource: resourceName,
      };
    
      try {
        const [policy] = await client.getIamPolicy(request);
        console.log(
          'Successfully retrieved IAM policy for data policy %s:',
          resourceName,
        );
        console.log(JSON.stringify(policy, null, 2));
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Error: Data Policy '${dataPolicyId}' not found in location '${location}' of project '${projectId}'. ` +
              'Make sure the data policy exists and the resource name is correct.',
          );
        } else {
          console.error(
            `Error getting IAM policy for data policy '${dataPolicyId}':`,
            err,
          );
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import bigquery_datapolicies_v2
    from google.iam.v1 import iam_policy_pb2
    
    client = bigquery_datapolicies_v2.DataPolicyServiceClient()
    
    
    def get_data_policy_iam_policy(
        project_id: str,
        location: str,
        data_policy_id: str,
    ) -> None:
        """Get the IAM policy for a specified data policy resource from the BigQuery Data Policy API.
        This is useful for auditing which members have which roles on the policy.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the data policy (for example, "us").
            data_policy_id: The ID of the data policy.
        """
    
        resource_name = client.[data_policy_path](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_data_policy_path)(
            project=project_id,
            location=location,
            data_policy=data_policy_id,
        )
    
        request = iam_policy_pb2.GetIamPolicyRequest(resource=resource_name)
    
        try:
            policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.html#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_get_iam_policy)(request=request)
    
            print(f"Successfully retrieved IAM policy for data policy: {resource_name}")
            print("Policy Version:", policy.version)
            if policy.bindings:
                print("Policy Bindings:")
                for binding in policy.bindings:
                    print(f"  Role: {binding.role}")
                    print(f"  Members: {', '.join(binding.members)}")
                    if binding.condition.expression:
                        print(f"  Condition: {binding.condition.expression}")
            else:
                print("No bindings found in the policy.")
    
        except exceptions.NotFound:
            print(f"Error: Data policy '{resource_name}' not found.")
            print("Make sure the project ID, location, and data policy ID are correct.")
        except exceptions.GoogleAPIError as e:
            print(f"An API error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
