---
url: https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini/
title: Chat with Gemini Code Assist Standard and Enterprise \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:28.226005+00:00
---

# Chat with Gemini Code Assist Standard and Enterprise  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Chat with Gemini Code Assist Standard and Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview), an AI-powered collaborator in your IDE, to help you do the following in VS Code or IntelliJ and other [supported JetBrains IDEs](https://docs.cloud.google.com/gemini/docs/codeassist/supported-languages#supported_ides):

  * Receive guidance to help you solve problems with your code.
  * Generate code for your project.
  * Manage the context of your project by specifying files and folders.
  * Create custom commands and rules.



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




## Use the Gemini Code Assist chat to explain your code

In this section, you prompt Gemini Code Assist to provide an explanation of your existing code.

###  VS Code 

To get an explanation of your code, follow these steps:

  1. Open your code file.

  2. In the activity bar of your IDE, click spark **Gemini Code Assist**.

  3. In the **Gemini Code Assist** pane, enter the prompt `Explain this code to me` and click send **Send**.

Gemini Code Assist uses the code in your code file as a reference to your prompt and responds with an explanation of your code.

To refer to a specific block of code instead of all the code in the file, you can select the block in your code file and then prompt Gemini Code Assist.




###  IntelliJ 

To get an explanation of your code, follow these steps:

  1. In your IDE, open your code file.

  2. In the Gemini Code Assist tool window, enter the prompt `Explain this code to me` and click **Submit**.




Gemini Code Assist uses the code in your code file as a reference to your prompt and responds with an explanation of your code.

If you only want an explanation of a certain part of your code, you can select certain code and then prompt Gemini Code Assist again. Gemini Code Assist will only use the selected code as a reference to its generated response.

When Gemini Code Assist provides you with code in its response, you can select the following options listed at the end of its response:

  * **Insert at Cursor** : Inserts the generated code into your current file at your current cursor position.

  * **Insert in New File** : Opens a new file and inserts the generated code into the new file.

