---
url: https://docs.cloud.google.com/resource-manager/docs/listing-all-resources/
title: List all projects and folders in your hierarchy \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:26.935720+00:00
---

# List all projects and folders in your hierarchy  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/listing-all-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  List all projects and folders in your hierarchy Stay organized with collections  Save and categorize content based on your preferences. 

Resources in Google Cloud are organized into a [hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), with each node (Organizations, Folders, Projects, and so forth) having a reference to its parent. You can use that reference as a key filter term for scans to improve the consistency of resource searches.

You can grant users permissions using [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles). These roles operate on the principle of least privilege, and generally provide only the minimum necessary permissions required to do a particular task.

This scheme can be useful for isolating different user groups. For example:

  * A large company with departments that shouldn't be able to inspect the resources of their peers.
  * Contractors who are given permissions to a specific Project, but no other resources.



As a result of their restricted permissions, however, custom roles may cause many resources in your hierarchy to be omitted when executing a list operation. When performing searches as a user that has been granted a custom role, it can be difficult to tell why certain resources are not appearing.

To avoid this scenario, this page discusses the best practices for listing all of the resources managed by the Cloud Resource Manager API in your resource hierarchy. You can use this guidance to configure custom audit checks, or to create your own user experience on top of the Cloud Resource Manager API.

## List all resource nodes

When you scan your resource hierarchy to list every resource, you need strongly consistent results. If your scan misses resources or provides outdated results, it can be hard to tell that something has gone wrong. To make sure that you always get the most accurate and complete results, use a service account and perform a scan in the following way:

  1. Grant a service account the `list` and `get` permissions for Organizations, Folders, and Projects on the Organization resource.
  2. If you are listing Project and Folder resources, specify the parent resource in the filter string.
  3. Run the [`projects.list()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list) method with this service account for each type of resource you want to find, and for any intermediate resources such as Folders.



### Example to list all resource nodes

The following pseudocode demonstrates how to list every resource node in your Organizations:
    
    
    organizations = organizations.search()
    projects = emptyList()
    
    parentsToList = queueOf(organizations)
    while (parent = parentsToList.pop()) {
      // TODO: Iterate over paginated results as needed.
      // TODO: Handle PERMISSION_DENIED appropriately.
      projects.addAll(projects.list(parent.type, parent.id))
      parentsToList.addAll(folders.list(parent))
    }
    

When building a custom user experience, you may also want to mix in search results and load the parent resources as needed (while also catching the `PERMISSION_DENIED` exception).

## Reduce latency on gcloud projects list

If your `gcloud projects list` query fails or takes too long, the number of Google Cloud projects to return might be too large. To fix this, apply the `filter` and `page-size` flags to your `gcloud projects list` command.

To learn more about the flags you can add to your `gcloud projects list` command, see [gcloud projects list](https://docs.cloud.google.com/sdk/gcloud/reference/projects/list).

### Exclude Apps Script projects example

The most common cause of query failures or latency is a high number of Apps Script projects within an organization. The following command shows how to exclude Apps Script projects from the projects list and limit the number of resources returned per page.
    
    
    gcloud projects list --filter="NOT parent.id: 'APPS_SCRIPT_FOLDER_ID' "--page-size='30'
    

#### Get the Apps Script folder ID

To find your Apps Script folder ID, take the following steps.

  1. In the toolbar of the Google Cloud console, click **Search for resources, docs, products, and more** and type `apps-script`.

[Go to Google Cloud console](https://console.cloud.google.com/welcome)

  2. Under **Resources** select the **apps-script** folder.

  3. Under **Folder ID** copy the folder ID.




## Search resources

If your scan is intended to search for a resource that was created some time ago, you can perform a faster scan that has eventual consistency rather than strong consistency. Note that this search method may omit some resources from the search result, particularly any resources that have been changed recently. To search for resources:

  1. Use a service account that has the `get` permission for the resource you are searching for.
  2. Run the [`projects.search()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search) method with this service account.



## Troubleshooting omitted resources

If you are developing a scanning tool, we recommend that you use `list` and `get` permissions granted at the Organization level. This avoids issues caused by the user having partial permissions, which results in some resources being omitted from the list.

If you are designing a custom user experience that checks user permissions, there is no straightforward solution. If a user does not have Organization-level permissions, they will need certain permissions on every resource for it to appear. If a user is missing permissions on a resource somewhere in the hierarchy, some resources may not appear.

If a user has the `list` permission but not the `get` permission for a particular resource, that resource won't be visible at all in the Google Cloud console. However, the resource will be returned in a search using the API or Google Cloud CLI that specifies the resource's parent. This disparity between the Google Cloud console and other methods is a common source of confusion when trying to scan the resource hierarchy.

The following diagrams demonstrate some common configurations of permissions, and how they change what resources are visible to a user running a search.

![Listing all resources](https://docs.cloud.google.com/resource-manager/img/list-all.svg)

In this example, all required permissions are granted in the Organization resource. Therefore, the entire hierarchy is visible when performing a list or search.

![Missing organization permissions](https://docs.cloud.google.com/resource-manager/img/list-no-org.svg)

The user in this example has all required permissions except for `resourcemanager.organizations.get`, but they are granted those permissions at the Folder level. This permissions gap gives them full visibility on list or search of that part of the hierarchy, but not the other half.

![Project get permission only](https://docs.cloud.google.com/resource-manager/img/list-project-get.svg)

This example shows the experience of a user with only the `resourcemanager.projects.get` permission granted at the Folder resource level. They are able to see the Projects underneath that Folder in the hierarchy, but only by searching. Using the list functionality won't return any results.

![Folder get permission only](https://docs.cloud.google.com/resource-manager/img/list-folder-get.svg)

This example illustrates a similar scenario where the granted permissions only let you find your Folder resources by searching. The list operation does not return any results.

![Mixed permissions](https://docs.cloud.google.com/resource-manager/img/list-mixed.svg)

The user in this example has a mix of permissions throughout their Organization. They can list folders from the Organization level, which allows them to find them with searches that specify the parent resource throughout the hierarchy. They can list Project resources for one Folder, but not the other, and they have `resourcemanager.projects.get` permission on one Project at the bottom of the hierarchy.

The result is that they aren't able to return the Projects on the left side of this resource hierarchy. They can list the Projects on the right side only by using a search that specifies the parent resource, and only one Project is visible when viewed in the Google Cloud console.

![Undiscoverable resources](https://docs.cloud.google.com/resource-manager/img/list-undiscoverable.svg)

In this example, you can get the Organization resource and list Project resources by specifying the parent throughout the hierarchy. However, you don't have permission to list or search any intermediate Folders. Your Projects are searchable if you know the ID of their parent Folder. The Folders are not visible to you, so you can't discover the ID if you don't already have it. The only resource that appears in the Google Cloud console is the Organization.

When designing your custom user experience, it's important to be aware of situations similar to these situations. You can use a combination of listing and searching to render the resource hierarchy. You should also consider how to communicate to users that they are missing permissions that would allow them to see the whole resource hierarchy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
