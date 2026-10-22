---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auto-completion/
title: gdcloud CLI autocomplete \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:32.588694+00:00
---

# gdcloud CLI autocomplete  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auto-completion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  gdcloud CLI autocomplete Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for configuring and using the gdcloud CLI autocomplete feature that enables you to use the `Tab` key to complete a partially entered command. This feature is available for Bash, Zsh, and Fish shells. The gdcloud CLI autocompletion is a feature that provides suggestions for commands and options as you type. This can be helpful when you are not sure what command to use or when you want to use a command that you have not used before.

## Activate autocompletion

To activate the auto–completion feature you will need to run a command for your terminal. The gdcloud CLI autocompletion feature is available for the Bash, Zsh, and Fish shells. Use the following command to figure out which shell you use.
    
    
    echo $SHELL
    

The output looks like `bin/$SHELL` where `$SHELL` is either bash, zsh, or fish.

### Bash

To load completions in your current shell session:
    
    
    source <(gdcloud completion bash)
    

To load completions for every new session, execute once:
    
    
    gdcloud completion bash > /etc/bash_completion.d/gdcloud
    

### Zsh

If shell completion is not already enabled in your environment, you must enable it. Check whether shell completion is enabled. 

Check the value of the `COMP_LINE` variable. If the value of the `COMP_LINE` variable is empty, then shell completion is not enabled. You can check this value by running the following command:
    
    
    echo $COMP_LINE
    

Try to use shell completion with a command. If you try to use shell completion with a command and it does not work, the shell completion is not enabled. For example, try typing the following command and pressing `Tab`. If shell completion is enabled, you must see a list of possible completions for the `ls` command.
    
    
    ls
    

Check the output of the compgen -c command. If the output of the `compgen -c` command contains no commands, then shell completion is not enabled. You can run the following command to see the output of the `compgen -c` command. If shell completion is enabled, the output of the command should include a list of commands that have completion functions.
    
    
    compgen -c
    

If you are not sure if shell completion is enabled in your environment, check documentation for your shell. If shell completion is not enabled in your environment, execute the following command to enable it:
    
    
    echo "autoload -U compinit; compinit" >> ~/.zshrc
    

To load completions in your current shell session:
    
    
    source <(gdcloud completion zsh); compdef _gdcloud gdcloud
    

To load completions for each session, execute once:

#### Linux
    
    
    gdcloud completion zsh > "${fpath[1]}/_gdcloud"
    

You must start a new shell for this setup to take effect.

### Fish

To load completions in your current shell session:
    
    
    gdcloud completion fish | source
    

To load completions for each session, run:
    
    
    gdcloud completion fish > ~/.config/fish/completions/gdcloud.fish
    

You must start a new shell for this setup to take effect.

## Use autocompletion

To use gdcloud CLI autocompletion, type the first few characters of the command that you want to use and then press the `Tab` key. If there is only one possible completion, it is automatically inserted into the command line. If the command does not autofill, then that means there are multiple possible completions and you must press the `Tab` key again to view all the possible commands.

### Autocomplete examples

Type a command partially and then press `Tab` to autocomplete the command:
    
    
    gdcloud con <Tab>
    

Complete command after pressing `Tab` once:
    
    
    gdcloud config
    

Type a command partially and then press `Tab` twice to see a list of all possible commands:
    
    
    gdcloud clusters <TAB> <TAB>
    describe get-credentials list
    gdcloud clusters
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