![Gemini lists code actions at the end of a generated code response.](https://docs.cloud.google.com/static/code/docs/intellij/images/gemini-code-assist-code-actions.png)




These options are available when Gemini Code Assist identifies the language used in your code block, and if this language is supported in your current IDE.

**View query history**

If you want to re-use your previous prompts, you can find them in your **Query History** in the **Gemini Code Assist** tool window by clicking schedule **Show Query History**.

![Gemini Query History in the tool window.](https://docs.cloud.google.com/static/code/docs/intellij/images/gemini-code-assist-query-history.png)

### Create multiple chats

You can create multiple chats with Gemini Code Assist which contain their own context separate from other chats. Your chat history shows your first chat and the last updated timestamp. There's a limit of 20 chats. Once you reach this limit, the oldest chat is automatically deleted when you add a new chat.

###  VS Code 

  1. To add a new chat, click add **New Chat** and enter your prompt in the text field. After you enter the prompt, Gemini Code Assist creates the new chat.
  2. To access your previous chat, click history **Resume Previous Chat**. A list of your chats appear. Select the chat that you want to view.
  3. To delete a chat thread, click **Resume Previous Chat** and then click delete **Delete** next to the chat that you want to delete.



###  IntelliJ 

  1. To add a new chat, click add **New Chat** and enter your prompt in the text field. After you enter the prompt, Gemini Code Assist creates the new chat.
  2. To access your previous chat, click chat_bubble **Recent Chats**. A list of your chats appear. Select the chat that you want to view.
  3. To delete a chat thread, click **Recent chats** and then click delete **Delete** next to the chat that you want to delete.



### Clear chat history

Gemini Code Assist uses the chat history for additional context when responding to your prompts. If your chat history is no longer relevant, you can [clear the chat history](https://docs.cloud.google.com/gemini/docs/codeassist/use-gemini-code-assist-chat#clear-chat-history).

## Manage your chat

You can manage your Gemini Code Assist chat settings by doing the following:

### Configure automatic scrolling

###  VS Code 

By default, Gemini Code Assist automatically scrolls through your chat. To disable this behavior, perform the following tasks:

  1. Navigate to **Settings** > **Extensions** > **Gemini Code Assist**.

  2. Search for the **Automatic Scrolling** setting and unselect the checkbox.




###  IntelliJ 

This feature isn't supported in Gemini Code Assist for IntelliJ and other JetBrains IDEs.

### Stop in-progress chat

###  VS Code 

You can stop an in-progress chat response by pressing stop **Stop** :

![Button to stop in-progress VS Code Gemini Code Assist chat response](https://docs.cloud.google.com/static/gemini/images/vscode-stop-chat.png)

###  IntelliJ 

You can stop an in-progress chat response by pressing stop **Stop** :

![Button to stop in-progress IntelliJ Gemini Code Assist chat response](https://docs.cloud.google.com/static/gemini/images/intellij-stop-chat.png)

### Select the model

If you use [Gemini Code Assist Standard or Enterprise](https://docs.cloud.google.com/gemini/docs/codeassist/overview), you can select the model that Gemini Code Assist uses when processing your prompts.

###  VS Code 

  1. In the Gemini Code Assist chat pane, click the model selector dropdown.

  2. Select the model that you want Gemini Code Assist to use.




###  IntelliJ 

  1. In the Gemini Code Assist chat pane, click the model selector dropdown.

  2. Select the model that you want Gemini Code Assist to use.




### Edit a prior prompt

When you edit a prior prompt, Gemini Code Assist regenerates the response to the edited prompt. To edit your prompt, follow these steps:

###  VS Code 

  1. In the chat pane, hold your pointer over the prompt that you want to edit.

  2. Click edit **Edit**.

![Modify prompt in VS Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/vscode-edit-prompt.png)

  3. Make changes to your prompt and click **Update**.

Gemini Code Assist generates a new response to your edited prompt.




###  IntelliJ 

  1. In the chat pane, hold your pointer over the prompt that you want to edit.

  2. Click edit **Edit**.

![Modify prompt in IntelliJ Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/intellij-edit-prompt.png)

  3. Make changes to your prompt and click **Update**.

Gemini Code Assist generates a new response to your edited prompt.




### Regenerate a prompt response

If preferred, you can regenerate a different response to your most recent prompt by following these steps:

###  VS Code 

In the Gemini Code Assist Chat pane, at the bottom of your most recent response, click replay **Regenerate response**.

Gemini Code Assist re-evaluates your recent prompt and provides a new response.

###  IntelliJ 

In the Gemini Code Assist Chat pane, at the bottom of your most recent response, click replay **Regenerate response**.

Gemini Code Assist re-evaluates your recent prompt and provides a new response.

### Delete prompt and response pairs

To delete your prompt and Gemini Code Assist's response to that particular prompt, follow these steps:

###  VS Code 

  1. In the chat pane, hold your pointer over your prompt that you wish to remove.

  2. Click **Delete**.

![Delete prompt and response pair in VS Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/vscode-delete-prompt-response-pair.png)

  3. When prompted to confirm if you want to delete the prompt and response pair, select **Delete**. Otherwise, click **Cancel** to cancel the operation.

Your prompt and response pair is removed from your chat history with Gemini Code Assist.




###  IntelliJ 

  1. In the chat pane, hold your pointer over your prompt that you wish to remove.

  2. Click **Delete**.

![Delete prompt and response pair in IntelliJ Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/intellij-delete-prompt-response-pair.png)

  3. When prompted to confirm if you want to delete the prompt and response pair, select **Delete**. Otherwise, click **Cancel** to cancel the operation.

Your prompt and response pair is removed from your chat history with Gemini Code Assist.




### Configure code preview pane

By default, the code preview pane setting for Gemini Code Assist chat is enabled. With this setting enabled, the preview code block in the Gemini Code Assist chat shows the first 6 lines of code. You can expand and collapse code blocks.

To change the default setting, perform the following tasks:

###  VS Code 

  1. In your IDE, navigate to **Settings** > **Extensions** > **Gemini Code Assist**.

  2. Search for the **Default Code Block Display** setting.

  3. Select one of the following options:

     * **Expanded** : Automatically expands all code blocks in Gemini Code Assist chat responses.

     * **Preview** : Only shows the first 6 lines of code in the code block. You must expand the code block in the Gemini Code Assist chat response to see the rest of the code. This is the default setting.

     * **Collapse** : Automatically collapses all code blocks in Gemini Code Assist chat responses.

When the IDE reloads, the new setting takes effect.




###  IntelliJ 

This feature is the default in IntelliJ Gemini Code Assist and other JetBrains IDEs and is not configurable.

## Prompt Gemini Code Assist with selected code using chat

Gemini Code Assist can perform tasks or answer your questions based on the code that you select. To get generated code that's based on a prompt with selected code, follow these steps:

###  VS Code 

  1. In the activity bar, click spark **Gemini Code Assist** to open the **Gemini Code Assist** pane.

  2. In your code file, select a block of code.

  3. In the **Gemini Code Assist** pane text field, enter a prompt for the selected code.

For example, select a function in your code and enter the prompt `Write a unit test for this function`.

Gemini uses your selected code as reference and responds to your prompt.




###  IntelliJ 

  1. In the activity bar, click spark **Gemini Code Assist** to open the **Gemini Code Assist** tool window.

  2. In your code file, select a block of code.

  3. In the **Gemini Code Assist** tool window text field, enter a prompt for the selected code.

For example, select a function in your code and enter the prompt `Write a unit test for this function.`

Gemini Code Assist uses your selected code as reference and responds to your prompt.




### Add selected code snippets to context

You can select, attach, and direct Gemini Code Assist to focus on code snippets. Code snippet selection enables discrete analysis of smaller code blocks instead of entire files.

When you select a code snippet in your code file, you can instruct Gemini Code Assist add the code snippet to the Context Drawer.

Anything selected in the editor window, but not yet added to the Context Drawer, is also automatically included in the context. Selected code snippets only show up for a single chat turn. They won't persist in the Context Drawer, but remain in your Gemini Code Assist chat history.

In this section, you add a selected code snippet to your context and get an explanation about the code snippet from Gemini Code Assist:

###  VS Code 

  1. In your code file, select a code snippet.

  2. In the Gemini Code Assist Chat text field, click **Add to Chat Context**.

Gemini Code Assist adds the selected code snippet to your Context Drawer.

  3. In the Gemini Code Assist Chat text field, enter the prompt `what does this code do?`.

Gemini Code Assist responds to your prompt based on your selected code snippet in the Context Drawer.




###  IntelliJ 

  1. In your code file, select a code snippet.

  2. Select the spark Gemini icon and then select **Add Selected Text to Chat Context** from the menu.

The code snippet is added to your Context Drawer.




## Prompt Gemini Code Assist with selected terminal output using chat

Gemini Code Assist can perform tasks or answer your questions based on selected terminal output. To get an explanation of selected terminal output, follow these steps:

###  VS Code 

  1. In your IDE, open your terminal (**View** > **Terminal**).

  2. Select any terminal output.

  3. Right-click the selected terminal output and select **Gemini Code Assist: Add to Chat Context**.

Gemini Code Assist adds your terminal output to the Context Drawer.

  4. In the Gemini Code Assist Chat text field, enter the prompt `what does this do?`.

Gemini Code Assist responds to your prompt based on your selected terminal output in the Context Drawer.




###  IntelliJ 

  1. In the Gemini Code Assist Chat text field, enter `@terminal`.

  2. In the list that appears, under **Terminals** , select the terminal that you want to enquire about.

![Select a terminal in IntelliJ.](https://docs.cloud.google.com/static/gemini/images/intellij-select-terminal.png)

  3. In the Gemini Code Assist Chat text field, enter the prompt `what does this do?`.

Gemini Code Assist responds to your prompt based on your selected terminal output.




## Specify files and folders in your workspace context

By default, Gemini Code Assist uses the current open file as context. You can specify files or folders in your workspace for Gemini Code Assist to use as additional context. When you specify a folder, Gemini Code Assist uses the files in the folder as well as the files in subfolders as context.

**Note:** When you include a folder, Gemini Code Assist selects up to the first 100 files it finds within the folder and its subfolders. If you require codebase awareness beyond this limit, you may want to consider use of [code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview).

###  VS Code 

To specify files or folders in your chat prompt, type `@` and select the file or folder you want to specify.

![Specify files and folders with local codebase awareness for VS Code.](https://docs.cloud.google.com/static/gemini/images/vscode-local-codebase-awareness-specify-files-folders.png)

To get an explanation on the differences of two files in your codebase, follow these steps:

  1. In the activity bar, click spark **Gemini Code Assist**.

  2. In the **Gemini Code Assist** pane, enter the prompt `Explain the difference between @YOUR_FILE_NAME_1 and @YOUR_FILE_NAME_2` and press `Enter` (for Windows and Linux) or `Return` (for macOS), or `Tab`. You can also click the name of the file in the list to select the file. Clicking the file name adds the file to your prompt context and opens the file in your IDE.




Gemini Code Assist responds to your prompt while using the two files you specified for context. Gemini Code Assist also includes the files you specified in **Context Sources**.

Now that you've specified those files, you can continue asking additional questions or prompts in the same chat history, without having to specify the files again.

For example: In the **Gemini Code Assist** pane, enter the prompt `How can I improve YOUR_FILE_NAME_1?` (without the `@` symbol) and press `Enter` (for Windows and Linux) or `Return` (for macOS).

Gemini Code Assist responds to your enquiry about the file you specified in your prompt.

**Note:** If you clear your chat history, Gemini Code Assist no longer uses your files for context and you must re-specify the files in the chat pane using the `@` symbol if you want to make more enquiries about the files.

###  IntelliJ 

To specify files or folders in your chat prompt, type `@` and select the files or folders you want to specify.

![Specify files with local codebase awareness for IntelliJ.](https://docs.cloud.google.com/static/gemini/images/intellij-local-codebase-awareness-specify-files-folders.png)

To get an explanation on the differences of two files in your codebase, follow these steps:

  1. In the activity bar, click spark **Gemini Code Assist**.

  2. In the **Gemini Code Assist** pane, enter the prompt `Explain the difference between @YOUR_FILE_NAME_1 and @YOUR_FILE_NAME_2` and press `Enter` (for Windows and Linux) or `Return` (for macOS), or `Tab`. You can also click the name of the file in the list to select the file. Clicking the file name adds the file to your prompt context and opens the file in your IDE.




Gemini Code Assist responds to your prompt while using the two files you specified for context. Gemini Code Assist also includes the files you specified in **Context Sources**.

Now that you've specified those files, you can continue asking additional questions or prompts in the same chat history, without having to specify them again.

For example: In the **Gemini Code Assist** pane, enter the prompt `How can I improve YOUR_FILE_NAME_1?` (without the `@` symbol) and press `Enter` (for Windows and Linux) or `Return` (for macOS).

Gemini Code Assist responds to your enquiry about the file you specified in your prompt.

**Note:** If you clear your chat history, Gemini Code Assist no longer uses your files for context and you must re-specify the files or folders in the chat pane using the `@` symbol if you want to make more enquiries about the files.

### Manage files and folders in the Context Drawer

After you specify a file or folder to be used as context for your Gemini Code Assist prompts, these files and folders are placed in the _Context Drawer_ , where you can view and remove them from the prompt context.

To manage the files and folders in your Context Drawer, perform the following tasks:

###  VS Code 

**Note:** Chats created with Gemini Code Assist for VS Code, prior to version `2.34.0`, won't retain and display the saved context in the Context Drawer. This can lead to issues where the chat doesn't display the correct context. To build and retain context among chats, we recommend you clear chats prior to this version.

  1. In the activity bar of your IDE, click spark **Gemini Code Assist**.

  2. To view the files and folders in your Context Drawer, click **Context items**.

![Context Drawer for Gemini Code Assist for VS Code](https://docs.cloud.google.com/static/gemini/images/vscode-context-drawer.png)

  3. To remove items from the Context Drawer, click close **Remove**.




###  IntelliJ 

  1. In the activity bar, click spark **Gemini Code Assist.**

  2. To view the files and folders in your Context Drawer, click **Context**.

![Context Drawer for Gemini Code Assist for IntelliJ](https://docs.cloud.google.com/static/gemini/images/intellij-context-drawer.png)

  3. To remove files and folders from the Context Drawer, click close **Remove**.




## Exclude files from local context

If files are specified in a `.aiexclude` or `.gitignore` file, Gemini Code Assist by default excludes them from local use in the context for code completion, code generation, code transformation, and chat.

To learn how to exclude files from local use, see [Exclude files from Gemini Code Assist use](https://docs.cloud.google.com/gemini/docs/codeassist/create-aiexclude-file).

## Revert to a checkpoint in chat

After applying the changes that Gemini Code Assist generates based on your prompt, you can choose to revert the modified code file(s) to a certain checkpoint, which reverts all of the applied changes to the code file(s).

Reverting to a checkpoint does _not_ revert manual changes that you may have made to the code file(s).

To revert your code file to a checkpoint, follow these steps:

###  VS Code 

In the Gemini Code Assist chat pane, click undo **Revert to checkpoint**. This reverts your code file back to the checkpoint state before the edits were made.

###  IntelliJ 

If you've already clicked check **Accept changes** for a chat generated code suggestion, then you have the option to rollback the changes using the undo **Rollback changes** button:

In the Gemini Code Assist chat pane, click undo **Rollback Changes**. This reverts your code file back to the checkpoint state before the edits were made.

![Revert to checkpoint button in IntelliJ Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/intellij-revert-to-checkpoint.png)

## View code diffs

By default, Gemini Code Assist suggests changes to your code with a code diff. You can trigger this diff any time you ask Gemini Code Assist to make changes to your code.

In this section, you prompt Gemini Code Assist to optimize your code file, view the diff in your code file, and accept or reject changes as preferred.

###  VS Code 

  1. With your code file opened, prompt Gemini Code Assist to `optimize this file`. If you want to optimize multiple files and folders, prompt Gemini Code Assist to `optimize @FILE1 and @FILE2`.

Gemini Code Assist responds to your prompt with code change suggestions in the code file(s) along with an inline diff that illustrates these changes.

  2. In the code file, click check_small **Accept** or close_small **Reject**.

![Accept or reject suggested a single change in a file in VS Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/vscode-accept-reject-diff.png)

  3. If Gemini Code Assist suggests multiple changes throughout your code file(s), click **View** above the suggestion and then click **Next** or **Previous** , to cycles through the other suggestions.

  4. If you want to accept or reject all of the suggested changes, click **Accept file** or **Reject file**.

![Accept or reject all changes in a file in VS Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/vscode-accept-reject-file.png)

  5. You can also use the Quick Preview in the prompt response to accept or reject all suggestions across multiple code files.

![Quick Preview in VS Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/vscode-quick-preview.png)




###  IntelliJ 

  1. With your code file opened, prompt Gemini Code Assist to `optimize this file`. If you want to optimize multiple files and folders prompt Gemini Code Assist to `optimize @FILE1 and @FILE2`.

Gemini Code Assist responds to your prompt with code change suggestions in the code file(s) along with an inline diff that illustrates these changes.

  2. In the code file, click check_small **Accept** or undo **Reject**.

![Accept or reject suggested a single change in a file in IntelliJ Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/intellij-accept-reject-diff.png)

  3. If Gemini Code Assist suggests multiple changes throughout your code file(s), click arrow_upward or arrow_downward to cycle through the other suggestions.

![Cycle through changes in a file in IntelliJ Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/intellij-cycle-diffs.png)

  4. You can also use the Quick Preview in the prompt response to accept or reject all suggestions across multiple code files.

![Quick Preview in IntelliJ Code Gemini Code Assist.](https://docs.cloud.google.com/static/gemini/images/intellij-quick-preview.png)




### Change diff view settings

###  VS Code 

If you prefer, you can change this setting to have a separate diff view window in your IDE by following these steps:

  1. In the activity bar, navigate to settings **Settings** > **Settings**.

  2. In the **User** tab of the settings, navigate to **Extensions** > **Gemini Code Assist**.

  3. Scroll to the **Geminicodeassist > Chat: Change View** setting.

  4. In the dropdown list, select one of the following options:

     * **Inline suggestions** (enabled by default): Code changes displayed in your code file.

     * **Default diff view** : Opens a new file with side-by-side code changes.




###  IntelliJ 

  1. In the chat response of the Gemini Code Assist sidebar Ask panel, click the **Preview in diff mode** button (compare_arrows).

A **Side-by-side** tab appears in the main coding pane.

  2. Click on the **Side-by-side** tab to view side-by-side code changes.




## Generate and view a file outline

By default, Gemini Code Assist generates an outline for the file in focus in your IDE. Note that outlines don't persist between IDE sessions, which means a new outline is generated for a given file when you start a new session, unless you disable automatic outline generation. To view the outline generated by Gemini Code Assist, do the following:

###  VS Code 

  1. In the Explorer sidebar, click the **Gemini Code Assist outline** icon.

The Gemini Code Assist outline pane opens.

  2. By default, the outline pane automatically generates an outline for the current file in focus.

     * If you previously disabled automatic outline generation, click the **Generate outline** button to generate an outline for the current file in focus.
  3. (Optional): Click on a node in the outline to automatically scroll to that portion of the code file.

  4. (Optional): Click the **Eye** icon in the outline pane to display the outline in-line in the code file itself.




When you make changes to a file that has an outline, a new outline is not automatically generated. Instead, an **Obsolete** banner appears at the bottom of the outline with an option to manually **Refresh** the outline.

###  IntelliJ 

  1. In the Gemini Code Assist chat pane, click the **Outline** tab.

The outline for the active file appears in the tab.

  2. (Optional): Click the **Eye** icon associated with the file outline to display the outline in-line in the code file itself.

  3. (Optional): Click the **Eye** icon that appears next to the **Outline** tab to display all available outlines in-line in their respective code files.




When you make changes to a file that has an outline, a new outline is not automatically generated. Instead, the option to manually **Refresh outline** becomes available in the **Outline** tab.

### Toggle automatic outline generation

To toggle automatic Gemini Code Assist outline generation of your code files, do the following:

###  VS Code 

  1. Navigate to **Settings** > **User** > **Extensions** > **Gemini Code Assist**.

  2. In the **Gemini Code Assist** window, toggle **Outlines: Automatic Outline Generation**.




If you disable automatic outline generation, you can manually generate an outline for the file in focus by right-clicking in the file and selecting **Gemini Code Assist** > **Outline current file** , or by going to the **Gemini Code Assist outline** pane and clicking the **Generate outline** button.

###  IntelliJ 

  1. In your IDE, navigate to **Settings** > **Tools** > **Gemini**.

  2. In the **Gemini settings** window, toggle **Enable automatic outline generation**.




If you disable automatic outline generation, you can manually generate an outline for the file in focus by going to the **Outline** tab and clicking **Generate Outline**.

## Create custom commands

By default, Gemini Code Assist provides commands like `/generate` for VS Code and **Generate Code** for IntelliJ and [other supported JetBrains IDEs](https://docs.cloud.google.com/gemini/docs/codeassist/supported-languages#supported_ides). You can also create your own custom commands to help you accomplish repetitive tasks faster in your IDE.

In this section, you create a custom command called `add-comments` that adds comments to the code in your code file. For IntelliJ and other supported JetBrains IDEs, you'll create, save, and execute the custom command from the Prompt Library, and from the in-editor prompt.

###  VS Code 

  1. In your code file, press `Control+I` (for Windows and Linux) or `Command+I` (for macOS) to open the **Gemini Code Assist Quick Pick** menu.

  2. In the menu, search for and select **Preferences: Open Settings (UI)**.

  3. In the **Search settings** field, enter `Geminicodeassist: Custom Commands`.

  4. In the **Custom Commands** box, select **Add Item**.

  5. In the **Item** field, enter `add-comments` as the name of the command.

  6. In the **Value** field, enter `add comments to all functions without comments in my code` as the prompt.

  7. Click **OK**.




You can now use the custom command `add-comments` in your IDE. The command appears in the list of commands in the Gemini Code Assist Quick Pick menu (`Control+I` (for Windows and Linux) or `Command+I` (for macOS)).

###  IntelliJ 

  1. In your IDE, navigate to **Settings** > **Tools** > **Gemini** > **Prompt Library**.

![Prompt Library for IntelliJ Gemini Code Assist](https://docs.cloud.google.com/static/gemini/images/intellij-prompt-library.png)

  2. In the **Prompt Library** window, click add **Add**.

  3. Name your custom command `add-comments`.

  4. In the Prompt Library's text box, enter the prompt: `Add comments to all functions without comments in this code`.

  5. Select the **Show in In-Editor Prompt** checkbox if it's unselected.

  6. Click **OK** to save the custom command in the Prompt Library.

  7. In your code file, highlight the code that you want to modify.

  8. Right-click the highlighted code and navigate to **Gemini** > **Prompt Library** and then select the custom command `add-comments`.

Gemini Code Assist executes the `add-comments` command and adds comments to your highlighted code.




You can also invoke the custom command with the in-editor prompt by performing the following tasks:

  1. In your code file, highlight the code that you want to modify, and press `Alt+\` (for Windows and Linux) or `Cmd+\` (for macOS) to open the **Gemini Code Assist Quick Pick** menu.

  2. In the menu, select your custom command `add-comments`.

Gemini Code Assist executes the `add-comments` command and adds comments to your highlighted code.




In the Gemini Code Assist chat pane, you can type `@` to retrieve and use a saved prompt in your Prompt Library.

## Create rules

You can create rules for Gemini Code Assist to follow, and the rules are included in every chat prompt you enter.

Rules in Gemini let you define your preferences, such as:

  * Coding style
  * Output formats
  * Tech stack
  * Language



For example, you can create a rule such as "Always give me concise responses in Kotlin."

###  VS Code 

  1. In your code file, press `Control+I` (for Windows and Linux) or `Command+I` (for macOS) to open the **Gemini Code Assist Quick Pick** menu.

  2. In the menu, search for and select **Preferences: Open Settings (UI)**.

  3. In the **Search settings** field, enter `Geminicodeassist: Rules`.

  4. In the text field, enter a rule such as: `Always generate unit tests when creating a new function`. You can also add one or more rules with multiple lines in the text field.

After adding rules in the Rules settings, Gemini Code Assist considers the rule for every prompt or request you make.

To remove the rule, delete the content from the Rules text field.




###  IntelliJ 

**Note:** Rules aren't used in agent mode.

  1. To create a rule, go to **Settings > Tools > Gemini > Prompt Library > Rules** and then edit the text in the editor.
  2. To set the scope of the rule, in the **Scope** drop-down, select **IDE** or **Project**.

     * IDE-level rules are private to yourself and can be used across multiple projects.
     * Project-level rules can be shared among teammates working on the same project.

To share prompts across the team you must add the `.idea` folder to the version control system.




![Create Gemini rules in IntelliJ](https://docs.cloud.google.com/static/gemini/images/intellij-rules.png)

## Known issues

For a list of known issues with Gemini Code Assist in your IDE, see [known issues](https://docs.cloud.google.com/gemini/docs/codeassist/code-overview#known-issues).

## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn about [Gemini Code Assist Standard and Enterprise pricing](https://cloud.google.com/products/gemini/pricing).
  * Learn about [security, privacy, and compliance of Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/security-privacy-compliance).
  * Learn [how Gemini Code Assist uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
