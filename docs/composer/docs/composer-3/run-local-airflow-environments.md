---
url: https://docs.cloud.google.com/composer/docs/composer-3/run-local-airflow-environments/
title: Run a local Airflow environment with Composer Local Development CLI tool \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:26.258830+00:00
---

# Run a local Airflow environment with Composer Local Development CLI tool  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/run-local-airflow-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Run a local Airflow environment with Composer Local Development CLI tool Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/run-local-airflow-environments "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

This section describes how to create, configure, and run a local Airflow environment using Composer Local Development CLI tool.

If you want to run a Managed Airflow environment for development purposes instead, consider creating a [development mode](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#development-mode) environment, which you can hibernate when you're not using it.

## About Composer Local Development CLI tool

Composer Local Development CLI tool streamlines Apache Airflow DAG development for Managed Airflow by running an Airflow environment locally. This local Airflow environment uses a Airflow build image used by a specific [Managed Airflow version](https://docs.cloud.google.com/composer/docs/composer-versions).

You can create a local Airflow environment based on an existing Managed Airflow environment. In this case, the local Airflow environment takes the list of installed PyPI packages and environment variable names from your Managed Airflow environment.

You can use this local Airflow environment for testing and development purposes, such as to test new DAG code, PyPI packages, or Airflow configuration options.

**Warning:** Use local Airflow environments **only for testing and development purposes**. Managed Airflow does not support using locally deployed Airflow build images for production purposes.

## Before you begin

  * Composer Local Development CLI tool supports Airflow 3 builds as follows:

    * Airflow 3.3.1 and later versions are supported starting from composer-3-airflow-3.3.1-build.0.
    * Airflow 3.2.2 is supported starting from composer-3-airflow-3.2.2-build.3.
    * Airflow 3.1.8 is not supported.
    * Earlier Airflow 3 builds are supported starting from composer-3-airflow-3.1.0-build.8.


  * Composer Local Development CLI tool creates local Airflow environments in a directory where you run the `composer-dev create` command. To access your local Airflow environment later, run the tool commands in the path where you initially created the local environment. All data for the local environment is stored in a subdirectory at the path where you created the local environment: `./composer/<local_environment_name>`.

  * Your computer must have enough disk space to store Airflow build images. Composer Local Development CLI tool stores one image file for each Airflow build. For example, if you have two local Airflow environments with different Airflow builds, then Composer Local Development CLI tool stores two Airflow build images.

  * Composer Local Development CLI tool uses colorized output. You can disable colorized output with the `NO_COLOR=1` variable: `NO_COLOR=1 composer-dev <other commands>`.

  * If you have only one local environment, you can omit the local environment's name from all `composer-dev` commands, except the `run-airflow-cmd`.

  * Install Composer Local Development CLI tool dependencies:

    * Python versions from 3.8 to 3.11 with `pip`
    * [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install)
  * Docker ([Linux/macOS/Windows](https://www.docker.com/get-started/)) or Podman ([Linux](https://podman.io/docs/installation) or [Windows](https://podman.io/docs/installation#windows)) must be installed and running on your computer. 

To verify that Docker or Podman is running, run any Docker CLI or Podman CLI command, such as `docker ps` or `podman ps`. All of the instructions apply to both Docker and Podman unless specified otherwise, and any Docker commands can be replaced by equivalent Podman commands.




## Configure credentials

If not already done, [get new user credentials to use for Application Default Credentials](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login):
    
    
    gcloud auth application-default login
    

Login in gcloud CLI using your Google account:
    
    
    gcloud auth login
    

All API calls done by the Composer Local Development CLI tool and DAGs are executed from the account that you use in gcloud CLI. For example, if a DAG in your local Airflow environment reads contents of a Cloud Storage bucket, then this account must have permissions to access the bucket. This is different from Managed Airflow environments, where an environment's service account makes the calls.

## Install Composer Local Development CLI tool

Clone the Composer Local Development CLI repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/composer-local-dev.git
    

In the top-level directory of the cloned repository, run:
    
    
    pip install .
    

Depending on your `pip` configuration, the path at which the tool is installed might not be in `PATH` variable. If this is the case, `pip` displays a warning message. You can use information from this warning message to add this directory to the `PATH` variable in your operating system.

## (Podman) Configure Podman

If you're using Podman, follow these steps to configure it:

###  Linux 

  1. Enable the Podman user service socket.

The `composer-dev` CLI communicates through standard Docker API calls. You must activate Podman's background service socket wrapper at the user level to mimic the Docker daemon.

First, verify if the user-level socket is already active:
         
         systemctl --user is-active podman.socket
         

If the command returns `inactive` or `failed`, enable and start the socket:
         
         # Enable and start Podman's user-level systemd socket
         systemctl --user enable --now podman.socket
         

  2. Configure environment variables for Podman.

Add the following command to your shell configuration file (such as `.bashrc` or `.zshrc`):
         
         export DOCKER_HOST="unix:///run/user/$UID/podman/podman.sock"
         




###  Windows 

  1. Set WSL 2 configuration (`.wslconfig`). Before initializing your Podman machine, check that WSL 2 has a defined memory and swap boundary. Without it, multi-container deployments can cause memory spikes during image extraction. It is also important to set a restriction for concurrent downloads limit.

Change or create the `%USERPROFILE%\.wslconfig` file:
         
         [wsl2]
         memory=4GB
         swap=2GB
         
         [registry]
         max_concurrent_downloads = 2
         

  2. In PowerShell, initialize the Podman machine:
         
         podman machine init
         

  3. Start the machine:
         
         podman machine start
         




After you perform these steps, you can work with composer-dev CLI commands. The tool automatically detects your Podman environment on Windows and adapt the architecture mappings.

## Create a local Airflow environment with a Airflow build image

To list available Airflow build images, run:
    
    
    composer-dev list-available-versions --include-past-releases --limit 10
    

To create a local Airflow environment with default parameters, run:
    
    
    composer-dev create \
      --from-image-version IMAGE_VERSION \
      LOCAL_ENVIRONMENT_NAME
    

Other parameters:
    
    
    composer-dev create LOCAL_ENVIRONMENT_NAME \
      --from-image-version IMAGE_VERSION \
      --project PROJECT_ID \
      --port WEB_SERVER_PORT \
      --dags-path LOCAL_DAGS_PATH \
      --plugins-path LOCAL_PLUGINS_PATH \
      --database DATABASE_ENGINE \
      --editable-dependencies EDITABLE_DEPENDENCY_PATH
    

Replace:

  * `LOCAL_ENVIRONMENT_NAME` with the name of this local Airflow environment.
  * `IMAGE_VERSION` with the name of the [Airflow build image](https://docs.cloud.google.com/composer/docs/composer-versions).
  * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * `WEB_SERVER_PORT` with the port that Airflow web server must listen at.
  * `LOCAL_DAGS_PATH` with the path to a local directory where the DAG files are located.
  * `LOCAL_PLUGINS_PATH` with the path to a local directory where the plugin files are located.
  * `DATABASE_ENGINE` with the database engine to use. Possible values are `postgresql` (default) and `sqlite`.

**Note:** If you want to use `LocalExecutor` as Airflow's Core Executor, set `DATABASE_ENGINE` to `postgresql`. This is required for the `LocalExecutor` to work properly.
  * _(Linux/macOS only)_ `EDITABLE_DEPENDENCY_PATH` with the path to a local directory containing a Python package to install in editable mode. This argument isn't supported in Windows.

Paths can be absolute or relative (relative paths are resolved against the current working directory). This directory must be accessible by the container engine.

To specify multiple editable packages, repeat the option. Example: `--editable-dependencies ./pkg1 --editable-dependencies ./pkg2`.

Installing the packages with `pip install -e` immediately applies changes to these packages inside the project.




Example:
    
    
    composer-dev create \
      --from-image-version composer-3-airflow-2.11.1-build.20 \
      example-local-environment
    

## Create a local Airflow environment from a Managed Airflow environment

**Caution:** Composer Local Development CLI tool **does not produce a local copy of your Managed Airflow environment**.

Only the following information is taken from a Managed Airflow environment:

  * Specific Airflow build that is used by your environment. 

  * List of [custom PyPI packages](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies) installed in your environment. 

  * Commented list of names of [environment variables](https://docs.cloud.google.com/composer/docs/composer-3/set-environment-variables) set in your environment.

**Important:** Managed Airflow **does not copy the values** of environment variables. You can manually uncomment environment variables in the configuration file and set their values, as required.



Other information and configuration parameters from the environment, such as DAG files, DAG run history, Airflow variables, and connections, are not copied from your Managed Airflow environment.

To create a local Airflow environment from an existing Managed Airflow environment:
    
    
    composer-dev create LOCAL_ENVIRONMENT_NAME \
        --from-source-environment ENVIRONMENT_NAME \
        --location LOCATION \
        --project PROJECT_ID \
        --port WEB_SERVER_PORT \
        --dags-path LOCAL_DAGS_PATH \
        --plugins-path LOCAL_PLUGINS_PATH \
        --database DATABASE_ENGINE \
        --editable-dependencies EDITABLE_DEPENDENCY_PATH
    

Replace:

  * `LOCAL_ENVIRONMENT_NAME` with a name for the local Airflow environment.
  * `ENVIRONMENT_NAME` with the name of the Managed Airflow environment.
  * `LOCATION` with the region where the Managed Airflow environment is located.
  * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * `WEB_SERVER_PORT` with a port for the local Airflow web server.
  * `LOCAL_DAGS_PATH` with a path to a local directory where the DAGs are located.
  * `LOCAL_PLUGINS_PATH` with the path to a local directory where the plugins files are located.
  * `DATABASE_ENGINE` with the database engine to use. Possible values are `postgresql` (default) and `sqlite`.

**Note:** If you want to use `LocalExecutor` as Airflow's Core Executor, set `DATABASE_ENGINE` to `postgresql`. This is required for the `LocalExecutor` to work properly.
  * _(Linux/macOS only)_ `EDITABLE_DEPENDENCY_PATH` with the path to a local directory containing a Python package to install in editable mode. This argument isn't supported in Windows.

Paths can be absolute or relative (relative paths are resolved against the current working directory). This directory must be accessible by the container engine.

To specify multiple editable packages, repeat the option. Example: `--editable-dependencies ./pkg1 --editable-dependencies ./pkg2`.

Installing the packages with `pip install -e` immediately applies changes to these packages inside the project.




Example:
    
    
    composer-dev create example-local-environment \
      --from-source-environment example-environment \
      --location us-central1 \
      --project example-project \
      --port 8081 \
      --dags-path ./example_directory/dags \
      --plugins-path ./example_directory/plugins \
      --database postgresql \
      --editable-dependencies ./pkg1
    

## Start a local Airflow environment

To start a local Airflow environment, run:
    
    
    composer-dev start LOCAL_ENVIRONMENT_NAME
    

Replace:

  * `LOCAL_ENVIRONMENT_NAME` with the name of a local Airflow environment.



## Stop or restart a local Airflow environment

When you restart a local Airflow environment, Composer Local Development CLI tool restarts the Docker container where the environment runs. All Airflow components are stopped and started again. As a result, all DAG runs that are executed during a restart are marked as failed .

To restart or start a stopped local Airflow environment, run:
    
    
    composer-dev restart LOCAL_ENVIRONMENT_NAME
    

Replace:

  * `LOCAL_ENVIRONMENT_NAME` with the name of a local Airflow environment.



To stop a local Airflow environment, run:
    
    
    composer-dev stop LOCAL_ENVIRONMENT_NAME
    

**Note:** The `stop` command does not delete the local Airflow environment.

## Add and update DAGs

Dags are stored in the directory that you specified in the `--dags-path` parameter when you created your local Airflow environment. By default, this directory is `./composer/<local_environment_name>/dags`. You can get the directory used by your environment with the `describe` command.

To add and update DAGs, change files in this directory. You do not need to restart your local Airflow environment.

## View local Airflow environment logs

You can view recent logs from a Docker container that runs your local Airflow environment. In this way, you can monitor container-related events and check Airflow logs for errors such as dependency conflicts caused by PyPI packages installation.

**Note:** Composer Local Development CLI tool does not write DAG run and task logs to files. You can view these logs in the Airflow UI of your local Airflow environment.

To view logs from a Docker container that runs your local Airflow environment, run:
    
    
    composer-dev logs LOCAL_ENVIRONMENT_NAME --max-lines 10
    

To follow the log stream, omit the `--max-lines` argument:
    
    
    composer-dev logs LOCAL_ENVIRONMENT_NAME
    

## Run an Airflow CLI command

You can run [Airflow CLI commands](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html) in your local Airflow environment.

**Note:** The command syntax is different from [Google Cloud CLI syntax for Airflow CLI commands](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli).

To run an Airflow CLI command:
    
    
    composer-dev run-airflow-cmd LOCAL_ENVIRONMENT_NAME \
      SUBCOMMAND SUBCOMMAND_ARGUMENTS
    

Example:
    
    
    composer-dev run-airflow-cmd example-local-environment dags list -o table
    

## Configure local Airflow environments

Composer Local Development CLI tool stores configuration parameters for a local Airflow environment, such as environment variables and PyPI package requirements in the local environment's directory (`./composer/<local_environment_name>`).

Configuration is applied when a local Airflow environment is started. For example, if you add conflicting PyPI package requirements, then Composer Local Development CLI tool reports errors when you start the local environment.

**Important:** Composer Local Development CLI tool does not store the `airflow.cfg` file in this directory. This file is located in the Docker image of the environment. You can change Airflow configuration options by configuring environment variables.

Airflow connections are stored in the database of the local Airflow environment. You can configure them by running an Airflow CLI command or by storing the connection parameters in environment variables. For more information about ways to create and configure connections, see [Managing connections](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html) in the Airflow documentation.

### Get a list and status of local Airflow environments

To list all available local Airflow environments and display their status:
    
    
    composer-dev list
    

To describe a specific environment, and get details such as image version, DAGs path, and web server URL of an environment:
    
    
    composer-dev describe LOCAL_ENVIRONMENT_NAME
    

Replace:

  * `LOCAL_ENVIRONMENT_NAME` with the name of the local Airflow environment.



### List images used by local Airflow environments

To list all images used by Composer Local Development CLI tool, run:
    
    
    docker images --filter=reference='*/cloud-airflow-releaser/*/*'
    

### Install plugins and change data

Plugins and data for a local Airflow environment are taken from the local environment's directory: `./composer/<local_environment_name>/data` and `./composer/<local_environment_name>/plugins`).

To change the contents of `/data` and `/plugins` directories, add or remove files in these directories. Docker automatically propagates file changes to your local Airflow environment.

Composer Local Development CLI tool does not support specifying a different directory for data and plugins.

### Configure environment variables

To configure [environment variables](https://docs.cloud.google.com/composer/docs/composer-3/set-environment-variables), edit the `variables.env` file in the environment directory: `./composer/<local_environment_name>/variables.env`.

**Caution:** As a safety measure, values of environment variables are not copied from your Managed Airflow environment, and the list of variable names is commented. For example, you might want to specify different values so that your DAGs do not interact with your production environments, or to omit setting some of the variables.

The `variables.env` file must contain key-value definitions, one line for each environment variable. To change Airflow configuration options, use the `AIRFLOW__SECTION__KEY` format. For more information about the available environment variables, see [Airflow configuration reference](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html).
    
    
    EXAMPLE_VARIABLE=True
    ANOTHER_VARIABLE=test
    AIRFLOW__WEBSERVER__DAG_DEFAULT_VIEW=graph
    

To apply the changes, restart your local Airflow environment.

### Install or remove PyPI packages

To install or remove PyPI packages, modify the `requirements.txt` file in the environment directory: `./composer/<local_environment_name>/requirements.txt`.

Requirements must follow the format specified in [PEP-508](https://www.python.org/dev/peps/pep-0508/#grammar) where each requirement is specified in lowercase and consists of the package name with optional extras and version specifiers.

To apply the changes, restart your local Airflow environment.

### Switch to a different Airflow build image

You can use any Airflow build image with Composer Local Development CLI tool and switch between the images. This approach is different from [upgrading](https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments) your Managed Airflow environment, because configuration parameters of your local Airflow environment are applied when it starts.

For example, after a new Airflow build is released, you can switch your environment to use it, and keep existing local Airflow environment configuration. 

To change the environment's image used by your local Airflow environment:

  1. Edit the local environment configuration file: `./composer/<local_environment_name>/config.json`.

  2. Change the value of the `composer_image_version` parameter. To view available values, you can list available images.

  3. To apply the changes, restart your local Airflow environment.




### Delete a local Airflow environment

**Caution:** Make sure that you saved all required data from the environment, such as logs and configuration.

To delete a a local Airflow environment, run the following command:
    
    
    composer-dev remove LOCAL_ENVIRONMENT_NAME
    

If the environment is running, add the `--force` flag to force its removal.

### Delete Docker images

To delete all images downloaded by Composer Local Development CLI tool, run:
    
    
    docker rmi $(docker images --filter=reference='*/cloud-airflow-releaser/*/*' -q)
    

## Extra configuration and troubleshooting

This section provides solutions to common issues and extra configuration steps for configuring interaction of Composer Local Development CLI tool with other tools and services.

### Shell tab completion

The `composer-dev` CLI supports tab completion for Bash, Zsh, and Fish shells. You can use tab completion to discover available subcommands and options without consulting the help text.

###  Zsh 

Generate the completion script and source it in your `~/.zshrc`:
    
    
    _COMPOSER_DEV_COMPLETE=zsh_source composer-dev > ~/.composer-dev-complete.zsh
    

Then add it to your `~/.zshrc`:
    
    
    echo 'source ~/.composer-dev-complete.zsh' >> ~/.zshrc
    

###  Bash 

Generate the completion script and source it in your `~/.bashrc`:
    
    
    _COMPOSER_DEV_COMPLETE=bash_source composer-dev > ~/.composer-dev-complete.bash
    

Then add it to your `~/.bashrc`:
    
    
    echo 'source ~/.composer-dev-complete.bash' >> ~/.bashrc
    

###  Fish 

Generate the completion script and save it to the Fish completions directory:
    
    
    _COMPOSER_DEV_COMPLETE=fish_source composer-dev > ~/.config/fish/completions/composer-dev.fish
    

### Interacting with Kubernetes clusters

By default, the file `~/.kube/config` is not mounted. You can specify path to Kubernetes configuration file by exporting `KUBECONFIG` environment variable before starting environment.
    
    
    export KUBECONFIG=~/.kube/config
    

### Interacting with other services on the host machine

The `localhost` in a Managed Airflow environment is pointing to the container itself, not the host machine because of how network works on Docker or Podman containers. For convenience, composer-dev CLI tool configures the container's network to access the machine through the `host.docker.internal` domain alias. Examples:

  * Redis: Use `host.docker.internal:6379` instead of `localhost:6379` if `Redis` is running on port `6379`.
  * PostgreSQL: Use `host.docker.internal:25432` instead of `localhost:25432` if `PostgreSQL` is running on port `25432`.
  * Any other service: Follow this pattern: `host.docker.internal:<PORT>`

**Note:** If you are running your target service inside another docker container make sure that the port is also exposed to the host machine.

### Unable to start a local environment on macOS

If you installed the `composer-dev` package to a directory where Docker cannot access it, then your local environment might not start.

For example, if Python is installed in the `/opt` directory, such as when you install it with default Homebrew configuration on macOS, then the `composer-dev` package is also installed in the `/opt` directory. Because Docker complies with Apple's sandbox rules, the `/opt` directory isn't available by default. In addition, you cannot add it through the UI (Settings > Resources > File sharing).

In this case, Composer Local Development CLI tool generates an error message that is similar to the following example:
    
    
    Failed to create container with an error: 400 Client Error for ...
    Bad Request ("invalid mount config for type "bind": bind source path does not exist:
    /opt/homebrew/lib/python3.9/site-packages/composer_local_dev/docker_files/entrypoint.sh
    
    Possible reason is that composer-dev was installed in the path that is
    not available to Docker. See...")
    

You can use one of the following solutions:

  * Install Python or the `composer-dev` package to a different directory, so that Docker can access the package.
  * Manually edit the `~/Library/Group\ Containers/group.com.docker/settings.json` file and add `/opt` to `filesharingDirectories`.



### Container user access to mounted files and directories from the host

By default, the Managed Airflow environment's container runs as the `airflow` user with UID `999`. The user must have access to files and directories mounted from the host, for example `~/.config/gcloud/application_default_credentials.json`.

Known issues:

  * `google.auth.exceptions.DefaultCredentialsError: Your default credentials were not found`: can be generated when running the container with the default user `airflow (999)` and the host directory `~/.config/gcloud/` is missing the execute permission for the user.
  * `[Errno 13] Permission denied: '/home/airflow/.config/gcloud/application_default_credentials.json'`: can be generated when you are running the container with the default user `airflow (999)` and the host file `~/.config/gcloud/application_default_credentials.json` is missing the read permission for the user.



On Linux or macOS, it's recommended that you run the container as the current host user by adding `COMPOSER_CONTAINER_RUN_AS_HOST_USER=True` to `composer/<LOCAL_ENVIRONMENT_NAME>/variables.env`.This feature isn't available on Windows, so you might need to update the permissions of the mounted files and directories on the host to allow access by the user inside of the container.

### (Podman) Fix permission or lchown errors for corporate users

To prevent rootless Podman from auto-allocating user namespaces that overlap with your primary corporate user ID (causing `lchown: invalid argument` or permission errors), you must manually push your subordinate ranges above the 4-million block.

  1. Open `/etc/subuid` and `/etc/subgid` with root privileges (for example: `sudo nano /etc/subuid`).

  2. Update or add your username entry to look exactly like this:
         
         YOUR_USERNAME:4000000:3000000
         

  3. Save both files and run the following to apply the new namespace mapping rules to Podman:
         
         podman system migrate
         




### (Podman) Remove stuck files and permission denied errors

If you updated your subuid ranges while old containers existed, then your current namespace will be blocked from accessing its own data cache.

**Warning:** Running the following command will **remove all your volumes**. Proceed with caution if you have other work stored.

Force-clear the local storage graph using host-level root privileges:
    
    
    podman rm -fa
    podman volume rm --all --force
    podman system migrate
    

### (Podman) Fix DNS Failures ("Name or service not known")

If your Airflow container generates a `psycopg2.OperationalError` stating it cannot translate or resolve the hostname for the database container (`your-environment-name`), then Podman's internal virtual bridge network is out of sync.

Flush the runtime states and force `netavark` and `aardvark-dns` to regenerate clean routing tables.

**Warning:** The following commands **will remove all networks**. Proceed with caution if you have other work stored.
    
    
    podman rm -fa
    podman network prune --force
    
    rm -rf /run/user/$UID/containers/*
    rm -rf /run/user/$UID/netavark/*
    rm -rf COMPOSER_LOCAL_DEV_PATH/composer/*
    
    podman system migrate
    

### (Podman) Verify your engine status

To verify that Podman is managing your workflow rootless and isn't bypassing your configuration into system Docker:

  1. Verify network DNS backend:
         
         podman info | grep -A 3 -i "dns"
         

The output must contain `backend: netavark` and a valid executable path to `aardvark-dns`.

  2. Verify process ownership mapping. With your environment running, check the host process owner:
         
         ps -ef | grep -i "postgres"
         

The leftmost column should display a high UID number (such as `4000069`) corresponding to your subuid map range, proving that it is running entirely rootless.




### (Podman, Windows) Fix pipe errors during deployment

If the database or Airflow container exits immediately with pipe errors during deployment, then Podman might be hitting a memory limit. To fix it, you can try increasing memory and swap limits in the `.wslconfig` file:

  1. Stop your Podman machine and WSL 2 virtual machine by running the following command in PowerShell:
         
         podman machine stop
         wsl --shutdown
         

  2. Make changes in the `%USERPROFILE%\.wslconfig` file to adapt your swap and memory limits. For reference, see [WSL config reference](https://learn.microsoft.com/en-us/windows/wsl/wsl-config).

  3. Start your Podman machine by running:
         
         podman machine start
         




If you encounter errors, you can try hard-resetting the Windows virtualization and networking stack. To do it, open PowerShell as an Administrator and run:
    
    
    Restart-Service -Name vmms -Force
    Restart-Service -Name hns -Force
    wsl --shutdown
    

## What's next

  * [Write DAGs](https://docs.cloud.google.com/composer/docs/composer-3/write-dags)
  * [Test, synchronize, and deploy your DAGs from GitHub](https://docs.cloud.google.com/composer/docs/composer-3/dag-cicd-github)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
