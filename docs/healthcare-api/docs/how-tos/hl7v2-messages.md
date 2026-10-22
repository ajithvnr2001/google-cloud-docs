---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages/
title: Creating and managing HL7v2 messages \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:38.570951+00:00
---

# Creating and managing HL7v2 messages  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Creating and managing HL7v2 messages Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to ingest, create, label, list, view, and delete HL7v2 messages. HL7v2 messages are used to transmit clinical data between systems. An HL7v2 message might contain information about an observation result, a prescription to send to a pharmacy, a financial transaction, or other clinical events.

## Overview of creating and ingesting HL7v2 messages

Use either of the following methods to store an HL7v2 message in the Cloud Healthcare API:

  * [`messages.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/create)
  * [`messages.ingest`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/ingest)



When you use `messages.ingest`, the method generates a response containing one of the following:

  * An HL7v2 acknowledgement (`ACK`) message when successful
  * A negative acknowledgement (`NACK`) message when there is an error



The `ACK` and `NACK` messages are used for replying to HL7v2 interface systems that expect these acknowledgements.

### Message ingestion and creation with an MLLP adapter

HL7v2 messages are delivered between care systems and the Cloud Healthcare API using the minimal lower layer protocol (MLLP). For more information, see [MLLP and the Google Cloud Platform MLLP adapter](https://docs.cloud.google.com/healthcare-api/docs/concepts/hl7v2#mllp_and_the_google_cloud_platform_mllp_adapter). For instructions on how to configure an MLLP adapter to communicate securely with the Cloud Healthcare API, see [Transmitting HL7v2 messages over TCP/IP connections](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter).

## Ingesting HL7v2 messages

After the Cloud Healthcare API ingests the message from a care system, the Cloud Healthcare API generates a response containing an `hl7ack` field which contains a base64-encoded HL7v2 message with the following characteristics:

  * The message type is `ACK`.
  * The sending facility and the receiving facility are reversed, and the sending application and receiving application are reversed.
  * The send time of the message is the current time and a new control ID is generated.
  * The `MSH-9.1` field's value defines the message type.
  * The `MSA.1` field's value defines a response type. An `AA` response type indicates `Application Accept`, meaning that the message was validated and successfully ingested.
  * The `MSA.2` value contains the original message's [control ID](https://www.hl7.org/documentcenter/public_temp_7890F70A-1C23-BA17-0C771A64EC211E18/wg/conf/HL7MSH.htm#MessControl).



The following samples show how to ingest an HL7v2 message using the [`projects.locations.datasets.hl7V2Stores.messages.ingest`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/ingest) method.

### curl

To ingest an HL7v2 message, make a `POST` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * A [`Message`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#Message)



The following sample shows a `POST` request using `curl` and a sample JSON file called [`hl7v2-sample.json`](https://cloud.google.com/healthcare-api/docs/resources/hl7v2-sample.json).
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data-binary @hl7v2-sample.json \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages:ingest"

The following sample response shows the `hl7Ack` and message details.
    
    
    {
      "hl7Ack": "TVNIfF5+XCZ8QXxBfEF8U0VORF9GQUNJTElUWXwyMDIwMDIxNDIxMjAwNXx8QUNLfDFmMmQ1MjQzLTFhOWEtNGE4My05ZmI5LWNlNTIzMTVmZjk2M3xUfDAuMA1NU0F8QUF8MjAxODAxMDEwMDAwMDA=",
      "message": {
        "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
        "data": "TVNIfF5+XCZ8QXxTRU5EX0ZBQ0lMSVRZfEF8QXwyMDE4MDEwMTAwMDAwMHx8VFlQRV5BfDIwMTgwMTAxMDAwMDAwfFR8MC4wfHx8QUF8fDAwfEFTQ0lJDUVWTnxBMDB8MjAxODAxMDEwNDAwMDANUElEfHwxNAExMTFeXl5eTVJOfDExMTExMTExXl5eXk1STn4xMTExMTExMTExXl5eXk9SR05NQlI=",
        "sendFacility": "SEND_FACILITY",
        "sendTime": "2018-01-01T00:00:00Z",
        "messageType": "TYPE",
        "createTime": "CREATE_TIME",
        "patientIds": [
          {
            "value": "14\u0001111",
            "type": "MRN"
          },
          {
            "value": "11111111",
            "type": "MRN"
          },
          {
            "value": "1111111111",
            "type": "ORGNMBR"
          }
        ]
      }
    }
    

### PowerShell

To ingest an HL7v2 message, make a `POST` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * A [`Message`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#Message)



The following sample shows a `POST` request using PowerShell and a sample JSON file called [`hl7v2-sample.json`](https://cloud.google.com/healthcare-api/docs/resources/hl7v2-sample.json).
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -InFile hl7v2-sample.json `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages:ingest" | Select-Object -Expand Content

The following sample response shows the `hl7Ack` and message details.
    
    
    {
      "hl7Ack": "TVNIfF5+XCZ8QXxBfEF8U0VORF9GQUNJTElUWXwyMDIwMDIxNDIxMjAwNXx8QUNLfDFmMmQ1MjQzLTFhOWEtNGE4My05ZmI5LWNlNTIzMTVmZjk2M3xUfDAuMA1NU0F8QUF8MjAxODAxMDEwMDAwMDA=",
      "message": {
        "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
        "data": "TVNIfF5+XCZ8QXxTRU5EX0ZBQ0lMSVRZfEF8QXwyMDE4MDEwMTAwMDAwMHx8VFlQRV5BfDIwMTgwMTAxMDAwMDAwfFR8MC4wfHx8QUF8fDAwfEFTQ0lJDUVWTnxBMDB8MjAxODAxMDEwNDAwMDANUElEfHwxNAExMTFeXl5eTVJOfDExMTExMTExXl5eXk1STn4xMTExMTExMTExXl5eXk9SR05NQlI=",
        "sendFacility": "SEND_FACILITY",
        "sendTime": "2018-01-01T00:00:00Z",
        "messageType": "TYPE",
        "createTime": "CREATE_TIME",
        "patientIds": [
          {
            "value": "14\u0001111",
            "type": "MRN"
          },
          {
            "value": "11111111",
            "type": "MRN"
          },
          {
            "value": "1111111111",
            "type": "ORGNMBR"
          }
        ]
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"os"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // ingestHL7V2Message ingests an HL7V2 message.
    func ingestHL7V2Message(w io.Writer, projectID, location, datasetID, hl7V2StoreID, messageFile string) error {
    	ctx := context.Background()
    
    	hl7v2message, err := os.ReadFile(messageFile)
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	messagesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores.Messages
    
    	req := &healthcare.IngestMessageRequest{
    		Message: &healthcare.Message{
    			Data: base64.StdEncoding.EncodeToString(hl7v2message),
    		},
    	}
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7V2StoreID)
    
    	resp, err := messagesService.Ingest(parent, req).Do()
    	if err != nil {
    		return fmt.Errorf("Create: %w", err)
    	}
    
    	fmt.Fprintf(w, "Ingested HL7V2 message: %q\n", resp.Message.Name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores.Messages;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.IngestMessageRequest;
    import com.google.api.services.healthcare.v1.model.IngestMessageResponse;
    import com.google.api.services.healthcare.v1.model.Message;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.nio.charset.Charset;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.util.Collections;
    import java.util.List;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public class HL7v2MessageIngest {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final String MESSAGE_NAME =
          "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2MessageIngest(String hl7v2StoreName, String filePath) throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Load the data from file and format it into an ingest request.
        List<String> lines = Files.readAllLines(Paths.get(filePath), Charset.defaultCharset());
        String data = String.join("\n", lines);
        Message message = new Message().setData(data);
        IngestMessageRequest ingestRequest = new IngestMessageRequest().setMessage(message);
    
        // Create request and configure any parameters.
        Messages.Ingest request =
            client
                .projects()
                .locations()
                .datasets()
                .hl7V2Stores()
                .messages()
                .ingest(hl7v2StoreName, ingestRequest);
    
        // Execute the request and process the results.
        IngestMessageResponse response = request.execute();
        System.out.println("HL7v2 message ingested: " + response.toPrettyString());
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential =
            GoogleCredentials.getApplicationDefault()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        // Create a HttpRequestInitializer, which will provide a baseline configuration to all requests.
        HttpRequestInitializer requestInitializer =
            request -> {
              new HttpCredentialsAdapter(credential).initialize(request);
              request.setConnectTimeout(60000); // 1 minute connect timeout
              request.setReadTimeout(60000); // 1 minute read timeout
            };
    
        // Build the client for interacting with the service.
        return new CloudHealthcare.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
            .setApplicationName("your-application-name")
            .build();
      }
    }

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    const fs = require('fs');
    const util = require('util');
    const readFile = util.promisify(fs.readFile);
    
    const ingestHl7v2Message = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      // const hl7v2MessageFile = 'hl7v2-message.json';
      const hl7v2Message = JSON.parse(await readFile(hl7v2MessageFile));
    
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
      const request = {parent, resource: hl7v2Message};
    
      const response =
        await healthcare.projects.locations.datasets.hl7V2Stores.messages.ingest(
          request
        );
      const data = response.data.hl7Ack;
      const buff = new Buffer.from(data, 'base64');
      const hl7Ack = buff.toString('ascii');
      console.log('Ingested HL7v2 message with ACK:\n', hl7Ack);
    };
    
    ingestHl7v2Message();

### Python
    
    
    def ingest_hl7v2_message(
        project_id, location, dataset_id, hl7v2_store_id, hl7v2_message_file
    ):
        """Ingests a new HL7v2 message from the hospital and sends a notification
        to the Cloud Pub/Sub topic. Return is an HL7v2 ACK message if the message
        was successfully stored.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        # Imports Python's built-in "json" module
        import json
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        # hl7v2_message_file = 'hl7v2-message.json'  # replace with the path to the HL7v2 file
        hl7v2_parent = f"projects/{project_id}/locations/{location}"
        hl7v2_store_name = "{}/datasets/{}/hl7V2Stores/{}".format(
            hl7v2_parent, dataset_id, hl7v2_store_id
        )
    
        with open(hl7v2_message_file) as hl7v2_message:
            hl7v2_message_content = json.load(hl7v2_message)
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .messages()
            .ingest(parent=hl7v2_store_name, body=hl7v2_message_content)
        )
    
        response = request.execute()
        print(f"Ingested HL7v2 message from file: {hl7v2_message_file}")
        return response
    
    

## Creating HL7v2 messages

The following samples show how to create an HL7v2 message using the [`projects.locations.datasets.hl7V2Stores.messages.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/create) method.

### REST

To create an HL7v2 message, use the [`projects.locations.datasets.hl7V2Stores.messages.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/create) method.

If you need an HL7v2 message file to use with the sample commands, you can download the [`hl7v2-sample.json`](https://cloud.google.com/healthcare-api/docs/resources/hl7v2-sample.json) JSON file.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID
  * HL7V2_MESSAGE_FILE: the path to a JSON-formatted file containing an HL7v2 message on your local machine



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         --data-binary @HL7V2_MESSAGE_FILE \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -InFile HL7V2_MESSAGE_FILE `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The following output is returned when creating a message using the [`hl7v2-sample.json`](https://docs.cloud.google.com/static/healthcare-api/docs/resources/hl7v2-sample.json) JSON file: 

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
      "data": "TVNIfF5+XCZ8QXxTRU5EX0ZBQ0lMSVRZfEF8QXwyMDE4MDEwMTAwMDAwMHx8VFlQRV5BfDIwMTgwMTAxMDAwMDAwfFR8MC4wfHx8QUF8fDAwfEFTQ0lJDUVWTnxBMDB8MjAxODAxMDEwNDAwMDANUElEfHwxNAExMTFeXl5eTVJOfDExMTExMTExXl5eXk1STn4xMTExMTExMTExXl5eXk9SR05NQlI=",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "1970-01-01T00:00:00Z",
      "patientIds": [
        {
          "value": "14\u0001111",
          "type": "MRN"
        },
        {
          "value": "11111111",
          "type": "MRN"
        },
        {
          "value": "1111111111",
          "type": "ORGNMBR"
        }
      ]
    }
    

### Go
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"os"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // createHL7V2Message creates an HL7V2 message.
    func createHL7V2Message(w io.Writer, projectID, location, datasetID, hl7V2StoreID, messageFile string) error {
    	ctx := context.Background()
    
    	hl7v2message, err := os.ReadFile(messageFile)
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	messagesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores.Messages
    
    	req := &healthcare.CreateMessageRequest{
    		Message: &healthcare.Message{
    			Data: base64.StdEncoding.EncodeToString(hl7v2message),
    		},
    	}
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7V2StoreID)
    	resp, err := messagesService.Create(parent, req).Do()
    	if err != nil {
    		return fmt.Errorf("messagesService.Create: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created HL7V2 message: %q\n", resp.Name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores.Messages;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.CreateMessageRequest;
    import com.google.api.services.healthcare.v1.model.Message;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.nio.charset.Charset;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.util.Collections;
    import java.util.List;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public class HL7v2MessageCreate {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2MessageCreate(String hl7v2StoreName, String messageId, String filePath)
          throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
        // String messageId = "your-message-id";
        // String filePath = "path/to/file.txt";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Load the data from file representing the message.
        List<String> lines = Files.readAllLines(Paths.get(filePath), Charset.defaultCharset());
        String data = String.join("\n", lines);
        Message message = new Message().setData(data).setName(messageId);
        CreateMessageRequest createRequest = new CreateMessageRequest().setMessage(message);
    
        // Create request and configure any parameters.
        Messages.Create request =
            client
                .projects()
                .locations()
                .datasets()
                .hl7V2Stores()
                .messages()
                .create(hl7v2StoreName, createRequest);
    
        // Execute the request and process the results.
        Message response = request.execute();
        System.out.println("HL7v2 message created: " + response.toPrettyString());
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential =
            GoogleCredentials.getApplicationDefault()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        // Create a HttpRequestInitializer, which will provide a baseline configuration to all requests.
        HttpRequestInitializer requestInitializer =
            request -> {
              new HttpCredentialsAdapter(credential).initialize(request);
              request.setConnectTimeout(60000); // 1 minute connect timeout
              request.setReadTimeout(60000); // 1 minute read timeout
            };
    
        // Build the client for interacting with the service.
        return new CloudHealthcare.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
            .setApplicationName("your-application-name")
            .build();
      }
    }

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    const fs = require('fs');
    const util = require('util');
    const readFile = util.promisify(fs.readFile);
    
    const createHl7v2Message = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      // const hl7v2MessageFile = 'hl7v2-message.json';
      const hl7v2Message = JSON.parse(await readFile(hl7v2MessageFile));
    
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
      const request = {parent, resource: hl7v2Message};
    
      const response =
        await healthcare.projects.locations.datasets.hl7V2Stores.messages.create(
          request
        );
      const {data} = response;
      console.log('Created HL7v2 message with data:\n', data);
    };
    
    createHl7v2Message();

### Python
    
    
    def create_hl7v2_message(
        project_id, location, dataset_id, hl7v2_store_id, hl7v2_message_file
    ):
        """Creates an HL7v2 message and sends a notification to the
        Cloud Pub/Sub topic.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        # Imports Python's built-in "json" module
        import json
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        # hl7v2_message_file = 'hl7v2-message.json'  # replace with the path to the HL7v2 file
        hl7v2_parent = f"projects/{project_id}/locations/{location}"
        hl7v2_store_name = "{}/datasets/{}/hl7V2Stores/{}".format(
            hl7v2_parent, dataset_id, hl7v2_store_id
        )
    
        with open(hl7v2_message_file) as hl7v2_message:
            hl7v2_message_content = json.load(hl7v2_message)
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .messages()
            .create(parent=hl7v2_store_name, body=hl7v2_message_content)
        )
    
        response = request.execute()
        print(f"Created HL7v2 message from file: {hl7v2_message_file}")
        return response
    
    

### HL7v2 message segment separators and encoding

The default segment separator in HL7v2 is a carriage return (`\r`). Most text editors use newline (`\n`) characters as segment separators. This produces HL7v2 messages that can't be ingested into the Cloud Healthcare API using the default configuration. To permit an HL7v2 store to ingest messages that use newline characters as segment separators, see Setting the segment terminator.

To convert the newline characters in a file to carriage returns, run the following command in a Linux shell:
    
    
    sed -z 's/\n/\r/g' INPUT_FILENAME > OUTPUT_FILENAME

The ingest and create methods expect HL7v2 messages to be base64 encoded strings. To convert a string to base64 encoding, run the following command in a Linux shell:
    
    
    openssl base64 -A -in ./INPUT_FILENAME -out ./OUTPUT_FILENAME

## Setting the segment terminator

When creating or ingesting data, the [HL7v2 message format](https://www.hl7.org/documentcenter/public/calendarofevents/FirstTime/Glossary%20of%20terms.pdf) requires that segments are terminated using the return character, `\r`. You can configure an HL7v2 store to accept HL7v2 messages with a non-standard terminator, such as `\n`.

Consider the following HL7v2 message that uses the default `\r` as the segment terminator. This message is accepted by default when you create an HL7v2 store.
    
    
    MSH|^~\\&|FROM_APP|FROM_FACILITY|TO_APP|TO_FACILITY|20150503223000||ADT^A01|20150503223000|P|2.5|**\r**
    EVN|A01|20110613083617|**\r**
    PID|1||21004053^^^^MRN||SULLY^BRIAN||19611209|M|||123 MAIN ST^^MOUNTAIN SPRINGS^CO^80439|**\r**
    PV1||I|H73 RM1^1^^HIGHWAY 73 CLINIC||||5148^MARY QUINN|||||||||Y||||||||||||||||||||||||||||20150503223000|**\r**
    

The following message is identical to the previous message, except that it uses `\n` as the segment terminator:
    
    
    MSH|^~\\&|FROM_APP|FROM_FACILITY|TO_APP|TO_FACILITY|20150503223000||ADT^A01|20150503223000|P|2.5|**\n**
    EVN|A01|20110613083617|**\n**
    PID|1||21004053^^^^MRN||SULLY^BRIAN||19611209|M|||123 MAIN ST^^MOUNTAIN SPRINGS^CO^80439|**\n**
    PV1||I|H73 RM1^1^^HIGHWAY 73 CLINIC||||5148^MARY QUINN|||||||||Y||||||||||||||||||||||||||||20150503223000|**\n**
    

To store the message with the non-standard terminator, configure the [`ParserConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig) object in the HL7v2 store and set the `segmentTerminator` field to the base64-encoding of `\n`.

The following samples show how to configure `segmentTerminator` in `ParserConfig` when you [create an HL7v2 store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2#creating_an_hl7v2_store). If you have an existing HL7v2 store, you can [edit it](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2#editing_an_hl7v2_store) to provide the `ParserConfig` body. After setting the segment terminator, you can create or ingest the message.

### curl

To create an HL7v2 store with the segment terminator set to `\n`, make a `POST` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * A `parserConfig` object with the `segmentTerminator` set to `Cg==` (the base64-encoding of `\n`)



The following sample shows a `POST` request using `curl`.
    
    
    curl -X POST \
        --data "{
          'parserConfig': {
            'segmentTerminator': 'Cg=='
          }
        }" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "parserConfig": {
        "segmentTerminator": "Cg=="
      }
    }
    

### PowerShell

To create an HL7v2 store with the segment terminator set to `\n`, make a `POST` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * A `parserConfig` object with the `segmentTerminator` set to `Cg==` (the base64-encoding of `\n`)



The following sample shows a `POST` request using PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
          'parserConfig': {
            'segmentTerminator': 'Cg=='
          }
      } `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "parserConfig": {
        "segmentTerminator": "Cg=="
      }
    }
    

## Using a null segment header

An HL7v2 message without a [message header segment (MSH)](https://www.hl7.org/documentcenter/public/wg/conf/HL7MSH.htm) has a null segment header. Typically, an HL7v2 message contains a MSH that defines metadata such as the message's source, intent, purpose, and destination. The MSH enables you to search and filter messages. However, you can store messages that don't contain an MSH by configuring the [`ParserConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserConfig) object in the HL7v2 store and set the `allowNullHeader` field to `true`.

The folllowing sample message contains a Patient Identification (PID) segment, but no MSH:
    
    
    PID|1||21004053^^^^MRN||SULLY^BRIAN||19611209|M|||123 MAIN ST^^MOUNTAIN SPRINGS^CO^80439
    

The following samples show how to configure `allowNullHeader` in `ParserConfig` when you [create an HL7v2 store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2#creating_an_hl7v2_store). If you have an existing HL7v2 store, you can [edit it](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2#editing_an_hl7v2_store) and provide the `ParserConfig` body. After setting `allowNullHeader` to `true`, you can create or ingest messages with null segment headers.

### curl

To create an HL7v2 store and store messages that don't contain an MSH, make a `POST` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * A `parserConfig` object with `allowNullHeader` set to `true`



The following sample shows a `POST` request using `curl`.
    
    
    curl -X POST \
        --data "{
          'parserConfig': {
            'allowNullHeader': true
          }
        }" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "parserConfig": {
        "allowNullHeader": true
      }
    }
    

### PowerShell

To create an HL7v2 store and store messages that don't contain an MSH, make a `POST` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * A `parserConfig` object with `allowNullHeader` set to `true`



The following sample shows a `POST` request using PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
          'parserConfig': {
            'nullTerminator': true
          }
      } `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "parserConfig": {
        "allowNullHeader": true
      }
    }
    

## Labeling an HL7v2 message

You can add one or more key-value labels to a message. A use case for labels is adding status labels to a message so that an application can query messages by status.

The following samples show how to add labels to an HL7v2 message using the [`projects.locations.datasets.hl7V2Stores.messages.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/patch) method.

