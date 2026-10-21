---
url: https://docs.cloud.google.com/shell/docs/use-cloud-shell-terminal/
title: Use the Cloud Shell Terminal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:15.077401+00:00
---

# Use the Cloud Shell Terminal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/use-cloud-shell-terminal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Use the Cloud Shell Terminal Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Cloud Shell Terminal. The Gemini CLI is available in Cloud Shell without additional setup.

## Use the terminal

Cloud Shell provides command-line access to the virtual machine instance in a terminal window that opens in the Google Cloud console. You can open multiple shell connections to the same instance.

To view the gcloud CLI available commands, run `gcloud --help`.

In addition to accessing the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and other utilities from the command line, you can use the `cloudshell` command to launch tutorials, open the Cloud Shell Editor, and download files.

For more information, run `cloudshell help`.

### Scroll the display

In addition to using your mouse while browser focus is on a session tab, you can scroll by pressing `Ctrl`+`Shift`+`PageUp` / `Ctrl`+`Shift`+`PageDn` (Windows and Linux) or `Fn`+`Shift`+`Up` / `Fn`+`Shift`+`Down` (on Mac OS X).

### Copy and paste text

To copy and paste text:

  1. Select some text in the session display or another window using your mouse.

  2. To copy the text, press `Ctrl`+`C` (on Windows or Linux) or `Cmd`+`C` (on macOS).

  3. To paste at your cursor location, press `Ctrl`+`V` (on Windows or Linux) or `Cmd`+`V` (on macOS).




### Send a key combination using the Google Cloud console

Click ![Send Key Combination Button](https://docs.cloud.google.com/static/shell/docs/images/send-keys.png)**Send Key Combination** and then press `Ctrl`+`V`.

## Configure terminal settings

To adjust your terminal settings, click ![Settings Button](https://docs.cloud.google.com/static/shell/docs/images/settings-button.png)**Settings**. In this menu, you can set your Terminal preferences for theme, font type and size, and copy, keyboard and scrollbar default settings.

### Keyboard layout support

If you're using an international keyboard or would like to customize your key bindings, Cloud Shell allows you to specify which key behaves as Alt Gr (your modifier key). To specify key mapping, go to the **Terminal Settings** menu, select **Terminal Preferences** > **Keyboard** > **Alt Gr Key** and choose one of the following options:

  * Auto - Autodetect based on browser language
  * None - Disable any AltGr related munging
  * Ctrl-Alt - Set Ctrl+Alt as AltGr
  * Left-Alt - Set left Alt as AltGr
  * Right-Alt - Set right Alt as AltGr



Additionally, you can set 'Alt is meta' to specify that your alt key should behave as a meta key.

## Open multiple terminal sessions

To open additional sessions, click ![Add Session Button](https://docs.cloud.google.com/static/shell/docs/images/add-session-button.png)**Add Cloud Shell Session** at the top of the Cloud Shell window. Each session connects to the same virtual machine instance. When you open a new session, it appears in a new tab at the bottom of the Google Cloud console.

## Tab title customization

Cloud Shell understands xterm escape sequences for [setting tab titles](http://tldp.org/HOWTO/Xterm-Title-4.html#ss4.3). To rename a tab title, set the `PS1` environment variable in your .bashrc to your desired configuration and source your .bashrc for the change to take.

## Use the Gemini CLI

To use the [Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) in Cloud Shell, run `gemini` in the Cloud Shell terminal.

To get started with the Gemini CLI, see the [Gemini CLI documentation](https://github.com/google-gemini/gemini-cli).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
