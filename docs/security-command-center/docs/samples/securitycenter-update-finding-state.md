---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-finding-state/
title: Update finding state \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:37.663343+00:00
---

# Update finding state  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-finding-state/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Update finding state Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to update the state of a threat or custom finding

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
    )
    
    // updateFindingState demonstrates how to update a security finding's state
    // in CSCC.  findingName is the full resource name of the finding to update.
    func setFindingState(w io.Writer, findingName string) error {
    	// findingName := "organizations/111122222444/sources/1234"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    	// Use now as the eventTime for the security finding.
    	now, err := ptypes.TimestampProto(time.Now())
    	if err != nil {
    		return fmt.Errorf("TimestampProto: %w", err)
    	}
    
    	req := &securitycenterpb.SetFindingStateRequest{
    		Name:  findingName,
    		State: securitycenterpb.[Finding_INACTIVE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv1_securitycenterpb_Finding_STATE_UNSPECIFIED_Finding_ACTIVE_Finding_INACTIVE),
    		// New state is effective immediately.
    		StartTime: now,
    	}
    
    	finding, err := client.SetFindingState(ctx, req)
    	if err != nil {
    		return fmt.Errorf("SetFindingState: %w", err)
    	}
    
    	fmt.Fprintf(w, "Finding updated: %s\n", finding.Name)
    	fmt.Fprintf(w, "Finding state: %v\n", finding.State)
    	fmt.Fprintf(w, "Event time (Epoch Seconds): %d\n", finding.EventTime.Seconds)
    
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static Finding setFindingState(FindingName findingName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // FindingName findingName = FindingName.of(/*organization=*/"123234324",
        // /*source=*/"423432321", /*findingId=*/"samplefindingid2");
    
        // Use the current time as the finding "event time".
        Instant eventTime = Instant.now();
    
        Finding response =
            client.setFindingState(
                findingName,
                State.INACTIVE,
                Timestamp.newBuilder()
                    .setSeconds(eventTime.getEpochSecond())
                    .setNanos(eventTime.getNano())
                    .build());
    
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
    
    // findingName is the full resource name of the source the finding should
    // be associated with.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // const findingName =
    // "organizations/111122222444/sources/1234/findings/findingid";
    async function setFindingState() {
      const eventTime = new Date();
      const [updatedFinding] = await client.setFindingState({
        name: findingName,
        state: 'INACTIVE',
        // use now as the time when the new state takes effect.
        startTime: {
          seconds: Math.floor(eventTime.getTime() / 1000),
          nanos: (eventTime.getTime() % 1000) * 1e6,
        },
      });
      console.log('Updated Finding: %j', updatedFinding);
    }
    setFindingState();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import datetime, timezone
    
    from google.cloud import securitycenter_v1
    from google.cloud.securitycenter_v1 import Finding
    
    # Create a client.
    client = securitycenter_v1.SecurityCenterClient()
    # 'source_name' is the resource path for a source that has been
    # created previously (you can use list_sources to find a specific one).
    # Its format is:
    # source_name = "organizations/{organization_id}/sources/{source_id}"
    # e.g.:
    # source_name = "organizations/111122222444/sources/1234"
    finding_name = f"{source_name}/findings/samplefindingid2"
    
    # Call the API to change the finding state to inactive as of now.
    new_finding = client.[set_finding_state](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_set_finding_state)(
        request={
            "name": finding_name,
            "state": Finding.State.INACTIVE,
            "start_time": datetime.now(timezone.utc),
        }
    )
    print(f"New state: {new_finding.state}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
