---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-group-all-assets-with-filter/
title: Group assets with filter \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:08.810550+00:00
---

# Group assets with filter  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-group-all-assets-with-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Group assets with filter Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to filter and group assets by type

## Code sample

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static ImmutableList<GroupResult> groupAssetsWithFilter(OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to filter all assets by type and group them by project in an
        // organization.
        // You can also use a project or folder as a parent resource and filter assets in them
        // respectively.
        GroupAssetsRequest.Builder request =
            GroupAssetsRequest.newBuilder()
                .setFilter(
                    "security_center_properties.resource_type=\"google.cloud.resourcemanager.Project\"")
                .setGroupBy("security_center_properties.resource_project")
                .setParent(organizationName.toString());
    
        // Call the API.
        GroupAssetsPagedResponse response = client.groupAssets(request.build());
    
        // This creates one list for all assets.  If your organization has a large number of assets
        // this can cause out of memory issues.  You can process them batches by returning
        // the Iterable returned response.iterateAll() directly.
        ImmutableList<GroupResult> results = ImmutableList.copyOf(response.iterateAll());
        System.out.println("All assets:");
        System.out.println(results);
        return results;
      } catch (IOException e) {
        throw new RuntimeException("Couldn't create client.", e);
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter
    
    client = securitycenter.SecurityCenterClient()
    
    # 'organization_id' is the numeric ID of the organization.
    # organization_id = "1234567777"
    org_name = f"organizations/{organization_id}"
    
    group_by_type = "security_center_properties.resource_type"
    only_projects = (
        "security_center_properties.resource_type="
        + '"google.cloud.resourcemanager.Project"'
    )
    # You can also use a project/ folder as a parent resource and filter assets in them
    # respectively.
    result_iterator = client.[group_assets](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_group_assets)(
        request={"parent": org_name, "group_by": group_by_type, "filter": only_projects}
    )
    for i, result in enumerate(result_iterator):
        print((i + 1), result)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
