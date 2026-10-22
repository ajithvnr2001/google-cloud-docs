---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-centos/
title: Create an agent with the installer for CentOS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:15.944399+00:00
---

# Create an agent with the installer for CentOS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-centos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an agent with the installer for CentOS 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document provides the required packages for installing an agent on CentOS 7.9. Before you install the agent, you must install and configure required packages listed in this document.

Google recommends running the commands one by one to make sure each action is run successfully.

**Note:** To install these packages, you must have superuser privileges. To make sure some dependencies remain accessible to non-root users, don't change the root user's `umask` from the default value of `0022`.

## Install and configure required packages

To install and configure required packages, follow these steps:

  1. Run the following commands to install Linux packages:
    
    yum update -y
    yum groupinstall -y 'development tools'
    yum install bzip2-devel -y
    yum install sqlite -y
    yum install libffi-devel -y
    yum install gcc -y
    yum install gcc-c++ -y
    yum install python-devel -y
    yum install python3-devel -y
    yum install zlib-devel -y
    yum install openssl-devel -y
    yum install epel-release -y
    yum install perl-core -y
    yum update -y
    yum install supervisor -y
    yum install at -y
    yum install sharutils -y

  2. Run the following commands to start the `atd` service:
    
    systemctl start atd
    systemctl enable atd

  3. Install OpenSSL 3.0.7.

Run the following commands to install OpenSSL 3.0.7:

**Important:** Keep the shell session open until you've completed the final step.
    
    cd /usr/local/src
    wget https://www.openssl.org/source/openssl-3.0.7.tar.gz
    tar -xf openssl-3.0.7.tar.gz
    cd openssl-3.0.7
    ./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib
    make -j$((`nproc`+1))
    make install
    cd /etc/ld.so.conf.d/
    echo /usr/local/ssl/lib64 > openssl-3.0.7.conf
    ldconfig -v
    echo PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/ssl/bin" > /etc/environment
    source /etc/environment
    ln -sf  /usr/local/ssl/bin/openssl /usr/bin/openssl
    export LDFLAGS="$LDFLAGS -L/usr/local/ssl/lib64"
    export LD_LIBRARY_PATH=/usr/local/ssl/lib64

  4. Run the following commands to install Python 3.11.8:
    
    cd /usr/src
    wget http://www.python.org/ftp/python/3.11.8/Python-3.11.8.tgz
    tar xzf Python-3.11.8.tgz
    cd Python-3.11.8
    make clean
    ./configure --prefix=/usr/local --enable-unicode=ucs4 --with-openssl=/usr/local/ssl
    make
    make altinstall

  5. Run the following command to create a Python symlink:
    
    ln -s /usr/local/bin/python3.11 /usr/local/bin/python3

  6. Run the following commands to configure `pip`:
    
    wget -O get-pip.py https://bootstrap.pypa.io/pip/2.7/get-pip.py
    /usr/local/bin/python3 get-pip.py
    /usr/local/bin/pip3 install --upgrade pip
    wget -O get-pip-3.11.py https://bootstrap.pypa.io/get-pip.py
    /usr/local/bin/python3.11 get-pip-3.11.py
    /usr/local/bin/python3.11 -m pip install --upgrade pip

  7. Optional: If you're using Microsoft SQL Integration, run the following commands to install **MsOdbc SQL driver utils** :
    
    yum -y remove unixODBC unixODBC-devel
    rpm -Uvh --replacepkgs https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm
    yum install -y msodbcsql-13.0.1.0-1 mssql-tools-14.0.2.0-1 unixODBC-utf16-devel
    ln -sfn /opt/mssql-tools/bin/bcp-13.0.1.0 /usr/bin/bcp
    ln -sfn /opt/mssql-tools/bin/sqlcmd-13.0.1.0 /usr/bin/sqlcmd




## Install a remote agent

Before you install a remote agent, make sure you have completed all the required configurations.

To install a remote agent, follow these steps:

  1. In the platform, go to **Settings** > **Advanced** > **Remote Agents**.
  2. On the **Remote Agents** page, click add**Add** > click **Manual installation**.
  3. Enter an agent name and select an environment.
  4. Click **Next**.
  5. Select an option to download the agent.

     * Download the agent to your machine.
     * Enter an email address to send download to the configured email address. Make sure you have configured the email integration to the correct environment.
  6. Optional: Click **Add environment contact** to add a contact person for the environment. 

The following files are downloaded:

     * `.env`: Siemplify environment variables
     * `SiemplifyAgent_Centos.sh`: Installer script file
  7. Click **Next**.
  8. Store the installer command in a secure location.
  9. Use **WinSCP** (or a similar tool) to copy the files to the machine where you want to install the agent.
  10. Sign in to the machine using SSH with your username and password.
  11. Run the following command to set the permissions:
`sudo chmod +x SiemplifyAgent_Centos.sh`
  12. Run the installer command you saved earlier to install the agent.
  13. Return to the installation process on your platform and then click **Next**. A confirmation message for agent connection appears.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
