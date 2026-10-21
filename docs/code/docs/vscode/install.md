---
url: https://docs.cloud.google.com/code/docs/vscode/install/
title: Install the Cloud Code for VS Code extension \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:49.529846+00:00
---

# Install the Cloud Code for VS Code extension  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Install the Cloud Code for VS Code extension Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** We have unified our tools into a single, multi-agent platform called Antigravity, with Antigravity CLI now available. Starting June 18, 2026, Gemini Code Assist IDE Extensions and Gemini CLI stopped serving requests for the Gemini Code Assist for individuals, Google AI Pro, and Google AI Ultra tiers. Affected users should migrate to Antigravity and Antigravity CLI. To learn more, see the [deprecation page](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals).

The Cloud Code for VS Code extension adds support for Google Cloud development to VS Code.

## Before you begin

Before you install Cloud Code, confirm that the following tools are installed and set up on your system:

  1. Install and set up [Visual Studio Code](https://code.visualstudio.com/) on your machine.
  2. Install and configure language support.

The Cloud Code extension works best with the following languages:

     * NodeJS (built-in support; no action required)
     * [Go](https://marketplace.visualstudio.com/items?itemName=ms-vscode.Go)
     * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
     * [Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug)
     * [.NET](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscode-dotnet-pack)
  3. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Git is required for copying samples to your machine.

  4. Install the [Docker client](https://docs.docker.com/install/#supported-platforms) and add it to the `PATH` environment variable:

     * If you're building exclusively using Cloud Build or Jib, you can skip installing Docker.
     * If you're using WSL but can't install Docker for Desktop, use minikube instead for local development with Cloud Code.
  5. If you're using Google Cloud, [create a Google Cloud project](https://console.cloud.google.com/cloud-resource-manager) and then [enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

Projects allow you to collect the related resources for a single application in one place, manage APIs, enable Google Cloud services, add and remove collaborators, and manage permissions for Google Cloud resources.




## Install Cloud Code

**Note:** When installing Cloud Code, the [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview) extension is also installed by default.

[Install the Google Cloud Code extension](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.cloudcode&ssr=false#overview) from the Visual Studio Code Marketplace.

Alternatively, open the **Extensions** view in VS Code:

  1. Click ![Extension icon](https://docs.cloud.google.com/static/code/docs/vscode/images/vscodeextension.png)**Extensions** or press `Ctrl`/`Cmd`+`Shift`+`X`.

  2. Search for `Google Cloud Code`.

![Cloud Code extension in VSC marketplace](https://docs.cloud.google.com/static/code/docs/vscode/images/cloud-code-vscode-extensions-marketplace.png)

  3. Click **Install**.

  4. If prompted, restart VS Code.

After the extension has successfully installed, the Cloud Code icon is added to the activity bar and ready for use. You can further configure your Cloud Code installation by specifying your preferences using the top-level application taskbar: navigate to **Code** > **Settings** > **Settings** > **Extensions** and search for `Gemini Code Assist + Google Cloud Code`.




### Custom versions of dependencies

By default, Cloud Code has _Auto dependencies_ turned on and installs some command-line dependencies for you automatically. If you turn off auto dependencies, you can use custom versions of the dependencies but you must install the dependencies yourself for Cloud Code to work.

To use custom versions of Cloud Code dependencies:

  1. Click settings **Manage** > **Settings** and then set **Auto Dependencies** (`cloudcode.autoDependencies`) to `off`.

  2. Install the following dependencies on your `PATH`:

     * [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
     * [Skaffold](https://skaffold.dev/docs/install/)
     * [minikube](https://minikube.sigs.k8s.io/docs/start/) for local development



#### Install the Google Cloud CLI

The first time you use a feature that requires the gcloud CLI, you're given the option to learn how to install the CLI from your IDE, use an existing installation, or continue with managed dependencies. If you prefer to install the gcloud CLI manually, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/install).

## Optional: Verify Cloud Code vsix using VsixSignTool

To verify the Cloud Code vsix with the VsixSignTool, perform the following steps:

  1. Ensure you're using the following:

     * Nuget package manager
     * Windows OS
     * A production release of Cloud Code
  2. Install the [Microsoft VsixSignTool](https://www.nuget.org/packages/Microsoft.VSSDK.Vsixsigntool) and take note of the installation path.

  3. Open VS Code and navigate to ![Extensions icon in VSC](https://docs.cloud.google.com/static/code/docs/vscode/images/vscodeextension.png)**Extensions** > **Cloud Code**.

  4. In the **Details** tab, under **Extension Resources** , click **Marketplace**.

  5. On the Marketplace page in your browser, under **Resources** , click **Download Extension** to download the packaged version of Cloud Code. This downloads the packaged version of Cloud Code, which has a `.vsix` file extension, to your default download directory.

  6. If you'd prefer to verify a different version than the latest, click the **Version History** tab and select a different version to download.

**Note:** The earliest Cloud Code version you're able to verify with VsixSignTool is `1.20.2`.
  7. When the download is complete, open a terminal window and run the following:
         
         PATH_TO_VSIXSIGNTOOL verify PATH_TO_DOWNLOADED_VSIX
         

  8. Confirm that the output matches the following:

`VsixSignTool Success: Package PATH_TO_DOWNLOADED_VSIX is valid.`




## Authenticate credentials for Google Cloud

To help with application development with Google Cloud APIs, when you sign in to the gcloud CLI, your [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/production#finding_credentials_automatically) are updated.

### Sign in to Google Cloud

If you aren't signed in to Google Cloud, follow these steps to sign in:

  1. In the Cloud Code status bar, click **Cloud Code - Sign in**.
  2. If this is your first time connecting to Google Cloud in your IDE, you're prompted to add `https://accounts.google.com` to Trusted Domain. Click **Configure Trusted Domains** in the dialog that appears:

![Configure Trusted Domain dialog](https://docs.cloud.google.com/static/code/docs/vscode/images/configure-trusted-domains.png)

  3. Follow the prompts to sign in using your web browser.

  4. When prompted to allow Cloud Code to access your Google Account, click **Allow**.




#### Known issue: Edge browser redirects to HTTPS on authentication callback

When using the Microsoft Edge browser to authenticate your credentials, you may notice that the Edge browser redirects the URL `http://localhost:3000` to `https://localhost:3000`. This leads to the following failure message:

`The connection for this site is not secure. localhost sent an invalid response. Try running Windows Network Diagnostics. ERR_SSL_PROTOCOL_ERROR.`

To solve this problem, you can exclude `localhost` from the redirection:

  1. In the address bar of your Edge browser, enter `edge://net-internals/#hsts`.

  2. Go to the **Delete domain security policies** section.

  3. Enter `localhost`, then click **Delete**.




### Log out of Google Cloud

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand **Help and Feedback**.
  2. Click **Sign Out of Google Cloud** and when prompted, select **Sign-out**.
  3. Alternatively, you can log out using the Command Palette. Press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette** , and then click **Sign out of all accounts in Google Cloud SDK**.



### Change the active Google Cloud project

  1. In the Cloud Code status bar, click the active project name.

![Active project name in status bar](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-status-bar.png)

  2. In the Quick Pick menu that appears, select sync_alt **Switch Project**.

  3. Select a project or enter keywords in the search bar to filter projects.




## Authenticate credentials for debugging applications locally

In addition to the authentication steps in the Sign in to Google Cloud section, you'll need to authenticate your credentials to debug an application locally in your IDE that makes Google API calls.

If you don't authenticate your credentials for debugging applications, an error message appears in your IDE when you attempt to run/debug a local application that tries to make a call to a Google API.

To authenticate your credentials for debugging applications locally, perform the following steps:

  1. Install [gcloud](https://docs.cloud.google.com/sdk/docs/install) to your machine if you haven't already done so.

  2. Run the following command:
         
         gcloud auth application-default login
         

  3. When you've finished debugging locally, you can sign out by running the following command:
         
         gcloud auth application-default revoke
         




To learn more about Application Default Credentials and Google APIs, see [Authenticate to Cloud services using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

## What's next

  * [Creating an application](https://docs.cloud.google.com/code/docs/vscode/creating-an-application)
  * [Create and configure a GKE cluster](https://docs.cloud.google.com/code/docs/vscode/create-configure-gke-cluster)
  * [Developing APIs using Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview)



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
