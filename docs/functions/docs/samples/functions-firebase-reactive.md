---
url: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-reactive/
title: React to value change by updating a value \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:50.670086+00:00
---

# React to value change by updating a value  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-reactive/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  React to value change by updating a value Stay organized with collections  Save and categorize content based on your preferences. 

Updates a value whenever it is changed in Firestore.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Google Cloud Firestore triggers (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/calling/cloud-firestore-1st-gen)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using [Google.Cloud.Firestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.html);
    using Google.Cloud.Functions.Framework;
    using Google.Cloud.Functions.Hosting;
    using Google.Events.Protobuf.Cloud.Firestore.V1;
    using Microsoft.AspNetCore.Hosting;
    using [Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Microsoft.Extensions.DependencyInjection.html);
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

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    FunctionsFramework.on_startup do
      # Lazily construct a Firestore client when needed, and reuse it on
      # subsequent calls.
      set_global :firestore_client do
        require "google/cloud/firestore"
        Google::Cloud::[Firestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin/latest/Google-Cloud-Firestore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore.html) project_id: ENV["GOOGLE_CLOUD_PROJECT"]
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