### curl

To add labels to an HL7v2 message, make a `PATCH` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * The label data to update
  * An update mask



The following sample shows a `PATCH` request using `curl`.
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'labels': {
            'KEY' : 'VALUE'
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?updateMask=labels"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
      "data": "DATA",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "CREATE_TIME",
      "patientIds": [
        {
            "value": "VALUE_1",
            "type": "TYPE_1"
        },
        {
            "value": "VALUE_2",
            "type": "TYPE_2"
        }
      ],
      "labels": {
        "KEY": "VALUE"
      }
    }
    

### PowerShell

To add labels to an HL7v2 message, make a `PATCH` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * The label data to update
  * An update mask



The following sample shows a `PATCH` request using PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Patch `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
          'labels': {
            'KEY': 'VALUE'
          }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?updateMask=labels" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
      "data": "DATA",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "CREATE_TIME",
      "patientIds": [
        {
            "value": "VALUE_1",
            "type": "TYPE_1"
        },
        {
            "value": "VALUE_2",
            "type": "TYPE_2"
        }
      ],
      "labels": {
        "KEY": "VALUE"
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"os"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // patchHL7V2Message patches an HL7V2 message.
    func patchHL7V2Message(w io.Writer, projectID, location, datasetID, hl7V2StoreID, hl7V2MessageID, messageFile string) error {
    	ctx := context.Background()
    
    	hl7v2message, err := os.ReadFile(messageFile)
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	messagesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores.Messages
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s", projectID, location, datasetID, hl7V2StoreID, hl7V2MessageID)
    	message := &healthcare.Message{
    		Data:   base64.StdEncoding.EncodeToString(hl7v2message),
    		Labels: map[string]string{"my-label": "true"},
    	}
    
    	call := messagesService.Patch(name, message)
    	call.UpdateMask("labels")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("Patch: %w", err)
    	}
    
    	fmt.Fprintf(w, "Patched HL7V2 message: %q\n", resp.Name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores.Messages;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Message;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    import java.util.HashMap;
    import java.util.Map;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public class HL7v2MessagePatch {
      private static final String MESSAGE_NAME =
          "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2MessagePatch(String hl7v2MessageName) throws IOException {
        // String hl7v2MessageName =
        //    String.format(
        //        MESSAGE_NAME, "project-id", "region-id", "dataset-id", "hl7v2-id", "message-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Fetch the initial state of the message.
        Messages.Get getRequest =
            client.projects().locations().datasets().hl7V2Stores().messages().get(hl7v2MessageName);
        Message message = getRequest.execute();
    
        // Update the Message fields as needed as needed. For a full list of Message fields, see:
        // https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages
        Map<String, String> labels = new HashMap<>();
        labels.put("key1", "value1");
        labels.put("key2", "value2");
        message.setLabels(labels);
    
        // Create request and configure any parameters.
        Messages.Patch request =
            client
                .projects()
                .locations()
                .datasets()
                .hl7V2Stores()
                .messages()
                .patch(hl7v2MessageName, message)
                .setUpdateMask("labels");
    
        // Execute the request and process the results.
        message = request.execute();
        System.out.println("HL7v2 message patched: \n" + message.toPrettyString());
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential =
            GoogleCredentials.getApplicationDefault()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        // Create a HttpRequestInitializer, which will provide a baseline configuration to all requests.
        HttpRequestInitializer requestInitializer =
            request -> {
              new HttpCredentialsAdapter(credential).initialize(request);
              request.setConnectTimeout(60000); // 1 minute connect timeout
              request.setReadTimeout(60000); // 1 minute read timeout
            };
    
        // Build the client for interacting with the service.
        return new CloudHealthcare.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
            .setApplicationName("your-application-name")
            .build();
      }
    }

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const patchHl7v2Message = async () => {
      // TODO(developer): uncomment the lines beginning with 'const' before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      // The value for hl7v2MessageId is the server-generated ID returned when you
      // created or ingested the HL7v2 message in an HL7v2 store.
      // const hl7v2MessageId = 'qCnewKno44gTt3oBn4dQ0u8ZA23ibDdV9GpifD2E=';
      // const labelKey = 'status';
      // const labelValue = 'processed';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}/messages/${hl7v2MessageId}`;
      const request = {
        name,
        updateMask: 'labels',
        resource: {
          labels: {
            labelKey: labelValue,
          },
        },
      };
    
      await healthcare.projects.locations.datasets.hl7V2Stores.messages.patch(
        request
      );
      console.log('Patched HL7v2 message');
    };
    
    patchHl7v2Message();

