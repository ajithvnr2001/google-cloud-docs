---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NotebookSoftwareConfig/
title: NotebookSoftwareConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:17:32.460731+00:00
---

# NotebookSoftwareConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NotebookSoftwareConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  NotebookSoftwareConfig Stay organized with collections  Save and categorize content based on your preferences. 

Notebook Software Config. This is passed to the backend when user makes software configurations in UI.

Fields  
  
`env[]` `object (`[EnvVar](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/EnvVar)`)` Optional. Environment variables to be passed to the container. Maximum limit is 100. | `postStartupScriptConfig` `object (`[PostStartupScriptConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NotebookSoftwareConfig#PostStartupScriptConfig)`)` Optional. Post startup script config. | `runtime_image` `Union type`  
  
The image to be used by the notebook runtime. Can be one of release name, or custom container image. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`colabImage` `object (`[ColabImage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NotebookSoftwareConfig#ColabImage)`)` Optional. Google-managed NotebookRuntime colab image. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "env": [
        {
          object ([EnvVar](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/EnvVar))
        }
      ],
      "postStartupScriptConfig": {
        object ([PostStartupScriptConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NotebookSoftwareConfig#PostStartupScriptConfig))
      },
    
      // runtime_image
      "colabImage": {
        object ([ColabImage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NotebookSoftwareConfig#ColabImage))
      }
      // Union type
    }  
  
## ColabImage

Colab image of the runtime.

Fields  
  
`releaseName` `string` Optional. The release name of the NotebookRuntime Colab image, e.g. "py310". If not specified, detault to the latest release. | `description` `string` Output only. A human-readable description of the specified colab image release, populated by the system. Example: "Python 3.10", "Latest - current Python 3.11" | JSON representation  
---  
      
    
    {
      "releaseName": string,
      "description": string
    }  
  
## PostStartupScriptConfig

Post startup script config.

Fields  
  
`postStartupScript` `string` Optional. Post startup script to run after runtime is started. | `postStartupScriptUrl` `string` Optional. Post startup script url to download. Example: `gs://bucket/script.sh` | `postStartupScriptBehavior` `enum (`[PostStartupScriptBehavior](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NotebookSoftwareConfig#PostStartupScriptBehavior)`)` Optional. Post startup script behavior that defines download and execution behavior. | JSON representation  
---  
      
    
    {
      "postStartupScript": string,
      "postStartupScriptUrl": string,
      "postStartupScriptBehavior": enum ([PostStartupScriptBehavior](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NotebookSoftwareConfig#PostStartupScriptBehavior))
    }  
  
## PostStartupScriptBehavior

Represents a notebook runtime post startup script behavior.

Enums  
---  
`POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED` | Unspecified post startup script behavior.  
`RUN_ONCE` | Run post startup script after runtime is started.  
`RUN_EVERY_START` | Run post startup script after runtime is stopped.  
`DOWNLOAD_AND_RUN_EVERY_START` | Download and run post startup script every time runtime is started.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
