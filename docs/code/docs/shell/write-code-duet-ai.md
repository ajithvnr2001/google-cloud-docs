---
url: https://docs.cloud.google.com/code/docs/shell/write-code-duet-ai/
title: Code with Gemini Code Assist \u00a0|\u00a0 Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:47.446048+00:00
---

# Code with Gemini Code Assist  |  Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/write-code-duet-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Code with Gemini Code Assist Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview), an AI-powered collaborator in Google Cloud, to help you do the following in Cloud Shell: 

  * Provide guidance to help you solve problems with your code.

  * Generate code for your project.

  * Receive inline suggestions while you're coding.




Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

To help you comply with any license requirements for your code, Gemini Code Assist provides source citations when its suggestions directly quote at length from a specific source. To learn more about how and when Gemini cites sources, see [How Gemini helps you generate code and cites sources](https://docs.cloud.google.com/gemini/docs/discover/works#how-when-gemini-cites-sources). 

[Code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview) lets you get code suggestions based on your organization's private codebase directly from Gemini Code Assist. Learn [how to configure code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

This document is intended for developers of all skill levels. It assumes you have working knowledge of the Cloud Shell Editor and are familiar with Google Cloud. If you prefer, you can also explore Gemini Code Assist in [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/write-code-gemini), [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/write-code-gemini), and [VS Code](https://docs.cloud.google.com/code/docs/vscode/write-code-gemini). 

## Connect to Google Cloud and select a project

In this section, you'll connect to Google Cloud and select a Google Cloud project with the Gemini for Google Cloud API enabled in the Cloud Shell Editor. 

If you select a Google Cloud project without the Gemini for Google Cloud API enabled, you receive a notification that gives you the option to enable the API from the IDE. Select **Enable the API** in the notification window to enable the API for your project. For more information, see [Set up Gemini Code Assist for a project](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini).

**Note:** There are multiple places where you can set a Google Cloud project in Cloud Shell Editor, such as in the terminal or in the footer menu. To connect to Google Cloud and select a project in Cloud Shell Editor with Gemini Code Assist, you must use the dropdown menu next to the search bar, as described in the following steps. The project you select in this menu is used to check for a Gemini Code Assist subscription and determines your quota; it may also impact settings that apply to your Gemini usage, such as whether logging is enabled. 

To connect to Google Cloud in the Cloud Shell Editor, follow these steps:

  1. Launch the [Cloud Shell Editor](https://shell.cloud.google.com/?duet=true).

  2. If prompted to authorize Cloud Shell Editor to make Google Cloud API calls, click **Authorize**.

  3. Follow the prompts to sign into your Google Account.

  4. Next to the search bar, click the keyboard_arrow_down **Gemini Code Assist** dropdown menu.

![Gemini Code Assist dropdown menu.](https://docs.cloud.google.com/static/code/docs/shell/images/shell-gca-dropdown-menu.png)

  5. From the menu, select **Select Gemini Code Assist Project**. This opens the **Select Google Cloud project** menu.

  6. From the **Select Google Cloud project** menu, select a Google Cloud project that has the Gemini for Google Cloud API enabled.

You're now connected to Google Cloud. Gemini is ready to use.




## Chat with Gemini Code Assist

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

In this section, learn how to open the **Gemini Code Assist** pane and chat with Gemini Code Assist to get your code explained.

To begin chatting with Gemini, follow these steps:

  1. Open a source file.

  2. Next to the search bar in Cloud Shell Editor, click chat_spark **Open Gemini Code Assist Chat**.

  3. In the **Gemini Code Assist** Chat pane, enter the prompt `Explain this code to me` and click send **Send**.

Gemini uses your file as context for your prompt and responds with an explanation of your code.

To focus on a specific block of code, select that block in your open file before entering your prompt.




### Reset chat history

Gemini Code Assist uses the chat history for additional context when responding to your prompts.

If your chat history is no longer relevant to what you're trying to achieve, you can reset the chat history: in the **Gemini Code Assist** pane, click delete **Reset Chat**.

**Note:** The chat history automatically resets when you switch the workspace or exit the Cloud Shell Editor. 

## Generate code with prompts

The following sections show you how to use Gemini Code Assist to generate code with the example prompt `Function to create a Cloud Storage bucket` inside a file. You can also select a part of your code and then prompt Gemini Code Assist for help through the chat feature, and receive and accept or reject code suggestions while you code.

### Prompt Gemini Code Assist in a file

  1. In a source file, on a new line, enter the comment `Function to create a Cloud Storage bucket`, and then press `Enter` (for Windows and Linux) or `Return` (for macOS).

  2. To generate code, press `Control+Enter` (for Windows and Linux) or `Control+Return` (for macOS).

Next to your prompt text in your file, Gemini Code Assist generates the code in the form of ghost text.

  3. Optional: To accept the generated code, press `Tab`.




#### Optional: Change keyboard shortcut for generating code

If the default keyboard shortcut for generating code isn't working as outlined in the previous section, you can change the keyboard shortcut by following these steps:

  1. In the Cloud Shell Editor, click menu **Menu** , and then navigate to **File** > **Preferences** > **Keyboard Shortcuts**.

  2. In the list of keyboard shortcuts, search for **Cloud Code: Generate Code**.

  3. Click **Cloud Code: Generate Code** , and then click edit **Change Keybinding**.

  4. In the dialog that appears, enter your own shortcut.

  5. Press `Enter` (for Windows and Linux) or `Return` (for macOS).

You can now use your newly assigned keyboard shortcut to generate code with Gemini.




### Prompt Gemini Code Assist with selected code using chat

Gemini Code Assist can perform tasks or answer your questions based on the code that you select. To get generated code that's based on a prompt with selected code, follow these steps:

  1. Next to the search bar in Cloud Shell Editor, click chat_spark **Open Gemini Code Assist Chat**.

  2. In a source file, select a block of code.

  3. In the **Gemini Code Assist** Chat text field, enter a prompt for the selected code.

For example, select a function in your code and enter the prompt `Write a unit test for this function`.

Gemini uses your selected code as reference and responds to your prompt.




### Get inline suggestions while you code

While you write code, Gemini Code Assist makes inline code suggestions that you can either accept or ignore. To try this feature, follow these steps:

  1. In a source file, on a new line, start writing a function. For example, if you're in a Python file, write `def`. Gemini suggests code in the form of ghost text.

  2. To accept the code suggestion from Gemini Code Assist, press `Tab`. Otherwise, to ignore the suggestion, press `Esc` or continue writing your code.




#### Optional: Disable inline suggestions

If you prefer to disable inline suggestions in Gemini Code Assist, follow these steps:

  1. In the Cloud Shell Editor, select menu **Menu** , and then navigate to **File** > **Preferences** > **Settings**.

  2. On the **User** tab of the **Settings** dialog, navigate to **Extensions** > **Cloud Code**.

  3. Scroll until you find the **Cloudcode: Gemini Code Assist: Inline Suggestions: Enable Auto** list, and then select **Off**.

This turns off the inline suggestions. You can still press `Control+Enter` (for Windows and Linux) or `Control+Return` (for macOS) to manually trigger inline suggestions.




### Optional: Exclude files from context with an .aiexclude file

You can exclude files from being considered by Gemini Code Assist for context by creating an `.aiexclude` file. An `.aiexclude` file follows the similar syntax as a `.gitignore` file, with the following differences:

  * An empty or nonexistent `.aiexclude` file blocks no files in its directory and all sub-directories.
  * An `.aiexclude` file doesn't support negation, where you prefix patterns with an exclamation point (`!`).
  * An `.aiexclude` file matches greedily on the `*` character. This will match indiscriminately on directories and files. This `.aiexclude` file doesn't differentiate between `**` or `*` with regards to folders or files.



Only a single `.aiexclude` file is supported currently. To configure your `.aiexclude` file, create a file titled `.aiexclude` in the root of your workspace folder. If you want to place this file outside of the workspace root, or rename the file, the path may be set in the VS Code settings under "Context Exclusion File". The path value provided in this setting will resolve relative to the root folder of your open workspace.

#### Examples

The following examples demonstrate how you can configure an `.aiexclude` file:

  * Block all files named `apikeys.txt` at or below the workspace directory:
        
        apikeys.txt
        

  * Block all files with the `.key` file extension at or below the workspace directory:
        
        *.key
        

  * Block only the apikeys.txtfile at the same directory as the `.aiexclude` file, but not any subdirectories:
        
        /apikeys.txt
        

  * Block all files in the directory `my/sensitive/dir` and all subdirectories. The path should be relative to the workspace root directory.
        
        my/sensitive/dir/*
        




## Disable code suggestions that match cited sources

Gemini provides citation information when it directly quotes at length from another source, such as publicly available source code. For more information, see [How and when Gemini cites sources](https://docs.cloud.google.com/gemini/docs/discover/works#how-when-gemini-cites-sources).

To prevent code that matches cited sources from being suggested, you can modify the `geminicodeassist.recitation.maxCitedLength` setting to `0` in a `settings.json` file:
    
    
    "geminicodeassist.recitation.maxCitedLength": 0
    

## Use smart actions

To help you be more productive while minimizing context switching, Gemini Code Assist provides AI-powered _smart actions_ directly in your source code editor. When you select code in your editor, you can view and select from a list of actions relevant to your context.

To use smart actions, follow these steps:

  1. In a source file, select a block of code.

  2. Next to the selected code block, click lightbulb **Show Code Actions**.

![Smart actions lightbulb icon appears after selecting a block of code in Shell and Workstations.](https://docs.cloud.google.com/static/code/docs/shell/images/duet-ai-shell-code-actions.png)

  3. Select an action such as **Generate unit tests**.

Gemini generates a response that's based on the action you selected.




## Use code transformation

Gemini Code Assist provides _code Transformation_ , which allows you to select a portion of code in a file and request modifications to your existing code through prompts in natural language, using an inline text box.

With code Transformation, you can do the following:

  * Generate comment lines to document your code
  * Troubleshoot code with issues
  * Improve code readability
  * Make code more efficient



You can also view context sources of a generated response in the **Gemini: Chat** pane.

### Prompt Gemini Code Assist with the inline text box

The inline text box allows you to interact with Gemini Code Assist directly in your code.

To open the inline text box and prompt Gemini, follow these steps:

  1. In a source file, press `Control+I` (for Windows and Linux) or `Command+I` (for macOS).

  2. Enter a prompt, like `Write a function to create a Cloud Storage bucket`, and press `Enter` (for Windows and Linux) or `Return` (for macOS).

Gemini Code Assist generates the code based on your prompt.




### View diff of refactored code

With the diff view built into the inline text box, you can see the changes that Gemini suggests and your original code. You can then accept or discard the suggested changes.

To view the diff of refactored code from the inline text box, perform the following steps:

  1. In a source file, select a function and open the inline text box by pressing `Control+I` (for Windows and Linux) or `Command+I` (for macOS).

  2. Enter a prompt, like `Add comments` and press `Enter` (for Windows and Linux) or `Return` (for macOS).

When Gemini generates the code changes to your selected function, the diff view appears.

![Context sources listed in the Gemini: Chat pane.](https://docs.cloud.google.com/static/code/docs/shell/images/gemini-diff-view.png)

  3. To accept or discard the changes, click **Accept** or **Discard**.




### View context sources of a generated response

The context display feature lists your project files (the _context sources_) that were used as reference to generate responses to your prompts. Knowing which files were used as references helps you to refine your prompts and get more specific responses. Context sources are shown every time you use Gemini chat.

To view the context sources of the generated response, in the **Gemini: Chat** pane, scroll until you see the **Context Sources** snippet. Expand the snippet to see all of the context sources.

![Context sources listed in the Gemini: Chat pane.](https://docs.cloud.google.com/static/code/docs/shell/images/gemini-context-sources.png)

### Use smart commands

_Smart commands_ are commands that you can use in the inline text box to perform specific actions to your code.

To get an explanation of an entire source file with the `/explain` smart command, follow these steps:

  1. In a file, open the inline text box by pressing `Control+I` (for Windows and Linux) or `Command+I` (for macOS).

  2. Press `/` to view the list of smart commands and their descriptions.

  3. Select `/explain`.

Gemini generates an explanation of the entire file in the inline text box.

  4. Optional: If you want to view the generated response in the **Gemini: Chat** pane, click **View in Chat**.




### View prompt history

Accessing your prompt history saves you time when you want to reuse prompts in a large source file.

To access your prompt history, in your file, open the inline text box by pressing `Control+I` (for Windows and Linux) or `Command+I` (for macOS) and then press `Control+Up arrow` (for Windows and Linux) or `Command+Up arrow` (for macOS). This allows you to cycle through your older prompts and re-use them when needed.

### Enhance code readability for non-native English speakers

If you're a non-native English speaker who relies on translation applications, you can use the inline text box to generate comments in other languages.

To convert English comments to another language or add new comments in another language, follow these steps:

  1. In a source file, select the code that you want to add comments to.

  2. Open the inline text box by pressing `Control+I` (for Windows and Linux) or `Command+I` (for macOS).

  3. Enter a prompt, like `Add spanish comments` and press `Enter` (for Windows and Linux) or `Return` (for macOS).

Gemini generates comments in the language that you specified in your prompt and views the diff of these suggestions.

  4. To accept or discard these changes to your code, click **Accept** or **Discard**.




## Test other example prompts

After reading through the Generate code with prompts section of this document, try some of the following example prompts.

### Get an explanation of code

  1. In a source file, select a function that you want explained.
  2. In the **Gemini Code Assist** pane, enter the prompt `Explain this code to me`.

Gemini uses your selected code as a reference and responds with an explanation of the selected function.




### Generate test plans

  1. In a source file, select the code that you want to add unit tests for.
  2. In the **Gemini Code Assist** pane, enter the prompt `Write unit tests for my code`.



### Get help with debugging code

  1. In a source file, select the code that you want to debug.
  2. In the **Gemini Code Assist** pane, enter the prompt `Help me debug my code`.



### Make your code more readable

  1. In a source file, select the code that you want to make more readable.
  2. In the **Gemini Code Assist** pane, enter the prompt `Make my code more readable`.

If you prefer to focus on a specific part of your code, then select the preferred part of code before prompting Gemini.




## Known issues

The following sections outline the known issues of Gemini Code Assist.

### License recitation warnings don't persist across sessions

If license recitation warnings don't persist across sessions, refer to the persistent logs:

  1. Click menu **Menu** > **View** > **Output**.

  2. Select **Gemini Code Assist - Citations**.




### Connectivity issues in the Gemini Code Assist output window

If you see a connection error or other connectivity problems in the Gemini Code Assist output window, try the following:

  * Configure your firewall to allow access to `oauth2.googleapis.com` and `cloudaicompanion.googleapis.com`.

  * Configure your firewall to allow communication over HTTP/2, which gRPC uses.




You can use the `grpc-health-probe` tool to test connectivity. A successful check results in the following output:

`$ grpc-health-probe -addr cloudaicompanion.googleapis.com:443 -tls error: this server does not implement the grpc health protocol (grpc.health.v1.Health): GRPC target method can't be resolved`

An unsuccessful check results in the following output:

`timeout: failed to connect service "cloudaicompanion.googleapis.com:443" within 1s`

To obtain more details, run the following before `grpc-health-probe`:
    
    
    export GRPC_GO_LOG_SEVERITY_LEVEL=info
    

### 'Activate Gemini Code Assist' still appears after selecting Gemini Code Assist project

If you selected your project per the instructions in this guide, which includes enabling the Gemini for Google Cloud API, then there may be an issue with the LS server.

To find out more details about your issue, perform the following actions:

  1. Next to the search bar in Cloud Shell Editor, click chat_spark **Open Gemini Code Assist Chat**.

  2. In the **Gemini Code Assist** Chat pane, click **Leave Feedback**.

  3. Click **Show** for any of the log files to see more details and to help troubleshoot the issue.




## Leave feedback

To leave feedback of your experience, follow these steps:

  1. Next to the search bar in Cloud Shell Editor, click chat_spark **Open Gemini Code Assist Chat**.

  2. In the **Gemini Code Assist** Chat pane, click **Leave Feedback**.

![Gemini Code Assist feedback in Cloud Shell Editor.](https://docs.cloud.google.com/static/code/docs/shell/images/shell-gca-feedback.png)

  3. In the **Feedback for Gemini Code Assist** form, select the **Feedback category** and **Type** , and describe your issue in the **Comments** field.

  4. To share your Gemini Code Assist logs, select the **Send Gemini Code Assist logs** options.

  5. Click **Submit Feedback**.




## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