### Python
    
    
    def patch_hl7v2_message(
        project_id,
        location,
        dataset_id,
        hl7v2_store_id,
        hl7v2_message_id,
        label_key,
        label_value,
    ):
        """Updates the message.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        # hl7v2_message_id = '2yqbdhYHlk_ucSmWkcKOVm_N0p0OpBXgIlVG18rB-cw='  # replace with the HL7v2 message ID that was returned by the server
        # label_key = 'key1'  # replace with a key
        # label_value = 'label2'  # replace with a key value
        hl7v2_message_parent = f"projects/{project_id}/locations/{location}"
        hl7v2_message_name = "{}/datasets/{}/hl7V2Stores/{}/messages/{}".format(
            hl7v2_message_parent, dataset_id, hl7v2_store_id, hl7v2_message_id
        )
    
        patch = {"labels": {label_key: label_value}}
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .messages()
            .patch(name=hl7v2_message_name, updateMask="labels", body=patch)
        )
    
        response = request.execute()
        print(
            "Patched HL7v2 message {} with labels:\n\t{}: {}".format(
                hl7v2_message_id, label_key, label_value
            )
        )
        return response
    
    

## Getting HL7v2 message contents

The following samples show how to get the contents of an HL7v2 message using the [`projects.locations.datasets.hl7V2Stores.messages.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/get) method. To determine the parts of the message to get, supply the `view` query parameter with one of the following options:

  * `BASIC`: Include only the `name` field.
  * `RAW_ONLY`: Include all the message fields except the `parsedData` field.
  * `PARSED_ONLY`: Include all the message fields except the `data` field.
  * `FULL`: Include all the message fields. This is the default.



The following samples show how to get the contents of an HL7v2 message using the `FULL`, `RAW_ONLY`, and `PARSED_ONLY` views.

### Using the `FULL` view

You don't need to explicitly set the `FULL` view, as `FULL` is the default value. However, in the following `curl` and PowerShell samples, the `FULL` view is added as a query parameter for completeness.

### curl

To get the contents of an HL7v2 message using the `FULL` view, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * `FULL` as the `view`



The following sample shows a `GET` request using `curl`.
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?view=FULL"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
      "data": "DATA",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "CREATE_TIME",
      "patientIds": [
        {
            "value": "VALUE_1",
            "type": "TYPE_1"
        },
        {
            "value": "VALUE_2",
            "type": "TYPE_2"
        },
        {
            "value": "VALUE_3",
            "type": "TYPE_3"
        }
      ],
      "parsedData": {
        "segments": [
          {
            ""segmentId": "SEGMENT_ID_1",
            "fields": {
              FIELDS_1
            }
          },
          {
            "segmentId": "SEGMENT_ID_2",
            "fields": {
              FIELDS_2
            }
          },
          {
            "segmentId": "SEGMENT_ID_3",
            "fields": {
              FIELDS_3
            }
          }
        ]
      }
    }
    

### PowerShell

To get the contents of an HL7v2 message using the `FULL` view, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * `FULL` as the `view`



The following sample shows a `GET` request using PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?view=FULL" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
      "data": "DATA",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "CREATE_TIME",
      "patientIds": [
        {
            "value": "VALUE_1",
            "type": "TYPE_1"
        },
        {
            "value": "VALUE_2",
            "type": "TYPE_2"
        },
        {
            "value": "VALUE_3",
            "type": "TYPE_3"
        }
      ],
      "parsedData": {
        "segments": [
          {
            ""segmentId": "SEGMENT_ID_1",
            "fields": {
              FIELDS_1
            }
          },
          {
            "segmentId": "SEGMENT_ID_2",
            "fields": {
              FIELDS_2
            }
          },
          {
            "segmentId": "SEGMENT_ID_3",
            "fields": {
              FIELDS_3
            }
          }
        ]
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"encoding/base64"
    	"encoding/json"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getHL7V2Message gets an HL7V2 message.
    func getHL7V2Message(w io.Writer, projectID, location, datasetID, hl7V2StoreID, hl7V2MessageID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	messagesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores.Messages
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s", projectID, location, datasetID, hl7V2StoreID, hl7V2MessageID)
    	message, err := messagesService.Get(name).Do()
    	if err != nil {
    		return fmt.Errorf("Get: %w", err)
    	}
    
    	rawData, err := base64.StdEncoding.DecodeString(message.Data)
    	if err != nil {
    		return fmt.Errorf("base64.DecodeString: %w", err)
    	}
    
    	fmt.Fprintf(w, "Got HL7V2 message.\n")
    	fmt.Fprintf(w, "Raw length: %d.\n", len(rawData))
    	fmt.Fprintf(w, "Parsed data:\n")
    	parsedJSON, _ := json.MarshalIndent(message.ParsedData, "", "  ")
    	fmt.Fprintf(w, "%s", parsedJSON)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores.Messages;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Message;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public class HL7v2MessageGet {
      private static final String MESSAGE_NAME =
          "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2MessageGet(String hl7v2MessageName) throws IOException {
        // String hl7v2MessageName =
        //    String.format(
        //        MESSAGE_NAME, "project-id", "region-id", "dataset-id", "hl7v2-id", "message-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Messages.Get request =
            client.projects().locations().datasets().hl7V2Stores().messages().get(hl7v2MessageName);
    
        // Execute the request and process the results.
        Message store = request.execute();
        System.out.println("HL7v2 message retrieved: \n" + store.toPrettyString());
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential =
            GoogleCredentials.getApplicationDefault()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        // Create a HttpRequestInitializer, which will provide a baseline configuration to all requests.
        HttpRequestInitializer requestInitializer =
            request -> {
              new HttpCredentialsAdapter(credential).initialize(request);
              request.setConnectTimeout(60000); // 1 minute connect timeout
              request.setReadTimeout(60000); // 1 minute read timeout
            };
    
        // Build the client for interacting with the service.
        return new CloudHealthcare.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
            .setApplicationName("your-application-name")
            .build();
      }
    }

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const getHl7v2Message = async () => {
      // TODO(developer): uncomment the lines beginning with 'const' before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      // The value for hl7v2MessageId is the server-generated ID returned when you
      // created or ingested the HL7v2 message in an HL7v2 store.
      // const hl7v2MessageId = 'qCnewKno44gTt3oBn4dQ0u8ZA23ibDdV9GpifD2E=';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}/messages/${hl7v2MessageId}`;
      // Use the 'FULL' enum to include all of the message fields in the response.
      const view = 'FULL';
      const request = {name, view};
    
      const hl7v2Message =
        await healthcare.projects.locations.datasets.hl7V2Stores.messages.get(
          request
        );
      console.log('Got HL7v2 message:\n', hl7v2Message.data);
    };
    
    getHl7v2Message();

### Python
    
    
    def get_hl7v2_message(
        project_id, location, dataset_id, hl7v2_store_id, hl7v2_message_id
    ):
        """Gets an HL7v2 message.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        # hl7v2_message_id = '2yqbdhYHlk_ucSmWkcKOVm_N0p0OpBXgIlVG18rB-cw='  # replace with the HL7v2 message ID that was returned by the server
        hl7v2_parent = f"projects/{project_id}/locations/{location}"
        hl7v2_message_name = "{}/datasets/{}/hl7V2Stores/{}/messages/{}".format(
            hl7v2_parent, dataset_id, hl7v2_store_id, hl7v2_message_id
        )
    
        msgs = client.projects().locations().datasets().hl7V2Stores().messages()
        message = msgs.get(name=hl7v2_message_name).execute()
    
        print("Name: {}".format(message.get("name")))
        print("Data: {}".format(message.get("data")))
        print("Creation time: {}".format(message.get("createTime")))
        print("Sending facility: {}".format(message.get("sendFacility")))
        print("Time sent: {}".format(message.get("sendTime")))
        print("Message type: {}".format(message.get("messageType")))
        print("Patient IDs:")
        patient_ids = message.get("patientIds")
        for patient_id in patient_ids:
            print("\tPatient value: {}".format(patient_id.get("value")))
            print("\tPatient type: {}".format(patient_id.get("type")))
        print("Labels: {}".format(message.get("labels")))
    
        print(message)
        return message
    
    

