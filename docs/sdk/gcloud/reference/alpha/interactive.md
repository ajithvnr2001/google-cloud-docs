---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/interactive/
title: gcloud alpha interactive \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:57.183526+00:00
---

# gcloud alpha interactive  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/interactive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha interactive Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha interactive - start the gcloud interactive shell 
SYNOPSIS
    

`gcloud alpha interactive` [`--context`=`CONTEXT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha interactive` provides an enhanced `bash`(1) command line with features that include: 

  * auto-completion and active help for all commands 
  * state preservation across commands: `cd`, local/environment variables 


Display
     The `gcloud alpha interactive` display window is divided into sections, described here from top to bottom. 

`Previous Output`
     Command output scrolls above the command input section as commands are executed. 
`Command Input`
     Commands are typed, completed, and edited in this section. The default prompt is "$ ". If a context has been set, then its tokens are prepopulated before the cursor. 
`Active Help`
     As you type, this section displays in-line help summaries for commands, flags, and arguments. You can toggle active help on and off via the `F2` key. Hit `F8` to display the help text in your browser. 
`Status Display`
     Current `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` project and account information, and function key descriptions and settings are displayed in this section. Function keys toggle mode/state settings or run specific actions. 

`F2:help:``STATE`
     Toggles the active help section, `ON` when enabled, `OFF` when disabled. 
`F7:context`
     Sets the context for command input, so you won't have to re-type common command prefixes at every prompt. The context is the command line from just after the prompt up to the cursor. 

For example, if you are about to work with `[gcloud compute](https://docs.cloud.google.com/sdk/gcloud/reference/compute)` for a while, type `[gcloud compute](https://docs.cloud.google.com/sdk/gcloud/reference/compute)` and hit `F7`. This will display `[gcloud compute](https://docs.cloud.google.com/sdk/gcloud/reference/compute)` at subsequent prompts until the context is changed. 

Hit ctrl-c and `F7` to clear the context, or edit a command line and/or move the cursor and hit `F7` to set a different context. 

`F8:web-help`
     Opens a web browser tab/window to display the complete man page help for the current command. If there is no active web browser (running in `ssh`(1) for example), then command specific help or `man`(1) help is attempted. 
`F9:quit`
     Exit. 
Auto and Tab Completion
     Command completions are displayed in a scrolling pop-up menu. Use `tab` and up/down keys to navigate the completions, and `space` or `/` to select the highlighted completion. 

Completions for `known` commands, flags, and static flag values are displayed automatically. Positional and dynamic flag value completions for known commands are displayed after `tab` is entered. Known commands include `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)`, `bq`, `gsutil`, `kubectl`, and any command with a man page that has been executed at least once in any `interactive` session. 

`tab` completion for unknown commands defers to `bash`(1), while still using the `interactive` user interface. Absent specific command information, a file/path completer is used when `tab` is entered for unknown positionals (arguments that do not start with '-'). The default completer handles '~' path notation and embedded `$var` references, but does not expand their values in completions. 

Configure bash completions as you normally would. `gcloud alpha interactive` starts up bash in a mode that sources `~/.bashrc` with the environment variable `COSHELL_VERSION` set to a non-empty version value. 

Command completion resets with each simple command in the command line. Simple commands are separated by '|', ';', '&' and may appear after '$(', '(', '{', '!', `if`, `then`, `elif`, `while`, and `name`=`value` per command exports. Use `tab` on an empty line to enable command executable search on PATH for the first token in each simple command. 

Currently simple and compound commands must be entered in a single line. 

Refer to [Using gcloud interactive](https://cloud.google.com/sdk/docs/interactive-gcloud) for more information and animated GIFs. 

Control Characters
     Control characters affect the currently running command or the current command line being entered at the prompt. 

`ctrl-c`
     If a command is currently running, then that command is interrupted. This terminates the command. Otherwise, if no command is running, ctrl-c clears the current command line. 
`ctrl-d`
     Exits when entered as the first character at the command prompt. You can also run the `exit` command at the prompt. 
`ctrl-w`
     If a command is not currently running, then the last word on the command line is deleted. This is handy for "walking back" partial completions. 
Command history
     `gcloud alpha interactive` maintains persistent command history across sessions. 
emacs mode
    

^N">`^N`
     Move ahead one line in the history. 

^P">`^P`
     Move back one line in the history. 
^R">`^R`
     Search backwards in the history. 
vi mode
    

/
     Search backwards in the history. 

`j`
     Move ahead one line in the history. 
`k`
     Move back one line in the history. 
`n`
     Search backwards for the next match. 
`N`
     Search forwards for the next match. 
history search mode
    

`ENTER/RETURN`
     Retrieve the matched command line from the history. 

^R-1">`^R`
     Search backwards for the next match. 
^S">`^S`
     Search forwards for the next match. 
Layout Configuration
     Parts of the layout are configurable via `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set)` interactive/`property`. These properties are only checked at startup. You must exit and restart to see the effects of new settings. 

`bottom_bindings_line`
     If True, display the bottom key bindings line. The default value is `true`. 
`bottom_status_line`
     If True, display the bottom status line. The default value is `false`. 
`completion_menu_lines`
     Number of lines in the completion menu. The default value is `4`. 
`context`
     Command context string. The default value is "". 
`debug`
     If True, enable the debugging display. The default value is `false`. 
`fixed_prompt_position`
     If True, display the prompt at the same position. The default value is `false`. 
`help_lines`
     Maximum number of help snippet lines. The default value is `10`. 
`hidden`
     If True, expose hidden commands/flags. The default value is `false`. 
`justify_bottom_lines`
     If True, left- and right-justify bottom toolbar lines. The default value is `false`. 
`manpage_generator`
     If True, use the manpage CLI tree generator for unsupported commands. The default value is `true`. 
`multi_column_completion_menu`
     If True, display the completions as a multi-column menu. The default value is `false`. 
`obfuscate`
     If True, obfuscate status PII. The default value is `false`. 
`prompt`
     Command prompt string. The default value is "$ ". 
`show_help`
     If True, show help as command args are being entered. The default value is `true`. 
`suggest`
     If True, add command line suggestions based on history. The default value is `false`. 
CLI Trees
     `gcloud alpha interactive` uses CLI tree data files for typeahead, command line completion, and help snippet generation. A few CLI trees are installed with their respective Google Cloud CLI components: `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` (core component), `bq`, `gsutil`, and `kubectl`. Trees for commands that have man(1) pages are generated on the fly. See `$ [gcloud topic cli-trees](https://docs.cloud.google.com/sdk/gcloud/reference/topic/cli-trees)` for details. 
EXAMPLES
     To set the command context of `gcloud alpha interactive` to "gcloud ", run: 
    
    
    gcloud alpha interactive --context="gcloud "

FLAGS
    

`--context`=`CONTEXT`
     Default command context. This is a string containing a command name, flags, and arguments. The context is prepopulated in each command line. You can inline edit any part of the context, or ctrl-c to eliminate it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     On Windows, install `git`(1) for a `bash`(1) experience. `gcloud alpha interactive` will then use the `git` (MinGW) `bash` instead of `cmd.exe`. 

Please run `$ [gcloud feedback](https://docs.cloud.google.com/sdk/gcloud/reference/feedback)` to report bugs or request new features. 

This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta interactive](https://docs.cloud.google.com/sdk/gcloud/reference/beta/interactive)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
