---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-finding/
title: Create a finding \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:12.565362+00:00
---

# Create a finding  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-finding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Create a finding Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to create a new finding

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
    	"google.golang.org/protobuf/types/known/timestamppb"
    )
    
    // createFinding demonstrates how to create a new security finding in CSCC.
    // sourceName is the full resource name of the source the finding should
    // be associated with.
    func createFinding(w io.Writer, sourceName string) error {
    	// sourceName := "organizations/111122222444/sources/1234"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    	// Use now as the eventTime for the security finding.
    
    	now := time.Now()
    	eventTime := timestamppb.New(now)
    
    	uniqueFindingID := fmt.Sprintf("samplefindingid%d", now.Unix())
    
    	req := &securitycenterpb.CreateFindingRequest{
    		Parent:    sourceName,
    		FindingId: uniqueFindingID,
    		Finding: &securitycenterpb.Finding{
    			State: securitycenterpb.[Finding_ACTIVE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv1_securitycenterpb_Finding_STATE_UNSPECIFIED_Finding_ACTIVE_Finding_INACTIVE),
    			// Resource the finding is associated with. This is an
    			// example any resource identifier can be used.
    			ResourceName: "//cloudresourcemanager.googleapis.com/organizations/11232",
    			// A free-form category.
    			Category: "MEDIUM_RISK_ONE",
    			// The time associated with discovering the issue.
    			EventTime: eventTime,
    		},
    	}
    	finding, err := client.CreateFinding(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateFinding: %w", err)
    	}
    	fmt.Fprintf(w, "New finding created: %s\n", finding.Name)
    	fmt.Fprintf(w, "Event time (Epoch Seconds): %d\n", eventTime.Seconds)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static Finding createFinding(SourceName sourceName, String findingId) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // SourceName sourceName = SourceName.of(/*organization=*/"123234324",/*source=*/
        // "423432321");
        // String findingId = "samplefindingid";
    
        // Use the current time as the finding "event time".
        Instant eventTime = Instant.now();
    
        // The resource this finding applies to.  The CSCC UI can link
        // the findings for a resource to the corresponding Asset of a resource
        // if there are matches.
        String resourceName = "//cloudresourcemanager.googleapis.com/organizations/11232";
    
        // Start setting up a request to create a finding in a source.
        Finding finding =
            Finding.newBuilder()
                .setParent(sourceName.toString())
                .setState(State.ACTIVE)
                .setResourceName(resourceName)
                .setEventTime(
                    Timestamp.newBuilder()
                        .setSeconds(eventTime.getEpochSecond())
                        .setNanos(eventTime.getNano()))
                .setCategory("MEDIUM_RISK_ONE")
                .build();
    
        // Call the API.
        Finding response = client.createFinding(sourceName, findingId, finding);
    
        System.out.println("Created Finding: " + response);
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
    // sourceName is the full resource name of the source the finding should
    // be associated with.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // const sourceName = "organizations/111122222444/sources/1234";
    
    // Use now as the eventTime for the security finding.
    const eventTime = new Date();
    async function createFinding() {
      const [newFinding] = await client.createFinding({
        parent: sourceName,
        findingId: 'samplefindingid',
        finding: {
          state: 'ACTIVE',
          // Resource the finding is associated with.  This is an
          // example any resource identifier can be used.
          resourceName:
            '//cloudresourcemanager.googleapis.com/organizations/11232',
          // A free-form category.
          category: 'MEDIUM_RISK_ONE',
          // The time associated with discovering the issue.
          eventTime: {
            seconds: Math.floor(eventTime.getTime() / 1000),
            nanos: (eventTime.getTime() % 1000) * 1e6,
          },
        },
      });
      console.log('New finding created: %j', newFinding);
    }
    await createFinding();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import datetime, timezone
    
    from google.cloud import securitycenter_v1
    from google.cloud.securitycenter_v1 import Finding
    
    # Create a new client.
    client = securitycenter_v1.SecurityCenterClient()
    
    # Use the current time as the finding "event time".
    event_time = datetime.now(tz=timezone.utc)
    
    # 'source_name' is the resource path for a source that has been
    # created previously (you can use list_sources to find a specific one).
    # Its format is:
    # source_name = "organizations/{organization_id}/sources/{source_id}"
    # e.g.:
    # source_name = "organizations/111122222444/sources/1234"
    
    # The resource this finding applies to.  The CSCC UI can link
    # the findings for a resource to the corresponding Asset of a resource
    # if there are matches.
    resource_name = "//cloudresourcemanager.googleapis.com/organizations/11232"
    
    finding = Finding(
        state=Finding.State.ACTIVE,
        resource_name=resource_name,
        category="MEDIUM_RISK_ONE",
        event_time=event_time,
    )
    
    # Call The API.
    created_finding = client.[create_finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_finding)(
        request={"parent": source_name, "finding_id": finding_id, "finding": finding}
    )
    print(created_finding)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
