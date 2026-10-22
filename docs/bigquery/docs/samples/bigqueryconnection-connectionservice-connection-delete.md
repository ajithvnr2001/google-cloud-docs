---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryconnection-connectionservice-connection-delete/
title: Delete a BigQuery connection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:06.885980+00:00
---

# Delete a BigQuery connection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryconnection-connectionservice-connection-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Delete a BigQuery connection Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a specified BigQuery connection.

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
    import java.io.IOException;
    
    public class DeleteConnection {
    
      /**
       * Deletes a specified BigQuery connection.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the connection (for example, "us-central1").
       * @param connectionId The ID of the connection to delete (for example, "example-connection-id").
       */
      public static void deleteConnection(String projectId, String location, String connectionId) {
        [ConnectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html) name = [ConnectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html).of(projectId, location, connectionId);
    
        try ([ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html) client = [ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html).create()) {
          client.deleteConnection(name);
          System.out.printf("Connection '%s' was deleted.%n", connectionId);
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf(
              "error: connection '%s' not found in location '%s' for project '%s': %s%n",
              connectionId, location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to delete connection '%s' in location '%s' for project '%s': %s%n",
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
     * Deletes a connection and its associated credentials.
     *
     * @param {string} projectId Google Cloud project ID (for example, 'example-project-id').
     * @param {string} location The location where the connection resides (for example, 'us-central1').
     * @param {string} connectionId The ID of the connection to delete (for example, 'example-connection').
     */
    async function deleteConnection(projectId, location, connectionId) {
      const request = {
        name: client.connectionPath(projectId, location, connectionId),
      };
    
      try {
        await client.deleteConnection(request);
        console.log(`Connection ${connectionId} deleted successfully.`);
      } catch (error) {
        if (error.code === status.NOT_FOUND) {
          console.log(
            `Connection ${connectionId} does not exist in location ${location} of project ${projectId}.`,
          );
        } else {
          console.error(`Error deleting connection ${connectionId}:`, error);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    
    client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html)()
    
    
    def delete_connection(project_id: str, location: str, connection_id: str):
        """Deletes a BigQuery connection.
    
        Args:
            project_id: The Google Cloud project ID.
            location: Location of the connection (for example, "us-central1").
            connection_id: ID of the connection to delete.
        """
        name = client.[connection_path](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceClient_connection_path)(project_id, location, connection_id)
    
        try:
            client.[delete_connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceClient_delete_connection)(name=name)
            print(f"Connection '{connection_id}' was deleted.")
        except google.api_core.exceptions.NotFound:
            print(f"Connection '{connection_id}' not found.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
