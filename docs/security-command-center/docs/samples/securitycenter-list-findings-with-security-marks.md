---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-findings-with-security-marks/
title: List findings with security marks \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:58.246207+00:00
---

# List findings with security marks  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-findings-with-security-marks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List findings with security marks Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to filter and list findings by security mark

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
    
    // listFindingsWithMarks prints findings that don't have a security mark
    // key_a equal to value_a to w.  sourceName is the full resource name
    // of the source to search for findings under.
    func listFindingsWithMarks(w io.Writer, sourceName string) error {
    	// sourceName := "{parent}/sources/{sourceId}"
    	// where,
    	// Parent must be in one of the following formats:
    	//		"organizations/{orgId}"
    	//		"projects/{projectId}"
    	//		"folders/{folderId}"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.ListFindingsRequest{
    		Parent: sourceName,
    		Filter: `NOT security_marks.marks.key_a="value_a"`,
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
    
    
    static ImmutableList<ListFindingsResult> listFindingsWithQueryMarks(SourceName sourceName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to list all findings filtered by a specific security mark.
        //
        // 'parent' must be in one of the following formats:
        //    * OrganizationName organizationName = OrganizationName.of("organization-id");
        //      String parent = organizationName.getOrganization();
        //    * ProjectName projectName = ProjectName.of("project-id");
        //      String parent = projectName.getProject();
        //    * FolderName folderName = FolderName.of("folder-id");
        //      String parent = folderName.getFolder();
        // SourceName sourceName = SourceName.of(parent, {source-id});
    
        String filter = "NOT security_marks.marks.key_a=\"value_a\"";
    
        ListFindingsRequest.Builder request =
            ListFindingsRequest.newBuilder().setParent(sourceName.toString()).setFilter(filter);
    
        // Call the API.
        ListFindingsPagedResponse response = client.listFindings(request.build());
    
        // This creates one list for all findings in the filter.If your organization has a large
        // number of
        // findings this can cause out of memory issues.  You can process them batches by returning
        // the Iterable returned response.iterateAll() directly.
        ImmutableList<ListFindingsResult> results = ImmutableList.copyOf(response.iterateAll());
        System.out.println("Findings with security mark - key_a=value_a:");
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
    //  sourceName is the full resource path of the source to search for
    //  findings.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // const sourceName = `${parent}/sources/${sourceId}`;
    // where,
    // parent: must be in one of the following formats:
    //    `organizations/${organization_id}`
    //    `projects/${project_id}`
    //    `folders/${folder_id}`
    
    async function listFindingsWithSecurityMarks() {
      const [response] = await client.listFindings({
        // List findings across all sources.
        parent: sourceName,
        filter: 'NOT security_marks.marks.key_a="value_a"',
      });
      let count = 0;
      Array.from(response).forEach(result =>
        console.log(
          `${++count} ${result.finding.name} ${result.finding.resourceName}`
        )
      );
    }
    listFindingsWithSecurityMarks();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter
    
    client = securitycenter.SecurityCenterClient()
    
    # 'source_name' is the resource path for a source that has been
    # created previously (you can use list_sources to find a specific one).
    # Its format is:
    # source_name = "{parent}/sources/{source_id}"
    # 'parent' must be in one of the following formats:
    #   "organizations/{organization_id}"
    #   "projects/{project_id}"
    #   "folders/{folder_id}"
    # source_name = "organizations/111122222444/sources/1234"
    marks_filter = 'NOT security_marks.marks.finding_key_a="value_a"'
    
    # Call the API and print results.
    finding_iterator = client.[list_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_findings)(
        request={"parent": source_name, "filter": marks_filter}
    )
    for i, finding_result in enumerate(finding_iterator):
        print(i, finding_result)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
