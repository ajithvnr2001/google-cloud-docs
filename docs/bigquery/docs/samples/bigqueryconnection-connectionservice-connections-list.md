---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryconnection-connectionservice-connections-list/
title: List connections \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:05.512764+00:00
---

# List connections  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryconnection-connectionservice-connections-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  List connections Stay organized with collections  Save and categorize content based on your preferences. 

Lists all BigQuery connections defined in a specific Google Cloud project and location.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage connections](https://docs.cloud.google.com/bigquery/docs/working-with-connections)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html);
    import com.google.cloud.bigquery.connection.v1.[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.html);
    import com.google.cloud.bigquery.connection.v1.[ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ListConnectionsRequest.html);
    import com.google.cloud.bigquery.connection.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.LocationName.html);
    import com.google.cloud.bigqueryconnection.v1.[ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html);
    import java.io.IOException;
    
    public class ListConnections {
    
      /**
       * Lists all BigQuery connections in a given project and location.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the connections (for example, "us-central1").
       */
      public static void listConnections(String projectId, String location) {
        [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.LocationName.html).of(projectId, location);
    
        [ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ListConnectionsRequest.html) request =
            [ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ListConnectionsRequest.html).newBuilder().setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.LocationName.html#com_google_cloud_bigquery_connection_v1_LocationName_toString__)()).[setPageSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ListConnectionsRequest.Builder.html#com_google_cloud_bigquery_connection_v1_ListConnectionsRequest_Builder_setPageSize_int_)(100).build();
    
        try ([ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html) client = [ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html).create()) {
          System.out.printf(
              "Listing connections in project '%s' and location '%s':%n", projectId, location);
    
          for ([Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.html) connection : client.listConnections(request).iterateAll()) {
            System.out.printf("Connection Name: %s%n", connection.getName());
            System.out.printf("Friendly Name: %s%n", connection.getFriendlyName());
            System.out.printf("Has Credential: %b%n", connection.getHasCredential());
          }
    
          System.out.println("Finished listing connections.");
        } catch ([InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html) err) {
          System.err.printf(
              "error: invalid argument listing connections in location '%s' for project '%s': %s%n",
              location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to list connections in location '%s' for project '%s': %s%n",
              location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)');
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
    /**
     * Lists BigQuery connections in a given project and location.
     *
     * @param {string} projectId The Google Cloud project ID. for example, 'example-project-id'
     * @param {string} location The location to list connections for. for example, 'us-central1'
     */
    async function listConnections(projectId, location) {
      const parent = client.locationPath(projectId, location);
    
      const request = {
        parent,
        pageSize: 100,
      };
    
      try {
        const [connections] = await client.listConnections(request, {
          autoPaginate: false,
        });
    
        if (connections.length === 0) {
          console.log(
            `No connections found in ${location} for project ${projectId}.`,
          );
          return;
        }
    
        console.log('Connections:');
        for (const connection of connections) {
          console.log(`  Name: ${connection.name}`);
          console.log(`  Friendly Name: ${connection.friendlyName}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(
            `Project '${projectId}' or location '${location}' not found.`,
          );
        } else {
          console.error('Error listing connections:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    
    
    def list_connections(project_id: str, location: str):
        """Prints all connections in a given project and location.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the connections (for example, "us", "us-central1").
        """
        client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html)()
    
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceClient_common_location_path)(project_id, location)
    
        request = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ListConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.ListConnectionsRequest.html)(
            parent=parent,
            page_size=100,
        )
    
        print(f"Listing connections in project '{project_id}' and location '{location}':")
    
        try:
            for connection in client.[list_connections](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceClient_list_connections)(request=request):
                print(f"Connection ID: {connection.name.split('/')[-1]}")
                print(f"Friendly Name: {connection.friendly_name}")
                print(f"Has Credential: {connection.has_credential}")
                print("-" * 20)
    
            print("Finished listing connections.")
    
        except google.api_core.exceptions.InvalidArgument as e:
            print(
                f"Could not list connections. Please check that the project ID '{project_id}' "
                f"and location '{location}' are correct. Details: {e}"
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
