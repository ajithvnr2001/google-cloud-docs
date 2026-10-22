---
url: https://docs.cloud.google.com/code/docs/intellij/debug/
title: Debug Kubernetes applications with Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:15.010742+00:00
---

# Debug Kubernetes applications with Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/debug/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Debug Kubernetes applications with Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Debugging support is available for Java, Kotlin, Node.js, Go, and Python.

Cloud Code for IntelliJ allows you to easily debug your applications deployed to a Kubernetes cluster. You can debug an application on a local cluster (like minikube or Docker Desktop), Google Kubernetes Engine, or any other Cloud provider.

With Cloud Code's debugging support, you skip manual setup like setting up port forwarding, installing a debugging backend, or injecting language-specific debug arguments in the right way. All you need is a Cloud Code-ready Kubernetes application that includes a `skaffold.yaml` configuration file.

Cloud Code also enables you to [debug an application while making changes to, and iterating on, source code](https://docs.cloud.google.com/code/docs/intellij/watch-modes#applying-changes-while-debugging).

## Supported IDEs

The following table lists the languages and IDEs that Cloud Code supports for debugging. The table also lists the required plugins, where applicable:

Language | Supported IDEs and editions | Required plugin  
---|---|---  
Java | IntelliJ IDEA Ultimate | N/A  
IntelliJ IDEA Community | N/A  
Go | IntelliJ IDEA Ultimate | Go plugin  
GoLand | N/A  
Node.js | IntelliJ IDEA Ultimate | Node.js plugin  
WebStorm | N/A  
Python | IntelliJ IDEA Ultimate | Python plugin  
PyCharm Professional | N/A  
  
For more information about IDE support, see [Supported JetBrains IDEs](https://docs.cloud.google.com/code/docs/intellij/ides).

With Cloud Code, you can set breakpoints and debug remote applications running in containers for the following languages:

### Java

Cloud Code automatically adds an environment variable, `JAVA_TOOL_OPTIONS`, with the appropriate JDWP configuration to enable debugging. If `JAVA_TOOL_OPTIONS` is already present, Cloud Code uses existing settings specified in `JAVA_TOOL_OPTIONS`.

### Node.js

Depending on the structure of your application and its image build configuration, you might have to help the debugger map your local sources to the remote sources in the container. This enables the Node debugger to correctly process your breakpoints.

You can configure this in one of the following ways:

  * **Manual configuration**

Select the **Develop on Kubernetes** Run Configuration from the dropdown and then click **Edit Configurations**. On the **Debug** tab, configure the source mapping from your local application source to the source location in the remote container.

![Choosing a source location in the source mapping section of the Debug tab](https://docs.cloud.google.com/static/code/docs/intellij/images/source-mappings.png)

Configuration options:

    * **File/directory** \- the local file or directory of your application running on Kubernetes.
    * **Remote path** \- the path to the file or directory running in the container on Kubernetes.
  * **Automatic configuration**

You can choose to defer this mapping to Cloud Code. When you start your debug session, Cloud Code attempts to infer this mapping automatically. The inferred mapping is presented to you in a dialog; one dialog for each artifact you are debugging.

![Remote path mapping dialog for each artifact specifying remote path being used](https://docs.cloud.google.com/static/code/docs/intellij/images/remote-path-mapping.png)

Configuration options:

    * **Local path** \- the local path to the root of the artifact you are debugging.
    * **Remote path** \- the path to the file or directory running in the container on Kubernetes. You can choose to override this with your own value. If you click **Cancel** , no mapping is applied.
**Note:** Automatic mapping is a best effort guess based on heuristics.



### Go

To configure your application for debugging, your app must be a [Go Module](https://blog.golang.org/using-go-modules)-based application and be identified as being Go-based by setting one of the [standard Go runtime environment variables](https://godoc.org/runtime) in the container, such as `GODEBUG`, `GOGC`, `GOMAXPROCS`, or `GOTRACEBACK`. `GOTRACEBACK=single` is the default setting for Go and `GOTRACEBACK=all` is a generally useful configuration.

Optionally (but recommended), your app should be built with the `-gcflags='all=-N -l'` options to disable optimizations. Skaffold [Profiles](https://skaffold.dev/docs/environment/profiles/) are a useful option for this purpose and can be set with the **Deployment Profile** field in your Run configuration on the **Build/Deploy** tab.

### Python

To configure your application for debugging, ensure you meet the following prerequisites:

  * **IDE, edition, and plugin are compatible**

For compatible IDEs, editions, and plugins, see Supported IDEs.

  * **Skaffold version is 1.25.0 or greater**

You can allow Cloud Code to [manage your dependencies](https://docs.cloud.google.com/code/docs/intellij/install#managed_dependencies), or point to a local Skaffold installation. See **Preferences > Tools > Cloud Code > Dependencies**.

  * **Python interpreter is configured**

Without a Python interpreter configured in your project, debugging won't work, as there is no way to run `pydevd`, the underlying Python debugger.

IDE | How to configure  
---|---  
IntelliJ IDEA | Python debugging with Cloud Code requires a Python SDK to be configured for your project.   
  
Go to **File > Project Structure** and add a Python SDK in the **Project** tab. If none exists, add one under the **SDK** tab.  
PyCharm | Go to **File > Settings > Project > Python Interpreter** or for Mac OS X, **PyCharm > Preferences > Project > Python Interpreter**, and add a Python interpreter.  



For more information, see the [Skaffold debug documentation](https://skaffold.dev/docs/workflows/debug/).

## Debug an application

  1. To start the development cycle in debug mode on your Kubernetes cluster, click the debug action for ![run action icon](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-debug-action.png)**Develop on Kubernetes**.

![Starting the Kubernetes cluster development cycle in debug mode](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-debug-target.png)

The [continuous development cycle](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#continuous_development_on_kubernetes) initiates in debug mode.

Cloud Code attaches a debug session:

![Kubernetes debugger attached](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-debugger-attached.png)

  2. You can now perform the tasks you normally do when debugging local code, like setting breakpoints and stepping through code, against a live Kubernetes cluster.

![Kubernetes debugger session](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-debugger-session.png)

  3. To end the debugging session, click the stop icon on the **Develop on Kubernetes** Run Configuration.




## What's next

  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * Set up a [continuous development](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#continuous_development_on_kubernetes) environment in Cloud Code.
  * [View Kubernetes logs](https://docs.cloud.google.com/code/docs/intellij/view-logs) in Cloud Code.



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