### Using the `RAW_ONLY` view

The following samples show how to get the contents of an HL7v2 message using the `RAW_ONLY` view, which includes all of the message fields except for `parsedData`.

### curl

To get the contents of an HL7v2 message using the `RAW_ONLY` view, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * `RAW_ONLY` as the view



The following sample shows a `GET` request using `curl`.
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?view=RAW_ONLY"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
      "data": "DATA",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "CREATE_TIME",
      "patientIds": [
        {
            "value": "VALUE_1",
            "type": "TYPE_1"
        },
        {
            "value": "VALUE_2",
            "type": "TYPE_2"
        },
        {
            "value": "VALUE_3",
            "type": "TYPE_3"
        }
      ]
    }
    

### PowerShell

To get the contents of an HL7v2 message using the `RAW_ONLY` view, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * `RAW_ONLY` as the view



The following sample shows a `GET` request using PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?view=RAW_ONLY" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
      "data": "DATA",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "CREATE_TIME",
      "patientIds": [
        {
            "value": "VALUE_1",
            "type": "TYPE_1"
        },
        {
            "value": "VALUE_2",
            "type": "TYPE_2"
        },
        {
            "value": "VALUE_3",
            "type": "TYPE_3"
        }
      ]
    }
    

### Using the `PARSED_ONLY` view

