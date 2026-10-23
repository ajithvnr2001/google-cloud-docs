---
url: https://docs.cloud.google.com/storage/docs/gsutil_install/
title: Install gsutil \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:38.094981+00:00
---

# Install gsutil  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/gsutil_install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Install gsutil Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** gsutil is not the recommended CLI for Cloud Storage. [Use `gcloud storage`](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud) commands in the Google Cloud CLI instead.**Important:** After March 2027, gsutil will no longer be available as part of the Google Cloud CLI installation package. gsutil will only be distributed as a standalone tool that can be installed by using PyPI. We recommend that you migrate to using `gcloud storage` commands in the Google Cloud CLI instead of using gsutil. However, if you want to continue using gsutil with your existing scripts and receiving updates for gsutil, you can [install gsutil as a standalone tool](https://docs.cloud.google.com/storage/docs/gsutil_install#install). If you've already installed gsutil as part of the Google Cloud CLI, [remove the gsutil component from your Google Cloud CLI installation](https://docs.cloud.google.com/storage/docs/gsutil_install#gsutil-uninstall-from-sdk) before installing gsutil as a standalone tool.

gsutil is a tool that lets you access Cloud Storage from the command line by using HTTPS. This page describes how to install and set up gsutil as a standalone tool.

Once you install gsutil, you can read or write data in Cloud Storage as permitted, including reading public data. However, most tasks require specific permissions:

  * To access private data, you must authenticate your identity.

  * To create your own project and manage buckets within your project, you must [enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project).




This page also contains instructions on installing gsutil as part of the Google Cloud CLI, which is discouraged due to the eventual unbundling of gsutil from the Google Cloud CLI installation package.

## System requirements

  * The gsutil tool runs on Linux/Unix, Mac OS, and Windows (versions 8.1 or 10 and later).

  * gsutil versions 5.36 or later require Python 3.9 to 3.14, which you can obtain by using your Python version manager or by installing an appropriate version.




## Manage Python versions

The following instructions show you how to manage Python versions so you can use a version that supports gsutil.

### Linux

Prerequisites: Install a Python version manager (pyenv) and install a suitable Python version.

  1. Set the Global Python Version:

     * To set Python 3.14 as the global version:
           
           pyenv global 3.14

     * To set the Python version locally for a specific project folder:
           
           pyenv local 3.14

  2. Confirm that the correct Python version is in use:
         
         python --version

You should see the following response:
         
         Python 3.14




### macOS

**Manage Python versions by using Homebrew (brew)**

Prerequisites: Install Homebrew and install a suitable Python version through Homebrew.

  1. Set a specific Python version as the default by adding the version you want to your `$PATH`. For example, to use Python 3.14:
         
         export PATH="$(brew --prefix)/opt/python@3.14/bin:$PATH"

     * To make this change permanent, add the path to your shell configuration file (`~/.bash_profile`, `~/.zshrc`, or `~/.bashrc`).
  2. Confirm that the correct Python version is in use:
         
         python --version

You should see the following response:
         
         Python 3.14




**Manage Python versions by using pyenv**

Prerequisites: Install a Python version manager (pyenv) and install a suitable Python version through pyenv.

  1. Set the global Python version:

     * To set the Python version globally (for all terminals):
           
           pyenv global 3.14

     * To set the Python version locally for a specific project folder:
           
           pyenv local 3.14

  2. Confirm that the correct Python version is in use:
         
         python --version

You should see the following response:
         
         Python 3.14




### Windows

Prerequisites: Install a Python version manager (pyenv-win) and install a suitable Python version through pyenv.

  1. Set the Global Python Version:

     * To set Python 3.14 as the global version:
           
           pyenv global 3.14

     * To set the Python version locally for a specific project folder:
           
           pyenv local 3.14

  2. Confirm that the correct Python version is in use:
         
         python --version

You should see the following response:
         
         Python 3.14




