---
url: https://docs.cloud.google.com/shell/docs/open-in-cloud-shell/
title: Open in Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:31.882259+00:00
---

# Open in Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/open-in-cloud-shell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Open in Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

The Open in Cloud Shell feature allows you to publish a link that opens the Google Cloud console with a Git repository cloned into Cloud Shell and/or starts Cloud Shell with a custom image. You can also print instructions to the terminal to help users interact with the content.

Open in Cloud Shell links help developers experiment with your code samples and APIs without having to download the Google Cloud CLI, install required dependencies, or search for relevant source files. This page explains how to add an Open in Cloud Shell link to your Git repository.

**Note:** Only GitHub and Bitbucket repositories are permitted by default. If you would like to add a different repository, [ send feedback](https://docs.cloud.google.com/shell/docs/open-in-cloud-shell/) with the repository type you'd like to use with _Open in Cloud Shell_. 

## URL parameters

An Open in Cloud Shell link, optionally embedded in a button image, can be added to the README.md file of any directory in your Git repository. The recommended location for this link is the root README.md file of your Git repository.

### Required URL parameter

To create this link, use a base URL of `shell.cloud.google.com` (or any page in the Google Cloud console that begins with `console.cloud.google.com`) with the following required URL parameter:

URL Parameter | Description | Supported Values  
---|---|---  
`cloudshell_git_repo` | URL of the Git repository to clone. After the repository is cloned, the root of the project folder is opened, displaying its contents in the left navigation pane. | Valid URL for a Git repository. This URL consists of a permitted domain (GitHub or Bitbucket) and a path. The following characters are permitted: uppercase and lowercase letters, digits, underscores (_), hyphens (-), periods (.), and forward-slashes (/). Only allow listed repos owned by Google will open in the default Cloud Shell environment and have access to the user's credentials. All other repos will use a temporary Cloud Shell environment without access to the user's credentials.  
  
### Optional URL parameters

You can also specify any of the following optional parameters:

URL Parameter | Description | Supported Values  
---|---|---  
`cloudshell_git_branch` | Branch from the Git repository to clone. Only applicable when _cloudshell_git_repo_ is specified. The default branch is _master_. | Any valid branch in the repository. The following characters are permitted: uppercase and lowercase letters, digits, tildes (~), underscores (_), hyphens (-), periods (.), forward-slashes (/), and colons (:).   
`cloudshell_image` | Custom Docker image that runs a [customized environment](https://docs.cloud.google.com/shell/docs/configuring-cloud-shell#environment_customization) during the session. This allows you to provide custom tooling in Cloud Shell that users can use to work with your repository.  Opening a repository in Cloud Shell with this parameter specified creates a temporary environment with a scratch home directory that is deleted when the session ends.  | URL of a Docker image hosted in [ Artifact Registry.](https://docs.cloud.google.com/artifact-registry/docs/overview) The Docker image must be based on the base Cloud Shell image and be publicly accessible.  Note that large images take some time to download to the Cloud Shell VM when the URL is opened.   
`cloudshell_open_in_editor` |  File(s) to open in Cloud Shell Editor. Can be repeated to specify multiple files to open. If multiple are specified, they open in the order provided.  Specified file(s) are opened in the right hand editor tabs, one tab per file, in the opened project. File paths are relative to the current directory. If the _working_dir_ param is provided, the path to these files is treated as relative to _working_dir_. | Any valid file path that consists of the following permitted characters: uppercase and lowercase letters, digits, tildes (~), underscores (_), hyphens (-), periods (.), forward slashes (/), and colons (:).  
`cloudshell_print` | File in the Git repository, usually consisting of instructions to be printed to the terminal to guide a user's next steps. The file path is relative to the current directory. If the _working_dir_ param is provided, the path to this file is treated as relative to _working_dir_. | Any valid file path that consists of the following permitted characters: uppercase and lowercase letters, digits, tildes (~), underscores (_), hyphens (-), periods (.), forward slashes (/), and colons (:).  
`cloudshell_tutorial` | [Tutorial Markdown](https://docs.cloud.google.com/shell/docs/tutorials#writing_a_tutorial) file in the Git repository consisting of instructions to be launched as a tutorial to guide users through a project. The file path is relative to the current directory. | Any well-formed Tutorial Markdown file with a valid filename.  
`cloudshell_working_dir` **(Deprecated)** | This parameter is deprecated. Use `cloudshell_workspace` instead. | Any valid file path that consists of the following permitted characters: uppercase and lowercase letters, digits, tildes (~), underscores (_), hyphens (-), periods (.), forward slashes (/), and colons (:).   
`cloudshell_workspace` |  Working directory for Cloud Shell. The terminal opens in the specified directory. Cloud Shell Editor opens the directory as a [workspace](https://docs.cloud.google.com/shell/docs/workspaces).  | Any valid file path relative to the cloned repository. You can leave the parameter value empty or use `.` to specify the root of the cloned repository. If no repository is specified, the path is relative to the Cloud Shell home directory. The following characters are permitted: uppercase and lowercase letters, digits, tildes (~), underscores (_), hyphens (-), periods (.), forward slashes (/), and colons (:).   
`ephemeral` | Opening a repository in Cloud Shell with this parameter specified creates a temporary environment with a scratch home directory that is deleted when the session ends. For more information, see [Choosing ephemeral mode](https://docs.cloud.google.com/shell/docs/using-cloud-shell#choosing_ephemeral_mode).  | `true`, `false`  
`show` | Open with just the terminal, just the Cloud Shell Editor, or both. | `ide`, `terminal`, `ide%2Cterminal`  
  
## Examples

To embed a button to open a sample Git repository in Cloud Shell, include the following Markdown in your repository's README.md file:
    
    
      [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=http://path-to-repo/sample.git)
    

To embed the same functionality into a website, use this equivalent HTML snippet:
    
    
      <a href="https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=http://path-to-repo/sample.git">
      <img alt="Open in Cloud Shell" src ="https://gstatic.com/cloudssh/images/open-btn.svg">
      </a>
    

## Open in Cloud Shell link generator

To define the behavior of the Open in Cloud Shell link more specifically, you can use the form below to experiment with parameters needed to open your repository in Cloud Shell.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