The following samples show how to get the contents of an HL7v2 message using the `PARSED_ONLY` view, which includes all of the message fields except for `data`.

### curl

To get the contents of an HL7v2 message using the `PARSED_ONLY` view, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * `PARSED_ONLY` as the view



The following sample shows a `GET` request using `curl`.
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?view=PARSED_ONLY"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "CREATE_TIME",
      "patientIds": [
        {
            "value": "VALUE_1",
            "type": "TYPE_1"
        },
        {
            "value": "VALUE_2",
            "type": "TYPE_2"
        },
        {
            "value": "VALUE_3",
            "type": "TYPE_3"
        }
      ],
      "parsedData": {
        "segments": [
          {
            "segmentId": "SEGMENT_ID_1",
            "fields": {
              FIELDS_1
            }
          },
          {
            "segmentId": "SEGMENT_ID_2",
            "fields": {
              FIELDS_2
            }
          },
          {
            "segmentId": "SEGMENT_ID_3",
            "fields": {
              FIELDS_3
            }
          }
        ]
      }
    }
    

### PowerShell

To get the contents of an HL7v2 message using the `PARSED_ONLY` view, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * `PARSED_ONLY` as the view



The following sample shows a `GET` request using PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?view=PARSED_ONLY" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
      "sendFacility": "SEND_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "TYPE",
      "createTime": "CREATE_TIME",
      "patientIds": [
        {
            "value": "VALUE_1",
            "type": "TYPE_1"
        },
        {
            "value": "VALUE_2",
            "type": "TYPE_2"
        },
        {
            "value": "VALUE_3",
            "type": "TYPE_3"
        }
      ],
      "parsedData": {
        "segments": [
          {
            "segmentId": "SEGMENT_ID_1",
            "fields": {
              FIELDS_1
            }
          },
          {
            "segmentId": "SEGMENT_ID_2",
            "fields": {
              FIELDS_2
            }
          },
          {
            "segmentId": "SEGMENT_ID_3",
            "fields": {
              FIELDS_3
            }
          }
        ]
      }
    }
    

