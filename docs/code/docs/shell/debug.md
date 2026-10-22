---
url: https://docs.cloud.google.com/code/docs/shell/debug/
title: Debug Kubernetes applications in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:17.888963+00:00
---

# Debug Kubernetes applications in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/debug/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Debug Kubernetes applications in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Debugging support is available for Node.js, Python, Go, Java, and .NET.

Cloud Code lets you debug an application deployed to a Google Kubernetes Engine (GKE) cluster by leveraging [`skaffold debug`](https://skaffold.dev/docs/workflows/debug).

You can debug your application on a local cluster (like [minikube](https://docs.cloud.google.com/code/docs/vscode/minikube-local-development) or [Docker Desktop](https://www.docker.com/products/docker-desktop/)), GKE, or any other cloud provider.

With Cloud Code's debugging support, you don't have to complete manual setup like setting up port forwarding or injecting language-specific debug arguments. Debugging requires a Cloud Code-ready GKE application that includes a `skaffold.yaml` configuration file and a `cloudcode.kubernetes` launch configuration.

## Debug a GKE application

To begin debugging your GKE application, follow these steps:

  1. In the Cloud Code status bar, click the active project name.

![Active project name in status bar](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-status-bar.png)

  2. In the Quick Pick menu that appears, select **Debug on Kubernetes**. 

  3. If your application doesn't have the necessary `skaffold.yaml` configuration or `cloudcode.kubernetes` launch configuration, Cloud Code [helps you set these up](https://docs.cloud.google.com/code/docs/shell/setting-up-an-existing-app).

  4. Confirm whether to use the current [Kubernetes context](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#context) to run the app in (or switch to a preferred one).

  5. If you chose a remote cluster as the context, when prompted, choose an image registry to push the images to.

If your project has [Artifact Registry API enabled](https://docs.cloud.google.com/artifact-registry/docs/enable-service) and at least one [Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/manage-repos), you can browse to and select an existing Artifact Registry repository.

The following samples demonstrate how to specify where container images are stored for some common registries:

Artifact Registry  | `REGION`-docker.pkg.dev/`PROJECT_ID`/`REPO_NAME`  
---|---  
Docker Hub  | docker.io/`ACCOUNT`   
Make sure that you're [properly authenticated](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry) if you're using a private Docker Hub repository.   
  
To generate the final image repository name, Cloud Code concatenates this image registry with the image name specified in the Kubernetes manifests. This choice is stored in your `cloudcode.kubernetes` launch configuration (found in `.vscode/launch.json`).

For more information, see the [image registry handling guide](https://skaffold.dev/docs/environment/image-registries).

Cloud Code builds your containers, pushes them to the registry, applies Kubernetes configurations to the cluster, and waits for the rollout.

After the rollout, Cloud Code automatically port-forwards all declared container ports to your machine and displays the URLs in the output window so that you can browse your live application.

  6. For each debuggable container in your application, confirm or enter the directory in the remote container where the program you want to debug is located.

Alternatively, you can press `ESC` to skip debugging the container.

![Remote Root prompt](https://docs.cloud.google.com/static/code/docs/vscode/images/debug-remote-root-prompt.png)

Cloud Code attaches a debug session for each debuggable container in the application.

You can now perform the same tasks you normally do when debugging local code, like setting breakpoints and stepping through code, against a live Kubernetes cluster.

By default, when a change to your application is autosaved, Cloud Code redeploys your application and sets up a new debug session. You can toggle this feature with the `watch` flag in your project's launch configuration. 

  7. To inspect variables and stack info, use the [Debug Sidebar](https://code.visualstudio.com/Docs/editor/debugging). To interact with the debugging session, use the [Debug Console](https://code.visualstudio.com/Docs/editor/debugging#_debug-console-repl) in the bottom pane debugger.

  8. After your session completes, you can use the following contextual menu commands:

     * **Open Deployment Logs:** Open the application logs of a specific deployment with the Cloud Code logs explorer.
     * **Open Service URL:** Open the application service URL of a specific service in a web browser
  9. If you've turned off watch mode in your launch configuration and you want to make changes to your application and rebuild and redeploy the application, in the Development sessions pane, pause on the run action and then click ![Rebuild and redeploy icon](https://docs.cloud.google.com/static/code/docs/vscode/images/rebuild-redeploy-app-icon.png)**Rebuild and redeploy the application**.

  10. To end the debugging session, click ![Debug stop icon](https://docs.cloud.google.com/static/code/docs/vscode/images/debug-stop-icon.png)**Stop** in the Debug Toolbar.

After you end the debugging session, all the deployed Kubernetes resources are deleted from the cluster.




## Configuration details

**Note:** Cloud Code doesn't modify your local Kubernetes configurations. The transformations happen at deploy-time and are visible only on the server.

Cloud Code automatically handles the following configuration details for all supported languages:

  * Port forwarding the debug port so that the debugger can be attached.
  * Attaching a debugger to one or more debuggable containers in your application. If your application has multiple debuggable containers (containers whose language is supported by Cloud Code debug) configured in `skaffold.yaml`, then a debugger is attached to each debuggable container.
  * Persisting source mapping definitions across sessions; you can customize these definitions by editing your `.vscode/launch.json` file directly.



Cloud Code also handles the following language-specific configuration details:

### Node.js

Rewriting the entrypoint to invoke:
    
    
    node --inspect=localhost:9229
    

### Python

Installing the [`ptvsd` module](https://skaffold.dev/docs/workflows/debug/) using an Init Container and rewriting the entrypoint to invoke:
    
    
    python -m ptvsd --host localhost --port 5678
    

### Go

Installing the [`dlv` debugger](https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md) using an Init Container and rewriting the entrypoint such that the launched debug session runs with a debug server only (in headless mode), continues the debugged process on start, accepts multiple client connections, and listens at `localhost:56268`:
    
    
      dlv exec --headless --continue --accept-multiclient --listen=localhost:56268 --api-version=2, <app> --
    

### Java

Adding an environment `JAVA_TOOLS_OPTIONS` with the appropriate Java Debug Wire Protocol (JDWP) configuration such that the JDWP debugging agent listens for a socket connection on port 5005 and allows the VM to begin executing before the debugger is attached:
    
    
      jdwp=transport=dt_socket,server=y,suspend=n,address=5005,quiet=y
    

For more details on debugging using `skaffold debug`, see the [documentation](https://skaffold.dev/docs/workflows/debug/).

## Set up your container

To prepare your container for debugging, follow the instructions for the language you're using:

### Node.js

  * Start the Node.js application with `--inspect=<debugPort>` where `debugPort` comes from the [attach configuration](https://docs.cloud.google.com/code/docs/shell/debug-k8-pod#configuration_attributes). For example: `CMD ["node", "--inspect=9229", "index.js"]`



### Python

  * Make sure that you have the [`ptvsd`](https://github.com/Microsoft/ptvsd) module installed on your machine and in your container.
  * Start the Python application through `ptvsd`. Match the port specified to the `debugPort` field in the [attach configuration](https://docs.cloud.google.com/code/docs/shell/debug-k8-pod#configuration_attributes). For example: 
        
        CMD ["python", "-m", "ptvsd", "--port", "", "app.py"]




### Go

  * Make sure that you have the [`dlv`](https://github.com/derekparker/delve) package installed on your machine and your Go container.
  * Start your Go application through [`dlv debug`](https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv_debug.md).

The port specified in the starting command should be the same as the `debugPort` attribute value in the [attach configuration](https://docs.cloud.google.com/code/docs/shell/debug-k8-pod#configuration_attributes). For example: 
        
        CMD ["dlv", "debug", "--headless", "--listen=:<debugPort>", "--log"]

**Troubleshooting Tip:** When debugging a Go application, the application will stop and wait for a debugger to attach. Attach a debugger for the service to start.




### Java

  * Make sure that JVM is installed on your machine.
  * Start the Java application with the following options, where `debugPort` comes from the [attach configuration](https://docs.cloud.google.com/code/docs/shell/debug-k8-pod#configuration_attributes). 
        
        -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=,quiet=y

For example, to start the Java application in debug mode and listen on port `debugPort` for connection: 
        
        ENTRYPOINT ["java","-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=<debugPort>,quiet=y", "-jar", "my-app-1.0.jar"]




### .NET Core

  * Make sure that you have the `vsdbg`, the .NET Core command line debugger from Microsoft, installed on your Kubernetes container.

For example: 
        
        RUN apt-get update   
          && apt-get install -y --no-install-recommends unzip   
          && apt-get install -y procps   
          && rm -rf /var/lib/apt/lists/*   
          && curl -sSL https://aka.ms/getvsdbgsh | bash /dev/stdin -v latest -l /dbg/netcore/vsdbg




## Set up your attach configuration

To attach to a debuggable container, you need to have an [attach configuration](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations) of type `cloudcode.kubernetes`.

### Add a .vscode/launch.json file

If your project doesn't have a `launch.json` file in its `.vscode` folder, you can add one using the Debug panel.

  1. To navigate to the Debug panel, click ![Debug icon](https://docs.cloud.google.com/static/code/docs/vscode/images/debugicon.png)**Debug** in the Activity bar.

  2. Select **Add Configuration** from the drop-down menu.

  3. Select **Cloud Code: Kubernetes** as the environment.

![Setting Cloud Code: Kubernetes as the environment](https://docs.cloud.google.com/static/code/docs/vscode/images/select-cloud-code-kubernetes.png)

  4. Select the **Attach to Kubernetes Pod** option.

![Select Kubernetes configuration option](https://docs.cloud.google.com/static/code/docs/vscode/images/select-kubernetes-configuration-option.png)

  5. Select the programming language you're using.

This creates and opens a `launch.json` file for your project and creates an attach configuration for you.

  6. Update configuration attributes in the `launch.json` file to match those of your project. For more information on configuration attributes, see [Configuration attributes](https://docs.cloud.google.com/code/docs/shell/debug-k8-pod#configuration_attributes).




### Add an attach configuration to your .vscode/launch.json file

To add a new attach configuration to an existing `.vscode/launch.json` file:

  1. Open the `launch.json` file.
  2. To invoke the snippet Intellisense, click **Add Configuration**.
  3. To add an attach configuration, select the **Cloud Code: Attach to Kubernetes Pod** snippet for the language you're using.
  4. Update attributes in the configuration to match those of your project. For more information on configuration attributes, see [Configuration attributes](https://docs.cloud.google.com/code/docs/shell/debug-k8-pod#configuration_attributes).



### Configuration attributes

Attribute  | Description   
---|---  
debugPort  | Debug port used on the container.   
podSelector  | Set of key-value pairs used to select the debug pod. For more information, see the [guide on selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels)). The following sample shows a typical `podSelector`:   
  
` "podSelector": { "app": <deployment-name> } `  
localRoot  | Path to the local directory containing the program being debugged. Defaults to ${workspaceFolder}.   
remoteRoot  | Absolute path to the remote directory containing the program being debugged (on the Kubernetes container).   
  
## Attach a debugger to your Kubernetes pod

Cloud Code for Cloud Shell supports attaching a debugger to a Kubernetes pod for Node.js, Python, Go, Java and .NET. All you need is a debuggable container and an attach configuration of type `cloudcode.kubernetes`.

For information about how attaching to a Kubernetes pod differs from debugging a Kubernetes application, see How attaching a debugger to a pod differs from debugging a Kubernetes application.

To attach a debugger to your Kubernetes pod, perform the following tasks:

  1. To navigate to the Debug panel, click ![Debug icon](https://docs.cloud.google.com/static/code/docs/vscode/images/debugicon.png)**Debug** in the Activity bar.
  2. Select and launch the configuration by pressing `F5`.

     * `localhost:${debugPort}` is port-forwarded to `debugPort` on the container while debugging.

The debugging session is now successfully set up. You can perform the tasks you normally do when debugging local code, like setting breakpoints and stepping through code.

  3. To inspect variables and stack info, use the [Debug Sidebar](https://code.visualstudio.com/Docs/editor/debugging). To interact with the debugging session, use the [Debug Console](https://code.visualstudio.com/Docs/editor/debugging#_debug-console-repl) in the bottom pane debugger.

  4. To end the debugging session, click ![Debug stop icon](https://docs.cloud.google.com/static/code/docs/vscode/images/debug-stop-icon.png)**Stop** in the Debug Toolbar.




### How attaching a debugger to a pod differs from debugging a Kubernetes application

Attach to a Kubernetes pod  | Debug a Kubernetes application   
---|---  
Debugs a single Kubernetes pod.  | Debugs all the debuggable containers in the application.   
The application must be running in the Kubernetes pod before debugging.  | Runs the application on the Kubernetes cluster and attaches the debugger.   
Uses [configuration (.vscode/launch.json)](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations) of type `cloudcode.kubernetes` and request `attach`.  | Uses [configuration (.vscode/launch.json)](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations) of type `cloudcode.kubernetes` and request `launch`.  
For more information, see [Launch versus attach configurations](https://code.visualstudio.com/docs/editor/debugging#_launch-versus-attach-configurations).   
Sample Config: 
    
    
    {
      "name": "Attach to Kubernetes Pod (NodeJS)",
      "type": "cloudcode.kubernetes",
      "request": "attach",
      "language": "Node",
      "debugPort": 9229,
      "podSelector": {
         "app": "hello-world"
      },
      "localRoot": "${workspaceFolder}",
      "remoteRoot": "/app"
    }
    

| Sample Config: 
    
    
    {
      "name": "Run/Debug on Kubernetes",
      "type": "cloudcode.kubernetes",
      "request": "launch",
      "skaffoldConfig": "${workspaceFolder}/skaffold.yaml",
      "watch": true,
      "cleanUp": true,
      "portForward": true
    }
      
  
This configuration can't be used to run the application.  | This configuration can be used to run or debug the application.   
This configuration is language specific.  | This configuration is not language specific.   
No dedicated command.  | **Debug on Kubernetes** command.   
  
## What's next

  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/shell/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * Set up a [continuous development](https://docs.cloud.google.com/code/docs/shell/speed-up-k8s-development#continuous_development_on_kubernetes) environment in Cloud Code.
  * [View Kubernetes logs](https://docs.cloud.google.com/code/docs/shell/view-logs) in Cloud Code.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
