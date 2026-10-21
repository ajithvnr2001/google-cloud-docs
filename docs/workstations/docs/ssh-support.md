---
url: https://docs.cloud.google.com/workstations/docs/ssh-support/
title: SSH support \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:06.984704+00:00
---

# SSH support  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/ssh-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  SSH support Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the `gcloud` CLI to connect to your workstation from a local machine using SSH (or any other TCP protocol).

Cloud Workstations uses a tunnel to forward TCP traffic between a port on your local machine and a port on your workstation without openly exposing your workstation to the internet. Connections are authenticated using credentials from the `gcloud` CLI and authorized according to the target workstation's IAM policies.

Once the TCP tunnel is established between your local port and the workstation, you can use it to forward traffic from an SSH client, curl, or any other application that uses TCP.

For convenience, Cloud Workstations provides the [`gcloud workstations ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/ssh) command, which establishes the TCP tunnel and runs an SSH client with a single `gcloud` CLI command.

For all other use cases, use the [`gcloud workstations start-tcp-tunnel`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel) command to establish the TCP tunnel and run the application that will use the tunnel (for example, `curl`) in a separate terminal.

**Note:** All preconfigured Cloud Workstations images include an SSH server that runs on workstation port `22`.

## Before you begin

  1. If you don't already have a workstation to connect to, [set up a workstation](https://docs.cloud.google.com/workstations/docs/quickstart-set-up-workstations-console).

  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the `gcloud` CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. Make sure that you have the [Cloud Workstations User](https://docs.cloud.google.com/workstations/docs/access-control#workstations-user) IAM role on the workstation you will connect to.

[ Go to IAM](https://console.cloud.google.com/iam-admin/iam)




## Connect to your workstation using SSH

To establish a secure SSH connection to your workstation, use the [`gcloud workstations ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/ssh) command, which starts a TCP tunnel and runs an SSH client.

Run the following command in a local terminal window:
    
    
    gcloud workstations ssh \
        --project=PROJECT_ID \
        --region=REGION \
        --cluster=CLUSTER_NAME \
        --config=CONFIG_NAME  \
        --port=WORKSTATION_PORT  \
        --local-host-port=localhost:LOCAL_PORT  \
        WORKSTATION_NAME
    

Replace the following values:

  * `PROJECT_ID`: the Google Cloud project ID for the project containing the workstation. If omitted, the current project is used.

  * `REGION`: the region where the workstation's cluster is located—for example, `us-central1`.

  * `CLUSTER_NAME`: the name of the workstation cluster containing the workstation.

  * `CONFIG_NAME`: the name of the workstation configuration containing this workstations.

  * `WORKSTATION_PORT` (Optional): the port on the workstation to which traffic should be sent. If omitted, traffic will be sent to port `22`. All preconfigured Cloud Workstations images include an SSH server that runs on workstation port `22`.

  * `LOCAL_PORT` (Optional): the localhost port from which traffic will be sent. Valid port numbers are `1024` to `65535`. If you omit the `--local-host-port` flag or specify a port of `0` an unused port is selected automatically.

  * `WORKSTATION_NAME`: the name of the workstation.




### SSH configuration and the `.ssh/config` file

When you use `gcloud workstations ssh`, the command routes your connection through `localhost`. As a result, it doesn't automatically apply `Host` entries from your `~/.ssh/config` file that use the workstation's name.

To apply custom SSH configurations, choose one of the following options:

#### Option 1: Pass flags on the command line

You can pass SSH options directly to the underlying SSH client by appending them after a double-dash (`--`):
    
    
    gcloud workstations ssh \
        --project=PROJECT_ID \
        --region=REGION \
        --cluster=CLUSTER_NAME \
        --config=CONFIG_NAME \
        WORKSTATION_NAME \
        -- -o SSH_OPTION=VALUE
    

#### Option 2: Use a persistent TCP tunnel and `.ssh/config`

If you prefer to use your `~/.ssh/config` file:

  1. Start a persistent TCP tunnel in a separate terminal window and specify a local port:
         
         gcloud workstations start-tcp-tunnel \
             --project=PROJECT_ID \
             --region=REGION \
             --cluster=CLUSTER_NAME \
             --config=CONFIG_NAME \
             --local-host-port=localhost:LOCAL_PORT \
             WORKSTATION_NAME \
             22
         

  2. Add a configuration block to your `~/.ssh/config` file on your local machine:
         
         Host WORKSTATION_NAME
             HostName localhost
             Port LOCAL_PORT
             User user
             # Disable host key checking for ephemeral cloud workstations
             StrictHostKeyChecking no
             UserKnownHostsFile /dev/null
             # Add any other SSH options here
         

  3. Connect to your workstation using standard SSH:
         
         ssh WORKSTATION_NAME
         




## Use a TCP tunnel to forward arbitrary TCP traffic to your workstation

