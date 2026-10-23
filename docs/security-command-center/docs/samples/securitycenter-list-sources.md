---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-sources/
title: List security sources \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:27.556234+00:00
---

# List security sources  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-sources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List security sources Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list all security sources in an organization

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"google.golang.org/api/iterator"
    )
    
    // listSources prints all sources in  orgID to w.  orgID is the numeric
    // identifier of the organization.
    func listSources(w io.Writer, orgID string) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.ListSourcesRequest{
    		// Parent must be in one of the following formats:
    		//		"organizations/{orgId}"
    		//		"projects/{projectId}"
    		//		"folders/{folderId}"
    		Parent: fmt.Sprintf("organizations/%s", orgID),
    	}
    	it := client.ListSources(ctx, req)
    	for {
    		source, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    		fmt.Fprintf(w, "Source Name: %s, ", source.Name)
    		fmt.Fprintf(w, "Display name: %s, ", source.DisplayName)
    		fmt.Fprintf(w, "Description: %s\n", source.Description)
    	}
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static ImmutableList<Source> listSources(OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to list sources in an organization, project, or folder.
        // Parent must be in one of the following formats:
        //    OrganizationName organizationName = OrganizationName.of("organization-id");
        //    ProjectName projectName = ProjectName.of("project-id");
        //    FolderName folderName = FolderName.of("folder-id");
        ListSourcesRequest.Builder request =
            ListSourcesRequest.newBuilder().setParent(organizationName.toString());
    
        // Call the API.
        ListSourcesPagedResponse response = client.listSources(request.build());
    
        // This creates one list for all sources.  If your organization has a large number of sources
        // this can cause out of memory issues.  You can process them batches by returning
        // the Iterable returned response.iterateAll() directly.
        ImmutableList<Source> results = ImmutableList.copyOf(response.iterateAll());
        System.out.println("Sources:");
        System.out.println(results);
        return results;
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
    //  organizationId is the numeric ID of the organization.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // parent: must be in one of the following formats:
    //    `organizations/${organization_id}`
    //    `projects/${project_id}`
    //    `folders/${folder_id}`
    const parent = `organizations/${organizationId}`;
    // Call the API with automatic pagination.
    async function listSources() {
      const [response] = await client.listSources({parent: parent});
      let count = 0;
      console.log('Sources:');
      Array.from(response).forEach(source =>
        console.log('%d %j', ++count, source)
      );
    }
    
    listSources();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter_v1
    
    # Create a new client.
    client = securitycenter_v1.SecurityCenterClient()
    # 'parent' must be in one of the following formats:
    #   "organizations/{organization_id}"
    #   "projects/{project_id}"
    #   "folders/{folder_id}"
    parent = f"organizations/{organization_id}"
    
    # Call the API and print out each existing source.
    for i, source in enumerate(client.[list_sources](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_sources)(request={"parent": parent})):
        print(i, source)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
