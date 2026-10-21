---
url: https://docs.cloud.google.com/billing/docs/how-to/reports-project-hierarchy/
title: Billing reports: Analyzing your costs by project hierarchy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:14.887438+00:00
---

# Billing reports: Analyzing your costs by project hierarchy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/reports-project-hierarchy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Billing reports: Analyzing your costs by project hierarchy Stay organized with collections  Save and categorize content based on your preferences. 

Viewing your costs by project hierarchy helps you analyze costs by folder or organization. For example, if you use folders in an organization to represent cost centers, you can effectively configure your report to group all costs by those cost centers.

To analyze your costs by project hierarchy, including costs by Organizations or costs by Folders, set the report's [**Group by** option to **Project hierarchy**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project-hierarchy). You can also use the report's [**Folders & Organizations filter**](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-folders-orgs) to select specific folders/organizations to focus the data returned in the report.

![Shows report configured to group by project hierarchy.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-project-hierarchy.png)

## About project and resource hierarchy

[Projects](https://docs.cloud.google.com/billing/docs/concepts#projects) form the basis for creating, enabling, and using all Google Cloud services. [Folders](https://docs.cloud.google.com/billing/docs/concepts#folders) are used to group projects under the [organization node](https://docs.cloud.google.com/billing/docs/concepts#organization) in a [resource hierarchy](https://docs.cloud.google.com/billing/docs/concepts#gcp_resource_hierarchy_overview). A folder can contain projects, other folders, or a combination of both. Each resource has exactly one parent.

Metaphorically speaking, the Google Cloud resource hierarchy resembles the file system found in traditional operating systems as a way of organizing and managing entities hierarchically. From a cost management perspective, you might use folders in an organization to represent cost centers (such as _Devops_ or _Finance_). You can view your costs by project hierarchy to analyze your costs by folder.

_Project hierarchy_ is the ancestry of a project, the resource hierarchy mapping of the project (Organization > Folder > Project). Projects can stand alone (that is, not be associated with any folders or organizations) or be the child of an _Organization_ or _Folder_. Project hierarchy tracks the _current_ and _historical_ project ancestry. For example, changing a project's name, or moving a project to a different folder or organization, affects the _historical_ project ancestry.

To gain a deeper understanding about resource hierarchy and Cloud Billing, refer to [Cloud Billing concepts, Resource hierarchy ](https://docs.cloud.google.com/billing/docs/concepts#gcp_resource_hierarchy_overview).

## Configure your report to show project hierarchy

To view your costs by project hierarchy (organization > folder > project), take the following steps:

  1. In the Google Cloud console, [open the Reports page](https://console.cloud.google.com/billing/reports) for the Cloud Billing account you want to analyze.
  2. In the report Filters, set a [**Time range**](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range) to use a **_starting date_** _on or after_ **January 1, 2022**.
  3. In the [**Group by**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) selector, choose [**Project hierarchy**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project-hierarchy).

The report returns a row for each unique combination of _Organization > Folder > Project_, and the table includes columns for _Project_ , _Project ID_ , _Project number_ , and _Project hierarchy_.

The values listed in the _Project hierarchy_ column show _Organization name > Folder name_.




### Analyze the report when grouped by Project hierarchy

  * You can [**sort the table data**](https://docs.cloud.google.com/billing/docs/how-to/reports#data_order) on different columns to view the project hierarchy costs in different ways:

    * To visualize _all of the projects_ that have the _same project hierarchy_ , sort the table by the **Project hierarchy** column.
    * To visualize if you have the _same project_ associated with _more than one_ ancestry, sort the table by the **Project ID** column.
  * You can narrow the report's project hierarchy results using the [**Folders & Organizations**](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-folders-orgs) filter.

  * While you are viewing the report grouped by _Project hierarchy_ , if you change the report's time range to include a _starting date prior to January 1, 2022_ , the [_Group by_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) selection is automatically updated to group by _Project_.

  * If you select some folders or organizations in the [_filter_](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-folders-orgs), and then update the _time range_ to include a _starting date prior to January 1, 2022_ , the folders/organizations selections are removed.




## Understand and analyze changes in project ancestry

For the time range you are analyzing, it is possible for the same Project to be listed in more than one row in the report table. This can occur if something related to the project's ancestry has changed. Changes that affect a project's ancestry include the following:

  * Changing the project's name
  * Moving the project to a different organization and/or folder
  * Changing a parent folder's name
  * Moving a parent folder into another folder and/or organization



To **visualize if you have projects associated with more than one ancestry** , [**sort the table data**](https://docs.cloud.google.com/billing/docs/how-to/reports#data_order) by the **Project ID** column.

### Examples of changes in project hierarchy

The following examples show different scenarios where something related to the project's ancestry was changed, and how that change impacts the results in the report, depending on how you **Group** the results.

All of these examples assume that the changes affecting the project ancestry occurred after January 1, 2022.

### Example 1: Project name change

You can edit a project's display name, but the project ID and the project number are immutable and remain constant.

[Group by _Project_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project)

Project (name) | Project ID | Project number  
---|---|---  
Current Project Name | my-project-1 | 123456  
  
[Group by _Project hierarchy_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project-hierarchy)

Project (name) | Project ID | Project number | Project hierarchy  
---|---|---|---  
**Old Project Name** | my-project-1 | 123456 | Org1.net > folder1  
Current Project Name | my-project-1 | 123456 | Org1.net > folder1  
  
Notes about _project name changes_ when grouping by _project hierarchy_ :

  * For the report's time range, if the project has not incurred any usage _after_ the name is changed, then you will only see one row for the project, listed as _Old Project Name_.
  * For the report's time range, if the selected time range _starts after_ the date the project's name was changed, then you will only see one row for the project, listed as _Current Project Name_.
  * If you use the [Project filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-projects) to select a project, the project's name displayed in the list of options is always the _Current Project Name_. The _project ID_ is not editable and remains the same after a project's name is edited.



### Example 2: Project moved to a different parent folder

In this example, _My test project_ is moved from _folder1_ to _folder2_. After the move, _My test project_ is now a child of _folder2_. Folders are always the child of a parent organization.

[Group by _Project_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project)

Project (name) | Project ID | Project number  
---|---|---  
My test project | my-project-1 | 123456  
  
[Group by _Project hierarchy_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project-hierarchy)

Project (name) | Project ID | Project number | Project hierarchy  
---|---|---|---  
My test project | my-project-1 | 123456 | Org1.net > folder1  
My test project | my-project-1 | 123456 | **Org1.net > folder2**  
  
### Example 3: Parent folder moved _into_ a different folder

In this example, _folder1_ is moved into _test folder_. After the move, _folder1_ is now a child (or subfolder) in the parent _test folder_. Folders are always the child of a parent organization.

[Group by _Project_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project)

Project (name) | Project ID | Project number  
---|---|---  
My test project | my-project-1 | 123456  
  
[Group by _Project hierarchy_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project-hierarchy)

Project (name) | Project ID | Project number | Project hierarchy  
---|---|---|---  
My test project | my-project-1 | 123456 | Org1.net > folder1  
My test project | my-project-1 | 123456 |  **Org1.net > test folder > folder1**  
  
### Example 4: Name change of a parent folder

You can edit a folder's display name, but the folder ID is immutable and remains constant.

[Group by _Project_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project)

Project (name) | Project ID | Project number  
---|---|---  
My test project | my-project-1 | 123456  
  
[Group by _Project hierarchy_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project-hierarchy)

Project (name) | Project ID | Project number | Project hierarchy  
---|---|---|---  
My test project | my-project-1 | 123456 | Org1.net > Folder Old Name  
My test project | my-project-1 | 123456 | **Org1.net > Folder New Name**  
  
Notes about _folder name changes_ when grouping by _project hierarchy_ :

  * For the report's time range, if the folder's projects have not incurred any usage _after_ the folder's name is changed, then you will only see one row for the folder, listed as the Org > _old folder name_.
  * For the report's time range, if the selected time range _starts after_ the date the folder's name was changed, then you will only see one row for the folder, listed as the Org > _current folder name_.
  * If you use the [Folders & Organizations filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-folders-orgs) to select a folder, the folder's name displayed in the list of options is always the _Current Folder Name_. The _folder ID_ (displayed below the folder name) is not editable and remains the same after a folder's name is edited.



### Example 5: Project moved to a different organization

In this example, _My test project_ is moved from _Org1.net_ to _Org2.com_ , and the project is not in any folder. After the move, _My test project_ is now a child of _Org2.com_.

[Group by _Project_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project)

Project (name) | Project ID | Project number  
---|---|---  
My test project | my-project-1 | 123456  
  
[Group by _Project hierarchy_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project-hierarchy)

Project (name) | Project ID | Project number | Project hierarchy  
---|---|---|---  
My test project | my-project-1 | 123456 | Org1.net  
My test project | my-project-1 | 123456 | **Org2.com**  
  
### Example 6: Project moved to a different billing account

Cloud Billing accounts exist outside of the project's [resource hierarchy](https://docs.cloud.google.com/billing/docs/concepts#gcp_resource_hierarchy_overview). If you [move a project to a different billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project), the project hierarchy remains attached to the project.

[Grouped by _Project hierarchy_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project-hierarchy)

Viewing report for **OLD billing account**

Project (name) | Project ID | Project number | Project hierarchy  
---|---|---|---  
My test project | my-project-1 | 123456 | Org1.net > Folder1  
  
Viewing report for **NEW billing account**

Project (name) | Project ID | Project number | Project hierarchy  
---|---|---|---  
My test project | my-project-1 | 123456 | Org1.net > Folder1  
  
## Related topic

  * [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
