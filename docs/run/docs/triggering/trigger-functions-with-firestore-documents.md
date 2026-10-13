---
url: https://docs.cloud.google.com/run/docs/triggering/trigger-functions-with-firestore-documents/
title: Trigger functions with Firestore documents \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:18.590949+00:00
---

# Trigger functions with Firestore documents  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/trigger-functions-with-firestore-documents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Trigger functions with Firestore documents Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows examples of functions that are triggered when you make changes to a document inside of a specified collection.

## Before you begin

Before you run the sample code in this guide, you'll need to do the following:

  * [Enable APIs and grant the required roles for deploying functions](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#before_you_begin)
  * [Set up a Firestore database](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#set_up_your_database)



## Examples

The following examples demonstrate how to write functions that respond to a Firestore trigger.

### Example 1: Hello Firestore function

The following sample prints the fields of a triggering Firestore event:

### Node.js
    
    
    /**
     * Cloud Event Function triggered by a change to a Firestore document.
     */
    const functions = require('@google-cloud/functions-framework');
    const protobuf = require('protobufjs');
    
    functions.cloudEvent('helloFirestore', async cloudEvent => {
      console.log(`Function triggered by event on: ${cloudEvent.source}`);
      console.log(`Event type: ${cloudEvent.type}`);
    
      console.log('Loading protos...');
      const root = await protobuf.load('data.proto');
      const DocumentEventData = root.lookupType(
        'google.events.cloud.firestore.v1.DocumentEventData'
      );
    
      console.log('Decoding data...');
      const firestoreReceived = DocumentEventData.decode(cloudEvent.data);
    
      console.log('\nOld value:');
      console.log(JSON.stringify(firestoreReceived.oldValue, null, 2));
    
      console.log('\nNew value:');
      console.log(JSON.stringify(firestoreReceived.value, null, 2));
    });
    

### Python
    
    
    from cloudevents.http import CloudEvent
    import functions_framework
    from google.events.cloud import firestore
    
    
    @functions_framework.cloud_event
    def hello_firestore(cloud_event: CloudEvent) -> None:
        """Triggers by a change to a Firestore document.
    
        Args:
            cloud_event: cloud event with information on the firestore event trigger
        """
        firestore_payload = firestore.DocumentEventData()
        firestore_payload._pb.ParseFromString(cloud_event.data)
    
        print(f"Function triggered by change to: {cloud_event['source']}")
    
        print("\nOld value:")
        print(firestore_payload.old_value)
    
        print("\nNew value:")
        print(firestore_payload.value)
    
    

### Go
    
    
    // Package hellofirestore contains a Cloud Event Function triggered by a Cloud Firestore event.
    package hellofirestore
    
    import (
    	"context"
    	"fmt"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    	"github.com/googleapis/google-cloudevents-go/cloud/firestoredata"
    	"google.golang.org/protobuf/proto"
    )
    
    func init() {
    	functions.CloudEvent("helloFirestore", HelloFirestore)
    }
    
    // HelloFirestore is triggered by a change to a Firestore document.
    func HelloFirestore(ctx context.Context, event event.Event) error {
    	var data firestoredata.DocumentEventData
    
    	// If you omit `DiscardUnknown`, protojson.Unmarshal returns an error
    	// when encountering a new or unknown field.
    	options := proto.UnmarshalOptions{
    		DiscardUnknown: true,
    	}
    	err := options.Unmarshal(event.Data(), &data)
    
    	if err != nil {
    		return fmt.Errorf("proto.Unmarshal: %w", err)
    	}
    
    	fmt.Printf("Function triggered by change to: %v\n", event.Source())
    	fmt.Printf("Old value: %+v\n", data.GetOldValue())
    	fmt.Printf("New value: %+v\n", data.GetValue())
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.events.cloud.firestore.v1.[DocumentEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html);
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import io.cloudevents.CloudEvent;
    import java.util.logging.Logger;
    
    public class FirebaseFirestore implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(FirebaseFirestore.class.getName());
    
      @Override
      public void accept(CloudEvent event) throws [InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html) {
        [DocumentEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html) firestoreEventData = [DocumentEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html)
            .parseFrom(event.getData().toBytes());
    
        logger.info("Function triggered by event on: " + event.getSource());
        logger.info("Event type: " + event.getType());
    
        logger.info("Old value:");
        logger.info(firestoreEventData.[getOldValue](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html#com_google_events_cloud_firestore_v1_DocumentEventData_getOldValue__)().toString());
    
        logger.info("New value:");
        logger.info(firestoreEventData.[getValue](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html#com_google_events_cloud_firestore_v1_DocumentEventData_getValue__)().toString());
      }
    }
    

### C#
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Cloud.Firestore.V1;
    using Microsoft.Extensions.Logging;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace FirebaseFirestore;
    
    public class Function : ICloudEventFunction<DocumentEventData>
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, DocumentEventData data, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Function triggered by event on {subject}", cloudEvent.Subject);
            _logger.LogInformation("Event type: {type}", cloudEvent.Type);
            MaybeLogDocument("Old value", data.OldValue);
            MaybeLogDocument("New value", data.Value);
    
            // In this example, we don't need to perform any asynchronous operations, so the
            // method doesn't need to be declared async.
            return Task.CompletedTask;
        }
    
        /// <summary>
        /// Logs the names and values of the fields in a document in a very simplistic way.
        /// </summary>
        private void MaybeLogDocument(string message, Document document)
        {
            if (document is null)
            {
                return;
            }
    
            // ConvertFields converts the Firestore representation into a .NET-friendly
            // representation.
            IReadOnlyDictionary<string, object> fields = document.ConvertFields();
            var fieldNamesAndTypes = fields
                .OrderBy(pair => pair.Key)
                .Select(pair => $"{pair.Key}: {pair.Value}");
            _logger.LogInformation(message + ": {fields}", string.Join(", ", fieldNamesAndTypes));
        }
    }

#### Deploy the Hello Firestore function

If you haven't already done so, set up your [Firestore database](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#set_up_your_database).

After deploying a function, you can configure a trigger using the Google Cloud console, Google Cloud CLI, or Terraform.

###  Console 

When you use the Google Cloud console to create a function, you can also add a trigger to your function. Follow these steps to create a trigger for your function:

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click **Write a function** , and enter the function details. For more information about configuring functions during deployment, see [Deploy functions](https://docs.cloud.google.com/run/docs/deploy-functions#console).

  3. In the **Trigger** section, click **Add trigger**.

  4. Select **Firestore trigger**.

  5. In the **Eventarc trigger** pane, modify the trigger details as follows:

     1. Enter a name for the trigger in the **Trigger name** field, or use the default name.

     2. Select a **Trigger type** from the list:

        * **Google Sources** to specify triggers for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.

        * **Third-party** to integrate with non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview).

     3. Select **Cloud Firestore** from the **Event provider** list, to select a product that provides the type of event for triggering your function. For the list of event providers, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).

     4. Select **type=google.cloud.firestore.document.v1.written** from the **Event type** list. Your trigger configuration varies depending on the supported event type. For more information, see [Event types](https://docs.cloud.google.com/eventarc/docs/event-types).

     5. Leave the **Event data content type** field as is. 

     6. In the **Filters** section, select a database, operation and attribute values, or use the default selections. 

     7. If the **Region** field is enabled, select a [location](https://docs.cloud.google.com/eventarc/docs/overview#trigger-location) for the Eventarc trigger. In general, the location of an Eventarc trigger should match the location of the Google Cloud resource that you want to monitor for events. In most scenarios, you should also deploy your function in the same region. See [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations) for more details about Eventarc trigger locations.

     8. In the **Service account** field, select a service account. Eventarc triggers are linked to service accounts to use as an identity when invoking your function. Your Eventarc trigger's service account must have the permission to invoke your function. By default, Cloud Run uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

     9. Optionally, specify the **Service URL path** to send the incoming request to. This is the relative path on the destination service to which the events for the trigger should be sent. For example: `/`, `/route`, `route`, and `route/subroute`.

     10. Optionally, to enable retries if the delivery attempt fails, select the **Enable retry on failure** checkbox; otherwise, the default behavior is a single delivery attempt with no retries. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events).

  6. Once you've completed the required fields, click **Save trigger**.

  7. Click **Create**.

  8. In the **Source** tab, edit the source code if needed, then select **Save and redeploy**.




###  gcloud 

When you create a function using the gcloud CLI, you must first [deploy](https://docs.cloud.google.com/run/docs/deploy-functions) your function, and then create a trigger. Follow these steps to create a trigger for your function:

  1. Run the following command in the directory that contains the sample code to deploy your function:
         
         gcloud run deploy FUNCTION \
             --source . \
             --function FUNCTION_ENTRYPOINT \
             --base-image BASE_IMAGE_ID \
             --region REGION
         

Replace the following:

     * `FUNCTION`: the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

     * `FUNCTION_ENTRYPOINT`: the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.

     * `BASE_IMAGE_ID`: the base image environment for your function. For more details about base images and the packages included in each image, see [Runtimes base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

     * `REGION`: the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) where you want to deploy your function. For example, `europe-west1`.

  2. Run the following command to create a trigger that filters and routes events:
         
         gcloud eventarc triggers create TRIGGER_NAME  \
             --location=LOCATION \
             --destination-run-service=FUNCTION  \
             --destination-run-region=DESTINATION_RUN_REGION \
             --event-filters="type=EVENT_FILTER_TYPE" \
             --event-filters=database='(default)' \
             --event-data-content-type=application/protobuf \
             --event-filters-path-pattern=document='users/{username}' \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         

Replace the following:

     * `TRIGGER_NAME`: the ID of the trigger or a fully qualified identifier.
     * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`. 

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

     * `FUNCTION`: the name of the deployed Cloud Run function that receives the events for the trigger. 
     * `DESTINATION_RUN_REGION`: (optional) the [Cloud Run location](https://docs.cloud.google.com/run/docs/locations) in which the destination Cloud Run function can be found. If not specified, it is assumed that the function is in the same region as the trigger. 
     * `EVENT_FILTER_TYPE`: the identifier of the event. An event is generated when an API call for the method succeeds. For long-running operations, the event is only generated at the end of the operation, and only if the action is performed successfully. For a list of supported event types, see [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source). 
     * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
     * `PROJECT_ID`: your Google Cloud project ID. 

Notes:

     * After a trigger is created, the event filter type can't be changed. For a different event type, you must create a new trigger. 
     * `--event-filters=type=google.cloud.firestore.document.v1.written` specifies that the function is triggered when a document is created, updated or deleted, per the [event type](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#event_types).
     * `--event-filters=database='(default)'` specifies the Firebase database. For the default database name, use `(default)`.
     * `--event-filters-path-pattern=document='users/{username}'` provides the path pattern of the documents that should be monitored for relevant changes. This path pattern states that all documents in the `users` collection should be monitored. For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).
     * Optionally, to specify a single event delivery attempt with no retries, use the `--max-retry-attempts` flag. The only valid value is `1`. If you omit the flag, the standard retry behavior applies. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events). 
     * Other flags are available. For more information, see [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create). 



###  Terraform 

To create an Eventarc trigger for a Cloud Run function, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).

#### Test the Hello Firestore function

To test the Hello Firestore function, set up a collection called `users` in your [Firestore database](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#set_up_your_database):

  1. In the Google Cloud console, go to the Firestore databases page:

[Go to Firestore](https://console.cloud.google.com/firestore/databases)

  2. Click **Start a collection**.

  3. Specify `users` as the collection ID.

  4. To start adding the collection's first document, under **Add its first document** accept the auto-generated **Document ID**.

  5. Add at least one field for the document, specifying a name and value. For example, in **Field name** , enter `username`, and in **Field value** , enter `rowan`.

  6. When you're done, click **Save**.

This action creates a new document, thereby triggering your function.

  7. To confirm that your function was triggered, click the linked name of the function in the Google Cloud console [Cloud Run Overview page](https://console.cloud.google.com/run/services) to open the **Service details** page.

  8. In the **Observability** tab, select the **Logs** tab and look for the following string:
         
         Function triggered by change to: //firestore.googleapis.com/projects/your-project-id/databases/(default)'




### Example 2: Convert to Uppercase function

The following example retrieves the value added by the user, converts the string at that location to uppercase, and replaces the value with the uppercase string:

### Node.js

Use [protobufjs](https://www.npmjs.com/package/protobufjs) to decode the event data. Include the `google.events.cloud.firestore.v1` [`data.proto`](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/tree/main/functions/v2/firebase/firestore/helloFirestore) in your source.
    
    
    const functions = require('@google-cloud/functions-framework');
    const Firestore = require('[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)');
    const protobuf = require('protobufjs');
    
    const firestore = new [Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore.html)({
      projectId: process.env.GOOGLE_CLOUD_PROJECT,
    });
    
    // Converts strings added to /messages/{pushId}/original to uppercase
    functions.cloudEvent('makeUpperCase', async cloudEvent => {
      console.log('Loading protos...');
      const root = await protobuf.load('data.proto');
      const DocumentEventData = root.lookupType(
        'google.events.cloud.firestore.v1.DocumentEventData'
      );
    
      console.log('Decoding data...');
      const firestoreReceived = DocumentEventData.decode(cloudEvent.data);
    
      const resource = firestoreReceived.value.name;
      const affectedDoc = firestore.doc(resource.split('/documents/')[1]);
    
      const curValue = firestoreReceived.value.fields.original.stringValue;
      const newValue = curValue.toUpperCase();
    
      if (curValue === newValue) {
        // Value is already upper-case
        // Don't perform a(nother) write to avoid infinite loops
        console.log('Value is already upper-case.');
        return;
      }
    
      console.log(`Replacing value: ${curValue} --> ${newValue}`);
      affectedDoc.set({
        original: newValue,
      });
    });

### Python
    
    
    from cloudevents.http import CloudEvent
    import functions_framework
    from google.cloud import firestore
    from google.events.cloud import firestore as firestoredata
    
    client = firestore.[Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html)()
    
    
    # Converts strings added to /messages/{pushId}/original to uppercase
    @functions_framework.cloud_event
    def make_upper_case(cloud_event: CloudEvent) -> None:
        firestore_payload = firestoredata.DocumentEventData()
        firestore_payload._pb.ParseFromString(cloud_event.data)
    
        path_parts = firestore_payload.value.name.split("/")
        separator_idx = path_parts.index("documents")
        collection_path = path_parts[separator_idx + 1]
        document_path = "/".join(path_parts[(separator_idx + 2) :])
    
        print(f"Collection path: {collection_path}")
        print(f"Document path: {document_path}")
    
        affected_doc = client.[collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html#google_cloud_firestore_v1_client_Client_collection)(collection_path).document(document_path)
    
        cur_value = firestore_payload.value.fields["original"].string_value
        new_value = cur_value.upper()
    
        if cur_value != new_value:
            print(f"Replacing value: {cur_value} --> {new_value}")
            affected_doc.set({"original": new_value})
        else:
            # Value is already upper-case
            # Don't perform a second write (which can trigger an infinite loop)
            print("Value is already upper-case.")
    
    

### Go
    
    
    // Package upper contains a Firestore Cloud Function.
    package upper
    
    import (
    	"context"
    	"errors"
    	"fmt"
    	"log"
    	"os"
    	"strings"
    
    	"cloud.google.com/go/firestore"
    	firebase "firebase.google.com/go/v4"
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    	"github.com/googleapis/google-cloudevents-go/cloud/firestoredata"
    	"google.golang.org/protobuf/proto"
    )
    
    // set the GOOGLE_CLOUD_PROJECT environment variable when deploying.
    var projectID = os.Getenv("GOOGLE_CLOUD_PROJECT")
    
    // client is a Firestore client, reused between function invocations.
    var client *firestore.Client
    
    func init() {
    	// Use the application default credentials.
    	conf := &firebase.Config{ProjectID: projectID}
    
    	// Use context.Background() because the app/client should persist across
    	// invocations.
    	ctx := context.Background()
    
    	app, err := firebase.NewApp(ctx, conf)
    	if err != nil {
    		log.Fatalf("firebase.NewApp: %v", err)
    	}
    
    	client, err = app.Firestore(ctx)
    	if err != nil {
    		log.Fatalf("app.Firestore: %v", err)
    	}
    
    	// Register cloud event function
    	functions.CloudEvent("MakeUpperCase", MakeUpperCase)
    }
    
    // MakeUpperCase is triggered by a change to a Firestore document. It updates
    // the `original` value of the document to upper case.
    func MakeUpperCase(ctx context.Context, e event.Event) error {
    	var data firestoredata.DocumentEventData
    
    	// If you omit `DiscardUnknown`, protojson.Unmarshal returns an error
    	// when encountering a new or unknown field.
    	options := proto.UnmarshalOptions{
    		DiscardUnknown: true,
    	}
    	err := options.Unmarshal(e.Data(), &data)
    
    	if err != nil {
    		return fmt.Errorf("proto.Unmarshal: %w", err)
    	}
    
    	if data.[GetValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/apiv1/firestorepb.html#cloud_google_com_go_firestore_apiv1_firestorepb_StructuredQuery_FieldFilter_GetValue)() == nil {
    		return errors.New("Invalid message: 'Value' not present")
    	}
    
    	fullPath := strings.[Split](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Expression_Split)(data.[GetValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/apiv1/firestorepb.html#cloud_google_com_go_firestore_apiv1_firestorepb_StructuredQuery_FieldFilter_GetValue)().GetName(), "/documents/")[1]
    	pathParts := strings.[Split](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Expression_Split)(fullPath, "/")
    	collection := pathParts[0]
    	doc := strings.[Join](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Expression_Join)(pathParts[1:], "/")
    
    	var originalStringValue string
    	if v, ok := data.[GetValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/apiv1/firestorepb.html#cloud_google_com_go_firestore_apiv1_firestorepb_StructuredQuery_FieldFilter_GetValue)().GetFields()["original"]; ok {
    		originalStringValue = v.[GetStringValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/apiv1/firestorepb.html#cloud_google_com_go_firestore_apiv1_firestorepb_Value_GetStringValue)()
    	} else {
    		return errors.New("Document did not contain field \"original\"")
    	}
    
    	newValue := strings.[ToUpper](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Expression_ToUpper)(originalStringValue)
    	if originalStringValue == newValue {
    		log.Printf("%q is already upper case: skipping", originalStringValue)
    		return nil
    	}
    	log.Printf("Replacing value: %q -> %q", originalStringValue, newValue)
    
    	newDocumentEntry := map[string]string{"original": newValue}
    	_, err = client.Collection(collection).Doc(doc).Set(ctx, newDocumentEntry)
    	if err != nil {
    		return fmt.Errorf("Set: %w", err)
    	}
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.firestore.[Firestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html);
    import com.google.cloud.firestore.[FirestoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FirestoreOptions.html);
    import com.google.cloud.firestore.[SetOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.SetOptions.html);
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.events.cloud.firestore.v1.[DocumentEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html);
    import com.google.events.cloud.firestore.v1.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import io.cloudevents.CloudEvent;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    import java.util.logging.Logger;
    
    public class FirebaseFirestoreReactive implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(FirebaseFirestoreReactive.class.getName());
      private final [Firestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html) firestore;
    
      private static final String FIELD_KEY = "original";
      private static final String APPLICATION_PROTOBUF = "application/protobuf";
    
      public FirebaseFirestoreReactive() {
        this([FirestoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FirestoreOptions.html).getDefaultInstance().getService());
      }
    
      public FirebaseFirestoreReactive([Firestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html) firestore) {
        this.firestore = firestore;
      }
    
      @Override
      public void accept(CloudEvent event)
          throws [InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html), InterruptedException, ExecutionException {
        if (event.getData() == null) {
          [logger](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.MetricsUtil.html#com_google_cloud_firestore_telemetry_MetricsUtil_logger).warning("No data found in event!");
          return;
        }
    
        if (!event.getDataContentType().equals(APPLICATION_PROTOBUF)) {
          [logger](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.MetricsUtil.html#com_google_cloud_firestore_telemetry_MetricsUtil_logger).warning(String.format("Found unexpected content type %s, expected %s",
              event.getDataContentType(),
              APPLICATION_PROTOBUF));
          return;
        }
    
        [DocumentEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html) firestoreEventData = [DocumentEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html)
            .parseFrom(event.getData().[toBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Blob.html#com_google_cloud_firestore_Blob_toBytes__)());
    
        // Get the fields from the post-operation document snapshot
        // https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases.documents#Document
        Map<String, Value> fields = firestoreEventData.[getValue](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html#com_google_events_cloud_firestore_v1_DocumentEventData_getValue__)().getFieldsMap();
        if (!fields.containsKey(FIELD_KEY)) {
          [logger](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.MetricsUtil.html#com_google_cloud_firestore_telemetry_MetricsUtil_logger).warning("Document does not contain original field");
          return;
        }
        String currValue = fields.get(FIELD_KEY).getStringValue();
        String newValue = currValue.toUpperCase();
    
        if (currValue.equals(newValue)) {
          [logger](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.MetricsUtil.html#com_google_cloud_firestore_telemetry_MetricsUtil_logger).info("Value is already upper-case");
          return;
        }
    
        // Retrieve the document name from the resource path:
        // projects/{project_id}/databases/{database_id}/documents/{document_path}
        String affectedDoc = firestoreEventData.[getValue](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.firestore.v1.DocumentEventData.html#com_google_events_cloud_firestore_v1_DocumentEventData_getValue__)()
            .getName()
            .[split](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_split_com_google_cloud_firestore_pipeline_expressions_Expression_)("/documents/")[1]
            .replace("\"", "");
    
        [logger](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.MetricsUtil.html#com_google_cloud_firestore_telemetry_MetricsUtil_logger).info(String.format("Replacing values: %s --> %s", currValue, newValue));
    
        // Wait for the async call to complete
        this.firestore
            .document(affectedDoc)
            .set(Map.of(FIELD_KEY, newValue), [SetOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.SetOptions.html).merge())
            .get();
      }
    }
    

### C#
    
    
    using CloudNative.CloudEvents;
    using [Google.Cloud.Firestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.html);
    using Google.Cloud.Functions.Framework;
    using Google.Cloud.Functions.Hosting;
    using Google.Events.Protobuf.Cloud.Firestore.V1;
    using Microsoft.AspNetCore.Hosting;
    using [Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Microsoft.Extensions.DependencyInjection.html);
    using Microsoft.Extensions.Logging;
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace FirestoreReactive;
    
    public class Startup : FunctionsStartup
    {
        public override void ConfigureServices(WebHostBuilderContext context, IServiceCollection services) =>
            services.AddSingleton([FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)());
    }
    
    // Register the startup class to provide the Firestore dependency.
    [FunctionsStartup(typeof(Startup))]
    public class Function : ICloudEventFunction<DocumentEventData>
    {
        private readonly ILogger _logger;
        private readonly [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) _firestoreDb;
    
        public Function(ILogger<Function> logger, [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) firestoreDb) =>
            (_logger, _firestoreDb) = (logger, firestoreDb);
    
        public async Task HandleAsync(CloudEvent cloudEvent, DocumentEventData data, [CancellationToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Transaction.html#Google_Cloud_Firestore_Transaction_CancellationToken) cancellationToken)
        {
            // Get the recently-written value. This expression will result in a null value
            // if any of the following is true:
            // - The event doesn't contain a "new" document
            // - The value doesn't contain a field called "original"
            // - The "original" field isn't a string
            string currentValue = data.[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Value.html)?.ConvertFields().GetValueOrDefault("original") as string;
            if (currentValue is null)
            {
                _logger.LogWarning($"Event did not contain a suitable document");
                return;
            }
    
            string newValue = currentValue.ToUpperInvariant();
            if (newValue == currentValue)
            {
                _logger.LogInformation("Value is already upper-cased; no replacement necessary");
                return;
            }
    
            // The CloudEvent subject is "documents/x/y/...".
            // The Firestore SDK FirestoreDb.Document method expects a reference relative to
            // "documents" (so just the "x/y/..." part). This may be simplified over time.
            if (cloudEvent.Subject is null || !cloudEvent.Subject.StartsWith("documents/"))
            {
                _logger.LogWarning("CloudEvent subject is not a document reference.");
                return;
            }
            string documentPath = cloudEvent.Subject.Substring("documents/".[Length](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Blob.html#Google_Cloud_Firestore_Blob_Length));
    
            _logger.LogInformation("Replacing '{current}' with '{new}' in '{path}'", currentValue, newValue, documentPath);
            await _firestoreDb.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Document_System_String_)(documentPath).[UpdateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_UpdateAsync_System_Collections_Generic_IDictionary_Google_Cloud_Firestore_FieldPath_System_Object__Google_Cloud_Firestore_Precondition_System_Threading_CancellationToken_)("original", newValue, cancellationToken: cancellationToken);
        }
    }

**Note:** Updating the function-triggering Firestore document might create subsequent `updated` events, which might cascade into an infinite loop within your function. To solve this problem, use trigger types that ignore updates (such as `created`), or configure your function to only write to Firestore if the underlying value has changed.

#### Deploy the Convert to Uppercase function

If you haven't already done so, set up your [Firestore database](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#set_up_your_database).

After deploying a function, you can configure a trigger using the Google Cloud console, Google Cloud CLI, or Terraform.

###  Console 

When you use the Google Cloud console to create a function, you can also add a trigger to your function. Follow these steps to create a trigger for your function:

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click **Write a function** , and enter the function details. For more information about configuring functions during deployment, see [Deploy functions](https://docs.cloud.google.com/run/docs/deploy-functions#console).

  3. In the **Trigger** section, click **Add trigger**.

  4. Select **Firestore trigger**.

  5. In the **Eventarc trigger** pane, modify the trigger details as follows:

     1. Enter a name for the trigger in the **Trigger name** field, or use the default name.

     2. Select a **Trigger type** from the list:

        * **Google Sources** to specify triggers for Pub/Sub, Cloud Storage, Firestore, and other Google event providers.

        * **Third-party** to integrate with non-Google providers that offer an Eventarc source. For more information, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview).

     3. Select **Firestore** from the **Event provider** list, to select a product that provides the type of event for triggering your function. For the list of event providers, see [Event providers and destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).

     4. Select **type=google.cloud.firestore.document.v1.written** from the **Event type** list. Your trigger configuration varies depending on the supported event type. For more information, see [Event types](https://docs.cloud.google.com/eventarc/docs/event-types).

     5. Leave the **Event data content type** field as is. 

     6. In the **Filters** section, select a database, operation and attribute values, or use the default selections. If you named your database, enter the name in the **Attribute value 1** field. 

     7. If the **Region** field is enabled, select a [location](https://docs.cloud.google.com/eventarc/docs/overview#trigger-location) for the Eventarc trigger. In general, the location of an Eventarc trigger should match the location of the Google Cloud resource that you want to monitor for events. In most scenarios, you should also deploy your function in the same region. See [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations) for more details about Eventarc trigger locations.

     8. In the **Service account** field, select a service account. Eventarc triggers are linked to service accounts to use as an identity when invoking your function. Your Eventarc trigger's service account must have the permission to invoke your function. By default, Cloud Run uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

     9. Optionally, specify the **Service URL path** to send the incoming request to. This is the relative path on the destination service to which the events for the trigger should be sent. For example: `/`, `/route`, `route`, and `route/subroute`.

     10. Optionally, to enable retries if the delivery attempt fails, select the **Enable retry on failure** checkbox; otherwise, the default behavior is a single delivery attempt with no retries. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events).

  6. Once you've completed the required fields, click **Save trigger**.

  7. Click **Create**.

  8. In the **Source** tab, edit the source code if needed, then select **Save and redeploy**.




###  gcloud 

When you create a function using the gcloud CLI, you must first [deploy](https://docs.cloud.google.com/run/docs/deploy-functions) your function, and then create a trigger. Follow these steps to create a trigger for your function:

  1. Run the following command in the directory that contains the sample code to deploy your function:
         
         gcloud run deploy FUNCTION \
             --source . \
             --function FUNCTION_ENTRYPOINT \
             --base-image BASE_IMAGE_ID \
             --region REGION
         

Replace the following:

     * `FUNCTION`: the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

     * `FUNCTION_ENTRYPOINT`: the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.

     * `BASE_IMAGE_ID`: the base image environment for your function. For more details about base images and the packages included in each image, see [Runtimes base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

     * `REGION`: the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) where you want to deploy your function. For example, `europe-west1`.

  2. Run the following command to create a trigger that filters and routes events:
         
         gcloud eventarc triggers create TRIGGER_NAME  \
             --location=LOCATION \
             --destination-run-service=FUNCTION  \
             --destination-run-region=DESTINATION_RUN_REGION \
             --event-filters=type=google.cloud.firestore.document.v1.written \
             --event-filters=database='(default)' \
             --event-data-content-type=application/protobuf \
             --event-filters-path-pattern=document='messages/{pushId}' \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         

Replace the following:

     * `TRIGGER_NAME`: the ID of the trigger or a fully qualified identifier.
     * `LOCATION`: the location of the Eventarc trigger. Alternatively, you can set the `eventarc/location` property; for example, `gcloud config set eventarc/location us-central1`. 

To avoid any performance and data residency issues, the location must match the location of the Google Cloud service that is generating events. For more information, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

     * `FUNCTION`: the name of the deployed Cloud Run function that receives the events for the trigger. 
     * `DESTINATION_RUN_REGION`: (optional) the [Cloud Run location](https://docs.cloud.google.com/run/docs/locations) in which the destination Cloud Run function can be found. If not specified, it is assumed that the function is in the same region as the trigger. 
     * `EVENT_FILTER_TYPE`: the identifier of the event. An event is generated when an API call for the method succeeds. For long-running operations, the event is only generated at the end of the operation, and only if the action is performed successfully. For a list of supported event types, see [Google event types supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source). 
     * `SERVICE_ACCOUNT_NAME`: the name of your user-managed service account. 
     * `PROJECT_ID`: your Google Cloud project ID. 

Notes:

     * After a trigger is created, the event filter type can't be changed. For a different event type, you must create a new trigger. 
     * `--event-filters=type=google.cloud.firestore.document.v1.written` specifies that the function is triggered when a document is created, updated or deleted, per the [event type](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#event_types).
     * `--event-filters=database='(default)'` specifies the Firebase database. For the default database name, use `(default)`.
     * `--event-filters-path-pattern=document='users/{username}'` provides the path pattern of the documents that should be monitored for relevant changes. This path pattern states that all documents in the `users` collection should be monitored. For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).
     * Optionally, to specify a single event delivery attempt with no retries, use the `--max-retry-attempts` flag. The only valid value is `1`. If you omit the flag, the standard retry behavior applies. For more information, see [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events). 
     * Other flags are available. For more information, see [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create). 



###  Terraform 

To create an Eventarc trigger for a Cloud Run function, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).

Use the other fields as is:

  * `--event-filters=type=google.cloud.firestore.document.v1.written` specifies that the function is triggered when a document is created, updated or deleted, per the `google.cloud.firestore.document.v1.written` [event type](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#event_types).
  * `--event-filters=database='(default)'` specifies the Firestore database. For the default database name, use `(default)`.
  * `--event-filters-path-pattern=document='messages/{pushId}'` provides the path pattern of the documents that should be monitored for relevant changes. This path pattern states that all documents in the `messages` collection should be monitored. For more information, see [Understand path patterns](https://docs.cloud.google.com/eventarc/docs/path-patterns).



#### Test the Convert to Uppercase function

To test the Convert to Uppercase function you just deployed, set up a collection called `messages` in your [Firestore database](https://docs.cloud.google.com/run/docs/triggering/firestore-triggers#set_up_your_database):

  1. In the Google Cloud console, go to the Firestore databases page:

[Go to Firestore](https://console.cloud.google.com/firestore/databases)

  2. Select the Database ID for your Firestore database.

  3. Click **Start a collection**.

  4. Specify `messages` as the collection ID.

  5. To start adding the collection's first document, under **Add its first document** accept the auto-generated **Document ID**.

  6. To trigger your deployed function, add a document where the **Field name** is `original` and the **Field value** is `minka`.

  7. When you save the document, you can see the lowercase word in the value field convert to uppercase.

If you subsequently edit the field value to contain lowercase letters, that triggers the function again, converting all lowercase letters to uppercase.




## Limitations for functions

  * Ordering is not guaranteed. Rapid changes can trigger function invocations in an unexpected order.
  * Events are delivered at least once, but a single event may result in multiple function invocations. Avoid depending on exactly-once mechanics, and write [idempotent functions](https://cloud.google.com/blog/products/serverless/cloud-functions-pro-tips-building-idempotent-functions).
  * A trigger is associated with a single database. You cannot create a trigger that matches multiple databases.
  * Deleting a database does not automatically delete any triggers for that database. The trigger stops delivering events but continues to exist until you [delete the trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
