---
url: https://docs.cloud.google.com/code/docs/vscode/debug-service/
title: Debug a Cloud Run service in Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:14.385487+00:00
---

# Debug a Cloud Run service in Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/debug-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Debug a Cloud Run service in Cloud Code for VS Code Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code for VS Code lets you easily debug an application deployed to Cloud Run by leveraging [`skaffold debug`](https://skaffold.dev/docs/workflows/debug). For detailed information, see [Debugging with Skaffold](https://skaffold.dev/docs/workflows/debug/).

You don't need to complete manual setup like setting up port forwarding or injecting language-specific debug arguments. Debugging requires a Cloud Code-ready Cloud Run application that includes a `skaffold.yaml` configuration file and a `launch.json` file of type `cloudcode.cloudrun`.

## Debug your Cloud Run service

To debug your service, follow these steps:

  1. To run your service and attach a debugger session to it, open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run the **Debug on Cloud Run Emulator** command.

  2. In the Run/Debug on Cloud Run Emulator dialog, set the specifications for your configuration:

     * Choose Docker or Buildpacks as your builder and then specify your Dockerfile or Buildpack.
     * (Optional) To specify a Dockerfile target or build arguments, click **Show Advanced Build Settings** and then specify the target or arguments.
     * (Optional) To specify a custom service name, container image URL, container port, identity for the service to use, number of dedicated CPUs, or amount of memory to allocate to each container instance, click **Show Advanced Service Settings** and then specify the values.
     * (Optional) To specify any [environment variables](https://docs.cloud.google.com/code/docs/vscode/develop-service#optional_customizing_your_configuration), click **Show Advanced Service Settings** , click **Environment Variables** , and then specify the values.
     * (Optional) To specify Cloud SQL connections, click **Connections** and then specify one connection per line. 
     * (Optional) To have VS Code reestablish a debugging session after you save a change to your code, check the **Automatically re-build and re-run on changes** checkbox. 

If you want to further customize how your service is run, you can edit [your `launch.json` file](https://docs.cloud.google.com/code/docs/vscode/develop-service#customizing_an_existing_launchjson_configuration) directly.

  3. To begin debugging your service, click **Debug**. 

  4. If prompted, [authenticate your credentials to run and debug an application locally](https://docs.cloud.google.com/code/docs/vscode/install#authenticate_credentials_for_debugging_applications_locally). 

  5. For each debuggable container in your service, confirm or enter the directory in the remote container where the program you'd like to debug is found.

Alternatively, you can press `ESC` to skip debugging a container.

![Remote Root prompt](https://docs.cloud.google.com/static/code/docs/vscode/images/debug-remote-root-prompt.png)

Cloud Code attaches a debug session for each debuggable container in the service.

By default, when you save a change to your application, Cloud Code redeploys your application and sets up a new debug session. You can toggle this feature with the `watch` flag in your project's launch configuration. 

  6. To add a breakpoint, click in the editor margin of the file you're debugging.

Red filled circles signify active breakpoints and gray hollow circles signify disabled breakpoints.

For finer breakpoint control, you can use the Breakpoints section in VS Code's Debug view.

![Breakpoints section in the left hand panel of Debug View that allows adding, removing, and disabling breakpoints](https://docs.cloud.google.com/static/code/docs/vscode/images/cccr-debug-breakpoints.png)

When you send a new request to your service, it pauses at the line you specified.

  7. After your session completes, right-click to use the following commands:

     * **View Logs:** Open the application logs of a specific deployment with the Cloud Code Logs Explorer
     * **Open URL:** Open the application service URL of a specific service in a web browser
  8. If you've turned off watch mode in your launch configuration and you want to make changes to your application and rebuild and redeploy the application, click the Cloud Code status bar and then click **Turn on watch mode**.

  9. If you want to inspect variables and stack info, use the [Debug Sidebar](https://code.visualstudio.com/Docs/editor/debugging). To interact with the debugging session, use the [Debug Console](https://code.visualstudio.com/Docs/editor/debugging#_debug-console-repl) in the bottom pane debugger.

  10. To stop your deployment, click the **Stop** button in the action bar for your current deployment.

![Action bar for Cloud Run deployment](https://docs.cloud.google.com/static/code/docs/vscode/images/action-bar.png)




### Troubleshoot container-building issues

If you're getting the `BUILD_DOCKER_UNKNOWN` error code, this indicates a problem with Docker. To resolve this issue, perform one or more of the following tasks:

  * Restart Docker and try building the container again.

  * If you're still getting the same error after restarting, Docker could be running out of disk space. To learn more about cleaning up unused objects in Docker, see [Prune unused Docker objects](https://docs.docker.com/config/pruning/#prune-unused-docker-objects).

  * Try Docker's [Disk Usage](https://hub.docker.com/extensions/docker/disk-usage-extension) extension to help reclaim space.




## Configuration details

Cloud Code handles the following language-specific configuration details:

### Node.js

Rewriting the entrypoint to invoke:

`node --inspect=localhost:9229`

### Python

Installing the `ptvsd` module using an Init Container and rewriting the entrypoint to invoke:

`python -m ptvsd --host localhost --port 5678`

### Go

Installing the [`dlv` debugger](https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md) using an Init Container and rewriting the entrypoint such that the launched debug session runs with a debug server only (in headless mode), continues the debugged process on start, accepts multiple client connections, and listens at `localhost:56268`:

`dlv exec --headless --continue --accept-multiclient --listen=localhost:56268 --api-version=2, <app> --`

### Java

Adding an environment `JAVA_TOOLS_OPTIONS` with the appropriate Java Debug Wire Protocol (JDWP) configuration such that the JDWP debugging agent listens for a socket connection on port 5005 and allows the VM to begin executing before the debugger is attached:

`jdwp=transport=dt_socket,server=y,suspend=n,address=5005,quiet=y`

### .NET

.NET Core applications are configured to be deployed along with `vsdbg` for VS Code.

If you encounter problems with the automatic configuration, see [Detailed debugger configuration and setup](https://skaffold.dev/docs/workflows/debug/#detailed-debugger-configuration-and-setup) for help troubleshooting.

## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
