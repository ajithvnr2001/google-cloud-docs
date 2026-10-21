---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-source/
title: Create a security source \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:46.063921+00:00
---

# Create a security source  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Create a security source Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to create a security source

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    )
    
    // createSource creates a new source for organization orgID. orgID is
    // the numeric identifier of the organization
    func createSource(w io.Writer, orgID string) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.CreateSourceRequest{
    		Source: &securitycenterpb.Source{
    			DisplayName: "Customized Display Name",
    			Description: "A new custom source that does X",
    		},
    		Parent: fmt.Sprintf("organizations/%s", orgID),
    	}
    	source, err := client.CreateSource(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateSource: %w", err)
    	}
    
    	fmt.Fprintf(w, "New source created: %s\n", source.Name)
    	fmt.Fprintf(w, "Display Name: %s\n", source.DisplayName)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static Source createSource(OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to create a source in an organization.
        // OrganizationName organizationName = OrganizationName.of(/*organizationId=*/"123234324");
        Source source =
            Source.newBuilder()
                .setDisplayName("Customized Display Name")
                .setDescription("A new custom source that does X")
                .build();
    
        CreateSourceRequest.Builder request =
            CreateSourceRequest.newBuilder().setParent(organizationName.toString()).setSource(source);
    
        // Call the API.
        Source response = client.createSource(request.build());
    
        System.out.println("Created Source: " + response);
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
    // organizationId is numeric organization identifier.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // const organizationId = "1234567777";
    async function createSource() {
      const [source] = await client.createSource({
        source: {
          displayName: 'Customized Display Name',
          description: 'A new custom source that does X',
        },
        parent: client.organizationPath(organizationId),
      });
      console.log('New Source: %j', source);
    }
    createSource();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter_v1
    
    client = securitycenter_v1.SecurityCenterClient()
    # organization_id is the numeric ID of the organization. e.g.:
    # organization_id = "111122222444"
    org_name = f"organizations/{organization_id}"
    
    created = client.[create_source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_source)(
        request={
            "parent": org_name,
            "source": {
                "display_name": "Customized Display Name",
                "description": "A new custom source that does X",
            },
        }
    )
    print(f"Created Source: {created.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
