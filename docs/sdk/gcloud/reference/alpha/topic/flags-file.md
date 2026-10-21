---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/flags-file/
title: gcloud alpha topic flags-file \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:13:07.322693+00:00
---

# gcloud alpha topic flags-file  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/flags-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha topic flags-file Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha topic flags-file - --flags-file=YAML_FILE supplementary help 
DESCRIPTION
     `(ALPHA)` The `--flags-file`=`YAML-FILE` flag, available to all `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` commands, supports complex flag values in any command interpreter. 

Complex flag values that contain command interpreter special characters may be difficult to specify on the command line. The combined list of `special` characters across commonly used command interpreters (shell, cmd.exe, PowerShell) is surprisingly large. Among them are `", ', `, *, ?, [, ], (, ), $, %, #, ^, &, |, {, }, ;, \, <, >,` `space`, `tab`, `newline`. Add to that the separator characters for `list` and `dict` valued flags, and it becomes all but impossible to construct portable command lines. 

The `--flags-file`=`YAML-FILE` flag solves this problem by allowing command line flags to be specified in a YAML/JSON file. String, numeric, list and dict flag values are specified using YAML/JSON notation and quoting rules. 

Flag specification uses dictionary notation. Use a list of dictionaries for flags that must be specified multiple times. 

For example, this YAML file defines values for Boolean, integer, floating point, string, dictionary and list valued flags: 
    
    
        --boolean:
        --integer: 123
        --float: 456.789
        --string: A string value.
        --dictionary:
          a=b: c,d
          e,f: g=h
          i: none
          j=k=l: m=$n,o=%p
          "y:": ":z"
          meta:
          - key: foo
            value: bar
          - key: abc
            value: xyz
        --list:
          - a,b,c
          - x,y,z

If the file is named `my-flags.yaml` then the command line flag `--flags-file=my-flags.yaml` will set the specified flags on any system using any command interpreter. `--flags-file` may be specified in a YAML file, and its value can be a YAML list to reference multiple files. 

This example specifies the `--metadata` flag multiple times: 
    
    
        - --metadata: abc
          --integer: 123
        - --metadata: xyz

Each `--flags-file` arg is replaced by its contents, so normal flag precedence applies. For example, given `flags-1.yaml`: 
    
    
        --zone: us-east2-a

`flags-2.yaml`: 
    
    
        --verbosity: info
        --zone: us-central1-a

and command line: 
    
    
        gcloud compute instances describe \
            --flags-file=flags-1.yaml my-instance --flags-file=flags-2.yaml

the effective command line is: 
    
    
        gcloud compute instances describe \
            --zone=us-east2-a my-instance --verbosity=info --zone=us-central1-a

using zone `us-central1-a` (not `us-east2-a`, because `flags-2.yaml`, to the right of `flags-1.yaml`, has higher precedence). 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud topic flags-file](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file)
    
    
    [gcloud beta topic flags-file](https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/flags-file)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
