---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-source/
title: Update a source \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:58.546968+00:00
---

# Update a source  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Update a source Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to update a source

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // updateSource changes a sources display name to "New Display Name" for a
    // specific source. sourceName is the full resource name of the source to be
    // updated.
    func updateSource(w io.Writer, sourceName string) error {
    	// sourceName := "organizations/111122222444/sources/1234"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.UpdateSourceRequest{
    		Source: &securitycenterpb.Source{
    			Name:        sourceName,
    			DisplayName: "New Display Name",
    		},
    		// Only update the display name field (if not set all mutable
    		// fields of the source will be updated.
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"display_name"},
    		},
    	}
    	source, err := client.UpdateSource(ctx, req)
    	if err != nil {
    		return fmt.Errorf("UpdateSource: %w", err)
    	}
    	fmt.Fprintf(w, "Source Name: %s, ", source.Name)
    	fmt.Fprintf(w, "Display name: %s, ", source.DisplayName)
    	fmt.Fprintf(w, "Description: %s\n", source.Description)
    
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static Source updateSource(SourceName sourceName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to update a source.
        // SourceName sourceName = SourceName.of(/*organization=*/"123234324",/*source=*/
        // "423432321");
        Source source =
            Source.newBuilder()
                .setDisplayName("Updated Display Name")
                .setName(sourceName.toString())
                .build();
        FieldMask updateMask = FieldMask.newBuilder().addPaths("display_name").build();
    
        UpdateSourceRequest.Builder request =
            UpdateSourceRequest.newBuilder().setSource(source).setUpdateMask(updateMask);
    
        // Call the API.
        Source response = client.updateSource(request.build());
    
        System.out.println("Updated Source: " + response);
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
    // sourceName is the full resource path to the update target.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // const sourceName = "organizations/111122222444/sources/1234";
    async function updateSource() {
      const [source] = await client.updateSource({
        source: {
          name: sourceName,
          displayName: 'New Display Name',
        },
        // Only update the display name field (if not set all mutable
        // fields of the source will be updated.
        updateMask: {paths: ['display_name']},
      });
      console.log('Updated source: %j', source);
    }
    
    updateSource();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter_v1
    from google.protobuf import field_mask_pb2
    
    client = securitycenter_v1.SecurityCenterClient()
    
    # Field mask to only update the display name.
    field_mask = field_mask_pb2.FieldMask(paths=["display_name"])
    
    # 'source_name' is the resource path for a source that has been
    # created previously (you can use list_sources to find a specific one).
    # Its format is:
    # source_name = "organizations/{organization_id}/sources/{source_id}"
    # e.g.:
    # source_name = "organizations/111122222444/sources/1234"
    updated = client.[update_source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_source)(
        request={
            "source": {"name": source_name, "display_name": "Updated Display Name"},
            "update_mask": field_mask,
        }
    )
    print(f"Updated Source: {updated}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