To connect to a workstation using a TCP application other than `ssh`, use the [`gcloud workstations start-tcp-tunnel`](https://cloud.google.com/sdk/gcloud/reference/workstations/start-tcp-tunnel) command:

  1. Run the following `gcloud` CLI command to create an authenticated TCP tunnel.

To copy the command to the copy-paste buffer, click content_copy **Copy code sample** and then paste the command into a local terminal window:
         
         gcloud workstations start-tcp-tunnel \
             --project=PROJECT_ID \
             --region=REGION \
             --cluster=CLUSTER_NAME \
             --config=CONFIG_NAME \
             --local-host-port=localhost:LOCAL_PORT \
             WORKSTATION_NAME \
             WORKSTATION_PORT
         

Replace the following values:

     * `PROJECT_ID`: the Google Cloud project ID for the project containing the workstation. If omitted, the current project is used.

     * `REGION`: the region where the workstation's cluster is located—for example, `us-central1`.

     * `CLUSTER_NAME`: the name of the workstation cluster containing the workstation.

     * `CONFIG_NAME`: the name of the workstation configuration containing this workstations.

     * `LOCAL_PORT` (Optional): the localhost port from which traffic will be sent. Valid port numbers are `1024` to `65535`. If you omit the `--local-host-port` flag or specify a port of `0` an unused port is selected automatically.

     * `WORKSTATION_NAME`: the name of the workstation.

     * `WORKSTATION_PORT`: the workstation port to which traffic should be sent. [Preconfigured Cloud Workstations images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) include an SSH server that runs on workstation port `22`.

  2. The `gcloud` CLI command performs a connectivity test with the workstation, opens a tunnel, and then displays a port number:
         
         Listening on port [LOCAL_PORT].
         

All traffic sent to `localhost:LOCAL_PORT` is forwarded to the workstation. The port is only accessible by applications running on your local computer.

  3. Leave the `gcloud` CLI running and open another terminal to run the application that connects to your workstation.

For example, if you are running a server on your workstation that serves port WORKSTATION_PORT, and in the previous step you created a TCP tunnel that forwards traffic between your local port LOCAL_PORT and the workstation port WORKSTATION_PORT, you could run `curl` on your local machine to connect to the server on your workstation:
         
         curl localhost:LOCAL_PORT
         Hello, world!
         

  4. When you are finished, return to the terminal where you started the TCP tunnel and interrupt the `gcloud` CLI by pressing `Control+C`.




## Use SSH servers on different ports

[Custom container images](https://docs.cloud.google.com/workstations/docs/custom-container-images) can also use SSH servers on any port. To support connections from the `gcloud` CLI tunnel, you must configure custom SSH servers to allow password authentication and set the target user with an empty password. Cloud Workstations uses [Cloud IAM](https://docs.cloud.google.com/iam/docs/overview) to help ensure that only authorized traffic is sent to the SSH server.

## Keep SSH sessions persistent

If your network connection drops, your SSH session disconnects. To keep your processes running while disconnected and reattach to your session later, use a tool like `tmux`.

To install `tmux` on your workstation:

  1. Install `tmux` manually in your current session to use it immediately:
         
         sudo apt update
         sudo apt install -y tmux
         

  2. Configure your workstation to install `tmux` on startup. Create or append to the `/home/user/.workstation/customize_environment` file to include the following commands:
         
         #!/bin/bash
         sudo apt update
         sudo apt install -y tmux
         

For more information, see [Customize an existing workstation image without extending it](https://docs.cloud.google.com/workstations/docs/customize-container-images#customize-without-extending-image).

  3. Make the file executable so it runs when the workstation starts:
         
         chmod +x /home/user/.workstation/customize_environment
         




Once `tmux` is installed:

  1. Connect to your workstation:
         
         gcloud workstations ssh \
             --project=PROJECT_ID \
             --region=REGION \
             --cluster=CLUSTER_NAME \
             --config=CONFIG_NAME \
             WORKSTATION_NAME
         

  2. Start a new tmux session from your workstation:
         
         tmux
         

  3. If your connection drops, reconnect and attach to your session by running the following command from your local terminal:
         
         gcloud workstations ssh \
             --project=PROJECT_ID \
             --region=REGION \
             --cluster=CLUSTER_NAME \
             --config=CONFIG_NAME \
             WORKSTATION_NAME \
             -- -t tmux attach
         




## What's next

  * [Set container environment variables in SSH sessions](https://docs.cloud.google.com/workstations/docs/customize-container-images#container_image_that_sets_container_environment_variables_in_ssh_sessions) for custom container images
  * [Enable X11 forwarding](https://docs.cloud.google.com/workstations/docs/customize-container-images#container_image_that_enables_x11_forwarding_for_ssh_sessions) for custom container images



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
