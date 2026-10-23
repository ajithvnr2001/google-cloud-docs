---
url: https://docs.cloud.google.com/sdk/docs/interactive-gcloud/
title: Using gcloud interactive shell \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:24.963418+00:00
---

# Using gcloud interactive shell  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/interactive-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)



Send feedback 

#  Using gcloud interactive shell Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The `gcloud` interactive shell provides a richer `bash` experience, simplifying command and documentation discovery with as-you-type autocompletion and help text snippets.

The `gcloud` interactive shell produces suggestions and auto-completion for any command that has a manual (man) page, including the `gcloud`, `bq`, `gsutil`, and `kubectl` command-line tools. As you type a command, sub-commands, flags, and file and resource arguments are completed and inline help is displayed in the lower section.

For more information about the interactive shell and its shortcuts, control characters, editor modes, and configurable layout options, see the [`gcloud beta interactive`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/interactive) reference page.

## Installation and use

The `gcloud` interactive shell is included in the `gcloud beta` components.

  1. To check if you have the `gcloud beta` components installed, run the following command:
         
         gcloud components list
         

  2. If you don't see the `gcloud beta` components listed, to install the beta components, run the following command:
         
         gcloud components install beta
         

  3. To enter the `gcloud` interactive mode, run the following command:
         
         gcloud beta interactive
         

Your usual shell prompt is replaced with the `gcloud` interactive shell prompt `$`.

  4. To get auto-suggestions and inline help, start typing a command.

  5. To save time when you're working with a command for a while, type the part of the command you'll reuse and then press `F7`. For example, to work with `gcloud compute`, type `gcloud compute` and then press `F7`. You can then type subcommands such as `list` without needing to first type `gcloud compute`. When you're no longer using the command, press `Ctrl-C` and `F7` to clear the context.

  6. To exit the interactive shell press `Ctrl-D` or `F9`.




## Auto-completion and help

`gcloud interactive` has auto prompting for commands and flags, and displays inline help snippets in the lower section as you type a command.

Static information, like command and sub-command names, and flag names and enumerated flag values, are auto-completed using dropdown menus.

![gcloud interactive shell example session](https://docs.cloud.google.com/static/sdk/docs/images/gcloudinteractiveshell.gif)

## Shortcuts

To accomplish common tasks, you can use the following shortcuts:

Action | Shortcut  
---|---  
Complete a file path or resource argument | `Tab`  
Refine the dropdown completion menu | Continue typing the command  
Scroll through the menu | `Tab`, `Shift+Tab`, or arrow keys  
Select a highlighted item or directory | `Space` or `/`  
Toggle the active help section, ON when enabled, OFF when disabled | `F2`  
Set the context for command input to avoid retyping command prefixes | `F7`  
Clear the context for command input | `Ctrl-C` and `F7`  
Open a web browser tab or window to display the complete man page for the current command | `F8`  
Exit | `F9` or `Ctrl+D`  
  
## Bash compatibility

`bash` completion configs, aliases, exports, functions, `set -o` settings, and variables initialized in your `.bashrc` are all available at the interactive command prompt. The interactive command line edit mode is derived from the `set -o emacs` or `set -o vi` setting.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
