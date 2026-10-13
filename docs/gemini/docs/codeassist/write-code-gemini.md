---
url: https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini/
title: Code with Gemini Code Assist Standard and Enterprise \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:32.771450+00:00
---

# Code with Gemini Code Assist Standard and Enterprise  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Code with Gemini Code Assist Standard and Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** We have unified our tools into a single, multi-agent platform called Antigravity, with Antigravity CLI now available. Starting June 18, 2026, Gemini Code Assist IDE Extensions and Gemini CLI stopped serving requests for the Gemini Code Assist for individuals, Google AI Pro, and Google AI Ultra tiers. Affected users should migrate to Antigravity and Antigravity CLI. To learn more, see the [deprecation page](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals).

This document describes how you can use [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview), an AI-powered collaborator in your IDE, to help you do the following in VS Code or IntelliJ and other [supported JetBrains IDEs](https://docs.cloud.google.com/gemini/docs/codeassist/supported-languages#supported_ides):

  * Generate code for your project with code transformation.
  * Receive code completions while you're coding.
  * Use smart actions.



If you're using [Gemini Code Assist Enterprise](https://docs.cloud.google.com/gemini/docs/codeassist/overview#editions-overview), you can use [Code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview), which lets you get code suggestions based on your organization's private codebase directly from Gemini Code Assist Enterprise. Learn [how to configure code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

This document is intended for developers of all skill levels. It assumes you have working knowledge of VS Code or IntelliJ and other supported JetBrains IDEs, and are familiar with Google Cloud. If you prefer, you can also explore Gemini Code Assist in [Cloud Shell Editor](https://docs.cloud.google.com/code/docs/shell/write-code-gemini), [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/write-code-gemini), and [Android Studio](https://developer.android.com/studio/gemini/overview).

**Note:** The behaviour of code generation, completion, and transformation are non-deterministic when used simultaneously with other plugins that either implement the same shortcuts and/or use the same platform API to process these actions.

## Before you begin

###  VS Code 

  1. [Set up Gemini Code Assist Standard or Enterprise](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini), if you haven't already.

  2. Before testing Gemini Code Assist capabilities in your code file, make sure your file's coding language is supported. For more information on supported coding languages, see [Supported coding languages](https://docs.cloud.google.com/gemini/docs/codeassist/supported-languages#coding-languages).

  3. If you prefer to use your IDE behind a proxy, see [Network Connections in Visual Studio Code](https://code.visualstudio.com/docs/setup/network).




###  IntelliJ 

  1. [Set up Gemini Code Assist Standard or Enterprise](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini), if you haven't already.

  2. Before testing Gemini Code Assist capabilities in your code file, make sure your file's coding language is supported. For more information on supported coding languages, see [Supported coding languages](https://docs.cloud.google.com/gemini/docs/codeassist/supported-languages#coding-languages).

  3. If you prefer to use your IDE behind a proxy, see [HTTP Proxy](https://www.jetbrains.com/help/idea/settings-http-proxy.html).




## Generate code with prompts

The following sections show you how to use Gemini Code Assist to generate code with the example prompt `Function to create a Cloud Storage bucket` inside your code file. You can also select a part of your code and then prompt Gemini Code Assist for help through the chat feature, and receive and accept or reject code suggestions while you code.

### Prompt Gemini Code Assist with code transformation

Code transformation allows you to use commands or natural language prompts in the Quick Pick menu to request modifications to your code, and provides you with a diff view to show pending changes to your code. To prompt Gemini Code Assist with code transformation, follow these steps:

###  VS Code 

  1. In your code file, on a new line, press `Control+I` (for Windows and Linux) or `Command+I` (for macOS) to open the **Gemini Code Assist Quick Pick** menu.

  2. In the menu, using the `/generate` command, enter `/generate function to create a Cloud Storage bucket` and then press `Enter` (for Windows and Linux) or `Return` (for macOS).

![Gemini Code Assist generates code with the /generate command.](https://docs.cloud.google.com/static/code/docs/vscode/images/gemini-code-assist-generate-command.png)

Gemini Code Assist generates the code based on your prompt in a diff view.

![Gemini Code Assist opens a diff view to show generated code.](https://docs.cloud.google.com/static/code/docs/vscode/images/gemini-code-assist-diff-view.png)

  3. Optional: To accept these changes, click **Accept**.




###  IntelliJ 

  1. In your code file, on a new line, press `Alt+\` (for Windows and Linux) or `Cmd+\` (for macOS) to open the **Gemini Code Assist Quick Pick** menu.

  2. In the menu, using the `/generate` command, enter `/generate function to create a Cloud Storage bucket` and then press `Enter` (for Windows and Linux) or `Return` (for macOS).

![Code transformation generate function in IntelliJ Gemini Code Assist](https://docs.cloud.google.com/static/gemini/images/cloud-transformation-generate-function-gca-intellij.png)

Gemini Code Assist generates the code based on your prompt in a diff view.

![Code transformation diff view in IntelliJ Gemini Code Assist](https://docs.cloud.google.com/static/gemini/images/cloud-transformation-diff-view-gca-intellij.png)

  3. Optional: To accept these changes, click **Accept Changes**.

You can use the following code transformation commands in your IDE:

     * `/fix`: Fix issues or errors in your code. Example: `/fix potential NullPointerExceptions in my code`.
     * `/generate`: Generate code. Example: `/generate a function to get the current time`.
     * `/doc`: Add documentation to your code. Example: `/doc this function`.
     * `/simplify`: Simplify your code. Example: `/simplify if statement in this code`.



### Prompt Gemini Code Assist in a code file with a comment

If you prefer, you can also prompt Gemini Code Assist in your code file with a comment by following these steps:

###  VS Code 

  1. On a new line, enter the comment `Function to create a Cloud Storage bucket`, and then press `Enter` (for Windows and Linux) or `Return` (for macOS).

  2. To generate code, press `Control+Enter` (for Windows and Linux) or `Control+Return` (for macOS).

Next to your prompt text in your code file, Gemini Code Assist generates the code in the form of ghost text.

  3. Optional: To accept the generated code, press `Tab`.




###  IntelliJ 

  1. In your code file, on a new line, enter the comment `Function to create a Cloud Storage bucket`.

  2. To generate code, press `Alt+G` (for Windows and Linux) or `Option+G` (for macOS). Alternatively, you can right-click next to the comment and select **Generate Code**.

Gemini Code Assist generates the code below your comment in the form of ghost text.

  3. Optional: To accept the generated code, press `Tab`.




### Optional: Change keyboard shortcut for generating code

If the default keyboard shortcut for generating code isn't working as outlined in the previous section, you can [change the keyboard shortcut](https://docs.cloud.google.com/gemini/docs/codeassist/keyboard-shortcuts#edit_keyboard_shortcuts).

## Get code completions

While you write code, Gemini Code Assist makes inline code suggestions, also known as _code completions_ , that you can either accept or ignore. To get code completions, follow these steps:

###  VS Code 

  1. In your code file, on a new line, start writing a function. For example, if you're in a Python file, write `def`.

Gemini Code Assist suggests code in the form of ghost text.

  2. To accept the code suggestion from Gemini Code Assist, press `Tab`. Otherwise, to ignore the suggestion, press `Esc` or continue writing your code.




###  IntelliJ 

  1. In your code file, on a new line, start writing a function. For example, if you're in a Python file, write `def`.

Gemini Code Assist suggests code in the form of an inline suggestion.

  2. To accept the code suggestion from Gemini Code Assist, press `Tab`. Otherwise, to ignore the suggestion, press `Esc` or continue writing your code.

  3. Optional: If you prefer to use a different shortcut key to accept the inline suggestion, hold your pointer over the inline suggestion and click the **Tab** dropdown that appears. Then, select your preferred shortcut or click **Custom** to enter your own shortcut.

![Gemini provides a dropdown menu to change your shortcut to accept an inline suggestion.](https://docs.cloud.google.com/static/code/docs/intellij/images/gemini-code-assist-change-inline-completion-shortcut.png)




### Optional: Disable code completion

Code completion is enabled by default. If you want to disable code completion, follow these steps:

###  VS Code 

  1. In your IDE, click **Code** (for macOS) or **File** (for Windows and Linux), and then navigate to **Preferences** > **Settings**.

  2. On the **User** tab of the **Settings** dialog, navigate to **Extensions** > **Gemini Code Assist**.

  3. Scroll until you find the **Geminicodeassist > Inline Suggestions: Enable Auto** list, and then select **Off**.

This turns off the inline suggestions. You can still press `Control+Enter` (for Windows and Linux) or `Control+Return` (for macOS) to manually trigger inline suggestions.




###  IntelliJ 

In the status bar of your IDE, click spark **Gemini Code Assist: Active** and select **Enable AI Code Completion**.

![Gemini Code Completion button in IntelliJ status bar.](https://docs.cloud.google.com/static/code/docs/intellij/images/gemini-code-assist-code-completion.png)

This disables the code completion setting, and Gemini Code Assist no longer makes inline suggestions until you enable the setting again.

## Use Next Edit Predictions

**Preview**

This product or feature is in preview. Products and features that are in preview are available "as is".

While code completion only suggests changes at your cursor in a code file, Next Edit Predictions provide predicted code suggestions throughout the file, even in locations away from the cursor.

You can enable Next Edit Predictions in the settings of your IDE.

To use Next Edit Predictions in your IDE, follow these steps:

###  VS Code 

To begin using Next Edit Predictions, enable the setting:

  1. Navigate to settings **Manage** > **Settings**.

  2. In the **User** tab of the settings window, navigate to **Extensions** > **Gemini Code Assist**.

  3. Scroll until you find **Geminicodeassist > Inline Suggestions: Next Edit Predictions**.

  4. Select the checkbox to enable Next Edit Predictions in VS Code.




Now that you've enabled the setting, you can start using Next Edit Predictions in a code file by performing these steps:

  1. In your code file, start writing code. Next Edit Predictions appear when you pause or stop typing.

![User triggers the Next Edit Predictions in VS Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/vscode-next-edits-triggererd.png)

  2. Press `Tab` to accept the provided Next Edit suggestion.

![User enters the Next Edit Prediction in VS Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/vscode-next-edits-entered.png)

  3. If you want to accept the next suggestion, press `Tab` again. A further suggestion may appear and the process can again be repeated. Otherwise, press `Esc` to dismiss, or continue typing to ignore the suggestion.

When you press `Tab` to enter the suggestion, you can hold your pointer over the suggestion to see the other suggestions, if applicable. If there are multiple suggestions, you can click the left and right arrows to cycle through the other suggestions.

![Available Next Edit Predictions in VS Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/vscode-next-edits-available.png)

Whenever you press `Esc` to dismiss the suggestion, Gemini Code Assist stops suggesting Next Edit Predictions for that specific code block. You continue to receive suggestions when you move to another section of your code.

**Note:** Gemini Code Assist only provides Next Edit Predictions in the file that you're currently in. Gemini Code Assist doesn't provide Next Edit Predictions in other files.



###  IntelliJ 

To begin using Next Edit Predictions, enable the setting:

  1. Navigate to **File** > **Settings** > **Tools** > **Gemini**.

  2. In the **Completion** section, select the **Next Edit Predictions** checkbox to enable the feature.




Now that you've enabled the setting, you can start using Next Edit Predictions in a code file by performing these steps:

  1. In your code file, start writing code. Next Edit Predictions appear when you pause or stop typing.

![User triggers the Next Edit Predictions in IntelliJ Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/intellij-next-edits-triggererd.png)

  2. Press `Tab` to accept the provided Next Edit suggestion.

![User enters the Next Edit Prediction in IntelliJ Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/intellij-next-edits-entered.png)

  3. If you want to accept the next suggestion, press `Tab` again. A further suggestion may appear and the process can again be repeated. Otherwise, press `Esc` to dismiss, or continue typing to ignore the suggestion.

Whenever you press `Esc` to dismiss the suggestion, Gemini Code Assist stops suggesting Next Edit Predictions for that specific code block. You continue to receive suggestions when you move to another section of your code.

**Note:** Gemini Code Assist only provides Next Edit Predictions in the file that you're currently in. Gemini Code Assist doesn't provide Next Edit Predictions that would impact code in other files.



## Finish changes in a file

Gemini Code Assist can generate code suggestion to complete your file's pseudocode, #TODOs, and half-written code.

###  VS Code 

  1. In your code file, start writing code until the `Alt+F` or `Opt+F` hint appears.

  2. To generate suggested code, press the keyboard shortcut provided by the hint, or right-click in the file and select **Gemini Code Assist** > **Finish changes**.

You can dismiss the hint or cancel the code generation process by pressing `Esc`.

  3. Once Gemini Code Assist finishes generating suggested code, you can click **Accept** , which applies the suggested code to your file, or you can click **Decline** , which leaves your original code unchanged.




###  IntelliJ 

  1. Check that there are portions of your focused file that have code in need of completion, such as pseudocode or #TODOs.

  2. In the file window, right-click > **Gemini** > **Finish changes**. Alternatively, you can [use the finish changes keyboard shortcut](https://docs.cloud.google.com/gemini/docs/codeassist/keyboard-shortcuts#code-shortcuts).

Gemini Code Assist generates code suggestions to finish the incomplete portions of your code.

  3. For each code suggestion, click check_small **Accept** or undo **Reject**.

Alternatively, the option to **Accept all** or **Reject all** is available at the top of the file.




## Get more relevant suggestions with remote repository context

You can get more contextually aware and relevant code suggestions by directing Gemini Code Assist to focus on specific remote repositories. This is useful when your task centers on a specific set of microservices, libraries, or modules.

### Before you begin

Before you use a remote repository as context, you must first [index and configure it for code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

### Use a remote repository as context

To direct Gemini Code Assist to use one or more repositories as the primary context for your prompts:

  1. In your IDE's chat, start your prompt with the `@` symbol. A list of your available indexed remote repositories appears.
  2. Select the repository (or repositories) you want to use for context from the list. You can also start typing the repository name to filter the list.
  3. After selecting the repositories, write the rest of your prompt.



Gemini Code Assist then prioritizes the selected repositories when generating a response.

### Example prompts

This section includes examples of how you can get more relevant suggestions with remote repository context.

  * Understand a repository 
    * `@REPOSITORY_NAME What is the overall structure of this repository?`
    * `@REPOSITORY_NAME I'm a new team member. Can you give me an overview of this repository's purpose and key modules?`
  * Generate and modify code 
    * `@REPOSITORY_NAME Implement an authentication function similar to the one in this repository.`
    * `@REPOSITORY_NAME Refactor the following code to follow the conventions in the selected repository.`
    * `Use the library-x in @REPOSITORY_A_NAME-A and implement the function-x`
  * Test 
    * `@UNIT_TEST_FILE_NAME Generate unit tests for module-x based on the examples in the selected file.`



By using remote repositories as a focused source of context, you can get more accurate and relevant suggestions from Gemini Code Assist, which can help you code faster and more efficiently.

## Use smart actions

To help you be more productive while minimizing context switching, Gemini Code Assist provides AI-powered smart actions directly in your code editor. When you select your code in your code editor, you can view and select from a list of actions relevant to your context.

To use smart actions in your code, follow these steps:

###  VS Code 

  1. In your code file, select a block of code.

  2. Next to the selected code block, click lightbulb **Show Code Actions**.

![Smart actions lightbulb icon appears after selecting a block of code in VS Code.](https://docs.cloud.google.com/static/code/docs/vscode/images/duet-ai-vsc-code-actions.png)

  3. Select an action such as **Generate unit tests**.

Gemini Code Assist generates a response that's based on the action you selected.




###  IntelliJ 

  1. In your code file, select a line or block of code.

  2. Right-click the selected code and select a smart action, like **Generate unit tests**.

Selecting the smart action will automatically prompt Gemini Code Assist to generate a response to the prompt in the **Gemini Code Assist** tool window.




## Use code transformation quick fix

If there's an error in your code, Gemini Code Assist gives you the option to apply a _quick fix_ to the error with code transformation.

To apply a quick fix in your code file, follow these steps:

###  VS Code 

  1. In your code file, hold your pointer over the squiggly error line and select **Quick Fix** , and then select **/fix**.

![Code transformation quick fix in the IDE.](https://docs.cloud.google.com/static/code/docs/vscode/images/code-transformation-quick-fix.png)

  2. When the quick fix is applied, a diff view appears. To accept these changes, click **Accept**.




###  IntelliJ 

  1. In your code file, click the red error bulb icon, which indicates an error in your code, and select **Fix with Gemini**.

![Code transformation option to fix with Gemini in the IDE.](https://docs.cloud.google.com/static/gemini/images/code-transformation-quick-fix-gca-intellij.png)

  2. When the fix is applied, a diff view appears. To accept these changes, click **Accept**.




## Exclude files from local context

If files are specified in a `.aiexclude` or `.gitignore` file, Gemini Code Assist by default excludes them from local use in the context for code completion, code generation, code transformation, and chat.

To learn how to exclude files from local use, see [Exclude files from Gemini Code Assist use](https://docs.cloud.google.com/gemini/docs/codeassist/create-aiexclude-file).

## Disable code suggestions that match cited sources

Gemini Code Assist provides citation information when it directly quotes at length from another source, such as existing open source code. For more information, see [How and when Gemini cites sources](https://docs.cloud.google.com/gemini/docs/discover/works).

To prevent code that matches cited sources from being suggested to you, do the following:

### VS Code

  1. In the activity bar of your IDE, click **Manage** > **Settings**.

  2. In the **User** tab of the settings window, navigate to **Extensions** > **Gemini Code Assist**.

  3. Scroll until you find **Geminicodeassist > Recitation: Max Cited Length**.

  4. Set the value to `0`.




Gemini Code Assist no longer suggests code to you that matches cited sources.

### IntelliJ

  1. In the status bar of your IDE, click spark **Gemini Code Assist: Active** and select then select **Configure Gemini**.

  2. Expand the **Advanced settings** section, and then select **Block selections that match external cited sources**.

  3. Click **OK**.




Gemini Code Assist no longer suggests code to you that matches cited sources.

## Known issues

For a list of known issues with Gemini Code Assist in your IDE, see [known issues](https://docs.cloud.google.com/gemini/docs/codeassist/code-overview#known-issues).

## Leave feedback

To leave feedback of your experience, see [Provide Gemini Code Assist feedback](https://docs.cloud.google.com/gemini/docs/support/feedback).

## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn [how Gemini Code Assist uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).
  * Learn about [Gemini Code Assist pricing](https://cloud.google.com/products/gemini/pricing).
  * Learn more about [Google Cloud compliance](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
