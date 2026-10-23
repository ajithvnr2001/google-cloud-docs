---
url: https://docs.cloud.google.com/source-repositories/docs/authentication/
title: Setting up local authentication \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:15.669048+00:00
---

# Setting up local authentication  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/authentication/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Setting up local authentication Stay organized with collections  Save and categorize content based on your preferences. 

Before you can access or interact with hosted repositories from your system, you must set up local authentication in your environment.

After you set up local authentication, you can access hosted repositories for which you have the appropriate [roles and permissions](https://docs.cloud.google.com/source-repositories/docs/configure-access-control). You can also perform standard Git operations such as `git clone`, `git pull`, and `git push`. Local authentication isn't required to perform operations in the Google Cloud console, for example, to browse the contents of a repository.

Cloud Source Repositories supports the following types of authentication:

  * SSH
  * Google Cloud CLI
  * Manually generated credentials



## Authenticate by using SSH

Cloud Source Repositories lets you use SSH public key authentication to access hosted repositories. In this scenario, you first generate a key pair on the local system from which you want to access the repository. Then you register the public key with Google Cloud. If you already have an SSH key pair on your system, you can re-use those keys for authentication. You can register up to 20 public keys per Google Account.

**Note:** You cannot configure authentication for service accounts by using SSH keys.

Cloud Source Repositories supports three SSH key types:

  * RSA (only for keys with more than 2048 bits)
  * ECDSA
  * ED25519



### Generate a key pair

The SSH key pair consists of a private key that resides on your local system and a public key that you register with Google Cloud.

###  Linux or macOS 

  1. Ensure that [OpenSSH](https://www.openssh.com/) is installed on your local system.

  2. At a command prompt, enter the following command:
         
         ssh-keygen -t [KEY_TYPE] -C "[USER_EMAIL]"
         

Where:

     * `[USER_EMAIL]` is your email address.
     * `[KEY_TYPE]` is one of the following: 
       * `rsa`
       * `ecdsa`
       * `ed25519`

For example:
    
    ssh-keygen -t rsa -C "user@example.com"
    

     1. When prompted, enter a filename for the public key file. To accept the default `~/.ssh` location, press **Enter** , otherwise specify a filename.

     2. When prompted, leave the passphrase empty and press **Enter**.

  3. Register your key




###  Windows 

  1. Ensure that [PuTTY](https://www.chiark.greenend.org.uk/%7Esgtatham/putty/latest.html) is installed on your local system.

  2. From the Windows **Start** menu, start PuTTYGen.

  3. In the window that opens, select the key type from the **Parameters** field.

  4. Click **Generate**.

PuTTYGen displays the generated public key string.

  5. Specify a passphrase to protect the key pair.

  6. To save the key pair you generated to your local system, click **Save Public Key** and **Save Private Key**.




### Use existing keys

You can also use an existing key pair for SSH authentication.

###  Linux or macOS 

By default, public key files are located in your `~/.ssh` directory.

At a command prompt, enter the following command:
    
    
    ls -a ~/.ssh
    

The default filenames are:

  * `id_rsa.pub`
  * `id_ecdsa.pub`
  * `id_ed25519.pub`



###  Windows 

  1. From the Windows **Start** menu, start PuTTYGen.

  2. In the window that opens, click **Load**.

  3. Browse the local file system for your public key file and select the file.

PuTTYGen displays the public key string. If you specified a passphrase when you saved the key file, PuTTYGen prompts you to enter it before you can view the public key.




### Register a public key

  1. In the Google Cloud console, open the **Manage SSH Keys** page.

[ Open Cloud Source Repositories](https://source.cloud.google.com/user/ssh_keys)

  2. Click **Register SSH key**.

The **Register SSH Key** dialog opens.

  3. In the **Key name** field, type a unique name for the key.

  4. In the **Key** field, copy the key string from your public key file.

  5. Click **Register**.




After you set up SSH authentication, you can [clone any repository](https://docs.cloud.google.com/source-repositories/docs/cloning-repositories#ssh) for which you have the required roles and permissions, or [push the contents](https://docs.cloud.google.com/source-repositories/docs/pushing-code-from-a-repository) of a local repository to an empty hosted repository.

## Authenticate by using the gcloud CLI

Cloud Source Repositories lets you authenticate by using the gcloud CLI. In this scenario, you run the [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) command on your system to set up local authentication.

  1. Ensure that the [gcloud CLI](https://docs.cloud.google.com/sdk/install) is installed on your local system.

  2. At a command prompt, run `gcloud init`:
         
         gcloud init
         

  3. Follow the instructions.




After you set up authentication by using the gcloud CLI, you can use standard Git commands to interact with the hosted repository on Cloud Source Repositories.

## Authenticate by using manually generated credentials

You can also use manually generated credentials for authentication. Cloud Source Repositories provides a set of scripts you can use to manually generate the credentials you need to access hosted repositories.

  1. Go to the **Configure Git** page to generate your credentials.

[Go to the Configure Git page](https://source.developers.google.com/auth/start?scopes=https://www.googleapis.com/auth/cloud-platform)

  2. Open a terminal window.

  3. Type the following command:
         
         git clone https://source.developers.google.com/p/PROJECT_ID/r/REPOSITORY_NAME
         

Where:

     * PROJECT_ID is the name of your project
     * REPOSITORY_NAME is the name of your repository



After you set up authentication with manually generated credentials, you can interact with the hosted repository on Cloud Source Repositories by using the standard Git commands.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
