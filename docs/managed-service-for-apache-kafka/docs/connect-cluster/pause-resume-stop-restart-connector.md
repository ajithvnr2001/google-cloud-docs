---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/pause-resume-stop-restart-connector/
title: Pause, resume, stop, and restart a connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:40.734336+00:00
---

# Pause, resume, stop, and restart a connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/pause-resume-stop-restart-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Pause, resume, stop, and restart a connector Stay organized with collections  Save and categorize content based on your preferences. 

You can control the operation of a connector by pausing, resuming, stopping, or restarting it. These actions allow you to manage data flow and address issues without deleting and recreating the connector.

To pause, resume, stop, or restart a connector in a Connect cluster, you can use the Google Cloud console, the gcloud CLI, the Managed Service for Apache Kafka client library, or the Managed Kafka API. You can't use the open source Apache Kafka API to change connector states.

## Required roles and permissions to pause, resume, stop, or restart a connector

To get the permissions that you need to pause, resume, stop, or restart a connector, ask your administrator to grant you the [Managed Kafka Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`) IAM role on the project containing the Connect cluster. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to pause, resume, stop, or restart a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to pause, resume, stop, or restart a connector:

  * Grant the pause connector permission on the requested connector: `managedkafka.connectors.pause`
  * Grant the resume connector permission on the requested connector: `managedkafka.connectors.resume`
  * Grant the restart connector permission on the requested connector: `managedkafka.connectors.restart`
  * Grant the stop connector permission on the requested connector: `managedkafka.connectors.stop`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Pause a connector

When you pause a connector, its state is preserved. This means the connector remembers where it left off in processing messages or data. Message processing is halted until the connector is resumed. You can resume a paused connector, and it continues from where it was paused. This is useful for troubleshooting or performing maintenance without losing the connector's setup.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster that hosts the connector you want to pause.

The **Connect cluster details** page is displayed.

  3. On the **Resources** tab, find the connector in the list and click its name.

You are redirected to the **Connector details** page.

  4. Click **Pause**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connectors pause`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/pause) command to pause a connector:
         
         gcloud managed-kafka connectors pause CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID
         

Replace the following:

     * CONNECTOR_ID: Required. The ID of the connector you want to pause.
     * LOCATION: Required. The location of the [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) containing the connector.
     * CONNECT_CLUSTER_ID: Required. The ID of the Connect cluster containing the connector.



### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func pauseConnector(w io.Writer, projectID, region, connectClusterID, connectorID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "my-connector"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	connectorPath := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s/connectors/%s", projectID, region, connectClusterID, connectorID)
    	req := &managedkafkapb.PauseConnectorRequest{
    		Name: connectorPath,
    	}
    	resp, err := client.PauseConnector(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.PauseConnector got err: %w", err)
    	}
    	fmt.Fprintf(w, "Paused connector: %#v\n", resp)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import com.google.cloud.managedkafka.v1.[PauseConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.PauseConnectorRequest.html);
    import java.io.IOException;
    
    public class PauseConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String connectClusterId = "my-connect-cluster";
        String connectorId = "my-connector";
        pauseConnector(projectId, region, connectClusterId, connectorId);
      }
    
      public static void pauseConnector(
          String projectId, String region, String connectClusterId, String connectorId)
          throws Exception {
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = 
            [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html) connectorName = [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html).of(projectId, region, connectClusterId, 
              connectorId);
          [PauseConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.PauseConnectorRequest.html) request = [PauseConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.PauseConnectorRequest.html).newBuilder()
              .setName(connectorName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html#com_google_cloud_managedkafka_v1_ConnectorName_toString__)()).build();
    
          // This operation is being handled synchronously.
          managedKafkaConnectClient.pauseConnector(request);
          System.out.printf("Connector %s paused successfully.\n", connectorId);
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.pauseConnector got err: %s\n", 
              e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import (
        [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html),
    )
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    # connector_id = "my-connector"
    
    connect_client = ManagedKafkaConnectClient()
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[PauseConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.PauseConnectorRequest.html)(
        name=connect_client.[connector_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connector_path)(project_id, region, connect_cluster_id, connector_id),
    )
    
    try:
        operation = connect_client.[pause_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_pause_connector)(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        operation.result()
        print(f"Paused connector {connector_id}")
    except GoogleAPICallError as e:
        print(f"Failed to pause connector {connector_id} with error: {e}")
    

## Resume a connector

Resuming a paused connector restarts its operation from where it left off.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster that hosts the connector you want to resume.

The **Connect cluster details** page is displayed.

  3. On the **Resources** tab, find the paused connector in the list and click its name.

You are redirected to the **Connector details** page.

  4. Click **Resume**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connectors resume`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/resume) command to resume a connector:
         
         gcloud managed-kafka connectors resume CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID
         

Replace the following:

     * CONNECTOR_ID: Required. The ID of the connector you want to resume.
     * LOCATION: Required. The location of the [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) containing the connector.
     * CONNECT_CLUSTER_ID: Required. The ID of the Connect cluster containing the connector.



### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func resumeConnector(w io.Writer, projectID, region, connectClusterID, connectorID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "my-connector"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	connectorPath := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s/connectors/%s", projectID, region, connectClusterID, connectorID)
    	req := &managedkafkapb.ResumeConnectorRequest{
    		Name: connectorPath,
    	}
    	resp, err := client.ResumeConnector(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.ResumeConnector got err: %w", err)
    	}
    	fmt.Fprintf(w, "Resumed connector: %#v\n", resp)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import com.google.cloud.managedkafka.v1.[ResumeConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ResumeConnectorRequest.html);
    import java.io.IOException;
    
    public class ResumeConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String connectClusterId = "my-connect-cluster";
        String connectorId = "my-connector";
        resumeConnector(projectId, region, connectClusterId, connectorId);
      }
    
      public static void resumeConnector(
          String projectId, String region, String connectClusterId, String connectorId)
          throws Exception {
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = 
            [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html) connectorName = [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html).of(projectId, region, connectClusterId, 
              connectorId);
          [ResumeConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ResumeConnectorRequest.html) request = [ResumeConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ResumeConnectorRequest.html).newBuilder()
              .setName(connectorName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html#com_google_cloud_managedkafka_v1_ConnectorName_toString__)()).build();
    
          // This operation is being handled synchronously.
          managedKafkaConnectClient.resumeConnector(request);
          System.out.printf("Connector %s resumed successfully.\n", connectorId);
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.resumeConnector got err: %s\n", 
              e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import (
        [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html),
    )
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    # connector_id = "my-connector"
    
    connect_client = ManagedKafkaConnectClient()
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[ResumeConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ResumeConnectorRequest.html)(
        name=connect_client.[connector_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connector_path)(project_id, region, connect_cluster_id, connector_id),
    )
    
    try:
        operation = connect_client.[resume_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_resume_connector)(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        operation.result()
        print(f"Resumed connector {connector_id}")
    except GoogleAPICallError as e:
        print(f"Failed to resume connector {connector_id} with error: {e}")
    

## Stop a connector

Stopping a connector stops all tasks of the connector. Stopping a connector preserves its state. To get the connector running again, you restart the connector. The logs and metrics are also stored durably.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster that hosts the connector you want to stop.

The **Connect cluster details** page is displayed.

  3. On the **Resources** tab, find the connector in the list and click its name.

You are redirected to the **Connector details** page.

  4. Click **Stop**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connectors stop`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/stop) command to stop a connector:
         
         gcloud managed-kafka connectors stop CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID
         

Replace the following:

     * CONNECTOR_ID: Required. The ID of the connector you want to stop.
     * LOCATION: Required. The location of the [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) containing the connector.
     * CONNECT_CLUSTER_ID: Required. The ID of the Connect cluster containing the connector.



### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func stopConnector(w io.Writer, projectID, region, connectClusterID, connectorID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "my-connector"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	connectorPath := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s/connectors/%s", projectID, region, connectClusterID, connectorID)
    	req := &managedkafkapb.StopConnectorRequest{
    		Name: connectorPath,
    	}
    	resp, err := client.StopConnector(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.StopConnector got err: %w", err)
    	}
    	fmt.Fprintf(w, "Stopped connector: %#v\n", resp)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import com.google.cloud.managedkafka.v1.[StopConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.StopConnectorRequest.html);
    import java.io.IOException;
    
    public class StopConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String connectClusterId = "my-connect-cluster";
        String connectorId = "my-connector";
        stopConnector(projectId, region, connectClusterId, connectorId);
      }
    
      public static void stopConnector(
          String projectId, String region, String connectClusterId, String connectorId)
          throws Exception {
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = 
            [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html) connectorName = [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html).of(projectId, region, connectClusterId, 
              connectorId);
          [StopConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.StopConnectorRequest.html) request = [StopConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.StopConnectorRequest.html).newBuilder()
              .setName(connectorName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html#com_google_cloud_managedkafka_v1_ConnectorName_toString__)()).build();
    
          // This operation is being handled synchronously.
          managedKafkaConnectClient.stopConnector(request);
          System.out.printf("Connector %s stopped successfully.\n", connectorId);
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.stopConnector got err: %s\n", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import (
        [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html),
    )
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    # connector_id = "my-connector"
    
    connect_client = ManagedKafkaConnectClient()
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[StopConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.StopConnectorRequest.html)(
        name=connect_client.[connector_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connector_path)(project_id, region, connect_cluster_id, connector_id),
    )
    
    try:
        operation = connect_client.[stop_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_stop_connector)(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        operation.result()
        print(f"Stopped connector {connector_id}")
    except GoogleAPICallError as e:
        print(f"Failed to stop connector {connector_id} with error: {e}")
    

## Restart a connector

Restarting a connector completely stops and then restarts its tasks. This can be useful for refreshing the connector's state or applying configuration changes.

**Note:** Restarting a connector might cause a brief interruption in data flow.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster that hosts the connector you want to restart.

The **Connect cluster details** page is displayed.

  3. On the **Resources** tab, find the connector in the list and click its name.

You are redirected to the **Connector details** page.

  4. Click **Restart**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud managed-kafka connectors restart`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/restart) command to restart a connector:
         
         gcloud managed-kafka connectors restart CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID
         

Replace the following:

     * CONNECTOR_ID: Required. The ID of the connector you want to restart.
     * LOCATION: Required. The location of the [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) containing the connector.
     * CONNECT_CLUSTER_ID: Required. The ID of the Connect cluster containing the connector.



### Go

Before trying this sample, follow the Go setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/managedkafka/latest/apiv1).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials(ADC). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/managedkafka/apiv1/managedkafkapb"
    	"google.golang.org/api/option"
    
    	managedkafka "cloud.google.com/go/managedkafka/apiv1"
    )
    
    func restartConnector(w io.Writer, projectID, region, connectClusterID, connectorID string, opts ...option.ClientOption) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// connectClusterID := "my-connect-cluster"
    	// connectorID := "my-connector"
    	ctx := context.Background()
    	client, err := managedkafka.NewManagedKafkaConnectClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("managedkafka.NewManagedKafkaConnectClient got err: %w", err)
    	}
    	defer client.Close()
    
    	connectorPath := fmt.Sprintf("projects/%s/locations/%s/connectClusters/%s/connectors/%s", projectID, region, connectClusterID, connectorID)
    	req := &managedkafkapb.RestartConnectorRequest{
    		Name: connectorPath,
    	}
    	resp, err := client.RestartConnector(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.RestartConnector got err: %w", err)
    	}
    	fmt.Fprintf(w, "Restarted connector: %#v\n", resp)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/overview).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.managedkafka.v1.[ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html);
    import com.google.cloud.managedkafka.v1.[ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html);
    import com.google.cloud.managedkafka.v1.[RestartConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RestartConnectorRequest.html);
    import java.io.IOException;
    
    public class RestartConnector {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the example.
        String projectId = "my-project-id";
        String region = "my-region"; // e.g. us-east1
        String connectClusterId = "my-connect-cluster";
        String connectorId = "my-connector";
        restartConnector(projectId, region, connectClusterId, connectorId);
      }
    
      public static void restartConnector(
          String projectId, String region, String connectClusterId, String connectorId)
          throws Exception {
        try ([ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html) managedKafkaConnectClient = 
            [ManagedKafkaConnectClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ManagedKafkaConnectClient.html).create()) {
          [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html) connectorName = [ConnectorName](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html).of(projectId, region, connectClusterId, 
              connectorId);
          [RestartConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RestartConnectorRequest.html) request = [RestartConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.RestartConnectorRequest.html).newBuilder()
              .setName(connectorName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-managedkafka/latest/com.google.cloud.managedkafka.v1.ConnectorName.html#com_google_cloud_managedkafka_v1_ConnectorName_toString__)()).build();
    
          // This operation is being handled synchronously.
          managedKafkaConnectClient.restartConnector(request);
          System.out.printf("Connector %s restarted successfully.\n", connectorId);
        } catch (IOException | [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
          System.err.printf("managedKafkaConnectClient.restartConnector got err: %s\n", 
              e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in [ Install the client libraries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/libraries#install). For more information, see the [ Managed Service for Apache Kafka Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).

To authenticate to Managed Service for Apache Kafka, set up Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.api_core.exceptions import GoogleAPICallError
    from google.cloud.managedkafka_v1.services.managed_kafka_connect import (
        [ManagedKafkaConnectClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html),
    )
    from google.cloud import [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest)
    
    # TODO(developer)
    # project_id = "my-project-id"
    # region = "us-central1"
    # connect_cluster_id = "my-connect-cluster"
    # connector_id = "my-connector"
    
    connect_client = ManagedKafkaConnectClient()
    
    request = [managedkafka_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest).[RestartConnectorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.RestartConnectorRequest.html)(
        name=connect_client.[connector_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_connector_path)(project_id, region, connect_cluster_id, connector_id),
    )
    
    try:
        operation = connect_client.[restart_connector](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.services.managed_kafka_connect.ManagedKafkaConnectClient.html#google_cloud_managedkafka_v1_services_managed_kafka_connect_ManagedKafkaConnectClient_restart_connector)(request=request)
        print(f"Waiting for operation {operation.operation.name} to complete...")
        operation.result()
        print(f"Restarted connector {connector_id}")
    except GoogleAPICallError as e:
        print(f"Failed to restart connector {connector_id} with error: {e}")
    

_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
