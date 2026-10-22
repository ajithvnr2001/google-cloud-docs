---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryconnection-connectionservice-connection-update/
title: Update a BigQuery connection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:03.192335+00:00
---

# Update a BigQuery connection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryconnection-connectionservice-connection-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Update a BigQuery connection Stay organized with collections  Save and categorize content based on your preferences. 

Updates the friendly name or description for an existing BigQuery connection. This method uses a field mask to specify which fields to change.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage connections](https://docs.cloud.google.com/bigquery/docs/working-with-connections)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.connection.v1.[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.html);
    import com.google.cloud.bigquery.connection.v1.[ConnectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html);
    import com.google.cloud.bigquery.connection.v1.[UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.UpdateConnectionRequest.html);
    import com.google.cloud.bigqueryconnection.v1.[ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateConnection {
    
      /**
       * Updates a BigQuery connection's friendly name and description.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the connection (for example, "us-central1").
       * @param connectionId The ID of the connection to update (for example, "example-connection-id").
       */
      public static void updateConnection(String projectId, String location, String connectionId) {
        [ConnectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html) name = [ConnectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html).of(projectId, location, connectionId);
    
        [Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.html) connection =
            [Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.html).newBuilder()
                .[setFriendlyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.Builder.html#com_google_cloud_bigquery_connection_v1_Connection_Builder_setFriendlyName_java_lang_String_)("Example Updated BigQuery Connection")
                .[setDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.Builder.html#com_google_cloud_bigquery_connection_v1_Connection_Builder_setDescription_java_lang_String_)("Updated description for the connection.")
                .build();
    
        // Specify only metadata fields in the FieldMask so existing credentials are not reset.
        [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask =
            [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("friendly_name").[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("description").build();
    
        [UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.UpdateConnectionRequest.html) request =
            [UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.UpdateConnectionRequest.html).newBuilder()
                .setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionName.html#com_google_cloud_bigquery_connection_v1_ConnectionName_toString__)())
                .setConnection(connection)
                .[setUpdateMask](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.UpdateConnectionRequest.Builder.html#com_google_cloud_bigquery_connection_v1_UpdateConnectionRequest_Builder_setUpdateMask_com_google_protobuf_FieldMask_)(updateMask)
                .build();
    
        try ([ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html) client = [ConnectionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient.html).create()) {
          [Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.html) response = client.updateConnection(request);
    
          System.out.printf("Connection '%s' updated successfully.%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.html#com_google_cloud_bigquery_connection_v1_Connection_getName__)());
          System.out.printf("Friendly Name: %s%n", response.[getFriendlyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.html#com_google_cloud_bigquery_connection_v1_Connection_getFriendlyName__)());
          System.out.printf("Description: %s%n", response.[getDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.html#com_google_cloud_bigquery_connection_v1_Connection_getDescription__)());
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf(
              "error: connection '%s' not found in location '%s' for project '%s': %s%n",
              connectionId, location, projectId, err.getMessage());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to update connection '%s' in location '%s' for project '%s': %s%n",
              connectionId, location, projectId, err.getMessage());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ConnectionServiceClient} =
      require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
    /**
     * Updates a BigQuery connection, demonstrating how to update the friendly name and description.
     *
     * @param {string} projectId The Google Cloud project ID. for example, 'example-project-id'
     * @param {string} location The location of the connection. for example, 'us-central1'
     * @param {string} connectionId The ID of the connection to update. for example, 'example-connection-id'
     */
    async function updateConnection(projectId, location, connectionId) {
      const name = connectionClient.connectionPath(
        projectId,
        location,
        connectionId,
      );
    
      const connection = {
        friendlyName: 'Example Updated Connection',
        description: 'A new description for the connection',
      };
    
      const updateMask = {
        paths: ['friendly_name', 'description'],
      };
    
      const request = {
        name,
        connection,
        updateMask,
      };
    
      try {
        const [response] = await connectionClient.updateConnection(request);
    
        console.log(`Connection updated: ${response.name}`);
        console.log(`  Friendly name: ${response.friendlyName}`);
        console.log(`  Description: ${response.description}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(`Connection not found: ${name}`);
        } else {
          console.error(`Error updating connection ${name}:`, err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    from google.protobuf import field_mask_pb2
    
    client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html)()
    
    
    def update_connection(project_id: str, location: str, connection_id: str):
        """Updates a BigQuery connection's friendly name and description.
    
        For security reasons, updating connection properties also resets the
        credential. The `update_mask` specifies which fields of the connection
        to update. This sample only updates metadata fields to avoid resetting
        credentials.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the connection (for example, "us-central1").
            connection_id: The ID of the connection to update.
        """
    
        connection_name = client.[connection_path](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceClient_connection_path)(project_id, location, connection_id)
    
        connection = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[Connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.Connection.html)(
            friendly_name="Example Updated BigQuery Connection",
            description="This is an updated description for the connection.",
        )
    
        update_mask = field_mask_pb2.FieldMask(paths=["friendly_name", "description"])
    
        try:
            response = client.[update_connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceClient_update_connection)(
                name=connection_name,
                connection=connection,
                update_mask=update_mask,
            )
    
            print(f"Connection '{response.name}' updated successfully.")
            print(f"Friendly Name: {response.friendly_name}")
            print(f"Description: {response.description}")
    
        except google.api_core.exceptions.NotFound:
            print(f"Connection '{connection_name}' not found. Please create it first.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
