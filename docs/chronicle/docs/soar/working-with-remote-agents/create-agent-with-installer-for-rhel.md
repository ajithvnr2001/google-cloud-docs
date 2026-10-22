---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-for-rhel/
title: Create an agent with the installer for RHEL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:05.293807+00:00
---

# Create an agent with the installer for RHEL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-for-rhel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an agent with the installer for RHEL

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This guide provides the required packages to install an agent on Red Hat Enterprise Linux (RHEL) 8.7. Before you install an agent, you must install and configure required packages listed in this document.

Google recommends running the commands one by one to make sure each action is run successfully.

**Note:** To install all the packages, you must have superuser privileges. However, to ensure some dependencies remain accessible to non-root users, don't change the root user's `umask` from the default value of `0022`.

## Install and configure required packages

To install and configure required packages, follow these steps:

  1. Run the following commands to configure the `PATH` variable:
    
    echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc
    source ~/.bashrc
    

  2. Run the following commands to install Linux packages:
    
    dnf update -y
    dnf groupinstall -y 'Development Tools'
    dnf install bzip2-devel -y
    dnf install sqlite -y
    dnf install libffi-devel -y
    dnf install gcc -y
    dnf install gcc-c++ -y
    dnf install python2-devel -y
    dnf install python3-devel -y
    dnf install zlib-devel -y
    dnf install openssl-devel -y
    dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
    dnf install epel-release -y
    subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms
    dnf install perl-core -y
    dnf update -y
    dnf install supervisor -y
    dnf install at -y
    dnf install sharutils -y

  3. Run the following commands to start the `atd` service:
    
    systemctl start atd
    systemctl enable atd

  4. Run the following commands to install OpenSSL 3.0.7:
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

  5. Run the following commands to install Python 3.11.8:
    
    cd /usr/src
    wget http://www.python.org/ftp/python/3.11.8/Python-3.11.8.tgz
    tar xzf Python-3.11.8.tgz
    cd Python-3.11.8
    make clean
    ./configure --prefix=/usr/local --enable-unicode=ucs4 --with-openssl=/usr/local/ssl
    make
    make altinstall

  6. Run the following command to create a Python symlink:
    
    ln -s /usr/local/bin/python3.11 /usr/local/bin/python3

  7. Run the following commands to configure `pip` for all Python versions:
    
    /usr/local/bin/python3 get-pip.py
    /usr/local/bin/pip3 install --upgrade pip
    wget -O get-pip-3.11.py https://bootstrap.pypa.io/get-pip.py
    /usr/local/bin/python3.11 get-pip-3.11.py
    /usr/local/bin/python3.11 -m pip install --upgrade pip

  8. Optional: If you're using Microsoft SQL Integration, run the following commands to install **MsOdbc SQL driver utils** :
    
    dnf -y remove unixODBC unixODBC-devel
    curl  <https://packages.microsoft.com/config/rhel/8/prod.repo> > /etc/yum.repos.d/mssql-release.repo
    dnf install -y msodbcsql17 mssql-tools unixODBC-devel
    ln -sfn /opt/mssql-tools/bin/bcp /usr/bin/bcp
    ln -sfn /opt/mssql-tools/bin/sqlcmd /usr/bin/sqlcmd




## Install a remote agent

Before you install a remote agent, make sure you've completed all the required configurations.

To install a remote agent, follow these steps:

  1. In the platform, go to **Settings** > **Advanced** > **Remote Agents**.
  2. On the **Remote Agents** page, click add**Add** > click **Manual installation**.
  3. Enter a name for the agent and select an environment.
  4. Click **Next**.
  5. Select an option to download the agent files:

     * Download the agent on your machine.
     * Enter an email address to send the download to the configured email address. Make sure you have configured the email integration to the correct environment.
  6. Optional: Click **Add environment contact** to add a contact person for the environment. 

The following files are downloaded:

     * `.env`: Siemplify environment variables
     * `SiemplifyAgent_Centos.sh`: Installer script file
  7. Click **Next**.
  8. Store the installer command in a secure location.
  9. Use **WinSCP** (or a similar tool) to copy the files to the machine where you want to install the agent.
  10. Sign in to the machine using SSH with your username and password.
  11. Run the following command to set the permissions for the installer script:
`sudo chmod +x SiemplifyAgent_Centos.sh`
  12. Run the installer command you saved to install the agent.
  13. Return to the installation process on your platform and then click **Next**. A confirmation message for agent connection appears.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
