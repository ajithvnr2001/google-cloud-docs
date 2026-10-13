---
url: https://docs.cloud.google.com/shell/docs/using-cloudshell-command/
title: Use the cloudshell command \u00a0|\u00a0 Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:35.103419+00:00
---

# Use the cloudshell command  |  Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/using-cloudshell-command/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/quickstart)



Send feedback 

#  Use the cloudshell command Stay organized with collections  Save and categorize content based on your preferences. 

The `cloudshell` command allows you to accomplish tasks like launching tutorials, downloading files, setting aliases, and opening existing files in the code editor from the Cloud Shell command line.

Available positional arguments for `cloudshell` are as follows:

Positional Argument | Alternative name | Description  
---|---|---  
help | -h, --help | show `cloudshell` help  
edit-files | edit-file, edit | Open specified file in the Cloud Shell Editor  
download-files | download-file, download, dl | Initiate the download of the specified file  
aliases |  | Generates short aliases for common subcommands  
  
## Example usage

To open your `.bashrc` file for edit in the Cloud Shell Editor, from the Cloud Shell command line, run:
    
    
    cloudshell edit $HOME/.bashrc
    

Similarly, to download your `.bashrc` file, run:
    
    
    cloudshell download $HOME/.bashrc
    

To display information about the `cloudshell` command from your [Cloud Shell session](https://console.cloud.google.com/cloudshell), run `cloudshell help`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
