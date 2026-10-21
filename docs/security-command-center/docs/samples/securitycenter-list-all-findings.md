---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-all-findings/
title: List findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:35.252007+00:00
---

# List findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-all-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List findings Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list all findings in an organization

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
    
    // listFindings prints all findings in orgID to w. orgID is the numeric
    // identifier of the organization.
    func listFindings(w io.Writer, orgID string) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.ListFindingsRequest{
    		// List findings across all sources.
    		// Parent must be in one of the following formats:
    		//		"organizations/{orgId}/sources/-"
    		//		"projects/{projectId}/sources/-"
    		//		"folders/{folderId}/sources/-"
    		Parent: fmt.Sprintf("organizations/%s/sources/-", orgID),
    	}
    	it := client.ListFindings(ctx, req)
    	for {
    		result, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    		finding := result.Finding
    		fmt.Fprintf(w, "Finding Name: %s, ", finding.Name)
    		fmt.Fprintf(w, "Resource Name %s, ", finding.ResourceName)
    		fmt.Fprintf(w, "Category: %s\n", finding.Category)
    	}
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static ImmutableList<ListFindingsResult> listAllFindings(OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Input parameters for SourceName must be in one of the following formats:
        //    * OrganizationName organizationName = OrganizationName.of("organization-id");
        //      organizationName.getOrganization();
        //    * ProjectName projectName = ProjectName.of("project-id");
        //      projectName.getProject();
        //    * FolderName folderName = FolderName.of("folder-id");
        //      folderName.getFolder();
        //
        // "-" Indicates listing across all sources.
        SourceName sourceName = SourceName.of(organizationName.getOrganization(), "-");
    
        ListFindingsRequest.Builder request =
            ListFindingsRequest.newBuilder().setParent(sourceName.toString());
    
        // Call the API.
        ListFindingsPagedResponse response = client.listFindings(request.build());
    
        // This creates one list for all findings.  If your organization has a large number of
        // findings this can cause out of memory issues.  You can process them in incrementally
        // by returning the Iterable returned response.iterateAll() directly.
        ImmutableList<ListFindingsResult> results = ImmutableList.copyOf(response.iterateAll());
        System.out.println("Findings:");
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
    // const organizationId = "1234567777";
    
    async function listAllFindings() {
      const [response] = await client.listFindings({
        // List findings across all sources.
        // parent: must be in one of the following formats:
        //    `organizations/${organization_id}/sources/-`
        //    `projects/${project_id}/sources/-`
        //    `folders/${folder_id}/sources/-`
        parent: `organizations/${organizationId}/sources/-`,
      });
      let count = 0;
      Array.from(response).forEach(result =>
        console.log(
          `${++count} ${result.finding.name} ${result.finding.resourceName}`
        )
      );
    }
    await listAllFindings();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter_v1
    
    # Create a client.
    client = securitycenter_v1.SecurityCenterClient()
    
    # 'parent' must be in one of the following formats:
    #   "organizations/{organization_id}"
    #   "projects/{project_id}"
    #   "folders/{folder_id}"
    parent = f"organizations/{organization_id}"
    # The "sources/-" suffix lists findings across all sources.  You
    # also use a specific source_name instead.
    all_sources = f"{parent}/sources/-"
    finding_result_iterator = client.[list_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_findings)(request={"parent": all_sources})
    for i, finding_result in enumerate(finding_result_iterator):
        print(
            "{}: name: {} resource: {}".format(
                i, finding_result.finding.name, finding_result.finding.resource_name
            )
        )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
