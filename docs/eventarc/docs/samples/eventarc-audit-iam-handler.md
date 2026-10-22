---
url: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-audit-iam-handler/
title: Create an event handler that receives and processes a Cloud Audit Log event with IAM data \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:07.396785+00:00
---

# Create an event handler that receives and processes a Cloud Audit Log event with IAM data  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-audit-iam-handler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Samples ](https://docs.cloud.google.com/eventarc/docs/samples)



#  Create an event handler that receives and processes a Cloud Audit Log event with IAM data Stay organized with collections  Save and categorize content based on your preferences. 

Creates an event handler that receives an incoming Cloud Audit Log event within an HTTP POST request as a CloudEvent.

## Code sample

### Go

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Processes CloudEvents containing Cloud Audit Logs for IAM
    package main
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    
    	cloudevent "github.com/cloudevents/sdk-go/v2"
    	"github.com/googleapis/google-cloudevents-go/cloud/auditdata"
    	"google.golang.org/protobuf/encoding/protojson"
    )
    
    func HandleCloudEvent(w http.ResponseWriter, r *http.Request) {
    	// Transform the HTTP request into a CloudEvent
    	event, err := cloudevent.NewEventFromHTTPRequest(r)
    	if err != nil {
    		w.WriteHeader(http.StatusBadRequest)
    		fmt.Fprintln(w, "Failed to create CloudEvent from request.")
    		log.Fatal("cloudevent.NewEventFromHTTPRequest:", err)
    	}
    
    	// Extract the LogEntryData from the CloudEvent
    	var logentry auditdata.LogEntryData
    	// AuditLog objects include a `@type` annotation, which errors when using
    	// `protojson.Unmarshal`. UnmarshalOptions prevents this error.
    	umo := &protojson.UnmarshalOptions{DiscardUnknown: true}
    	err = umo.Unmarshal(event.Data(), &logentry)
    	if err != nil {
    		w.WriteHeader(http.StatusBadRequest)
    		fmt.Fprintln(w, "Failed to parse Audit Log")
    		log.Fatal("protojson.Unmarshal:", err)
    	}
    
    	// Extract relevant fields from the audit log entry.
    	// Identify the user that requested key creation
    	actor := logentry.ProtoPayload.AuthenticationInfo.PrincipalEmail
    
    	// Extract the resource name from the CreateServiceAccountKey request
    	// For details of this type, see https://cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#createserviceaccountkeyrequest
    	principal := logentry.ProtoPayload.GetRequest().AsMap()["name"]
    
    	// The response is of type google.iam.admin.v1.ServiceAccountKey,
    	// which is described at https://cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.ServiceAccountKey
    	// This key path can be used with gcloud to disable/delete the key:
    	// e.g. gcloud iam service-accounts keys disable ${keypath}
    	keypath := logentry.ProtoPayload.GetResponse().AsMap()["name"]
    
    	s := fmt.Sprintf("New Service Account Key created for %s by %s: %v", principal, actor, keypath)
    	log.Print(s)
    	fmt.Fprintln(w, s)
    }
    

### Python

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    @app.route("/", methods=["POST"])
    def index():
        # Transform the HTTP request into a CloudEvent
        event = from_http(request.headers, request.get_data())
    
        # Extract the LogEntryData from the CloudEvent
        # The LogEntryData type is described at https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
        # re-serialize to json, to convert the json-style 'lowerCamelCase' names to the protobuf-style 'snake_case' equivalents.
        # ignore_unknown_fields is needed to skip the '@type' fields.
        log_entry = LogEntryData.from_json(
            json.dumps(event.get_data()), ignore_unknown_fields=True
        )
    
        # Ensure that this event is for service accout key creation, and succeeded.
        if log_entry.proto_payload.service_name != "iam.googleapis.com":
            return ("Received event was not from IAM.", 400)
        if log_entry.proto_payload.status.code != 0:
            return ("Key creation failed, not reporting.", 204)
    
        # Extract relevant fields from the audit log entry.
        # Identify the user that requested key creation
        user = log_entry.proto_payload.authentication_info.principal_email
    
        # Extract the resource name from the CreateServiceAccountKey request
        # For details of this type, see https://cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#createserviceaccountkeyrequest
        service_account = log_entry.proto_payload.request["name"]
    
        # The response is of type google.iam.admin.v1.ServiceAccountKey,
        # which is described at https://cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.ServiceAccountKey
        # This key path can be used with gcloud to disable/delete the key:
        # e.g. gcloud iam service-accounts keys disable ${keypath}
        keypath = log_entry.proto_payload.response["name"]
    
        print(f"New Service Account Key created for {service_account} by {user}: {keypath}")
        return (
            f"New Service Account Key created for {service_account} by {user}: {keypath}",
            200,
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=eventarc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
