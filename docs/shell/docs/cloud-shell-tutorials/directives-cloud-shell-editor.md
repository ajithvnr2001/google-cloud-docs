---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/directives-cloud-shell-editor/
title: Cloud Shell Editor directives \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:22.036239+00:00
---

# Cloud Shell Editor directives  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/directives-cloud-shell-editor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ Reference ](https://docs.cloud.google.com/shell/docs/apis)



Send feedback 

#  Cloud Shell Editor directives Stay organized with collections  Save and categorize content based on your preferences. 

This page lists directives related to Cloud Shell Editor.

## Open file
    
    
    <walkthrough-editor-open-file filePath="FILE_PATH">LINK_TEXT</walkthrough-editor-open-file>
    

Creates a link that opens a file on the Cloud Shell disk in the editor.

### Parameters

Parameter | Type | Description  
---|---|---  
`filePath` | String  | A file path relative to the workspace open in Cloud Shell.  
  
## Open file with text selected
    
    
    <walkthrough-editor-select-line filePath="FILE_PATH" startLine="START_LINE" endLine="END_LINE">LINK_TEXT</walkthrough-editor-select-line>
    

Creates a link that opens a file on the Cloud Shell disk in the editor, and selects lines of text within it.

### Parameters

Parameter | Type | Description  
---|---|---  
`filePath` | String  | A file path relative to the workspace open in Cloud Shell.  
`startLine` | Integer  | The file line where the selection starts. Unlike the code editor, the line count starts from `0`.  
`endLine` | Integer  | The file line where the selection ends. The selection ends at the beginning of this line. Unlike the code editor, the line count starts from `0`.  
`startCharacterOffset` | Integer  | The character number in the `startLine` to start the selection from.  
`endCharacterOffset` | Integer  | The number of characters after the `endLine` position to select.  
  
## Open file with text selected by regular expression
    
    
    <walkthrough-editor-select-regex filePath="FILE_PATH" regex="REGEX">LINK_TEXT</walkthrough-editor-select-regex>
    

Creates a link that opens a file on the Cloud Shell disk in the Cloud Shell Editor and selects text in the file based on a regular expression. Only the first match in the file is selected.

### Parameters

Parameter | Type | Description  
---|---|---  
`filePath` | String  | A file path relative to the workspace open in Cloud Shell.  
`regex` | String | A regular expression to match. Multi-line is on.  
  
## Spotlight pointers
    
    
    <walkthrough-editor-spotlight spotlightId="SPOTLIGHT_ID">LINK_TEXT</walkthrough-editor-spotlight>
    
    
    
    <walkthrough-editor-spotlight cssSelector="CSS_SELECTOR">LINK_TEXT</walkthrough-editor-spotlight>
    

Creates a link that highlights the specified UI element in the editor.

You can spotlight an element on the page in one of two ways:

Spotlight ID
    Using the `spotlightId` parameter, specify a DOM element's `spotlight-id` property value to select the element.
CSS selector
    For elements without a spotlight ID, use the `cssSelector` parameter with a CSS selector to select the element.

Only one of these parameters is required. If both are provided, `spotlightId` is used.

### Parameters

Parameter | Type | Description  
---|---|---  
`spotlightId` | String | An element's spotlight ID.  
`spotlightItem` | String  | Required when `spotlightId` is set to `navigator`. The expected value is a file path relative to the workspace open in Cloud Shell.  
  
The `spotlightId` parameter only accepts the following values:

Spotlight ID | Highlighted element  
---|---  
Activity bar  
`activity-bar-cloud-apis` | The Cloud API activity bar icon.  
`activity-bar-cloud-k8s` | The Cloud Kubernetes activity bar icon.  
`activity-bar-cloud-run` | The Cloud Run activity bar icon.  
`activity-bar-debug` | The Debug activity bar icon.  
`activity-bar-scm` | The Source Control activity bar icon.  
`activity-bar-search` | The Search activity bar icon.  
Cloud Code  
`cloud-code-gke-explorer` | Cloud Code Kubernetes Explorer > **Google Kubernetes Engine** section.  
`cloud-code-k8s-explorer` | Cloud Code Kubernetes Explorer > **Kubernetes** section.  
`cloud-code-k8s-explorer-minikube ` | Cloud Code Kubernetes Explorer > **minikube cluster** (if it exists).  
`cloud-code-logs-viewer-cluster` | Logs viewer > **Cluster** filter.  
`cloud-code-logs-viewer-container` | Logs viewer > **Container** filter.  
`cloud-code-logs-viewer-deployment` | Logs viewer > **Deployment** filter.  
`cloud-code-logs-viewer-namespace` | Logs viewer > **Namespace** filter.  
`cloud-code-logs-viewer-pod` | Logs viewer > **Pod** filter.  
`cloud-code-logs-viewer-refresh` | Logs viewer > **Refresh** button.  
`cloud-code-logs-viewer-stream-toggle` | Logs viewer > **Streaming** toggle.  
`cloud-code-new-app` | Cloud Code quick access > **New Application**.  
`cloud-code-debug-on-k8s` | Cloud Code quick access > **Debug on Kubernetes**.  
`cloud-code-run-on-k8s` | Cloud Code quick access > **Run on Kubernetes**.  
`cloud-code-open-welcome-page` | Cloud Code quick access > **Open Welcome Page**.  
`cloud-code-cloud-run-deploy` | Cloud Code quick access > **Deploy to Cloud Run**.  
`cloud-code-run-on-cloud-run-emulator` | Cloud Code quick access > **Run on Cloud Run Emulator**.  
Menus  
`menu-edit` | The **Edit** menu.  
`menu-file` | The **File** menu.  
`menu-terminal` | The **Terminal** menu.  
`menu-terminal-new-terminal` | **Terminal** menu > **New Terminal.**  
Status bar  
`cloud-code-status-bar` | The Cloud Code status bar menu button.  
`minikube-status-bar` | The minikube status bar menu button.  
Other elements  
`debug-configuration` | Debug view > configuration dropdown menu.  
`file-explorer` | The file explorer.  
`navigator` | A file in the Cloud Code file explorer. Must be paired with the `spotlightItem` parameter.  
`output` | The **Output** log.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
