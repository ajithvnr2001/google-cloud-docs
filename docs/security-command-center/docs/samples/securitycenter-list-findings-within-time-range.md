---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-findings-within-time-range/
title: List findings by event occurrence time \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:06.904607+00:00
---

# List findings by event occurrence time  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-findings-within-time-range/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List findings by event occurrence time Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to filter and list findings within a specific time range

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
    	"google.golang.org/api/iterator"
    )
    
    // listFindingsAtTime prints findings that where present for a specific source
    // as of five days ago to w. sourceName is the full resource name of the
    // source to search for findings under.
    func listFindingsAtTime(w io.Writer, sourceName string) error {
    	// Specific source:
    	// 		sourceName := "{parent}/sources/{sourceId}"
    	// All sources:
    	// 		sourceName := "{parent}/sources/-"
    	// where,
    	// Parent must be in one of the following formats:
    	//		"organizations/{orgId}"
    	//		"projects/{projectId}"
    	//		"folders/{folderId}"
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	fiveDaysAgo := time.Now().AddDate(0, 0, -5).Format(time.RFC3339)
    
    	req := &securitycenterpb.ListFindingsRequest{
    		Parent: sourceName,
    		Filter: fmt.Sprintf("event_time < %q", fiveDaysAgo),
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
    
    
    static ImmutableList<ListFindingsResult> listFindingsAtTime(SourceName sourceName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // parentId: must be one of the following:
        //    "organization-id"
        //    "project-id"
        //    "folder-id"
        // SourceName sourceName = SourceName.of(parentId, sourceId);
    
        // 5 days ago
        Instant fiveDaysAgo = Instant.now().minus(Duration.ofDays(5));
    
        // Create filter to only list findings that occurred before five days ago.
        String filter = String.format("event_time < \"%s\"", fiveDaysAgo.toString());
    
        ListFindingsRequest.Builder request =
            ListFindingsRequest.newBuilder().setParent(sourceName.toString()).setFilter(filter);
    
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
    // sourceName is the fully qualified source name to search for findings
    // under.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // const sourceName = `${parent}/sources/${sourceId}`;
    // where,
    // parent: must be in one of the following formats:
    //    `organizations/${organization_id}`
    //    `projects/${project_id}`
    //    `folders/${folder_id}`
    const fiveDaysAgo = new Date();
    fiveDaysAgo.setDate(fiveDaysAgo.getDate() - 5);
    
    async function listFindingsAtTime() {
      const [response] = await client.listFindings({
        parent: sourceName,
        filter: `event_time < "${fiveDaysAgo.toISOString()}"`,
      });
      let count = 0;
      Array.from(response).forEach(result =>
        console.log(
          `${++count} ${result.finding.name} ${result.finding.resourceName}`
        )
      );
    }
    listFindingsAtTime();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import datetime, timedelta, timezone
    
    from google.cloud import securitycenter_v1
    
    # Create a new client.
    # More info about SecurityCenterClient:
    # https://cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient
    client = securitycenter_v1.SecurityCenterClient()
    
    # 'source_name' is the resource path for a source that has been
    # created previously (you can use list_sources to find a specific one).
    # Its format is:
    # source_name = f"{parent}/sources/{source_id}"
    # 'parent' must be in one of the following formats:
    #   "organizations/{organization_id}"
    #   "projects/{project_id}"
    #   "folders/{folder_id}"
    # You an also use a wild-card "-" for all sources:
    #   source_name = "organizations/111122222444/sources/-"
    
    five_days_ago = datetime.now(timezone.utc) - timedelta(days=5)
    timestamp_milliseconds = int(five_days_ago.timestamp() * 1000)
    
    # More details about the request syntax:
    # https://cloud.google.com/security-command-center/docs/reference/rest/v1/folders.sources.findings/list
    finding_result_iterator = client.[list_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_findings)(
        request={
            "parent": source_name,
            "filter": f"event_time < {timestamp_milliseconds}",
        }
    )
    
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
