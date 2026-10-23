---
url: https://docs.cloud.google.com/shell/docs/configuring-cloud-shell/
title: Configure Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:43.510218+00:00
---

# Configure Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/configuring-cloud-shell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Configure Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the ways you can configure Cloud Shell to customize your experience.

## Configuration files in your Cloud Shell home directory

Cloud Shell provisions 5 GB of free [persistent disk storage](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) mounted as your `$HOME` directory. All files you store in your home directory, including installed software, scripts and user configuration files like `.bashrc` and `.vimrc`, persist between sessions. Since your `.bashrc` persists across sessions, it's a great way to customize your Cloud Shell behavior. Similarly, to have your installations persist, you can install packages into your home directory.

## Pre-configured environment variables

When Cloud Shell is started, the active project in Cloud Shell is propagated to your `gcloud` configuration inside Cloud Shell for immediate use. `GOOGLE_CLOUD_PROJECT`, the environmental variable used by Application Default Credentials library support to define project ID, is also set to point to the active project in Cloud Shell.

The `CLOUD_SHELL` environment variable is set to `true`. This variable can be checked from applications to determine if an application is running in Cloud Shell.

## gcloud CLI preferences

When using Cloud Shell, your gcloud CLI preferences are stored in a temporary `tmp` folder, set for your current tab only, and do not persist across sessions.

To have your gcloud CLI configurations persist, you can set them using one of the following methods:

  * To keep your gcloud CLI configuration customizable per tab but customize the default configuration itself, you can add `gcloud` configuration commands (such as `gcloud config set compute/region us-central1` to set a default region) to the end of your `$HOME/.bashrc` file.

This ensures that every new tab inherits your Google Cloud console project and your customized default configuration but also allows you to further customize each tab's configuration.

  * To always use the same gcloud CLI configuration, add `export CLOUDSDK_CONFIG=$HOME/.config/gcloud` to the end of your .bashrc file, and then run `gcloud config configurations create CONFIG_NAME` to create the configuration you'd like to use.




### Common properties

To set the project you'd like to work on, run:
    
    
    gcloud config set project [PROJECT_NAME]
    

Your command prompt updates to reflect your currently active project, respecting this format: `[USERNAME]@cloudshell:~ ([PROJECT_NAME])$`

To select your preferred region, run:
    
    
    gcloud config set compute/region us-east1
    

The commands above are examples of gcloud CLI configurations you can set; for a full list and greater detail about setting properties, refer to the [gcloud CLI properties guide](https://docs.cloud.google.com/sdk/docs/properties).

## Environment customization

**Note:** If you want a specific package included with Cloud Shell by default, [submit your suggestion as feedback](https://docs.cloud.google.com/shell/docs/getting-support#file_bugs_or_feature_requests).

Environment customization allows you to install additional packages into your Cloud Shell environment when it starts.

### Environment customization script

Cloud Shell automatically runs the script, `$HOME/.customize_environment`, when your instance boots up. Unlike `.profile` or `.bashrc`, this script runs once when Cloud Shell boots (rather than once for each shell login).

This script runs as root and you can install any packages that you want to exist in each Cloud Shell session using Debian package management commands.

For example, if you'd like to have erlang installed on Cloud Shell, your `.customize_environment` file will look like this:
    
    
    #!/bin/sh
    apt-get update
    apt-get -y install erlang
    

Execution logs of your `.customize_environment` script can be found at `/var/log/customize_environment`. The `.customize_environment` script runs as a background process and on successful execution, will touch `/google/devshell/customize_environment_done`. Because package installation runs in parallel with your logging in, the installed packages may become available a few moments after you reach the login prompt.

## Open Cloud Shell with a specified user account

The `authuser` parameter lets you specify a user account to use with Cloud Shell. You must be logged in with the specified user account. If you're not logged in to the specified account, Cloud Shell opens with the default logged in account. For example, you can open Cloud Shell logged in as `client1@example.com` using the URL `shell.cloud.google.com?authuser=client1@example.com`.

## tmux support

Cloud Shell uses `tmux`, which allows it to improve persistence across browser tab sessions. For example, if you refresh the Google Cloud console in a tab or connect to your Cloud Shell from a different machine, the session state will not be lost.

Cloud Shell supports the default [`tmux` key bindings](http://man.openbsd.org/OpenBSD-current/man1/tmux.1). For example, if you press **Ctrl+b** and then **%** , `tmux` splits the current session window into left and right panes, which can be useful for debugging.

## Usage statistics

Cloud Shell collects anonymized usage statistics on commands that are run inside the Cloud Shell terminal. Statistics are collected only on commands that come pre-installed in the Cloud Shell. These metrics can't be tied back to your account.

Metrics aren't collected on any personally identifiable information, such as arguments passed to these commands.

To change metrics collection preferences at any time, select **Terminal Usage Statistics** in the **Settings** menu ![Settings Button](https://docs.cloud.google.com/static/shell/docs/images/settings-button.png). Any change in your preferences on the Settings menu takes effect on the next session. To enable or disable metrics collection, close your tab and open another tab after you've made your change.

**Note:** This is separate from [gcloud usage statistics](https://docs.cloud.google.com/sdk/docs/usage-statistics), which is enabled by default in Cloud Shell.

To disable gcloud CLI metrics collection, run the following command in your Cloud Shell session:
    
    
    gcloud config set disable_usage_reporting true
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
