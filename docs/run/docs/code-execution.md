---
url: https://docs.cloud.google.com/run/docs/code-execution/
title: Code execution in Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:57.554666+00:00
---

# Code execution in Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/code-execution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Code execution in Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run sandboxes**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Run sandboxes let you execute untrusted code in an isolated environment directly within container workloads. This capability helps AI agents safely run sub-agents, execute computational tasks, or launch automated browsers without risking the host system.

## Key advantages

Cloud Run sandboxes provide the following key advantages:

  * **Fast creation** : Sandboxes are interactive and ready to execute commands almost instantly. By creating sandboxes within an existing Cloud Run resource where your agent runs, you reduce creation times when compared to creating a new Cloud Run resource for every task. This efficiency helps ensure that your agent remains responsive.

  * **Security** : Sandboxes isolate process execution. By default, sandboxes don't have access to the parent workload, environment variables, secrets, or the Google Cloud metadata server. All sandboxes are completely isolated from each other.

  * **Access control and environment** : Processes run with `sudo` privileges as a non-root user, letting you install tools using package managers such as `apt`, `pip`, or `npm` during execution. While the sandbox environment is ephemeral and deleted upon completion, you can use persistent directories or snapshots to save specific workspaces or map data to a Cloud Storage bucket.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Install and initialize](https://docs.cloud.google.com/sdk/docs) the gcloud CLI. 
  7. Deploy a Cloud Run resource, such as a [second generation ](https://docs.cloud.google.com/run/docs/configuring/execution-environments)[service](https://docs.cloud.google.com/run/docs/deploying), [job](https://docs.cloud.google.com/run/docs/create-jobs), [worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools), or [instance](https://docs.cloud.google.com/run/docs/instances/create-and-manage-instances). 



## Enable sandboxes

To use sandboxes, you must first enable them on your Cloud Run resource using the `--sandbox-launcher` flag or `sandboxLauncher` YAML attribute. For detailed configuration steps, choose from the following resource type:

  * [Services](https://docs.cloud.google.com/run/docs/configuring/services/sandboxes)
  * [Jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/sandboxes)
  * [Worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/sandboxes)
  * [Instances](https://docs.cloud.google.com/run/docs/configuring/instances/sandboxes) (Preview)



## Launch sandboxes

Once you enable sandboxes, you can launch sandboxes from within your container execution environment. The sandbox binary is located at `/usr/local/gcp/bin/sandbox`.

The examples in this guide use the `sandbox` command instead of its absolute path `/usr/local/gcp/bin/sandbox`.

You can execute the binary by referencing its absolute path in your source code. For example, to print `Hello` inside your isolated sandbox, choose one of the following options:

###  Node.js 

To execute the sandbox command from a Node.js application, include the following code:
    
    
    exec(`sandbox do -- /bin/echo "Hello"`, (e, stdout, stderr) => {
        res.send({ stdout, stderr });
    });
    

###  Python 

To execute the sandbox command from a Python application, include the following code:
    
    
    import subprocess
    result = subprocess.run(
        ["sandbox", "do", "--", "/bin/echo", "Hello"],
        capture_output=True,
        text=True,
    )
    return {"stdout": result.stdout, "stderr": result.stderr}
    

###  Go 

To execute the sandbox command from a Go application, include the following code:
    
    
    cmd := exec.Command("sandbox", "do", "--", "/bin/echo", "Hello")
    out, err := cmd.CombinedOutput()
    

###  Sandbox CLI 

To execute the sandbox command directly from the command line, run the following command:
    
    
    sandbox do -- /bin/echo "Hello"
    

To see the [complete list of available commands](https://docs.cloud.google.com/run/docs/reference/sandbox-cli), run the `sandbox -h` command.

## Use the sandbox command line capabilities

The `sandbox` command line tool contains commands to run, configure, and manage sandboxes.

### Run a command in your sandbox

You can execute an instruction in a new, ephemeral sandbox using the `sandbox do` command. The `sandbox do` command performs the following tasks:

  1. Spins up a sandbox environment (`sandbox run`).
  2. Executes the command you specify (`sandbox exec`).
  3. Deletes the sandbox after successful execution (`sandbox delete`).



For example, to perform a math calculation inside the sandbox, run the following code snippets for your preferred language. Ensure that any command or tool you run, such as `python3`, is installed in your container image:

###  Node.js 

To execute the sandbox command from a Node.js application:
    
    
    exec(`sandbox do -- /usr/bin/python3 -c "print(1+2)"`, (e, stdout, stderr) => {
        res.send({ stdout, stderr });
    });
    

###  Python 

To execute the sandbox command from a Python application:
    
    
    import subprocess
    result = subprocess.run(
        ["sandbox", "do", "--", "/usr/bin/python3", "-c", "print(1+2)"],
        capture_output=True,
        text=True,
    )
    return {"stdout": result.stdout, "stderr": result.stderr}
    

###  Go 

To execute the sandbox command from a Go application:
    
    
    cmd := exec.Command("sandbox", "do", "--", "/usr/bin/python3", "-c", "print(1+2)")
    out, err := cmd.CombinedOutput()
    

###  Sandbox CLI 

To execute the sandbox command directly from the command line:
    
    
    sandbox do -- /usr/bin/python3 -c "print(1+2)"
    

If you run a command by name without its absolute path, such as `python3` instead of `/usr/bin/python3`, explicitly configure the `PATH` environment variable in the sandbox using the `--env` flag.

### Persist data across different executions

Sandboxes are ephemeral by default. To persist data across different sandbox executions within the same Cloud Run instance, you can import and export workspace file system state using standard `tar` archive files. Alternatively, you can configure bind mounts to share directories directly between the host container and the sandbox environments.

Use the following flags when running the `sandbox do` command:

  * `--export-tar`: Captures modified overlay files into a `tar` archive file upon completion.
  * `--import-tar`: Extracts files from a `tar` archive file into the sandbox before execution.
  * `--sync-tar`: Performs a two-way sync by importing before execution and exporting upon completion.



For example, to pass data between two sandbox calls using archive files, run the following commands:

  1. Write data inside a sandbox and export the state to an archive file:
         
         sandbox do --write --export-tar=/tmp/work.tar \
           -- /usr/bin/bash -c "mkdir -p /tmp/work && echo 'task-complete' > /tmp/work/status.txt"
         

  2. Import the archive file in a subsequent call to retrieve the data:
         
         sandbox do --write --import-tar=/tmp/work.tar \
           -- /usr/bin/bash -c "cat /tmp/work/status.txt"
         




Alternatively, to automatically import existing archive state and export new changes in a single command, use `--sync-tar=/tmp/work.tar`. When a sandbox process terminates, Cloud Run permanently deletes ephemeral overlay files that weren't exported to an archive file.

### Run a command in the background

To run long-running processes, headless browsers, or background servers, such as a background agent loop that continuously listens for incoming requests, use the `--detach` flag.

For example, run the following command to start a detached sandbox with an idle or background program:
    
    
    sandbox run my-web-server --detach -- /usr/bin/long_running_or_idle_program
    

You can use the `detach` flag to reuse the same sandbox for multiple tests. To interact with or run additional commands inside a running detached sandbox, use the `sandbox exec` command and target your sandbox by its name.

For example, to execute a test command inside your existing `my-web-server` background sandbox, run the following command:
    
    
    sandbox exec my-web-server -- /usr/bin/python3 -c "print('test-complete')"
    

### Configure environment variables

Configure [environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables) on sandboxes just like you would any other container. Sandboxes don't inherit environment variables from the host container. You must explicitly provide them using the `--env` flag when running the `sandbox` command.

For example, to pass a configuration variable into a sandbox, run the following command:
    
    
    sandbox do --env AGENT_MODE="test" -- /usr/bin/bash -c "echo \$AGENT_MODE"
    

Avoid passing secrets using the `env` flag as they might be visible to the sandbox processes.

### Create file system snapshots

Deploy a named sandbox in the background to handle continuous tasks like web servers or long-running agent workflows, execute commands against the sandbox dynamically, and capture its modified file system state into a `tar` archive file.

**Tip:** If you run many commands repeatedly on a single sandbox, consider launching a sandbox once, with an idle entrypoint, such as `sleep 12m`, and then running the `sandbox exec` command that targets this sandbox for very fast command execution.

For example, to deploy a background sandbox, write a file to its overlay, and snapshot its state to verify the data was captured, run the following commands:

  1. Deploy a named sandbox in the background with write access enabled, creating a file within its workspace:
         
         sandbox run --write my-sandbox --detach -- /usr/bin/bash -c "echo 'hi' > /tmp/hello.txt && sleep 1h"
         

  2. Create a snapshot of the running sandbox's modified file system using the `sandbox tar` command:
         
         sandbox tar my-sandbox --file=/tmp/foo.tar
         

  3. Extract and verify that the snapshot archive file contains the data written inside the sandbox:
         
         tar -xvf /tmp/foo.tar
         

You should see the following results:
         
         ./
         ./tmp/
         ./tmp/hello.txt
         




### Configure networking

By default, all outbound traffic from the sandbox is blocked. To allow outbound network access, use the `--allow-egress` flag:

For example, to fetch data from an external endpoint, run the following command:
    
    
    sandbox do --allow-egress -- /usr/bin/python3 -c 'import urllib.request; print(urllib.request.urlopen("https://google.com").getcode())'
    

This command returns the standard HTTP status code `200`, indicating a successful connection.

### Access the file system

By default, processes you execute inside the sandbox have read-only access to the host container root file system. You can use the `--write` flag to enable writing to a temporary file system (tmpfs) overlay. However, the writes will be lost when the sandbox is deleted. To enable persistent writing to the host container, you can configure bind mounts.

#### Default read-only access

Inside the sandbox, processes can read files from the host container, and they can't write to the root file system.

The following examples assume you are executing commands from the root directory (`/`) of your host container.

To verify default read-only access, run the following commands:

  1. Create a Python script on the host container:
         
         mkdir -p /tmp/my-scripts
         echo "print('hi')" > /tmp/my-scripts/task.py
         

  2. Verify the file exists locally:
         
         cat /tmp/my-scripts/task.py
         

  3. Execute the file inside your sandbox:
         
         sandbox do -- /usr/bin/python3 /tmp/my-scripts/task.py
         

This command returns `hi`, confirming that the sandbox has read access.

If you attempt to write data directly to the sandbox root file system without additional configuration, the execution fails. For example, attempting to write to `/tmp` inside the default sandbox returns a read-only file system error:

Run the following command to write to the root file system:
         
         sandbox do -- /usr/bin/bash -c "echo 'hi' > /tmp/testfile.txt"
         

The command fails with the following error:
         
         /usr/bin/bash: line 1: /tmp/testfile.txt: Read-only file system
         Error: failed to exec in container: cmd.Wait(exec) failed: exit status 1
         




#### Share data using bind mounts

To allow processes inside the sandbox to write persistable data, attach a shared volume using the `--mount` flag:

  1. Create a shared volume directory on the host container and seed it with an initial file:
         
         mkdir -p /tmp/my-volume
         echo 'read' > /tmp/my-volume/readwrite.txt
         

  2. Execute the sandbox to read the file from the bind mount path:
         
         sandbox do --mount type=bind,source=/tmp/my-volume,destination=/mnt/my-mount -- /usr/bin/bash -c "cat /mnt/my-mount/readwrite.txt"
         

This command returns `read`.

  3. Execute the sandbox to write new data back to the host from inside the mount:
         
         sandbox do --mount type=bind,source=/tmp/my-volume,destination=/mnt/my-mount -- /usr/bin/bash -c "echo 'write' > /mnt/my-mount/readwrite.txt"
         

  4. Verify on the host container that the sandbox successfully modified the file:
         
         cat /tmp/my-volume/readwrite.txt
         

This command returns `write`.




#### Configure read-only mounts

To grant the sandbox access to a host directory while explicitly preventing it from modifying files, append the `readonly` attribute to the mount specification.

For example, run the following command to test write restrictions on a read-only bind mount:
    
    
    sandbox do --mount type=bind,source=/tmp/my-volume,destination=/mnt/my-mount,readonly -- /usr/bin/bash -c "echo 'fails' > /mnt/my-mount/hello.txt"
    

The write attempt fails with the following error:
    
    
    /usr/bin/bash: line 1: /mnt/my-mount/hello.txt: Read-only file system
    Error: failed to exec in container: cmd.Wait(exec) failed: exit status 1
    

### View logs

Cloud Run automatically captures sandbox lifecycle events, such as execution starts and exits, in Cloud Logging.

The `sandbox` CLI writes standard output (`stdout`) and standard error (`stderr`) from sandboxed commands directly to the standard streams of the invoking process. To view these logs in Cloud Logging, route the streams to your container's standard output and standard error:

###  Node.js 
    
    
    const { exec } = require('child_process');
    const child = exec('sandbox do -- /usr/bin/python3 -c "print(1+2)"');
    child.stdout.pipe(process.stdout);
    child.stderr.pipe(process.stderr);
    

###  Python 
    
    
    subprocess.run(
        ["sandbox", "do", "--", "/usr/bin/python3", "-c", "print(1+2)"],
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
    

###  Go 
    
    
    cmd := exec.Command("sandbox", "do", "--", "/usr/bin/python3", "-c", "print(1+2)")
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    cmd.Run()
    

## What's next

  * Learn more about [hosting AI agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
  * Explore [browser and OS automation in Cloud Run](https://docs.cloud.google.com/run/docs/browser-automation).
  * Review the [container runtime contract](https://docs.cloud.google.com/run/docs/container-contract).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
