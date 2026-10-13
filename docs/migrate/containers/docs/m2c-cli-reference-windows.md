---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli-reference-windows/
title: Migrate to Containers CLI reference for Windows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:37.569259+00:00
---

# Migrate to Containers CLI reference for Windows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli-reference-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Reference ](https://docs.cloud.google.com/migrate/containers/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate to Containers CLI reference for Windows

`m2c` is a command-line tool that lets you set up and execute migrations on your local machine.

## m2c

A command-line interface to Migrate to Containers.

Perform quick modernization for your workload by following a three step journey:

  1. Analyze the source VM's disk images to create a modernization plan.

  2. Edit the plan to customize modernization artifacts.

  3. Generate the modernization artifacts.




### Synopsis
    
    
    m2c COMMAND [options]
    

### Flags

`-q,--quiet`
    Don't output anything
`-v,--verbose`
    Show verbose output

### Commands

Command | Description  
---|---  
m2c analyze | Analyze the workload's configuration in the given file system.  
m2c completion | Generate the autocompletion script for the specified shell  
m2c config | View and edit configuration properties  
m2c generate | Generate migration artifacts from the given file system.  
m2c help | Help about any command  
m2c version | Print the CLI version.  
  
## m2c analyze

Analyze the workload's configuration in the given file system with a given plugin.

The resulting modernization plan will be available in the config.yaml file under the given output directory.

### Synopsis
    
    
    m2c analyze --source COPIED_FILESYSTEM_PATH --plugin PLUGIN_NAME --output OUTPUT_DIR [options]
    

### Flags

`-o,--output path`
    Output path that can be used as input to the `m2c generate` command
`-r,--parameter name=value`
    Plugin analysis parameters in the format "name=value". Can be specified multiple times
`-p,--plugin name`
    Plugin name
`-s,--source path`
    The path to a VHD image files
`--volume localPath:remotePath`
    Bind mounts a file or directory into the container in the format of "localPath:remotePath". Can be specified multiple times

## m2c completion

Generate the autocompletion script for m2c for the specified shell.

See each sub-command's help for details on how to use the generated script.

### Synopsis
    
    
    m2c completion
    

### Commands

Command | Description  
---|---  
m2c completion bash | Generate the autocompletion script for bash  
m2c completion fish | Generate the autocompletion script for fish  
m2c completion powershell | Generate the autocompletion script for powershell  
m2c completion zsh | Generate the autocompletion script for zsh  
  
## m2c completion bash

Generate the autocompletion script for the bash shell.

This script depends on the 'bash-completion' package.

If it is not installed already, you can install it via your OS's package manager.

To load completions in your current shell session:
    
    
        source <(m2c completion bash)
    

To load completions for every new session, execute once:

#### Linux:
    
    
        m2c completion bash > /etc/bash_completion.d/m2c
    

#### macOS:
    
    
        m2c completion bash > $(brew --prefix)/etc/bash_completion.d/m2c
    

You will need to start a new shell for this setup to take effect.

### Synopsis
    
    
    m2c completion bash
    

### Flags

`--no-descriptions`
    disable completion descriptions

## m2c completion fish

Generate the autocompletion script for the fish shell.

To load completions in your current shell session:
    
    
        m2c completion fish | source
    

To load completions for every new session, execute once:
    
    
        m2c completion fish > ~/.config/fish/completions/m2c.fish
    

You will need to start a new shell for this setup to take effect.

### Synopsis
    
    
    m2c completion fish
    

### Flags

`--no-descriptions`
    disable completion descriptions

## m2c completion powershell

Generate the autocompletion script for powershell.

To load completions in your current shell session:
    
    
        m2c completion powershell | Out-String | Invoke-Expression
    

To load completions for every new session, add the output of the above command

to your powershell profile.

### Synopsis
    
    
    m2c completion powershell
    

### Flags

`--no-descriptions`
    disable completion descriptions

## m2c completion zsh

Generate the autocompletion script for the zsh shell.

If shell completion is not already enabled in your environment you will need

to enable it. You can execute the following once:
    
    
        echo "autoload -U compinit; compi>>nit"  ~/.zshrc
    

To load completions in your current shell session:
    
    
        source <(m2c completion zsh)
    

To load completions for every new session, execute once:

#### Linux:
    
    
        m2c completion zsh > "${fpath[1]}/_m2c"
    

#### macOS:
    
    
        m2c completion zsh > $(brew --prefix)/share/zsh/site-functions/_m2c
    

You will need to start a new shell for this setup to take effect.

### Synopsis
    
    
    m2c completion zsh
    

### Flags

`--no-descriptions`
    disable completion descriptions

## m2c config

View and edit the configuration properties.

### Synopsis
    
    
    m2c config COMMAND
    

### Commands

Command | Description  
---|---  
m2c config get | Print the value of a configuration property.  
m2c config list | Print all the configuration properties and their values.  
m2c config set | Set the value of a configuration property.  
m2c config unset | Reset a configuration property to its default value.  
  
## m2c config get

Print the value of a configuration property.

### Synopsis
    
    
    m2c config get KEY
    

## m2c config list

Print all the configuration properties and their values.

### Synopsis
    
    
    m2c config list
    

## m2c config set

Set the value of a configuration property.

### Synopsis
    
    
    m2c config set KEY VALUE
    

## m2c config unset

Reset a configuration property to its default value.

### Synopsis
    
    
    m2c config unset KEY
    

## m2c generate

Generate migration artifacts from the given file system.

This utilizes the migration plan configuration generated by a previous analyze operation.

### Synopsis
    
    
    m2c generate -i ANALYSIS_DIRECTORY -o OUTPUT_PATH [options]
    

### Flags

`-i,--input path`
    The path to a directory generated by "m2c analyze"
`-o,--output path`
    The output path
`--volume localPath:remotePath`
    Bind mounts a file or directory into the container in the format of "localPath:remotePath". Can be specified multiple times

## m2c help

Help provides help for any command in the application.

Simply type m2c help [path to command] for full details.

### Synopsis
    
    
    m2c help [command]
    

## m2c version

Print the CLI version.

### Synopsis
    
    
    m2c version
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
