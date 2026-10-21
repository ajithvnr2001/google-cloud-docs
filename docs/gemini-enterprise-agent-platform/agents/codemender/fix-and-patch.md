---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/codemender/fix-and-patch/
title: Fix code vulnerabilities and manage diffs \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:45:54.370849+00:00
---

# Fix code vulnerabilities and manage diffs  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/codemender/fix-and-patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Fix code vulnerabilities and manage diffs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

CodeMender can automatically produce, validate, and apply source code patches for verified vulnerabilities, testing them in your local sandbox to prevent regressions.

## Generate vulnerability fixes

Use `cm fix` to generate a validated security patch for a verified finding:
    
    
    cm fix FINDING_ID

When you run `cm fix`, CodeMender performs the following validation steps:

  1. **Generates a patch candidate** using the cloud-hosted reasoning engine.
  2. **Applies the patch** to a copy of the source code inside your local sandbox.
  3. **Compiles and tests** the codebase by running your configured `build.command` to ensure the project builds and unit tests pass.
  4. **Re-runs the verified PoC exploit** to confirm that the vulnerability is no longer exploitable.



By default, CodeMender prompts you to confirm each file modification before writing it to disk in your workspace. Once all checks pass, CodeMender applies the verified patch to your workspace. You can then stage the changes.

### Fix flags

  * **Provide fix context (`-c` / `--context`)**: Provide architectural constraints or coding guidelines: 
        
        cm fix FINDING_ID -c "Use the safe parameterized database helper in src/db/query.go"

  * **Auto-approve writes (`-y` / `--yes`)**: Auto-approve all file writes and prompts during the fix process: 
        
        cm fix FINDING_ID -y

**Note:** You can also disable interactive write prompts globally by setting `confirm_writes: false` in your `config.yaml`.
  * **Control sandboxing (`--sandbox`)**: Explicitly enable or disable the sandbox for this run (for example, `--sandbox=false` to disable): 
        
        cm fix FINDING_ID --sandbox=false

  * **Bypass sandboxing (`--unrestricted`)**: Temporarily bypass all sandbox protections for this run, disabling file system boundaries and OS-level container isolation: 
        
        cm fix FINDING_ID --unrestricted

  * **Bypass cache (`--no-cache`)**: Force CodeMender to generate a fresh patch: 
        
        cm fix FINDING_ID --no-cache




## Inspect and manage local VCS diffs

CodeMender includes built-in VCS commands to help you inspect, stage, and manage code changes that patches introduce before you commit them:

  * **View repository status** : Check which files CodeMender modified or created in your local workspace. 
        
        cm vcs status

  * **Inspect diffs** : Review line-by-line unified diffs of all uncommitted code modifications the agent generated. 
        
        cm vcs diff

  * **Stage changes** : Add verified patch modifications to your local staging environment so you can test and commit them. 
        
        cm vcs stage

  * **Revert session modifications** : Discard all local file modifications CodeMender generated during the current session and restore your repository to its baseline state. 
        
        cm vcs reset




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
