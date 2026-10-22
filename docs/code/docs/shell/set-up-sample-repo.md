---
url: https://docs.cloud.google.com/code/docs/shell/set-up-sample-repo/
title: Manage custom sample repositories in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:25.966432+00:00
---

# Manage custom sample repositories in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/set-up-sample-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Manage custom sample repositories in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

A sample repository is a Git repository that contains custom samples you create that your team can use to develop applications.

This means that, within an organization or team, you can set up sample repositories with Cloud Code, custom to your organization, to offer a standard set of starter applications, services, and infrastructure configuration that others can use. This helps align new projects with your organization's preferred technical stack and standards, and encourages best practices at the beginning of the development cycle.

A sample repository can be an existing repository of sample applications you've already created or a new set of samples you'd like others to use. To import a repository with Cloud Code, you add a sample descriptor file to the repository.

When ready, sample repositories are easy to share with your team; they'll need Cloud Code set up and the Git URL of the sample repository to use. For private Git repositories, only members that have access to the repository can use the underlying custom samples.

To see an example of how a sample repository might be set up, reference this [repository](https://github.com/GoogleCloudPlatform/cloud-code-custom-samples-example/).

## Creating a sample repository

To use an existing repository, skip to creating a sample descriptor file. To create a new repository to use as a sample repository, follow these steps:

  1. Create a new Git repository.

Your Git repository can be hosted remotely or live on your local machine. This example uses a new GitHub repository, 'custom-sample-repo'.

![GitHub repository creation interface with repository name field filled with 'custom-sample-repo'](https://docs.cloud.google.com/static/code/docs/vscode/images/new-custom-repo.png)

  2. Add sample directories to the repository.

Your sample directories can contain anything and be located anywhere you want in the repository. In this example, two sample directories, 'hello-world' and 'kubernetes-custom-sample', have been added to 'custom-sample-repo'.

A readme file with instructions on how best to use your custom samples is highly recommended.

!['custom-sample-repo' with two underlying sample directories, 'hello-world' and 'kubernetes-custom-sample'](https://docs.cloud.google.com/static/code/docs/vscode/images/sample-repo-structure.png)

  3. Create a sample descriptor file.

A sample descriptor file provides Cloud Code with information on your sample to properly create your application. This file must be named `.cctemplate`, must be located in your root directory, and must have the schema defined in the sample descriptor file schema section.

  4. Test your custom sample by following the steps to [create an app from a custom sample](https://docs.cloud.google.com/code/docs/shell/create-app-from-custom-sample).




## Sample descriptor schema

**Key** | **Description** | **Type**  
---|---|---  
metadata  | Metadata used by Cloud Code to read. Conforms to the metadata schema.  | Metadata   
templates  | Array of samples contained in a repository. Objects in this array must conform to the Sample Schema.  | Array<Sample>  
name (optional) | Name of the sample repository.  | String   
  
#### Example
    
    
    {
       "metadata":{
          "version":"1"
       },
       "name": "My Sample Repository",
       "templates":[
          {
             "path":"/path/to/sample1_location",
             "name":"My Sample 1",
             "description":"The first sample of its name."
          },
          {
             "path":"/path/to/sample2_location",
             "name":"My Sample 2",
             "description":"The sequel."
          }
       ]
    }
    

### Sample schema

**Key** | **Description** | **Type**  
---|---|---  
path  | The location of the sample in a repository.  
The path is relative to the root of the repository.  | String   
name  | Name of a sample.  
The name is displayed in an IDE when selecting a sample to base an application on.  | String   
description (optional) | Description of a sample.  
The description is displayed in an IDE when selecting a sample to base an application on.  | String   
  
#### Example
    
    
    {
       "path":"path/to/sample1",
       "name":"My Sample 1",
       "description":"The first sample of its name."
    }
    

### Metadata schema

**Key** | **Description** | **Type**  
---|---|---  
version  | The version of the sample schema to use. The only valid version is `1`.  | String   
  
#### Example
    
    
    {
       "version":"1"
    }
    

## Deleting a custom sample repository

To delete a custom sample, which removes it from the custom application selector flow and from users' machines:

  1. In the `settings.json` file, look up the `localPath` for the custom sample entry.
         
         "cloudcode.customApplications": [
           {
             "repoUrl": https://github.com/GoogleCloudPlatform/cloud-code-custom-samples-example.git,
             "branchName": "",
             "localPath": "/Users/username/Library/cloud-code/custom-templates/https-github-com-google-cloud-platform-cloud-code-custom-samples-example-git"
           }
         ],
         

  2. Delete the template folder at the path.

**Note:** On Macs, `Library` is a hidden folder.
  3. Delete the custom sample section from the `settings.json` file.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