### Using the `BASIC` view

The following samples show how to get the contents of an HL7v2 message using the `BASIC` view, which includes only the `name` field.

### curl

To get the contents of an HL7v2 message using the `BASIC` view, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * `BASIC` as the view



The following sample shows a `GET` request using `curl`.
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?view=BASIC"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID"
    }
    

### PowerShell

To get the contents of an HL7v2 message using the `BASIC` view, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The message ID
  * `BASIC` as the view



The following sample shows a `GET` request using PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID?view=BASIC" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID"
    }
    

## Listing HL7v2 messages

The following samples show how to list the messages in an HL7v2 store using the method. To determine the information about each message to include in the list, specify the `view` query parameter with one of the following options:

  * `BASIC`: Include only the `name` field. This is the default.
  * `RAW_ONLY`: Include all the message fields except the `parsedData` field.
  * `PARSED_ONLY`: Include all the message fields except the `data` field.
  * `FULL`: Include all the message fields.



### curl

To list the messages in an HL7v2 store, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The `view`, one of `BASIC`, `RAW_ONLY`, `PARSED_ONLY`, or `FULL`, or omit to use the default of `BASIC`



The following sample shows a `GET` request using `curl`. The request specifies `?view=FULL` to include all the message fields.
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages?view=FULL"

