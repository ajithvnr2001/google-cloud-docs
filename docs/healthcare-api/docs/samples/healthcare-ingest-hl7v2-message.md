---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-ingest-hl7v2-message/
title: Ingest HL7v2 message \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:06.473906+00:00
---

# Ingest HL7v2 message  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-ingest-hl7v2-message/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Ingest HL7v2 message Stay organized with collections  Save and categorize content based on your preferences. 

Ingest a message into an HL7v2 store.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and managing HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages)
  * [Store healthcare data with client libraries](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Node.js setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Node.js API reference documentation](https://github.com/googleapis/google-api-nodejs-client/blob/main/src/apis/healthcare/README.md). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
