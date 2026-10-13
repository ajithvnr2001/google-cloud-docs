---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings/
title: Listing security findings using the Security Command Center API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:17.286761+00:00
---

# Listing security findings using the Security Command Center API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Listing security findings using the Security Command Center API Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security Command Center findings model the potential security risks of assets in a project or an organization. A finding always relates to a specific asset in Security Command Center.

This guide shows you how to use Security Command Center client libraries to access findings. Each finding belongs to a source. Most detectors or finding providers produce findings within the same source.

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

## Before you begin

Before you set up a source, you need to complete the following:

  * [Authenticate with the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/authentication)



### Page size

All Security Command Center list APIs are paginated. Each response returns a page of results and a token to return the next page. The page size is configurable. The default page size is 10. You can set it to a minimum of 1, and a maximum of 1000.

### Findings retention

Depending on your Security Command Center tier, findings remain available for you to list or query for specific periods of time. For more information about Security Command Center data retention, see [Data retention](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention).

**Important:** Performance limits at scale 

Standard synchronous API list calls (for example, [`ListFindings`](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#list_all_findings)) are designed for operational triage and small-to-medium datasets. Running queries on large datasets or with highly complex filters can degrade query performance or timeout.  
  
For large-scale data exports, multi-tenant analysis, or historical security reporting (for example, on millions of findings), don't rely on synchronous API pagination. We strongly recommend establishing a continuous or [Bulk BigQuery export](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data) pipeline. BigQuery is specifically designed for high-volume data warehousing and analysis, allowing you to offload heavy queries and safeguard your production API quotas.

## List all findings

### gcloud

To list all findings in a project, folder, or organization, run the following command:
    
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
      --location=LOCATION

Replace the following:

  * `PARENT_TYPE`: the level of the resource hierarchy for which to list findings; use `organizations`, `folders`, or `projects`.
  * `PARENT_ID`: the numeric ID of the organization, folder, or project, or the alphanumeric project ID.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to list findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.



For more examples, run: 
    
    
    gcloud scc findings list --help

For examples in the documentation, see [`gcloud scc findings list`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list).

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"google.golang.org/api/iterator"
    )
    
    // listFindings prints all findings in orgID to w. orgID is the numeric
    // identifier of the organization.
    func listFindings(w io.Writer, orgID string) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.ListFindingsRequest{
    		// List findings across all sources.
    		// Parent must be in one of the following formats:
    		//		"organizations/{orgId}/sources/-/locations/global"
    		//		"projects/{projectId}/sources/-/locations/global"
    		//		"folders/{folderId}/sources/-/locations/global"
    		Parent: fmt.Sprintf("organizations/%s/sources/-/locations/global", orgID),
    	}
    	it := client.ListFindings(ctx, req)
    	for {
    		result, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Done) {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    		finding := result.Finding
    		fmt.Fprintf(w, "Finding Name: %s, ", finding.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    		fmt.Fprintf(w, "Resource Name %s, ", finding.ResourceName)
    		fmt.Fprintf(w, "Category: %s\n", finding.Category)
    	}
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest.html);
    import com.google.cloud.securitycenter.v2.[ListFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsResponse.html).[ListFindingsResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsResponse.ListFindingsResult.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class ListAllFindings {
    
      public static void main(String[] args) throws IOException {
        // organizationId: The source to list all findings for.
        // You can also use project/ folder as the parent resource.
        String organizationId = "google-cloud-organization-id";
    
        // Specify the location to list the findings.
        String location = "global";
    
        // The source id to scope the findings.
        String sourceId = "source-id";
    
        listAllFindings(organizationId, sourceId, location);
      }
    
      // List all findings under a given parent resource.
      public static void listAllFindings(String organizationId, String sourceId, String location)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
          [ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest.html) request =
              [ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest.html).newBuilder()
                  // To list findings across all sources, use "-".
                  .setParent(
                      String.format("organizations/%s/sources/%s/locations/%s", organizationId,
                          sourceId,
                          location))
                  .build();
    
          for ([ListFindingsResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsResponse.ListFindingsResult.html) result : client.listFindings(request).iterateAll()) {
            System.out.printf("Finding: %s", result.getFinding().getName());
          }
          System.out.println("\nListing complete.");
        }
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // TODO(developer): Update the following for your own environment.
    const organizationId = '1081635000895';
    const location = 'global';
    
    // Required. Name of the source the findings belong to. If no location is
    // specified, the default is global. The following list shows some examples:
    // - `organizations/[organization_id]/sources/[source_id]/locations/[location_id]`
    // - `folders/[folder_id]/sources/[source_id]`
    // - `folders/[folder_id]/sources/[source_id]/locations/[location_id]`
    // - `projects/[project_id]/sources/[source_id]`
    // - `projects/[project_id]/sources/[source_id]/locations/[location_id]`
    // To groupBy across all sources provide a source_id of `-`.
    const parent = `organizations/${organizationId}/sources/-/locations/${location}`;
    
    // Build the list findings request.
    const listFindingsRequest = {
      parent,
    };
    
    async function listAllFindings() {
      // Call the API.
      const iterable = client.listFindingsAsync(listFindingsRequest);
      let count = 0;
    
      for await (const response of iterable) {
        // Just print a few for demonstration.
        if (count > 5) break;
        console.log(
          `${++count} ${response.finding.name} ${response.finding.resourceName}`
        );
      }
    }
    
    await listAllFindings();

### Python
    
    
    def list_all_findings(organization_id, source_name, location_id) -> int:
        """
        lists all findings for a source
        Args:
           organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
           source_name: is the resource path for a source that has been created
           location_id: GCP location id; example: 'global'
        Returns:
            int: returns the count of all findings for a source
        """
        from google.cloud import securitycenter_v2
    
        # Create a client.
        client = securitycenter_v2.SecurityCenterClient()
        parent = f"organizations/{organization_id}"
        all_sources = f"{parent}/sources/{source_name}/locations/{location_id}"
    
        # Create the request dictionary
        request = {"parent": all_sources}
    
        # Print the request for debugging
        print("Request: ", request)
    
        finding_result_iterator = client.[list_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_findings)(request={"parent": all_sources})
        for count, finding_result in enumerate(finding_result_iterator):
            print(
                "{}: name: {} resource: {}".format(
                    count, finding_result.finding.name, finding_result.finding.resource_name
                )
            )
        return finding_result_iterator
    
    

The output for each finding resembles the following. For a full list of fields, see [`ListFindingsResult`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings/list#ListFindingsResult).
    
    
    {
      "finding": {
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parentDisplayName": "SOURCE_DISPLAY_NAME",
        "resourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "state": "ACTIVE",
        "category": "Malware: Cryptomining Bad Domain",
        "eventTime": "2021-11-10T17:41:41.594Z",
        "createTime": "2021-11-10T17:41:42.014Z",
        "severity": "LOW",
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "mute": "UNDEFINED",
        "findingClass": "THREAT",
        "indicator": {
          "domains": ["DOMAIN"]
        }
      },
      "resource": {
        "name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "gcpMetadata": {
          "projectDisplayName": "PROJECT_ID"
        }
      }
    }

## Filter findings

A project, folder, or organization might have many findings. The preceding example doesn't use a filter, so all finding records are returned.

To help you get information about only the fields you want, you can use _finding filters_. These filters are like "where" clauses in SQL statements, but instead of columns, they apply to the objects returned by the API.

The following example lists only the findings that have a category "`MEDIUM_RISK_ONE`". Different finding providers (also known as [security sources](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources)) use different sets of categories. To determine the categories you can use in your filter, refer to the documentation of the finding provider.

### gcloud

Use the following command to filter findings:
    
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
      --location=LOCATION \
      --source=SOURCE_ID \
      --filter="FILTER"

Replace the following:

  * `PARENT_TYPE`: the level of the resource hierarchy for which to list findings; use `organizations`, `folders`, or `projects`.
  * `PARENT_ID`: the numeric ID of the organization, folder, or project, or the alphanumeric project ID.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to list findings with a filter; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `SOURCE_ID`: the ID of the security source that provides the finding type.
  * `FILTER`: the filter you need to use. For example, the following filter returns findings from the category of `MEDIUM_RISK_ONE` only: 
        
        --filter="category=\"MEDIUM_RISK_ONE\""




For more examples, run: 
    
    
    gcloud scc findings list --help

For examples in the documentation, see [`gcloud scc findings list`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list).

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"google.golang.org/api/iterator"
    )
    
    // listFilteredFindings prints findings with category 'MEDIUM_RISK_ONE' for a
    // specific source to w. sourceName is the full resource name of the source
    // to search for findings under.
    func listFilteredFindings(w io.Writer, sourceName string) error {
    	// Specific source:
    	// 		sourceName := "{parent}/sources/{sourceId}"
    	// All sources:
    	// 		sourceName := "{parent}/sources/-"
    	// where,
    	// Parent must be in one of the following formats:
    	//		"organizations/{orgId}"
    	//		"projects/{projectId}"
    	//		"folders/{folderId}"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.ListFindingsRequest{
    		Parent: sourceName,
    		Filter: `category="MEDIUM_RISK_ONE"`,
    	}
    	it := client.ListFindings(ctx, req)
    	for {
    		result, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Done) {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    		finding := result.Finding
    		fmt.Fprintf(w, "Finding Name: %s, ", finding.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    		fmt.Fprintf(w, "Resource Name %s, ", finding.ResourceName)
    		fmt.Fprintf(w, "Category: %s\n", finding.Category)
    	}
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest.html);
    import com.google.cloud.securitycenter.v2.[ListFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsResponse.html).[ListFindingsResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsResponse.ListFindingsResult.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class ListFindingsWithFilter {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the variables within {}
        // organizationId: Google Cloud Organization id.
        // You can also use project/ folder as the parent resource.
        String organizationId = "google-cloud-organization-id";
    
        // Specify the location to list the findings.
        String location = "global";
    
        // The source id to scope the findings.
        String sourceId = "source-id";
    
        listFilteredFindings(organizationId, sourceId, location);
      }
    
      // List filtered findings under a source.
      public static void listFilteredFindings(String organizationId, String sourceId, String location)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          // Use any one of the following formats:
          //  * organizations/{organization_id}/sources/{source_id}/locations/{location}
          //  * folders/{folder_id}/sources/{source_id}/locations/{location}
          //  * projects/{project_id}/sources/{source_id}/locations/{location}
          String parent = String.format("organizations/%s/sources/%s/locations/%s", organizationId,
              sourceId,
              location);
    
          // Listing all findings of category "MEDIUM_RISK_ONE".
          String filter = "category=\"MEDIUM_RISK_ONE\"";
    
          [ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest.html) request =
              [ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest.html).newBuilder()
                  .setParent(parent)
                  .setFilter(filter)
                  .build();
    
          for ([ListFindingsResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsResponse.ListFindingsResult.html) result : client.listFindings(request).iterateAll()) {
            System.out.printf("Finding: %s", result.getFinding().getName());
          }
          System.out.println("\nListing complete.");
        }
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // TODO(developer): Update the following for your own environment.
    const organizationId = '1081635000895';
    const location = 'global';
    
    // Required. Name of the source to groupBy. If no location is specified,
    // finding is assumed to be in global.
    //  The following list shows some examples:
    // - `organizations/[organization_id]/sources/[source_id]`
    // - `organizations/[organization_id]/sources/[source_id]/locations/[location_id]`
    // - `folders/[folder_id]/sources/[source_id]`
    // - `folders/[folder_id]/sources/[source_id]/locations/[location_id]`
    // - `projects/[project_id]/sources/[source_id]`
    // - `projects/[project_id]/sources/[source_id]/locations/[location_id]`
    // To groupBy across all sources provide a source_id of `-`.
    const parent = `organizations/${organizationId}/sources/-/locations/${location}`;
    
    // Listing all findings of category "MEDIUM_RISK_ONE".
    const filter = 'category="MEDIUM_RISK_ONE"';
    
    // Build the list findings with filter request.
    const listFilteredFindingsRequest = {
      parent,
      filter,
    };
    
    async function listFilteredFindings() {
      // Call the API.
      const iterable = client.listFindingsAsync(listFilteredFindingsRequest);
      let count = 0;
      console.log('Findings:');
      for await (const response of iterable) {
        // Just print a few for demonstration.
        if (count > 5) break;
        console.log(
          `${++count} ${response.finding.name} ${response.finding.resourceName}`
        );
      }
    }
    await listFilteredFindings();

### Python
    
    
    def list_filtered_findings(organization_id, source_name, location_id) -> int:
        """
        lists filtered findings for a source
        Args:
            organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
            source_name: is the resource path for a source that has been created
            location_id: GCP location id; example: 'global'
        Returns:
             int: returns the filtered findings for a source
        """
        count = 0
        from google.cloud import securitycenter_v2
    
        # Create a new client.
        client = securitycenter_v2.SecurityCenterClient()
        parent = f"organizations/{organization_id}"
        all_sources = f"{parent}/sources/{source_name}/locations/{location_id}"
        finding_result_iterator = client.[list_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_findings)(
            request={"parent": all_sources, "filter": 'severity="LOW"'}
        )
        # Iterate an print all finding names and the resource they are
        # in reference to.
        for count, finding_result in enumerate(finding_result_iterator):
            print(
                "{}: name: {} resource: {}".format(
                    count, finding_result.finding.name, finding_result.finding.resource_name
                )
            )
        return count
    
    

Security Command Center also supports full JSON arrays and objects as potential property types. You can filter on:

  * Array elements
  * Full JSON objects with partial string match within the object
  * JSON object subfields



### Supported operators

The query statements for Security Command Center findings support the operators that most Google Cloud APIs support.

The following list shows the use of various operators:

  * `state**=** "ACTIVE" **AND NOT** mute**=** "MUTED"`
  * `create_time**>** "2023-08-15T19:05:32.428Z"`
  * `resource.parent_name**:** "prod"`
  * `severity**=** "CRITICAL" **OR** severity**=** "HIGH"`



The following list shows all of the operators and functions that are supported in query statements for findings:

  * For strings:

    * `=` for an exact match

For example, `resource.parent_name="prod"` matches the value `prod`. It doesn't match `production` or `canaryprod`.

    * `:` for a partial match

For example, `resource.parent_name:"prod"` matches the values `prod`, `production`, and `canaryprod`.

  * For numbers (except int64):

    * `<`, `>`, `<=`, `>=` for inequalities
    * `=`, `!=` for equality
  * For numbers (int 64):

    * `=`, `!=` for equality
  * For booleans:

    * `=` for equality
  * For logical relationships:

    * `AND`
    * `OR`
    * `NOT` or `-`
  * For grouping expressions:

    * `(`, `)` (parentheses)


  * For arrays: 
    * `contains()`, a function for querying findings with an array field that contains at least one element that matches the specified filter
    * `containsOnly()`, a function for querying findings with an array field that only contains elements that match the specified filter
  * For IP addresses: 
    * `inIpRange()`, a function for querying IP addresses within a specified CIDR range



### Filtering on IP addresses

Certain finding properties include IP addresses. You can filter findings based on specific IP addresses or a range of IP addresses.

IP addresses appear as strings in a variety of findings and finding properties, including the following:

  * `access.caller_ip`
  * `connections.destinationIp`
  * `connections.sourceIp`
  * `indicator.ip_addresses`



To filter on a specific IP address, you can use the equality operator, as shown in the following example:
    
    
    access.caller_ip="192.0.2.0"

To filter findings based on a range of IP addresses, use the `inIpRange` function. Using the `inIpRange` function, you filter findings to only those findings that contain a IP address within a specified CIDR range. By using the `NOT` operation with `inIpRange`, you can filter findings to only those findings that contain an IP address outside of the specified CIDR range.

The following example shows the syntax of the `inIpRange` function:
    
    
    inIpRange(IP_FINDING_FIELD, "CIDR_RANGE")
    

If the IP address is in an array element in a finding field that contains an array, use the following syntax with both `contains` function and the `inIpRange` function:
    
    
    contains(ATTRIBUTE_WITH_ARRAY, inIpRange(IP_FINDING_FIELD, "CIDR_RANGE"))
    

In the following example, the `inIpRange` function evaluates each `destination_ip` element of the array that is contained in the `connections` finding field for an IP address that is in the CIDR range defined by `192.0.2.0/24`:
    
    
    contains(connections, inIpRange(destination_ip, "192.0.2.0/24"))
    

The following example shows a gcloud CLI command that uses the `inIpRange` function to filter findings that have an IP address in the `connections.source_ip` field that is within one range, but not in another. The `connections` field is an array-type field, so the `contains` function is used:
    
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="contains(connections, inIpRange(source_ip, \"2001:db8::/32\")) \
          AND NOT contains(connections, inIpRange(source_ip, \"192.0.2.0/24\"))"

### Example JSON object

The examples later on this page assume the following JSON object is a finding attribute:
    
    
    {
      "outer_object": {
        "middle_object": {
          "deeply_nested_object": {
            "x": 123
          },
          "y": "some-string-value"
        },
        "list_middle_object": [
          {
            "v": 321,
            "w": [
              {
                "a": 3,
                "b": 4
              }
            ]
          }
        ],
        "z": "some-other-string-value",
        "u": [
          "list-element-1",
          "list-element-2",
          "list-element-3"
        ]
      }
    }
    

### Filtering findings example

Suppose the previous JSON example is a finding attribute named `my_property`. The following example includes queries for findings that have the object as a property. You can also use these filters with other filters using `AND` and `OR` in your query. For example, the first query uses the `ACTIVE` filter to display active findings.
    
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="state=\"ACTIVE\""
        --filter="my_property.outer_object.middle_object.deeply_nested_object.x = 123"
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="my_property.outer_object.middle_object.y = \"some-string-value\""
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="my_property.outer_object.middle_object.y : \"string-value\""
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="my_property.outer_object.z = \"some-other-string-value\""
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="my_property.outer_object.z : \"other-string-value\""
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="my_property.outer_object.u : \"list-element-1\""
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="my_property.outer_object.u : \"list-element-2\""
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="my_property.outer_object.u : \"list-element-3\""

**Note:** If you want to use these filters in the Google Cloud console, don't include the escape characters. For example, instead of `\"string-value\"`, use `"string-value"`.

### Subfilters for array-type fields

When calling [`ListFindings`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings/list), you can use a substring match `:`, which does a single check for a partial string match across the entire contents of the array. Alternatively, you can run a subfilter directly against elements of the array and its subfields using one of the following functions:

  * The `contains()` function to return findings when any elements of the array contains the specified value.

  * The `containsOnly()` function to return findings only if all elements of the array match the subfilter.




Both of these functions support subfilter query capabilities such as the following:

  * Exact element matching: Match array elements that contain the exact string, `"example"`.
  * Specific number operations: Match array elements that are greater than or equal to `100`.
  * Complex filtering against array structures: Match array elements that contain property `x` with a corresponding value `y`.



#### Format of the `contains()` function

The `contains()` function has the following format:
    
    
    contains(ARRAY_ATTRIBUTE_NAME, SUBFILTER)
    

Replace the following:

  * `ARRAY_ATTRIBUTE_NAME`: a field or subfield that is of type array (a list).
  * `SUBFILTER`: an expression that defines the values to look for in the array. The subfilter's format differs depending on whether `ARRAY_ATTRIBUTE_NAME` is an array of objects or an array of primitive-type elements. If the `ARRAY_ATTRIBUTE_NAME` is an array of objects that have nested arrays, you can use a scoped subfilter to specify that you want all conditions to be satisfied within the same `ARRAY_ATTRIBUTE_NAME` element.



The Security Command Center API returns findings where the `ARRAY_ATTRIBUTE_NAME` contains at least one element that satisfies the `SUBFILTER`.

**Note:** If you want to use these filters in the Google Cloud console, don't include the escape characters. For example, instead of `\"string-value\"`, use `"string-value"`.

#### Format of the `containsOnly()` function

The `containsOnly()` function has the following format:
    
    
    containsOnly(ARRAY_ATTRIBUTE_NAME, SUBFILTER)
    

Replace the following:

  * `ARRAY_ATTRIBUTE_NAME`: a field or subfield that is of type array (a list). When you are running queries using the Security Command Center API, you can use the `containsOnly()` function for any available array attribute.
  * `SUBFILTER`: an expression that defines the values to look for in the array. The subfilter's format differs depending on whether `ARRAY_ATTRIBUTE_NAME` is an array of objects or an array of primitive-type elements. If the `ARRAY_ATTRIBUTE_NAME` is an array of objects that have nested arrays, you can use a scoped subfilter to specify that you want all conditions to be satisfied within the same `ARRAY_ATTRIBUTE_NAME` element.



The Security Command Center API returns findings where all of the `ARRAY_ATTRIBUTE_NAME` elements match the `SUBFILTER`.

**Note:** If you want to use these filters in the Google Cloud console, don't include the escape characters. For example, instead of `\"string-value\"`, use `"string-value"`.

#### Subfilter for an array of objects

The following is an excerpt of the previous JSON example. Here, the `list_middle_object` field is an array of objects:
    
    
        "list_middle_object": [
          {
            "v": 321,
            "w": [
              {
                "a": 3,
                "b": 4
              }
            ]
          }
        ]
    

The following example queries for findings where at least one of the elements in the `list_middle_object` field has a `v` subfield with a value greater than or equal to 321:
    
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="contains(my_property.outer_object.list_middle_object, v  >= 321)"

For practical examples that use the `contains()` and `containsOnly()` functions, see [Findings that contain specific array values](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#array-contains-filtering).

#### Subfilter for an array that contains primitive-type elements

Primitive types are strings, numbers, and booleans. To use the `contains()` function against an array that contains primitive types, you use the special keyword, `elem`.

The following is an excerpt of the previous JSON example. Here, the `u` field is an array of primitive-type elements:
    
    
    "u": ["list-element-1", "list-element-2", "list-element-3"]
    

The following example queries for findings where at least one of the elements in the `u` field is "list-element-1":
    
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="contains(my_property.outer_object.u, elem = \"list-element-1\")"

For practical examples that use the `contains()` function, see [Findings that contain specific array values](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#array-contains-filtering).

#### Scoped subfilter

The following is an excerpt of the previous JSON example. Here, the `list_middle_object` field is an array of objects, and objects in this array contain a nested array.
    
    
    "list_middle_object": [
      {
        "v": 321,
        "w": [
          {
            "a": 3,
            "b": 4
          }
        ]
      }
    ]
    

The following example queries for findings where both of the following conditions are satisfied within the same `list_middle_object` element:

  * The `v` subfield has a value greater than or equal to 321.
  * The `w` subfield doesn't contain an element with an `a` property equal to 3.


    
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter="contains(my_property.outer_object.list_middle_object, v  >= 321 AND -contains(w, a = 3))"

For practical examples that use the `contains()` function, see [Findings that contain specific array values](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#array-contains-filtering).

### Sorting findings example

You can sort findings by strict subfields that are primitive types—strings, numbers, and booleans. Suppose the previous JSON example is a finding attribute named `my_property`. The following example includes queries to sort the finding fields. The keyword `DESC` specifies that the field it follows must be sorted in descending order. The default order is ascending.
    
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --order-by="my_property.outer_object.middle_object.deeply_nested_object.x DESC"
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --order-by="my_property.outer_object.middle_object.deeply_nested_object.x"
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --order-by="my_property.outer_object.middle_object.y DESC"
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --order-by="my_property.outer_object.middle_object.y"
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --order-by="my_property.outer_object.z DESC"
    
    gcloud scc findings list PARENT_TYPE/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --order-by="my_property.outer_object.z"

## Filter examples

The following sections show practical examples of finding filters.

**Note:** If you want to use these filters in the Google Cloud console, don't include the escape characters. For example, instead of `\"string-value\"`, use `"string-value"`.

### Filter for findings that occurred after a point in time

These example filters match findings that most recently occurred after Wednesday, June 5, 2019 10:12:05 PM GMT. With the `event_time` filter, you can express time using the following formats and types:

  * Unix epoch time (in milliseconds) as an integer literal
        
        "event_time > 1559772725000"
        

  * RFC 3339 as a string literal
        
        "event_time > \"2019-06-05T22:34:40+00:00\""
        




### Filter on array-type fields

The following example shows the use of a partial string match on an array-type field within a filter:
    
    
    "indicator.domains : \"website.com\""
    

The Security Command Center API returns any finding with a `website.com` partial string within the array. For example, it matches a finding with `indicator.domains = [\"onewebsite.com\"]` because "website.com" is a substring in an element in the array.

In the following sections, the example filters show some options for use of rich array-type filtering using the `contains()` function.

#### Filter on the `vulnerability.cve.references` field

The following example returns findings where at least one element in the `vulnerability.cve.references` array has both a `source` property equal to `SOURCE_OF_REFERENCE` and a `uri` property that has `FILTERED_URI`.
    
    
    "contains(vulnerability.cve.references, source = \"SOURCE_OF_REFERENCE\" AND uri : \"FILTERED_URI\")"
    

Replace the following:

  * `SOURCE_OF_REFERENCE`: name of the source of a [Common Vulnerabilities and Exposures](https://cve.mitre.org) (CVE) reference—for example, `NVD`.
  * `FILTERED_URI`: URI of the source of the CVE reference.



#### Filter on the `indicator.domains` field

The following example returns findings where at least one indicator domain has both `mycompanyprefix` and `.ca`.
    
    
    "contains(indicator.domains, elem : \"mycompanyprefix\" AND elem : \".ca\")"
    

#### Filter on the `indicator.ip_addresses` field

The following example returns findings where at least one element in the `indicator.ip_addresses` array is equal to `IP_ADDRESS`.
    
    
    "contains(indicator.ip_addresses, elem = \"IP_ADDRESS\")"
    

Replace `IP_ADDRESS` with an IP address associated with the findings you're searching for.

#### Filter on external system assignees

The following example returns findings where at least one element in the `external_systems.EXTERNAL_SYSTEM_NAME.assignees` array is equal to `ASSIGNEE`.
    
    
    "contains(external_systems.EXTERNAL_SYSTEM_NAME.assignees, elem = \"ASSIGNEE\")"
    

Replace the following:

  * `EXTERNAL_SYSTEM_NAME`: the name of a third-party SIEM/SOAR system—for example, `demisto`.
  * `ASSIGNEE`: an assignee in the external system.



#### Filter on the `resource.folders.resource_folder` field

The following example returns findings where at least one element in the `resource.folders.resource_folder` array is not equal to `FOLDER_NAME`.
    
    
    "contains(resource.folders.resource_folder, -(elem = \"FOLDER_NAME\"))"
    

#### Filter on the `resource.folders.resource_folder_display_name` field

The following example returns findings where at least one element in the `resource.folders.resource_folder_display_name` array is equal to `DISPLAY_NAME`.
    
    
    "contains(resource.folders.resource_folder_display_name, elem = \"DISPLAY_NAME\")"
    

Replace `DISPLAY_NAME` with the user-defined name of the folder associated with the findings you're searching for.

#### Filter includes only specific service accounts

The following example returns findings only when every `iam_bindings` entry's member value is equal to one of the provided service accounts.
    
    
    containsOnly(iam_bindings, (member = SERVICE_ACCOUNT1 OR member = SERVICE_ACCOUNT2 OR member = "SERVICE_ACCOUNT3 "))
    

Replace `SERVICE_ACCOUNT1`, `SERVICE_ACCOUNT2`, and `SERVICE_ACCOUNT3` with the email addresses for the service accounts.

To learn how to use the `contains()` and `containsOnly()` functions in a finding filter, see Subfilters for array-type fields.

## What's next

Learn more about [setting up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
