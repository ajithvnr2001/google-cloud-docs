---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-group-all-findings/
title: Group findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:58.540608+00:00
---

# Group findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-group-all-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Group findings Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to group findings by properties

## Code sample

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static ImmutableList<GroupResult> groupFindings(OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Input parameters for 'SourceName' must be in one of the following formats:
        //    * OrganizationName organizationName = OrganizationName.of("organization-id");
        //      organizationName.getOrganization();
        //    * ProjectName projectName = ProjectName.of("project-id");
        //      projectName.getProject();
        //    * FolderName folderName = FolderName.of("folder-id");
        //      folderName.getFolder();
        SourceName sourceName = SourceName.of(organizationName.getOrganization(), "-");
    
        GroupFindingsRequest.Builder request =
            GroupFindingsRequest.newBuilder().setParent(sourceName.toString()).setGroupBy("category");
    
        // Call the API.
        GroupFindingsPagedResponse response = client.groupFindings(request.build());
    
        // This creates one list for all findings.  If your organization has a large number of
        // findings
        // this can cause out of memory issues.  You can process them batches by returning
        // the Iterable returned response.iterateAll() directly.
        ImmutableList<GroupResult> results = ImmutableList.copyOf(response.iterateAll());
        System.out.println("Findings:");
        System.out.println(results);
        return results;
      } catch (IOException e) {
        throw new RuntimeException("Couldn't create client.", e);
      }
    }

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
    group_result_iterator = client.[group_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_group_findings)(
        request={"parent": all_sources, "group_by": "category"}
    )
    for i, group_result in enumerate(group_result_iterator):
        print((i + 1), group_result)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