If the request is successful, the server returns a `200 OK` HTTP status code and an array of messages named `hl7_v2_messages`. The following sample response is truncated.
    
    
    {
      "hl7_v2_messages": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
          "data": "DATA",
          "sendFacility": "SEND_FACILITY",
          "sendTime": "SEND_TIME",
          "messageType": "MESSAGE_TYPE",
          "createTime": "CREATE_TIME",
          ...
        },
        ...
      ]
    }
    

### PowerShell

To list the messages in an HL7v2 store, make a `GET` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The `view`, one of `BASIC`, `RAW_ONLY`, `PARSED_ONLY`, or `FULL`, or omit to use the default of `BASIC`



The following sample shows a `GET` request using PowerShell. The request specifies `?view=FULL` to include all the message fields.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages?view=FULL" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. The sample response is truncated.
    
    
    {
      "hl7_v2_messages": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID",
          "data": "DATA",
          "sendFacility": "SEND_FACILITY",
          "sendTime": "SEND_TIME",
          "messageType": "MESSAGE_TYPE",
          "createTime": "CREATE_TIME",
          ...
        },
        ...
      ]
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // listHL7V2Messages prints a list of HL7V2 messages to w.
    func listHL7V2Messages(w io.Writer, projectID, location, datasetID, hl7V2StoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	messagesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores.Messages
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7V2StoreID)
    
    	resp, err := messagesService.List(parent).Do()
    	if err != nil {
    		return fmt.Errorf("List: %w", err)
    	}
    
    	fmt.Fprintln(w, "HL7V2 messages:")
    	for _, s := range resp.Hl7V2Messages {
    		fmt.Fprintln(w, s.Name)
    	}
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.ListMessagesResponse;
    import com.google.api.services.healthcare.v1.model.Message;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public class HL7v2MessageList {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2MessageList(String hl7v2StoreName) throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Results are paginated, so multiple queries may be required.
        String pageToken = null;
    
        do {
          // Create request and execute.
          ListMessagesResponse messageResponse =
              client
                  .projects()
                  .locations()
                  .datasets()
                  .hl7V2Stores()
                  .messages()
                  .list(hl7v2StoreName)
                  .setPageSize(100)
                  .setPageToken(pageToken)
                  .execute();
    
          if (messageResponse.getHl7V2Messages() != null) {
            // Print results.
            System.out.printf(
                "Retrieved %s HL7v2 messages: \n", messageResponse.getHl7V2Messages().size());
            for (Message message : messageResponse.getHl7V2Messages()) {
              System.out.println(message);
            }
          }
          // Update the page token for the next request.
          pageToken = messageResponse.getNextPageToken();
        } while (pageToken != null);
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential =
            GoogleCredentials.getApplicationDefault()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        // Create a HttpRequestInitializer, which will provide a baseline configuration to all requests.
        HttpRequestInitializer requestInitializer =
            request -> {
              new HttpCredentialsAdapter(credential).initialize(request);
              request.setConnectTimeout(60000); // 1 minute connect timeout
              request.setReadTimeout(60000); // 1 minute read timeout
            };
    
        // Build the client for interacting with the service.
        return new CloudHealthcare.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
            .setApplicationName("your-application-name")
            .build();
      }
    }

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const listHl7v2Messages = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
      const request = {parent};
    
      const response =
        await healthcare.projects.locations.datasets.hl7V2Stores.messages.list(
          request
        );
      const hl7v2Messages = response.data.hl7V2Messages;
      console.log(`HL7v2 messages: ${hl7v2Messages.length}`);
      for (const hl7v2Message of hl7v2Messages) {
        console.log(hl7v2Message);
      }
    };
    
    listHl7v2Messages();

