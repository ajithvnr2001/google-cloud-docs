---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryconnection-connectionservice-iampolicy-get/
title: Get a connection's IAM policy \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:12.074738+00:00
---

# Get a connection's IAM policy  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryconnection-connectionservice-iampolicy-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Get a connection's IAM policy Stay organized with collections  Save and categorize content based on your preferences. 

Get the current Identity and Access Management (IAM) policy for a BigQuery connection. The policy defines which principals have what permissions on the connection resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage connections](https://docs.cloud.google.com/bigquery/docs/working-with-connections)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.connection.v1.[ConnectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html);
    import com.google.cloud.bigqueryconnection.v1.[ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class GetIamPolicy {
    
      /**
       * Retrieves the IAM policy of a specified BigQuery connection.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the connection (for example, "us-central1").
       * @param connectionId The ID of the connection (for example, "example-connection-id").
       */
      public static void getIamPolicy(
          String projectId, String location, String connectionId) {
        [ConnectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html) resource = [ConnectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html).of(projectId, location, connectionId);
    
        [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request =
            [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder().setResource(resource.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html#com_google_cloud_bigquery_connection_v1_ConnectionName_toString__)()).build();
    
        try ([ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html) client = [ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html).create()) {
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = client.getIamPolicy(request);
    
          System.out.printf("Successfully retrieved IAM policy for connection: %s%n", resource);
          if (policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)().[isEmpty](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html#com_google_api_gax_rpc_LibraryMetadata_isEmpty__)()) {
            System.out.println("Policy is empty and has no bindings.");
          }
    
          for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
            System.out.printf("Role: %s%n", binding.getRole());
            System.out.println("Members:");
            for (String member : binding.getMembersList()) {
              System.out.printf("  - %s%n", member);
            }
          }
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf(
              "error: connection '%s' not found in location '%s' for project '%s': %s%n",
              connectionId, location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to get IAM policy for connection '%s' in location '%s' for project '%s': %s%n",
              connectionId, location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ConnectionServiceClient} =
      require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
    /**
     * Gets the IAM policy for a BigQuery connection.
     * @param {string} projectId Google Cloud project ID (for example, 'example-project-id').
     * @param {string} location The location of the connection (for example, 'us').
     * @param {string} connectionId The connection ID (for example, 'example-connection').
     */
    async function getIamPolicy(projectId, location, connectionId) {
    
      const resource = client.connectionPath(projectId, location, connectionId);
    
      const request = {
        resource,
      };
    
      try {
    
        const [policy] = await client.getIamPolicy(request);
    
        console.log(
          `Successfully retrieved IAM policy for connection: ${connectionId}`,
        );
    
        if (policy.bindings && policy.bindings.length > 0) {
          console.log('Bindings:');
          policy.bindings.forEach(binding => {
            console.log(`  Role: ${binding.role}`);
            console.log('  Members:');
            binding.members.forEach(member => {
              console.log(`    - ${member}`);
            });
          });
        } else {
          console.log('No policy bindings found.');
        }
      } catch (err) {
    
        if (err.code === status.NOT_FOUND) {
          console.log(
            `Connection '${connectionId}' not found in project '${projectId}' at location '${location}'.`,
          );
        } else {
          console.error('An error occurred while getting the IAM policy:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    
    client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html)()
    
    
    def get_connection_iam_policy(
        project_id: str,
        location: str,
        connection_id: str,
    ):
        """Gets the IAM policy of a connection.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the connection (for example, "us").
            connection_id: The ID of the connection.
        """
    
        resource = client.[connection_path](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceClient_connection_path)(project_id, location, connection_id)
    
        try:
            policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceClient_get_iam_policy)(resource=resource)
    
            print(f"Successfully retrieved IAM policy for connection: {resource}")
            if not policy.bindings:
                print("This policy is empty and has no bindings.")
    
            for binding in policy.bindings:
                print(f"Role: {binding.role}")
                print("Members:")
                for member in binding.members:
                    print(f"    - {member}")
    
        except google.api_core.exceptions.NotFound:
            print(f"Connection not found: {resource}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
