---
url: https://docs.cloud.google.com/secure-source-manager/docs/create-issues-pull-request-templates/
title: Create issue and pull request templates \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:11.177652+00:00
---

# Create issue and pull request templates  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/create-issues-pull-request-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Create issue and pull request templates Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and configure issues templates and pull request templates for Secure Source Manager. 

## Required roles

To get the permissions that you need to work with issues and pull request templates, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance
  * [Secure Source Manager Repo Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`) on the repository



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Templates overview

Issues and pull request templates let you standardize the information contributors provide to a repository. Issue templates offer predefined options a user can choose from depending on the type of issue they are submitting and the template types available. A pull request template is automatically applied to all pull requests, ensuring consistent contributions to the repository.

Templates can be created by anyone with permission to merge files in a repository.

## Create an issues template

Secure Source Manager lets you define issues templates using Markdown files in multiple locations in your repository. You can create multiple issue templates for different purposes. For example, you may want to have a separate templates for reporting bugs and submitting feature requests.

  1. Create a template that begins with the following information, in this exact format:
         
         ---
          name: TEMPLATE_NAME
          about: Insert description of template
          title: Placeholder title for the new issue when it is created
          ---
         

  2. Provide a name, and description. These are required and are used in the UI of the New Issues page.

  3. You can optionally include a title that is used as a placeholder title when a new issue is created.

  4. Below the required material, include any information you would like to be visible in the issue description that will assist users in providing necessary information.

  5. Save your template as a Markdown file in one of the following locations:

     * `/.securesourcemanager/ISSUE_TEMPLATES/`
     * `/.securesourcemanager/issue_templates/`

**Note:** If templates are found in more than one location, Secure Source Manager uses the template from the first folder in your directory.

### Default issues template

Secure Source Manager also supports the definition of a single default template. This template should be defined in one of the following locations:

  * `/.securesourcemanager/ISSUE_TEMPLATE.md`
  * `/.securesourcemanager/issue_template.md`



When a user creates a new issue, Secure Source Manager prompts that user to select a template, if any are available, or selects the default template. If there's no designated default template, nothing is pre populated into the new issue.

### Example Issues template

The first 5 lines of the template must follow the conventions outlined in the following example. Any additional information can be formatted in Markdown to suit the needs of the issue type.
    
    
    ---
    name: Bug #Used as UI element for the button on the New Issues page
    about: Use this template to submit a new bug #Used as description text on the New Issues page
    title: [BUG]: <Describe issue> #Used as placeholder name for newly created issue
    ---
    # Description
    
    # Expected result
    
    # Actual result
    
    # Steps to reproduce
    1.
    2.
    
    # Environment
    -OS:
    -Software version:
    -Screenshots:
    

## Create a pull request template

  1. Create a template that begins with the following information, in this exact format:
         
         ---
          title: "[PR]: <Insert title>"
          ---
         

  2. Below the required material, include any information you would like to be visible in the issue description to assist users in providing necessary information. See the example template in the following section for more details.

  3. Save the template as a Markdown file in one of the following locations inside a repository:

     * `/.securesourcemanager/PULL_REQUEST_TEMPLATE.md`
     * `/.securesourcemanager/pull_request_template.md`



When you create a new pull request, Secure Source Manager checks if a template exists in any of the defined locations and loads it. If you included **title** information in your template, it's automatically populated in the new pull request to provide users with a defined format to follow. Any additional information you included is added to the pull request description to be updated by the submitting user.

### Example Pull Request template

The first 3 lines of the template must follow the conventions shown in the following example. Everything that follows is options and should assist your users in creating pull requests that follow your conventions.
    
    
    ---
    title: "[PR]: <Insert title>"
    ---
    <!-- Thank you for your contribution! -->
    
    <!-- Include if applicable: -->
    Fixes: #nnn <!-- tracking issues that this PR will close -->
    **Related**: _Relevant tracking issues, for context_
    **Merge before/after**: _Dependent or prerequisite PRs_
    
    **Description**
    <!-- Describe your changes here. The more detail, the easier the review! -->
    
    **User facing changes (remove if N/A)**
    <!-- Describe any user facing changes this PR introduces. -->
    <!-- "Before" and "After" sections work great - bonus points for screenshots! -->
    <!-- Be sure all docs have been updated as well! -->
    
    **Follow-up Work (remove if N/A)**
    <!-- Mention any related follow up work to this PR. -->
    

## What's next

  * Visit [Work with issues and pull requests](https://docs.cloud.google.com/secure-source-manager/docs/work-with-issues-pull-requests) for details on how to work with issues and pull requests in Secure Source Manager.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
