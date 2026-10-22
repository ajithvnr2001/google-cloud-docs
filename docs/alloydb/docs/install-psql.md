---
url: https://docs.cloud.google.com/alloydb/docs/install-psql/
title: Install the psql command-line tool \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:16.432601+00:00
---

# Install the psql command-line tool  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/install-psql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Install the psql command-line tool Stay organized with collections  Save and categorize content based on your preferences. 

To connect to your AlloyDB for PostgreSQL instance from the command line, you can install the `psql` client tool on macOS, Linux, or Windows. The `psql` command-line tool is a terminal-based frontend to [PostgreSQL](https://www.postgresql.org/download/) that is required by the [`gcloud beta alloydb connect`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/connect) command and is also used for direct database connections.

## macOS

To install `psql` on macOS, we recommend using [Homebrew](https://brew.sh/):

  1. Install the `postgresql` package:
         
         brew install postgresql
         

  2. Add `psql` to your `PATH` by following the instructions provided in the terminal output after the installation completes. For example:
         
         echo 'export PATH="/opt/homebrew/opt/postgresql@18/bin:$PATH"' >> ~/.zshrc
         source ~/.zshrc
         

**Note:** The path might differ depending on your hardware architecture (Intel or Apple Silicon).



## Linux (Debian or Ubuntu)

Use your distribution's package manager to install the PostgreSQL client:
    
    
    sudo apt-get update
    sudo apt-get install postgresql-client
    

For other distributions, see the [official PostgreSQL download page](https://www.postgresql.org/download/).

## Windows

To install `psql` on Windows, you can use the interactive installer.

### Installer

  1. Download the **PostgreSQL Interactive Installer** for Windows from the [PostgreSQL downloads page](https://www.postgresql.org/download/windows/).
  2. Run the installer. When prompted to select components, you can install only **Command Line Tools**.
  3. Add the `bin` directory of your PostgreSQL installation (for example, `C:\Program Files\PostgreSQL\18\bin`) to your system `PATH` environment variable.



## Verify the installation

After installation, verify that `psql` is in your `PATH` and is working correctly:
    
    
    psql --version
    

If installed correctly, the output shows the version of the `psql` client tool.

## What's next

  * [Connect using gcloud CLI](https://docs.cloud.google.com/alloydb/docs/connect-gcloud).
  * [Connect from Compute Engine](https://docs.cloud.google.com/alloydb/docs/connect-psql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
