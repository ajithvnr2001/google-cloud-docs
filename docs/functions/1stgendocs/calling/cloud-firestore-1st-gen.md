---
url: https://docs.cloud.google.com/functions/1stgendocs/calling/cloud-firestore-1st-gen/
title: Google Cloud Firestore triggers (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:37.476742+00:00
---

# Google Cloud Firestore triggers (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/calling/cloud-firestore-1st-gen/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Cloud Firestore triggers (1st gen)

Cloud Run functions can handle events in Firestore in the same Google Cloud project as the function. You can read or update Firestore in response to these events using the [Firestore APIs and client libraries](https://docs.cloud.google.com/firestore/docs/apis).

In a typical lifecycle, a Firestore function does the following:

  1. Waits for changes to a particular document.

  2. Triggers when an event occurs and performs its tasks.

  3. Receives a data object with a snapshot of the affected document. For `write` or `update` events, the data object contains snapshots representing document state before and after the triggering event.




## Event types

Firestore supports `create`, `update`, `delete`, and `write` events. The `write` event encompasses all modifications to a document.

Event type | Trigger  
---|---  
`providers/cloud.firestore/eventTypes/document.create` (default) | Triggered when a document is written to for the first time.  
`providers/cloud.firestore/eventTypes/document.update` | Triggered when a document already exists and has any value changed.  
`providers/cloud.firestore/eventTypes/document.delete` | Triggered when a document with data is deleted.  
`providers/cloud.firestore/eventTypes/document.write` | Triggered when a document is created, updated or deleted.  
**Note:** Triggers happen at the document-level. It is not possible to create a trigger for a specific field only.

Wildcards are written in triggers using curly braces, as follows: `"projects/YOUR_PROJECT_ID/databases/(default)/documents/collection/{document_wildcard}"`

### Specifying the document path

To trigger your function, specify a document path to listen to. Functions only respond to document changes, and cannot monitor specific fields or [collections](https://firebase.google.com/docs/firestore/data-model#collections). Below are a few examples of valid document paths:

  * `users/marie`: valid trigger. Monitors a single document, `/users/marie`.

  * `users/{username}`: valid trigger. Monitors all user documents. Wildcards are used to monitor all documents in the collection.

  * `users/{username}/addresses`: _invalid_ trigger. Refers to the subcollection `addresses`, not a document.

  * `users/{username}/addresses/home`: valid trigger. Monitors the home address document for all users.

  * `users/{username}/addresses/{addressId}`: valid trigger. Monitors all address documents.




#### Using wildcards and parameters

If you do not know the specific document you want to monitor, use a `{wildcard}` instead of the document ID:

  * `users/{username}` listens for changes to all user documents.



In this example, when any field on any document in `users` is changed, it matches a wildcard called `{username}`.

If a document in `users` has [subcollections](https://docs.cloud.google.com/firestore/docs/concepts/structure-data#subcollections), and a field in one of those subcollections' documents is changed, the `{username}` wildcard is _not_ triggered.

Wildcard matches are extracted from document paths. You can define as many wildcards as you like to substitute explicit collection or document IDs.

## Event structure

This trigger invokes your function with an event similar to the one shown below: 
    
    
    {
        "oldValue": { // Update and Delete operations only
            A [Document](https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents) object containing a pre-operation document snapshot
        },
        "updateMask": { // Update operations only
            A [DocumentMask](https://firebase.google.com/docs/firestore/reference/rest/v1beta1/DocumentMask) object that lists changed fields.
        },
        "value": {
            // A [Document](https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents) object containing a post-operation document snapshot
        }
    }

Each `Document` object contains one or more `Value` objects. See the [`Value` documentation](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/Value) for type references. This is especially useful if you're using a typed language (like Go) to write your functions.

## Code sample

The sample Cloud Function below prints the fields of a triggering Cloud Firestore event:

###  Node.js 
    
    
    /**
     * Background Function triggered by a change to a Firestore document.
     *
     * @param {!Object} event The Cloud Functions event.
     * @param {!Object} context Cloud Functions event metadata.
     */
    exports.helloFirestore = (event, context) => {
      const triggerResource = context.resource;
    
      console.log(`Function triggered by event on: ${triggerResource}`);
      console.log(`Event type: ${context.eventType}`);
    
      if (event.oldValue && Object.keys(event.oldValue).length) {
        console.log('\nOld value:');
        console.log(JSON.stringify(event.oldValue, null, 2));
      }
    
      if (event.value && Object.keys(event.value).length) {
        console.log('\nNew value:');
        console.log(JSON.stringify(event.value, null, 2));
      }
    };

###  Python 
    
    
    import json
    
    def hello_firestore(data, context):
        """Triggered by a change to a Firestore document.
        Args:
            data (dict): The event payload.
            context (google.cloud.functions.Context): Metadata for the event.
        """
        trigger_resource = context.resource
    
        print("Function triggered by change to: %s" % trigger_resource)
    
        print("\nOld value:")
        print(json.dumps(data["oldValue"]))
    
        print("\nNew value:")
        print(json.dumps(data["value"]))
    
    

###  Go 
    
    
    // Package hello contains a Cloud Function triggered by a Firestore event.
    package hello
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	"cloud.google.com/go/functions/metadata"
    )
    
    // FirestoreEvent is the payload of a Firestore event.
    type FirestoreEvent struct {
    	OldValue   FirestoreValue `json:"oldValue"`
    	Value      FirestoreValue `json:"value"`
    	UpdateMask struct {
    		FieldPaths []string `json:"fieldPaths"`
    	} `json:"updateMask"`
    }
    
    // FirestoreValue holds Firestore fields.
    type FirestoreValue struct {
    	CreateTime time.Time `json:"createTime"`
    	// Fields is the data for this value. The type depends on the format of your
    	// database. Log the interface{} value and inspect the result to see a JSON
    	// representation of your database fields.
    	Fields     interface{} `json:"fields"`
    	Name       string      `json:"name"`
    	UpdateTime time.Time   `json:"updateTime"`
    }
    
    // HelloFirestore is triggered by a change to a Firestore document.
    func HelloFirestore(ctx context.Context, e FirestoreEvent) error {
    	meta, err := metadata.[FromContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Metadata_FromContext)(ctx)
    	if err != nil {
    		return fmt.Errorf("metadata.FromContext: %w", err)
    	}
    	log.Printf("Function triggered by change to: %v", meta.[Resource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Resource))
    	log.Printf("Old value: %+v", e.OldValue)
    	log.Printf("New value: %+v", e.Value)
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.functions.Context;
    import com.google.cloud.functions.RawBackgroundFunction;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import java.util.logging.Logger;
    
    public class FirebaseFirestore implements RawBackgroundFunction {
      private static final Logger logger = Logger.getLogger(FirebaseFirestore.class.getName());
    
      // Use GSON (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      @Override
      public void accept(String json, Context context) {
        JsonObject body = gson.fromJson(json, JsonObject.class);
        logger.info("Function triggered by event on: " + context.resource());
        logger.info("Event type: " + context.eventType());
    
        if (body != null && body.has("oldValue")) {
          logger.info("Old value:");
          logger.info(body.get("oldValue").getAsString());
        }
    
        if (body != null && body.has("value")) {
          logger.info("New value:");
          logger.info(body.get("value").getAsString());
        }
      }
    }
    

###  C# 
    
    
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

###  Ruby 
    
    
    require "functions_framework"
    
    # Triggered by a change to a Firestore document.
    FunctionsFramework.cloud_event "hello_firestore" do |event|
      # The event parameter is a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      payload = event.data
    
      logger.info "Function triggered by change to: #{event.source}"
      logger.info "Old value: #{payload['oldValue']}"
      logger.info "New value: #{payload['value']}"
    end

###  PHP 
    
    
    use Google\CloudFunctions\CloudEvent;
    
    function firebaseFirestore(CloudEvent $cloudevent)
    {
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
    
        fwrite($log, 'Event: ' . $cloudevent->getId() . PHP_EOL);
        fwrite($log, 'Event Type: ' . $cloudevent->getType() . PHP_EOL);
    
        $data = $cloudevent->getData();
    
        $resource = $data['resource'];
        fwrite($log, 'Function triggered by event on: ' . $resource . PHP_EOL);
    
        if (isset($data['oldValue'])) {
            fwrite($log, 'Old value: ' . json_encode($data['oldValue']) . PHP_EOL);
        }
    
        if (isset($data['value'])) {
            fwrite($log, 'New value: ' . json_encode($data['value']) . PHP_EOL);
        }
    }

The example below retrieves the value added by the user, converts the string at that location to uppercase, and replaces the value with the uppercase string:

###  Node.js 
    
    
    const Firestore = require('[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)');
    
    const firestore = new [Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore.html)({
      projectId: process.env.GOOGLE_CLOUD_PROJECT,
    });
    
    // Converts strings added to /messages/{pushId}/original to uppercase
    exports.makeUpperCase = event => {
      const resource = event.value.name;
      const affectedDoc = firestore.doc(resource.split('/documents/')[1]);
    
      const curValue = event.value.fields.original.stringValue;
      const newValue = curValue.toUpperCase();
    
      if (curValue !== newValue) {
        console.log(`Replacing value: ${curValue} --> ${newValue}`);
    
        return affectedDoc.set({
          original: newValue,
        });
      } else {
        // Value is already upper-case
        // Don't perform a(nother) write to avoid infinite loops
        console.log('Value is already upper-case.');
      }
    };

###  Python 
    
    
    from google.cloud import firestore
    
    client = firestore.[Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html)()
    
    
    # Converts strings added to /messages/{pushId}/original to uppercase
    def make_upper_case(data, context):
        path_parts = context.resource.split("/documents/")[1].split("/")
        collection_path = path_parts[0]
        document_path = "/".join(path_parts[1:])
    
        affected_doc = client.[collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html#google_cloud_firestore_v1_client_Client_collection)(collection_path).document(document_path)
    
        cur_value = data["value"]["fields"]["original"]["stringValue"]
        new_value = cur_value.upper()
    
        if cur_value != new_value:
            print(f"Replacing value: {cur_value} --> {new_value}")
            affected_doc.set({"original": new_value})
        else:
            # Value is already upper-case
            # Don't perform a second write (which can trigger an infinite loop)
            print("Value is already upper-case.")
    
    

###  Go 
    
    
    // Package upper contains a Firestore Cloud Function.
    package upper
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"os"
    	"strings"
    	"time"
    
    	"cloud.google.com/go/firestore"
    	firebase "firebase.google.com/go/v4"
    )
    
    // FirestoreEvent is the payload of a Firestore event.
    type FirestoreEvent struct {
    	OldValue   FirestoreValue `json:"oldValue"`
    	Value      FirestoreValue `json:"value"`
    	UpdateMask struct {
    		FieldPaths []string `json:"fieldPaths"`
    	} `json:"updateMask"`
    }
    
    // FirestoreValue holds Firestore fields.
    type FirestoreValue struct {
    	CreateTime time.Time `json:"createTime"`
    	// Fields is the data for this value. The type depends on the format of your
    	// database. Log an interface{} value and inspect the result to see a JSON
    	// representation of your database fields.
    	Fields     MyData    `json:"fields"`
    	Name       string    `json:"name"`
    	UpdateTime time.Time `json:"updateTime"`
    }
    
    // MyData represents a value from Firestore. The type definition depends on the
    // format of your database.
    type MyData struct {
    	Original struct {
    		StringValue string `json:"stringValue"`
    	} `json:"original"`
    }
    
    // GOOGLE_CLOUD_PROJECT is automatically set by the Cloud Functions runtime.
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
    }
    
    // MakeUpperCase is triggered by a change to a Firestore document. It updates
    // the `original` value of the document to upper case.
    func MakeUpperCase(ctx context.Context, e FirestoreEvent) error {
    	fullPath := strings.[Split](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Expression_Split)(e.[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/apiv1/firestorepb.html#cloud_google_com_go_firestore_apiv1_firestorepb_Value).Name, "/documents/")[1]
    	pathParts := strings.[Split](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Expression_Split)(fullPath, "/")
    	collection := pathParts[0]
    	doc := strings.[Join](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Expression_Join)(pathParts[1:], "/")
    
    	curValue := e.[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/apiv1/firestorepb.html#cloud_google_com_go_firestore_apiv1_firestorepb_Value).[Fields](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Fields).Original.StringValue
    	newValue := strings.[ToUpper](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_Expression_ToUpper)(curValue)
    	if curValue == newValue {
    		log.Printf("%q is already upper case: skipping", curValue)
    		return nil
    	}
    	log.Printf("Replacing value: %q -> %q", curValue, newValue)
    
    	data := map[string]string{"original": newValue}
    	_, err := client.Collection(collection).Doc(doc).Set(ctx, data)
    	if err != nil {
    		return fmt.Errorf("Set: %w", err)
    	}
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.firestore.[Firestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html);
    import com.google.cloud.firestore.[FirestoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FirestoreOptions.html);
    import com.google.cloud.firestore.[SetOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.SetOptions.html);
    import com.google.cloud.functions.[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.TraceUtil.Context.html);
    import com.google.cloud.functions.RawBackgroundFunction;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import java.util.HashMap;
    import java.util.Locale;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    import java.util.logging.Level;
    import java.util.logging.Logger;
    
    public class FirebaseFirestoreReactive implements RawBackgroundFunction {
    
      // Use GSON (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      private static final Logger logger = Logger.getLogger(FirebaseFirestoreReactive.class.getName());
      private static final [Firestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html) FIRESTORE = [FirestoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FirestoreOptions.html).getDefaultInstance().getService();
    
      private final [Firestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html) firestore;
    
      public FirebaseFirestoreReactive() {
        this(FIRESTORE);
      }
    
      FirebaseFirestoreReactive([Firestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html) firestore) {
        this.firestore = firestore;
      }
    
      @Override
      public void accept(String json, [Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.TraceUtil.Context.html) context) {
        // Get the recently-written value
        JsonObject body = gson.fromJson(json, JsonObject.class);
        JsonObject tempJson = body.getAsJsonObject("value");
    
        // Verify that value.fields.original.stringValue exists
        String currentValue = null;
        if (tempJson != null) {
          tempJson = tempJson.getAsJsonObject("fields");
        }
        if (tempJson != null) {
          tempJson = tempJson.getAsJsonObject("original");
        }
        if (tempJson != null && tempJson.has("stringValue")) {
          currentValue = tempJson.get("stringValue").getAsString();
        }
        if (currentValue == null) {
          throw new IllegalArgumentException("Malformed JSON: " + json);
        }
    
        // Convert recently-written value to ALL CAPS
        String newValue = currentValue.toUpperCase(Locale.getDefault());
    
        // Update Firestore DB with ALL CAPS value
        Map<String, String> newFields = Map.of("original", newValue);
    
        String affectedDoc = context.resource().[split](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_split_com_google_cloud_firestore_pipeline_expressions_Expression_)("/documents/")[1].replace("\"", "");
    
        if (!currentValue.equals(newValue)) {
          // The stored value needs to be updated
          // Write the upper-cased value to Firestore
          [logger](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.MetricsUtil.html#com_google_cloud_firestore_telemetry_MetricsUtil_logger).info(String.format("Replacing value: %s --> %s", currentValue, newValue));
          try {
            FIRESTORE.[document](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_document_java_lang_String_)(affectedDoc).set(newFields, [SetOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.SetOptions.html).[merge](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.SetOptions.html#com_google_cloud_firestore_SetOptions_merge__)()).get();
          } catch (ExecutionException | InterruptedException e) {
            [logger](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.MetricsUtil.html#com_google_cloud_firestore_telemetry_MetricsUtil_logger).[log](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_log_com_google_cloud_firestore_pipeline_expressions_Expression_com_google_cloud_firestore_pipeline_expressions_Expression_)(Level.SEVERE, "Error updating Firestore document: " + e.getMessage(), e);
          }
        } else {
          // The stored value is already upper-case, and doesn't need updating.
          // (Don't perform a "second" write, since that could trigger an infinite loop.)
          [logger](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.telemetry.MetricsUtil.html#com_google_cloud_firestore_telemetry_MetricsUtil_logger).info(String.format("Value is already upper-case."));
        }
      }
    }
    

###  C# 
    
    
    using CloudNative.CloudEvents;
    using [Google.Cloud.Firestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.html);
    using Google.Cloud.Functions.Framework;
    using Google.Cloud.Functions.Hosting;
    using Google.Events.Protobuf.Cloud.Firestore.V1;
    using Microsoft.AspNetCore.Hosting;
    using [Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Microsoft.Extensions.DependencyInjection.html);
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

###  Ruby 
    
    
    require "functions_framework"
    
    FunctionsFramework.on_startup do
      # Lazily construct a Firestore client when needed, and reuse it on
      # subsequent calls.
      set_global :firestore_client do
        require "google/cloud/firestore"
        Google::Cloud::[Firestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore.html) project_id: ENV["GOOGLE_CLOUD_PROJECT"]
      end
    end
    
    # Converts strings added to /messages/{pushId}/original to uppercase
    FunctionsFramework.cloud_event "make_upper_case" do |event|
      # Event-triggered Ruby functions receive a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      # The Firebase event payload can be obtained from the event data.
      cur_value = event.data["value"]["fields"]["original"]["stringValue"]
    
      # Compute new value and determine whether it needs to be modified.
      # If the value is already upper-case, don't perform another write,
      # to avoid infinite loops.
      new_value = cur_value.upcase
      if cur_value == new_value
        logger.info "Value is already upper-case"
        return
      end
    
      # Use the Firestore client library to update the value.
      # The document name can be obtained from the event subject.
      logger.info "Replacing value: #{cur_value} --> #{new_value}"
      doc_name = event.subject.split("documents/").last
      affected_doc = global(:firestore_client).doc doc_name
      new_doc_data = { original: new_value }
      affected_doc.set new_doc_data, merge: false
    end

###  PHP 
    
    
    use Google\Cloud\Firestore\FirestoreClient;
    use Google\CloudFunctions\CloudEvent;
    
    function firebaseReactive(CloudEvent $cloudevent)
    {
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
        $data = $cloudevent->getData();
    
        $resource = $data['value']['name'];
    
        $db = new FirestoreClient();
    
        $docPath = explode('/documents/', $resource)[1];
    
        $affectedDoc = $db->document($docPath);
    
        $curValue = $data['value']['fields']['original']['stringValue'];
        $newValue = strtoupper($curValue);
    
        if ($curValue !== $newValue) {
            fwrite($log, 'Replacing value: ' . $curValue . ' --> ' . $newValue . PHP_EOL);
    
            $affectedDoc->set(['original' => $newValue]);
        } else {
            // Value is already upper-case
            // Don't perform another write (it might cause an infinite loop)
            fwrite($log, 'Value is already upper-case.' . PHP_EOL);
        }
    }

**Note:** Updating the function-triggering Firestore document may create subsequent `update` events, which may cascade into an infinite loop within your function. To solve this problem, use trigger types that ignore updates (such as `document.create`), or configure your function to only write to Firestore if the underlying value has changed.

## Deploying your function

The following `gcloud` command deploys a function that is triggered by write events on the document `/messages/{pushId}`:
    
    
    gcloud functions deploy FUNCTION_NAME \
      --no-gen2 \
      --entry-point ENTRY_POINT \
      --runtime RUNTIME \
      --set-env-vars GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID \
      --trigger-event "providers/cloud.firestore/eventTypes/document.write" \
      --trigger-resource "projects/YOUR_PROJECT_ID/databases/(default)/documents/messages/{pushId}"

**Note:** When you deploy a function using the Google Cloud CLI, the command must include the name of the function contained in your code that you want the `deploy` command to execute. You can specify that function using either `FUNCTION_NAME` or the optional `--entry-point` flag, depending on the needs of your implementation. See the [deployment guide](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics) for more discussion.Argument | Description  
---|---  
`FUNCTION_NAME` | The registered name of the Cloud Function you are deploying. This can either be the name of a function in your source code, or an arbitrary string. If FUNCTION_NAME is an arbitrary string, then you must include the `--entry-point` flag.   
`--entry-point ENTRY_POINT` | The name of a function or class in your source code. Optional, unless you did not use `FUNCTION_NAME` to specify the function in your source code to be executed during deployment. In that case, you must use `--entry-point` to supply the name of the executable function.   
`--runtime RUNTIME` | The name of the runtime you are using. For a complete list, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime).   
`--set-env-vars GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID` | The unique identifier of the project as a runtime environment variable.   
`--trigger-event NAME` | The event type that the function will monitor for (one of `write`, `create`, `update` or `delete`).   
`--trigger-resource NAME` | The fully qualified database path to which the function will listen. This should conform to the following format: `"projects/YOUR_PROJECT_ID/databases/(default)/documents/PATH"` The `{pushId}` text is a wildcard parameter described above in Specifying the document path.   
  
## Limitations

Note the following limitations for Firestore triggers for Cloud Run functions:

  * Cloud Run functions (1st gen) prerequisites an existing "(default)" database in Firestore native mode. It does not support Firestore named databases or Datastore mode. Please use Cloud Run functions (2nd gen) to configure events in such cases.
  * Cross project setup with Cloud Run functions and Firestore trigger is a limitation. To setup Firestore trigger Cloud Run functions must be in the same project. 
  * Ordering is not guaranteed. Rapid changes can trigger function invocations in an unexpected order.
  * Events are delivered at least once, but a single event may result in multiple function invocations. Avoid depending on exactly-once mechanics, and write [idempotent functions](https://cloud.google.com/blog/products/serverless/cloud-functions-pro-tips-building-idempotent-functions).
  * [Firestore in Datastore mode](https://cloud.google.com/firestore/docs/firestore-or-datastore) requires Cloud Run functions (2nd gen). Cloud Run functions (1st gen) does not support Datastore mode.
  * A trigger is associated with a single database. You cannot create a trigger that matches multiple databases.
  * Deleting a database does not automatically delete any triggers for that database. The trigger stops delivering events but continues to exist until you [delete the trigger](https://cloud.google.com/eventarc/docs/managing-triggers#trigger-delete).
  * If a matched event exceeds the [maximum request size](https://cloud.google.com/functions/quotas#resource_limits), the event might not be delivered to Cloud Run functions (1st gen). 
    * Events not delivered because of request size are logged in [platform logs](https://cloud.google.com/logging/docs/api/platform-logs) and count towards the log usage for the project. 
    * You can find these logs in the Logs Explorer with the message "Event cannot deliver to Cloud function due to size exceeding the limit for 1st gen..." of `error` severity. You can find the function name under the `functionName` field. If the `receiveTimestamp` field is still within an hour from now, you can infer the actual event content by reading the document in question with a snapshot before and after the timestamp.
    * To avoid such cadence, you can: 
      * Migrate and upgrade to Cloud Run functions (2nd gen)
      * Downsize the document
      * Delete the Cloud Run functions in question
    * You can turn off the logging itself using [exclusions](https://cloud.google.com/logging/docs/routing/overview#exclusions) but note that the offending events will still not be delivered.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
