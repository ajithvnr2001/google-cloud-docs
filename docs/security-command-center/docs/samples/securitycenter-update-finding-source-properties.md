---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-finding-source-properties/
title: Update finding source properties \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:10.918152+00:00
---

# Update finding source properties  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-finding-source-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Update finding source properties Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to update source properties for a finding

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"github.com/golang/protobuf/ptypes"
    	structpb "github.com/golang/protobuf/ptypes/struct"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // updateFindingSourceProperties demonstrates how to update a security finding
    // in CSCC. findingName is the full resource name of the finding to update.
    func updateFindingSourceProperties(w io.Writer, findingName string) error {
    	// findingName := "organizations/111122222444/sources/1234/findings/findingid"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    	// Use now as the eventTime for the security finding.
    	eventTime, err := ptypes.TimestampProto(time.Now())
    	if err != nil {
    		return fmt.Errorf("TimestampProto: %w", err)
    	}
    
    	req := &securitycenterpb.UpdateFindingRequest{
    		Finding: &securitycenterpb.Finding{
    			Name:      findingName,
    			EventTime: eventTime,
    			SourceProperties: map[string]*structpb.Value{
    				"s_value": {
    					Kind: &structpb.Value_StringValue{StringValue: "new_string_example"},
    				},
    			},
    		},
    		// Needed to only update the specific source property s_value
    		// and EventTime. EventTime is a required field.
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"event_time", "source_properties.s_value"},
    		},
    	}
    
    	finding, err := client.UpdateFinding(ctx, req)
    	if err != nil {
    		return fmt.Errorf("UpdateFinding: %w", err)
    	}
    	fmt.Fprintf(w, "Finding updated: %s\n", finding.Name)
    	fmt.Fprintf(w, "Finding state: %v\n", finding.State)
    	fmt.Fprintf(w, "Event time (Epoch Seconds): %d\n", eventTime.Seconds)
    	fmt.Fprintf(w, "Source Properties:\n")
    	for k, v := range finding.SourceProperties {
    		fmt.Fprintf(w, "%s = %v\n", k, v)
    	}
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static Finding updateFinding(FindingName findingName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // FindingName findingName = FindingName.of(/*organization=*/"123234324",
        // /*source=*/"423432321", /*findingId=*/"samplefindingid2");
    
        // Use the current time as the finding "event time".
        Instant eventTime = Instant.now();
    
        // Define source properties values as protobuf "Value" objects.
        Value stringValue = Value.newBuilder().setStringValue("value").build();
    
        FieldMask updateMask =
            FieldMask.newBuilder()
                .addPaths("event_time")
                .addPaths("source_properties.stringKey")
                .build();
    
        Finding finding =
            Finding.newBuilder()
                .setName(findingName.toString())
                .setEventTime(
                    Timestamp.newBuilder()
                        .setSeconds(eventTime.getEpochSecond())
                        .setNanos(eventTime.getNano()))
                .putSourceProperties("stringKey", stringValue)
                .build();
    
        UpdateFindingRequest.Builder request =
            UpdateFindingRequest.newBuilder().setFinding(finding).setUpdateMask(updateMask);
    
        // Call the API.
        Finding response = client.updateFinding(request.build());
    
        System.out.println("Updated Finding: " + response);
        return response;
      } catch (IOException e) {
        throw new RuntimeException("Couldn't create client.", e);
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)');
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // findingName is the full resource name of the finding to update.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // const findingName =
    // "organizations/111122222444/sources/1234/findings/findingid";
    
    // Use now as the eventTime for the security finding.
    const eventTime = new Date();
    console.log(findingName);
    async function updateFinding() {
      const [newFinding] = await client.updateFinding({
        updateMask: {paths: ['event_time', 'source_properties.s_value']},
        finding: {
          name: findingName,
          // The time associated with discovering the issue.
          eventTime: {
            seconds: Math.floor(eventTime.getTime() / 1000),
            nanos: (eventTime.getTime() % 1000) * 1e6,
          },
          sourceProperties: {
            s_value: {stringValue: 'new_string_example'},
          },
        },
      });
      console.log('Updated Finding: %j', newFinding);
    }
    updateFinding();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import datetime, timezone
    
    from google.cloud import securitycenter_v1
    from google.cloud.securitycenter_v1 import Finding
    from google.protobuf import field_mask_pb2
    
    client = securitycenter_v1.SecurityCenterClient()
    # Only update the specific source property and event_time.  event_time
    # is required for updates.
    field_mask = field_mask_pb2.FieldMask(
        paths=["source_properties.s_value", "event_time"]
    )
    
    # Set the update time to Now.  This must be some time greater then the
    # event_time on the original finding.
    event_time = datetime.now(tz=timezone.utc)
    
    # 'source_name' is the resource path for a source that has been
    # created previously (you can use list_sources to find a specific one).
    # Its format is:
    # source_name = "organizations/{organization_id}/sources/{source_id}"
    # e.g.:
    # source_name = "organizations/111122222444/sources/1234"
    finding_name = f"{source_name}/findings/samplefindingid2"
    finding = Finding(
        name=finding_name,
        source_properties={"s_value": "new_string"},
        event_time=event_time,
    )
    updated_finding = client.[update_finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_finding)(
        request={"finding": finding, "update_mask": field_mask}
    )
    
    print(
        "New Source properties: {}, Event Time {}".format(
            updated_finding.source_properties, updated_finding.event_time
        )
    )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
