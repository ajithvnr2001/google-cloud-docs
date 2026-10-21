---
url: https://docs.cloud.google.com/code/docs/intellij/troubleshooting/
title: Troubleshoot common installation issues in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:21:32.655981+00:00
---

# Troubleshoot common installation issues in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Support ](https://docs.cloud.google.com/code/docs/intellij/troubleshooting)



Send feedback 

#  Troubleshoot common installation issues in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

## How do I fix 'executable not found on PATH' errors?

If, during deployment or continuous development, you are getting errors in the form of `executable file not found in $PATH`.

For example: 
    
    
    time="2018-11-01T12:46:38-04:00" level=fatal msg="exiting dev mode because the first build failed: building [gcr.io/**/my-proj]: tagging: pushing: getting auth config for gcr.io/** /my-proj:3c275201-dirty-50f870d: getting auth config: error getting credentials - err: exec: "docker-credential-gcr": executable file not found in $PATH, out: ``"
    

Then, you may be running into the problem where the IDE is not inheriting the shell environment variables. This can happen in some Linux environments when the `PATH` variables are defined in `.bash_profile` or `.bash_rc` and the IDE is launched from the GUI, causing the IDE not to see the `PATH` variables.

This can be solved by allowing Cloud Code to automatically manage updates to Kubernetes dependencies, using the Cloud Code settings within your IDE (**File** > **Settings** > **Tools** > **Cloud Code** > **Kubernetes** or for Mac OS X, **IntelliJ IDEA** > **Preferences** > **Tools** > **Cloud Code** > **Kubernetes**).

If you'd like to maintain custom versions of these dependencies, you can solve this issue in Linux using the following workaround:

  * Launch the IDE from the terminal

First, follow these instructions to enable a command-line launcher. Then launch the IDE from the terminal.

For example, to launch IntelliJ IDEA from the terminal, navigate to the project you wish to open, then execute:
        
        idea .
        

Similarly, to launch PyCharm, execute:
        
        charm .
        

  * Alternatively, set the `PATH` variables in a system-wide location such as /etc/environment.




## Diagnosing and reporting an issue

If your issue isn't covered in this doc, try finding a resolution to the issue by:

  * Searching the [Cloud Code for IntelliJ GitHub issues](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues?q=is%3Aissue+) and/or [StackOverflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-code%5D) for a similar problem

  * Joining the [`#cloud-code`](https://googlecloud-community.slack.com/messages/cloud-code/) channel, which is part of the [Google Cloud Slack community](https://join.slack.com/t/googlecloud-community/shared_invite/zt-3icuwfdvq-eq_58LqmOoCNc16mpZcaNA), and asking about the issue, where one of the community members may be able to identify the problem




If you couldn't resolve the issue after trying to diagnose it, then you can report the issue in the IntelliJ IDE:

  1. Click **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue**. This prompts you to report an issue on GitHub.

  2. Follow the template in the issue reporting box to describe the issue.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