If you plan to use [composite objects](https://docs.cloud.google.com/storage/docs/composite-objects), you need to install compiled crcmod. On Windows, this is only available for 32-bit Python. For more information on crcmod, install gsutil and see the help topic by using the command `gsutil help crc32c`.

**Warning:** On some Linux distributions, another tool named **gsutil** , by GrandStream BudgeTone, is pre-installed. If you run this command instead of the Cloud Storage gsutil, it will likely print an error message similar to `"Choose one of -b, -d, -e, or -r to do something"`. If this happens, you can either move the Cloud Storage version of gsutil to the front of your `PATH` environment variable, or you can specify the full path when running Cloud Storage gsutil (for example, `/home/users/joan/gsutil/gsutil ls`).

## Install gsutil by using the Python package index (PyPI)

Follow the instructions for your operating system to install gsutil by using PyPI:

### CentOS, RHEL, and Fedora

  1. Install required system packages.

Several packages are required to successfully install gsutil from PyPI. You can install them with the following command:
         
         sudo yum install gcc openssl-devel python-devel \
           python-setuptools libffi-devel

  2. Install pip with the pip installer by running the following command:
         
         sudo yum install python-pip

If you are using CentOS or RHEL and yum can't find the package `python-pip`, it's likely because you don't have the Extra Packages for Enterprise Linux (EPEL) repository source enabled. To enable it, [follow these instructions](https://fedoraproject.org/wiki/EPEL#How_can_I_use_these_extra_packages.3F).

  3. Install gsutil from PyPI by running the following command:
         
         sudo pipx install gsutil




### Debian and Ubuntu

  1. Install required system packages.

Several packages are required to successfully install gsutil from PyPI. You can install them with the following command:
         
         sudo apt-get install gcc python-dev python-setuptools
           libffi-dev

  2. Install pip with the pip installer by running the following command:
         
         sudo apt-get install python3-pip

  3. Install gsutil from PyPI by running the following command:
         
         sudo pip install gsutil




### macOS

  1. Install pip with the pip installer by running the following commands:
         
         python3 -m ensurepip --default-pip
         
         python3 -m pip install --upgrade pip

  2. Install gsutil from PyPI by running the following command:
         
         sudo pip install gsutil




### Windows

  1. Install pip by running the following command:
         
         python -m ensurepip

  2. Install gsutil from PyPI by running the following command:
         
         pip install gsutil




You're ready to start using gsutil. To see a listing of gsutil commands, type `gsutil` at the command prompt.

The gsutil update command is not available when installing gsutil using PyPI. To update gsutil, use the pip installer by running either of the following commands:
    
    
    pipx upgrade gsutil
    
    
    sudo pip install -U gsutil

## Remove gsutil as a Google Cloud CLI component

After March 2027, gsutil will no longer be available as a component in the Google Cloud CLI. If you have gsutil installed as part of the Google Cloud CLI and would like to continue using gsutil, we recommend that you remove gsutil from your Google Cloud CLI installation and install gsutil as a standalone tool so you can continue running your scripts and getting updates for the tool.

To check whether you have gsutil installed as part of the Google Cloud CLI, run the command `gsutil version -l` and check the value for `using cloud sdk`. If `False`, your system is using the standalone version of gsutil when you run commands. If `True`, your system is using gsutil as a bundled component of the Google Cloud CLI.

To remove gsutil as a component from the Google Cloud CLI, run the following command:
    
    
    gcloud components remove gsutil

The previous command works if you've installed the Google Cloud CLI by using the interactive archive script or the Windows installer. If the command doesn't work, or you used a different installation method, you can still use standalone gsutil by updating your system shell's `PATH` variable so that the directory of your standalone gsutil is listed before the `google-cloud-sdk/bin` directory. For example, add the following code to your `~/.bashrc` or equivalent profile file:
    
    
    if [ -d "/path/to/standalone/gsutil/directory" ]; then
        PATH="/path/to/standalone/gsutil/directory:$PATH"
    fi

## Install gsutil as part of the Google Cloud CLI

After March 2027, gsutil will no longer be available as part of the Google Cloud CLI installation package. We recommend migrating to the Google Cloud CLI and using `gcloud storage` commands instead of gsutil. However, if you want to continue using gsutil, you should install gsutil as a standalone tool by using PyPI to support your existing scripts and continue getting updates for the tool.

Although it's not recommended, you can use the following instructions to install gsutil as a part of the Google Cloud CLI. These instructions will work until March 2027, when gsutil will become unbundled from the Google Cloud CLI.

**Note:** The Google Cloud CLI and gsutil have specific Python version dependencies that can lead to compatibility issues. Note that the supported Python versions for the Google Cloud CLI and gsutil might not always be the same. If you choose to install gsutil as part of the Google Cloud CLI, ensure that you're using a version that's compatible with both tools and their requirements.Linux

  1. Confirm that you have a supported version of Python. The Google Cloud CLI requires Python 3.10 to 3.15. The x86_64 Linux package includes a bundled Python interpreter that will be preferred by default. For information on how to choose and configure your Python interpreter, see the [`gcloud topic startup` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup). 
  2. Download one of the following: **Note:** To determine your Linux platform, run `uname -a` at the command line.Platform | Package name | Size | SHA256 Checksum  
---|---|---|---  
Linux 64-bit (x86_64) | [google-cloud-cli-linux-x86_64.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz) | 94.0 MB | 351ed4a2812c5525c1cee00334257a42c020fcaffa27d3067c1eec0a618dd83f  
Linux 64-bit (Arm) | [google-cloud-cli-linux-arm.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-arm.tar.gz) | 54.4 MB | dc3ad610faefe6f9d2e4472affe1db71836315f43ab3a3747221eb7595b431cb  
Linux 32-bit (x86) | [google-cloud-cli-linux-x86.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86.tar.gz) | 54.4 MB | 704d32be816d1aef1250721e52fc2d9e0802eab6eac513aef97db4c7ace19b2b  
  
To download the Linux archive file, run the following command: 
         
         curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz

Refer to the table above and replace google-cloud-cli-linux-x86_64.tar.gz with the `*.tar.gz` package name that applies to your configuration. 

  3. To extract the contents of the file to your file system, run the following command: 
         
         tar -xf google-cloud-cli-linux-x86_64.tar.gz

To replace an existing installation, delete the existing `google-cloud-sdk` directory and then extract the archive to the same location. 
  4. Run the installation script from the root of the folder you extracted: 
         
         ./google-cloud-sdk/install.sh

The script prompts you to perform the following setup actions. To accept, answer `Y` when prompted. 
     * Add the gcloud CLI to your `PATH`.
     * Enable command completion.
     * Opt in to send [anonymous usage statistics](https://docs.cloud.google.com/sdk/docs/usage-statistics) to help improve the gcloud CLI. 
You can also perform the installation non-interactively by providing flags. To view available flags, run: 
    
    ./google-cloud-sdk/install.sh --help

  5. Optional: If you updated your `PATH` in the previous step, open a new terminal so that the changes take effect. 
  6. Run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to initialize, authorize, and configure the gcloud CLI. 
  7. Optional: Install additional components using the [component manager](https://docs.cloud.google.com/sdk/docs/managing-components). 

Debian/Ubuntu

**Package contents**

The gcloud CLI is available in package format for installation on Debian and Ubuntu systems. This package contains the `gcloud`, `gcloud alpha`, `gcloud beta`, `gsutil`, and `bq` command-line tools only. It doesn't include `kubectl` or the App Engine extensions required to deploy an application using `gcloud` commands. If you want these components, you must install them separately. 

**Package version availability:** Package versions published within the last 365 days are retained in the repository.**Note:** For specific setups, alternative installation methods are available: 

  * If you're running a modern Ubuntu release with Snap Package Manager and want automatic updates, you can install Google Cloud CLI as a [snap package](https://docs.cloud.google.com/sdk/docs/downloads-snap).
  * If you're using a Compute Engine instance, the gcloud CLI might already be installed. For a list of operating system images that include the CLI by default, see [OS details](https://docs.cloud.google.com/compute/docs/images/os-details#user-space-features).



**Before you begin**

Before you install the gcloud CLI, make sure that your operating system meets the following requirements:

  * It is an Ubuntu release that hasn't reached [end-of-life](https://wiki.ubuntu.com/Releases) or a Debian stable release that hasn't reached [end-of-life](https://www.debian.org/releases).
  * It has recently updated its packages. To do this now, run the following command: 
        
        sudo apt-get update

  * It has `ca-certificates`, `gnupg`, and `curl` installed. To install these packages, run the following command: 
        
        sudo apt-get install ca-certificates gnupg curl




**Installation**

  1. Import the Google Cloud public key. 
     * For newer distributions (Debian 9+ or Ubuntu 18.04+) run the following command:
           
           curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg

     * For older distributions, run the following command: 
           
           curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

     * If your distribution's apt-key command doesn't support the `--keyring` argument, run the following command:
           
           curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

     * If you can't get latest updates due to an expired key, [obtain the latest apt-get.gpg key file](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#keyexpired).

  2. Add the gcloud CLI distribution URI as a package source. 
     * For newer distributions (Debian 9+ or Ubuntu 18.04+), run the following command: 
           
           echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

     * For older distributions that don't support the signed-by option, run the following command:
           
           echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

**Note:** Make sure you don't have duplicate entries for the `cloud-sdk` repo in `/etc/apt/sources.list.d/google-cloud-sdk.list`. 
  3. Update and install the gcloud CLI: 
         
         sudo apt-get update && sudo apt-get install google-cloud-cli

**Note:** If installing in resource-constrained virtual machines, container images, or automated CI/CD runners, you can export the environment variable `CLOUDSDK_SKIP_PY_COMPILATION=1` during installation to skip host-side Python compilation. This drops package installation time from minutes down to seconds: 
         
         sudo CLOUDSDK_SKIP_PY_COMPILATION=1 apt-get install google-cloud-cli

Setting this variable skips byte-compilation on installation, trading some package setup speed for minor interactive command execution overhead.  For additional `apt-get` options, such as disabling prompts or dry runs, refer to the [`apt-get` man pages](https://linux.die.net/man/8/apt-get). 

**Docker Tip:** If installing the gcloud CLI inside a Docker image, use a single RUN step instead:
         
         RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && apt-get update -y && apt-get install google-cloud-cli -y
             

For older base images that do not support the `gpg --dearmor` command: 
         
         RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-cli -y
               

  4. Optional: Install any of the following [ additional components](https://docs.cloud.google.com/sdk/docs/components#additional_components): 
     * `google-cloud-cli-anthos-auth`
     * `google-cloud-cli-app-engine-go`
     * `google-cloud-cli-app-engine-grpc`
     * `google-cloud-cli-app-engine-java`
     * `google-cloud-cli-app-engine-python`
     * `google-cloud-cli-app-engine-python-extras`
     * `google-cloud-cli-bigtable-emulator`
     * `google-cloud-cli-cbt`
     * `google-cloud-cli-cloud-run-proxy`
     * `google-cloud-cli-config-connector`
     * `google-cloud-cli-datastore-emulator`
     * `google-cloud-cli-firestore-emulator`
     * `google-cloud-cli-gke-gcloud-auth-plugin`
     * `google-cloud-cli-kubectl-oidc`
     * `google-cloud-cli-local-extract`
     * `google-cloud-cli-minikube`
     * `google-cloud-cli-nomos`
     * `google-cloud-cli-pubsub-emulator`
     * `google-cloud-cli-skaffold`
     * `google-cloud-cli-spanner-emulator`
     * `google-cloud-cli-terraform-tools`
     * `google-cloud-cli-tests`
     * `kubectl`

For example, the `google-cloud-cli-app-engine-java` component can be installed as follows: 
    
    sudo apt-get install google-cloud-cli-app-engine-java

  5. Run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to initialize, authorize, and configure the gcloud CLI. 



**Downgrade gcloud CLI versions**

To revert to a specific version of the gcloud CLI, where `VERSION` is of the form `123.0.0`, run the following command:
    
    
    sudo apt-get update && sudo apt-get install google-cloud-cli=123.0.0-0

Package versions published within the last 365 days are retained in the repo.

Red Hat/Fedora/CentOS

**Package contents**

The gcloud CLI is available in package format for installation on Red Hat Enterprise Linux 7, 8, 9, and 10; Fedora 41 and 42; and CentOS 7 and 8 systems. This package contains the `gcloud`, `gcloud alpha`, `gcloud beta`, `gsutil`, and `bq` commands only. It doesn't include `kubectl` or the App Engine extensions required to deploy an application using `gcloud` commands, which can be installed separately as described later in this section. 

**Package version availability:** Package versions published within the last 365 days are retained in the repository.**Note:** If you're using an instance on Compute Engine, the Google Cloud CLI is installed by default on a number of OS images. See [OS details](https://docs.cloud.google.com/compute/docs/images/os-details#user-space-features) for a full list.

**Installation**

  1. Update DNF with gcloud CLI repository information. 
     * The following sample command is for a Red Hat Enterprise Linux 7, 8, or 9-compatible installations, but make sure that you update the settings as needed for your configuration:
           
           sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
           [google-cloud-cli]
           name=Google Cloud CLI
           baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el9-x86_64
           enabled=1
           gpgcheck=1
           repo_gpgcheck=0
           gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
           EOM

     * For RHEL 10-compatible installations, use the following command with the updated `gpgkey`:
           
           sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
           [google-cloud-cli]
           name=Google Cloud CLI
           baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el10-x86_64
           enabled=1
           gpgcheck=1
           repo_gpgcheck=0
           gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key-v10.gpg
           EOM

     * For ARM64 (aarch64) installations, use `https://packages.cloud.google.com/yum/repos/cloud-sdk-el9-aarch64` (RHEL 7, 8, or 9-compatible) or `https://packages.cloud.google.com/yum/repos/cloud-sdk-el10-aarch64` (RHEL 10-compatible) as the `baseurl` value. 

  2. Install `libxcrypt-compat.x86_64`. 
         
         sudo dnf install libxcrypt-compat.x86_64

  3. Install the gcloud CLI: 
         
         sudo dnf install google-cloud-cli

**Note:** If installing in resource-constrained virtual machines, container images, or automated CI/CD runners, you can export the environment variable `CLOUDSDK_SKIP_PY_COMPILATION=1` during installation to skip host-side Python compilation. This drops package installation time from minutes down to seconds: 
         
         sudo CLOUDSDK_SKIP_PY_COMPILATION=1 dnf install google-cloud-cli

Setting this variable skips byte-compilation on installation, trading some package setup speed for minor interactive command execution overhead. **Note:** If you haven't moved to [`dnf`](https://dnf.readthedocs.io/en/latest/command_ref.html) on your system, you can run these commands using `yum` instead.

You can also use `dnf`/`yum` options, such as disabling prompts or dry runs, with the provided commands.

  4. Optional: Install any of the following [additional components](https://docs.cloud.google.com/sdk/docs/components#additional_components): 
     * `google-cloud-cli-anthos-auth`
     * `google-cloud-cli-app-engine-go`
     * `google-cloud-cli-app-engine-grpc`
     * `google-cloud-cli-app-engine-java`
     * `google-cloud-cli-app-engine-python`
     * `google-cloud-cli-app-engine-python-extras`
     * `google-cloud-cli-bigtable-emulator`
     * `google-cloud-cli-cbt`
     * `google-cloud-cli-cloud-run-proxy`
     * `google-cloud-cli-config-connector`
     * `google-cloud-cli-datastore-emulator`
     * `google-cloud-cli-firestore-emulator`
     * `google-cloud-cli-gke-gcloud-auth-plugin`
     * `google-cloud-cli-kubectl-oidc`
     * `google-cloud-cli-local-extract`
     * `google-cloud-cli-minikube`
     * `google-cloud-cli-nomos`
     * `google-cloud-cli-pubsub-emulator`
     * `google-cloud-cli-skaffold`
     * `google-cloud-cli-spanner-emulator`
     * `google-cloud-cli-terraform-validator`
     * `google-cloud-cli-tests`
     * `kubectl`

For example, to install the `google-cloud-cli-app-engine-java` component, run the following command: 
    
    sudo dnf install google-cloud-cli-app-engine-java

  5. Run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to initialize, authorize, and configure the gcloud CLI. 



**Downgrade gcloud CLI versions**

To revert to a specific version of gcloud CLI, run the following command. Replace `123.0.0` with the version that you want to install: 
    
    
    sudo dnf downgrade google-cloud-cli-123.0.0

Package versions published within the last 365 days are retained in the repository.

macOS

  1. Confirm that you have a supported version of Python. The Google Cloud CLI requires Python 3.10 to 3.15. 

To check your Python version, run `python3 -V` or `python -V`.

The gcloud installer will install Python v3.14 and required extension modules by default.

For more information about configuring your Python interpreter, see the [`gcloud topic startup` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup).

  2. Download one of the following:  Note: To determine your platform, run `uname -m` from a command line. Platform | Package | Size | SHA256 Checksum  
---|---|---|---  
macOS 64-bit (x86_64) |  [google-cloud-cli-darwin-x86_64.tar.gz ](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-darwin-x86_64.tar.gz) | 54.5 MB |  9ff4e7c7fa49eca2e61af3d6ba31735ed08f90e5fae503d19d4c1c520f818736   
macOS 64-bit (ARM64, Apple silicon) |  [google-cloud-cli-darwin-arm.tar.gz ](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-darwin-arm.tar.gz) | 54.4 MB |  b1f80ffe9cc970ff1935b4adfddd0fb89d7e7b3341a88d70216d4283211b8d2d   
macOS 32-bit (x86) |  [google-cloud-cli-darwin-x86.tar.gz ](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-darwin-x86.tar.gz) | 52.9 MB |  b2da028700b7af4ebc2364fc59398921a3c2d67f91fe63d3a7a42648a54eb6ab   
  
Alternatively, you can download the archive from the command line. Replace `FILE_NAME` with the package name for your platform from the table above. 
         
         curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/FILE_NAME

  3. Extract the contents of the file to your preferred location on your file system. A common practice is to extract it to your home directory. 

On macOS, you can do this by opening the downloaded `.tar.gz` file in your preferred location. Alternatively, from the command line, run: 
         
         tar -xf FILE_NAME

To replace an existing installation, delete the existing `google-cloud-sdk` directory and then extract the archive to the same location. 

  4. Run the installation script from the root of the folder you extracted: 
         
         ./google-cloud-sdk/install.sh

The script prompts you to perform the following setup actions. To accept, answer `Y` when prompted. 
     * Install Python 3.14 and recommended modules if needed.
     * Add the gcloud CLI to your `PATH` and enable command completion.
     * Opt in to send [anonymous usage statistics](https://docs.cloud.google.com/sdk/docs/usage-statistics) to help improve the gcloud CLI. 
You can also perform the installation non-interactively by providing flags. To view available flags, run: 
    
    ./google-cloud-sdk/install.sh --help

To run the install script with screen reader mode enabled: 
    
    ./google-cloud-sdk/install.sh --screen-reader=true

  5. Optional: If you updated your `PATH` in the previous step, open a new terminal so that the changes take effect. 
  6. Run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to initialize, authorize, and configure the gcloud CLI. 
  7. Optional: Install additional components using the [component manager](https://docs.cloud.google.com/sdk/docs/managing-components). 

Windows

The Google Cloud CLI on Windows requires Windows 8.1 and later, or Windows Server 2012 and later.

  1. Download the [Google Cloud CLI installer](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe). 

Alternatively, open a PowerShell terminal and run the following PowerShell commands: 
         
         (New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
         
         & $env:Temp\GoogleCloudSDKInstaller.exe
             

  2. Launch the installer and follow the prompts. The installer is signed by Google LLC.

     * If you're using a screen reader, check the **Turn on screen reader mode** checkbox. This option configures `gcloud` to use status trackers instead of unicode spinners, display progress as a percentage, and flatten tables. For more information, see the [Accessibility features guide](https://docs.cloud.google.com/sdk/docs/enabling-accessibility-features). 
     * Google Cloud CLI requires Python; supported versions are Python 3.10 to 3.15. By default, the Windows version of Google Cloud CLI comes bundled with Python 3. To use Google Cloud CLI your operating system must be able to run a supported version of Python. 
     * The installer installs all necessary dependencies, including the needed Python version. While Google Cloud CLI installs and manages Python 3 by default, you can use an existing Python installation if necessary by **unchecking** the option to Install Bundled Python. See [`gcloud topic startup`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup) to learn how to use an existing Python installation. 
  3. After installation is complete, the installer gives you the option to create Start Menu and Desktop shortcuts, start the Google Cloud CLI shell, and configure the gcloud CLI. Leave the options to start the shell and configure your installation selected. The installer starts a terminal window and runs the [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) command to initialize, authorize, and configure the gcloud CLI. 
  4. The default installation doesn't include the App Engine extensions required to deploy an application using `gcloud` commands. These components can be installed using the [gcloud CLI component manager](https://docs.cloud.google.com/sdk/docs/managing-components). 



**Troubleshooting tips**

  * If your installation is unsuccessful due to the `find` command not being recognized, ensure your `PATH` environment variable is set to include the folder containing `find`. Usually, this is `C:\WINDOWS\system32;`.
  * If you uninstalled the gcloud CLI, you must reboot your system before installing the gcloud CLI again.
  * If unzipping fails, run the installer as an administrator.



## Setting up credentials to access protected data

Installing gsutil lets you [download and access publicly-accessible data](https://docs.cloud.google.com/storage/docs/request-endpoints#mtls), but in order to access protected data or write to a protected bucket, you need to set up credentials in order to authenticate. For example, if someone else has created a Google Cloud account and uploaded data to Cloud Storage that is only accessible to you or other specific individuals, you must set up your credentials to the Cloud Storage service to be able to access this data.

For more information and instructions on authenticating using different account credentials (such as OAuth2, HMAC, and service accounts), see the [gsutil creds.py documentation](https://github.com/GoogleCloudPlatform/gsutil/blob/master/gslib/addlhelp/creds.py) on GitHub.

Note the following reminders:

  * When authenticating with HMAC keys, you should disable credential passing from the Google Cloud CLI by using the following command:
        
        gcloud config set pass_credentials_to_gsutil false




## Enable mTLS

You might also want to enable mutual TLS (mTLS). When mTLS is enabled on your device, your device attempts to connect to the [mTLS request endpoint](https://docs.cloud.google.com/storage/docs/request-endpoints#mtls) for the JSON API. Before the connection is allowed, Cloud Storage verifies the certificate on your device.

**Note:** This feature only works when gsutil makes requests through the Cloud Storage JSON API.

The simplest way to to obtain a certificate is through [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk). You can set one manually in the [.boto](https://docs.cloud.google.com/storage/docs/boto-gsutil) file by setting the following values under "Credentials":

  * `use_client_certificate`: A flag controlling whether or not to use mTLS.

  * `cert_provider_command`: A shell command that prints a certificate to stdout 

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)




### Troubleshooting

You can authenticate gsutil by running `gsutil config -a` or `gsutil config -e` but by default, a gsutil installation bundled with the Google Cloud CLI prioritizes active `gcloud` OAuth2 credentials over local `.boto` credentials. As a result, running `gsutil config` has no operational effect unless credentials sharing is explicitly disabled by using `gcloud config set pass_credentials_to_gsutil false`. We recommend uninstalling gsutil from the Google Cloud CLI and installing gsutil as a standalone tool instead.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