### Python
    
    
    def list_hl7v2_messages(project_id, location, dataset_id, hl7v2_store_id):
        """Lists all the messages in the given HL7v2 store with support for
        filtering.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        hl7v2_messages_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        hl7v2_message_path = "{}/hl7V2Stores/{}".format(
            hl7v2_messages_parent, hl7v2_store_id
        )
    
        hl7v2_messages = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .messages()
            .list(parent=hl7v2_message_path)
            .execute()
            .get("hl7V2Messages", [])
        )
    
        for hl7v2_message in hl7v2_messages:
            print(hl7v2_message)
    
        return hl7v2_messages
    
    

## Deleting an HL7v2 message

The following samples show how to delete an HL7v2 message using the [`projects.locations.datasets.hl7V2Stores.messages.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/delete) method.

### curl

To delete an HL7v2 message, make a `DELETE` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The HL7v2 message ID



The following sample shows a `DELETE` request using `curl`.
    
    
    curl -X DELETE \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID"

If the request is successful, the server returns the empty body response in JSON format:
    
    
    {}
    

### PowerShell

To delete an HL7v2 message, make a `DELETE` request and specify the following information:

  * The name and location of the parent dataset
  * The name of the HL7v2 store
  * The HL7v2 message ID



The following sample shows a `DELETE` request using PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Delete `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID" | Select-Object -Expand Content

If the request is successful, the server returns the empty response body in JSON format:
    
    
    {}
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // deleteHL7V2Message deletes an HL7V2 message.
    func deleteHL7V2Message(w io.Writer, projectID, location, datasetID, hl7V2StoreID, hl7V2MessageID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	messagesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores.Messages
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s", projectID, location, datasetID, hl7V2StoreID, hl7V2MessageID)
    	if _, err := messagesService.Delete(name).Do(); err != nil {
    		return fmt.Errorf("Delete: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted HL7V2 message: %q\n", name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores.Messages;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public class HL7v2MessageDelete {
      private static final String MESSAGE_NAME =
          "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2MessageDelete(String hl7v2MessageName) throws IOException {
        // String hl7v2MessageName =
        //    String.format(
        //        MESSAGE_NAME, "project-id", "region-id", "dataset-id", "hl7v2-id", "message-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Messages.Delete request =
            client.projects().locations().datasets().hl7V2Stores().messages().delete(hl7v2MessageName);
    
        // Execute the request and process the results.
        request.execute();
        System.out.println("HL7v2 message deleted.");
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential =
            GoogleCredentials.getApplicationDefault()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        // Create a HttpRequestInitializer, which will provide a baseline configuration to all requests.
        HttpRequestInitializer requestInitializer =
            request -> {
              new HttpCredentialsAdapter(credential).initialize(request);
              request.setConnectTimeout(60000); // 1 minute connect timeout
              request.setReadTimeout(60000); // 1 minute read timeout
            };
    
        // Build the client for interacting with the service.
        return new CloudHealthcare.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
            .setApplicationName("your-application-name")
            .build();
      }
    }

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const deleteHl7v2Message = async () => {
      // TODO(developer): uncomment the lines beginning with 'const' before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      // The value for hl7v2MessageId is the server-generated ID returned when you
      // created or ingested the HL7v2 message in an HL7v2 store.
      // const hl7v2MessageId = 'qCnewKno44gTt3oBn4dQ0u8ZA23ibDdV9GpifD2E=';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}/messages/${hl7v2MessageId}`;
      const request = {name};
    
      await healthcare.projects.locations.datasets.hl7V2Stores.messages.delete(
        request
      );
      console.log('Deleted HL7v2 message');
    };
    
    deleteHl7v2Message();

### Python
    
    
    def delete_hl7v2_message(
        project_id, location, dataset_id, hl7v2_store_id, hl7v2_message_id
    ):
        """Deletes an HL7v2 message.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        # hl7v2_message_id = '2yqbdhYHlk_ucSmWkcKOVm_N0p0OpBXgIlVG18rB-cw='  # replace with the HL7v2 message ID that was returned by the server
        hl7v2_parent = f"projects/{project_id}/locations/{location}"
        hl7v2_message = "{}/datasets/{}/hl7V2Stores/{}/messages/{}".format(
            hl7v2_parent, dataset_id, hl7v2_store_id, hl7v2_message_id
        )
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .messages()
            .delete(name=hl7v2_message)
        )
    
        response = request.execute()
        print(f"Deleted HL7v2 message with ID: {hl7v2_message_id}")
        return response
    
    

## What's next

  * [Learn how to configure multiple Google Cloud services to send and receive HL7v2 messages over MLLP](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
