---
url: https://docs.cloud.google.com/code/docs/intellij/manage-sdk/
title: Install the Cloud Code for IntelliJ plugin \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:00:19.847212+00:00
---

# Install the Cloud Code for IntelliJ plugin  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/manage-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Install the Cloud Code for IntelliJ plugin Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** We have unified our tools into a single, multi-agent platform called Antigravity, with Antigravity CLI now available. Starting June 18, 2026, Gemini Code Assist IDE Extensions and Gemini CLI stopped serving requests for the Gemini Code Assist for individuals, Google AI Pro, and Google AI Ultra tiers. Affected users should migrate to Antigravity and Antigravity CLI. To learn more, see the [deprecation page](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals).

The Cloud Code for IntelliJ plugin adds support for Google Cloud development to the JetBrains family of IDEs, including IntelliJ (both Community and Ultimate editions), GoLand, PyCharm, WebStorm (and others).

## Prerequisites

**Note:** You must have a JetBrains IDE version of 2022.3++ to use Cloud Code for IntelliJ.

The following tools are expected to be installed and set up on your system and available on the `PATH` of your machine:

  * **JetBrains IDE version 2022.3+**

Your IDE should be a JetBrains IDE such as one of the following:

    * IntelliJ Ultimate or Community
    * PyCharm Professional or Community
    * WebStorm
    * GoLand
  * **[Git](https://git-scm.com/downloads)** so that Cloud Code can perform Git operations, like cloning a sample.

  * **[Docker](https://docs.docker.com/install/)** for building and pushing your container images.

  * **Configured Kubernetes cluster** which can either be a cluster for local development, such as [minikube](https://kubernetes.io/docs/tasks/tools/#minikube) or [Docker Kubernetes](https://docs.docker.com/docker-for-mac/kubernetes/) cluster, or a remote cluster, such as [Google Kubernetes Engine cluster](https://docs.cloud.google.com/kubernetes-engine). A minikube cluster is recommended for local development; minikube can be managed automatically by Cloud Code.

  * **[Google Cloud project](https://console.cloud.google.com/projectselector2/home/dashboard)** with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project) if you're using Google Cloud. Projects allow you to collect all of the related resources for a single application in one place as well as manage APIs, enable Google Cloud services, add and remove collaborators, and manage permissions for Google Cloud resources.




## Install the Cloud Code plugin

[Install the Cloud Code plugin](https://plugins.jetbrains.com/plugin/8079-google-cloud-code) from the JetBrains Marketplace.

**Note:** When installing Cloud Code, the [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview) plugin is also installed by default.

Alternatively, you can install the plugin directly from your IDE:

  1. Launch your IDE.

  2. Open your IDE's plugins marketplace:

     * For Windows, navigate to **File** > **Settings** > **Plugins**.
     * For macOS, navigate to **IntelliJ IDEA** > **Preferences** > **Plugins**.
  3. Enter `Google Cloud Code` in the search field and then install the Cloud Code plugin.

![Cloud Code plugin in IntelliJ marketplace](https://docs.cloud.google.com/static/code/docs/intellij/images/cloud-code-intellij-plugins-marketplace.png)

  4. If prompted, restart your IDE to activate the plugin.

  5. To avoid any conflicts if you're using Android Studio as your IDE, disable the Google Cloud Tools for Android Studio plugin after installing Cloud Code. The Google Cloud Tools for Android Studio plugin will be deprecated soon and will be fully removed in a future version of Android Studio.




### Custom versions of dependencies

By default, Cloud Code installs some required command-line dependencies automatically. To use custom versions of dependencies, opt out of dependency management as follows:

  1. Ensure that you have installed custom versions of the dependencies:

     * [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
     * [Skaffold](https://skaffold.dev/docs/install/)
     * [minikube](https://minikube.sigs.k8s.io/docs/start/) for local development
     * [Google Cloud CLI](https://docs.cloud.google.com/sdk/install) if developing with Google Cloud
  2. Specify the relevant Cloud Code settings in your IDE by opening **File** > **Settings** > **Tools** > **Cloud Code** > **Dependencies** or, for Mac OS X, **IntelliJ IDEA** > **Preferences** > **Tools** > **Cloud Code** > **Dependencies**.

  3. To manage the gcloud CLI, in the **Cloud SDK** section, select **Use a custom local installation** , click the **Browse** folder icon next to the field, navigate to the gcloud CLI installation that you want to use, and click **OK**.

  4. To manage other dependencies, in the **Deployment Tools** section, select **Use custom specified dependencies** , click the **Browse** folder icon for each dependency, specify a path to the custom version you want to use for each dependency, and click **OK**.




## Optional: Download and verify the Cloud Code binary

Verifying the Cloud Code binary helps to ensure you that the Cloud Code plugin hasn't been tampered with over the course of the publishing and delivery pipeline.

To download the Cloud Code _Stable_ or _Insiders_ binary to your machine, follow these steps:

  1. On Cloud Code's [**Plugin versions**](https://plugins.jetbrains.com/plugin/8079-cloud-code/versions) page, select either the [**Stable**](https://plugins.jetbrains.com/plugin/8079-cloud-code/versions/stable) or [**Insiders**](https://plugins.jetbrains.com/plugin/8079-cloud-code/versions/insiders) channel.

For more information on the Insiders build, see [Use pre-release features](https://docs.cloud.google.com/code/docs/intellij/insiders).

  2. Download the latest version of Cloud Code or a version that you want to verify that falls under the current versions that support verification:

     * Stable: Every release after `23.1.1-221`/`23.1.1-222` (`23.1.1-221`/`23.1.1-222` not included)

     * Insiders: Every release after `23.1.1-221-IB.1`/`23.1.1-222-IB.1` (`23.1.1-221-IB.1`/`23.1.1-222-IB.1` not included)

  3. Take note of the path to your Cloud Code binary (the `google-cloud-code.zip` file).




To verify the Cloud Code binary, follow these steps:

  1. Download the latest version of the [`marketplace-zip-signer-cli.jar`](https://github.com/JetBrains/marketplace-zip-signer/releases) file to your machine. Take note of the path to your `jar` file.

  2. Download [DigiCert Trusted Root G4](https://www.digicert.com/kb/digicert-root-certificates.htm). Take note of the path to your certificate file.

**Tip:** Since there are many items on the [DigiCert Trusted Root Authority Certificates page](https://www.digicert.com/kb/digicert-root-certificates.htm), use `Ctrl`/`Cmd`+`F` and search for `DigiCert Trusted Root G4`.
  3. Ensure you have the [JDK](https://www.oracle.com/ca-en/java/technologies/downloads/) installed. This is required to run Java commands.

  4. To verify the `zip` file (the Cloud Code binary), run the following in your command line:
         
         java -jar PATH_TO_ZIP_SIGNER_JAR verify -in PATH_TO_ZIP_FILE -cert PATH_TO_CERTIFICATE_FILE
         

If the verification fails, one of the following messages appears in your command line output:

     * `Zip archive is not signed by provided certificate authority.`
     * `Provided zip archive is not signed.`
     * `Signature of zip archive is invalid.`

If you don't see a message in the command line output, then the verification is successful.




## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
