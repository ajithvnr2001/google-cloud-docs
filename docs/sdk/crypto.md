---
url: https://docs.cloud.google.com/sdk/crypto/
title: The gcloud CLI and p12 service account keys \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:24.746079+00:00
---

# The gcloud CLI and p12 service account keys  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/crypto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)



Send feedback 

#  The gcloud CLI and p12 service account keys Stay organized with collections  Save and categorize content based on your preferences. 

**Recommendation:**

We recommend that you use JSON (.json) private keys to activate service accounts. JSON private keys do not require the special crypto library explained on this page. To create a new JSON private key for a service account, follow the steps in [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate#service-accounts). For steps to activate the service account with the Google Cloud CLI, see [`gcloud auth activate-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account). The rest of this page isn't applicable if you use JSON private keys. 

The gcloud CLI allows developers to use private keys to authenticate with service accounts, also known as robot accounts. This page describes how to create and use p12 keys of service accounts for the Google Cloud. 

## Install pyca/cryptography

The [pyca/cryptography](https://cryptography.io/en/latest/) library (version >= `2.5`) allows the gcloud CLI to decode the p12 format key files that identify a service account. Because it includes cryptographical routines, pyca/cryptography is not distributed with the gcloud CLI. 

If your system has `pip`, the command-line interface to the [Python Package Index](https://pypi.python.org/pypi/pip), installed, to install `pyca/cryptography`, run the following command. Refer to [Installation Instruction](https://cryptography.io/en/latest/#installation) for more information. 
    
    
    python -m pip install cryptography

**Note:** `python` should point to a python interpreter used by gcloud (shown by the following command). 
    
    
    gcloud info --format="text(basic.python_location)"

**Warning:** If you are running gcloud CLI of a version lower than `359.0.0`, install [pyOpenSSL](https://www.pyopenssl.org/en/stable/) instead. 

## CLOUDSDK_PYTHON_SITEPACKAGES=1

Once pyca/cryptography is installed, you will need to set the `CLOUDSDK_PYTHON_SITEPACKAGES` environment variable to `1`. This environment variable setting tells the gcloud CLI that it should look outside of its own `google-cloud-sdk/lib` directory for libraries to include. It is generally safe to set `CLOUDSDK_PYTHON_SITEPACKAGES=1`, but if something stops working you may need to undo it. 

## Creating a service account

To create a new service account and download a p12 key file, follow the steps in [Creating service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys). 

This key file should be considered a secret, and you should take precautions to make sure that it is not accessible by untrusted parties. On unix-like systems, you can ensure that a file is not visible to other remotely connected users (other than a root user) by using the following command. 
    
    
    chmod 0600 YOUR_KEY_FILE.p12

## Using your service account with the gcloud CLI

Service account credentials can be enabled by using [`gcloud auth activate-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account). 

To use your service account with the gcloud CLI, run `gcloud auth activate-service-account` and pass it the path to your key file with the required `--key-file` flag, and give it an account as a positional argument. 

The account you use should be the email for the service account listed in the Google Cloud console, but it will not be verified; it only helps you remember which account you are using. 
    
    
    gcloud auth activate-service-account --key-file ~/mykeys/my_key_file.p12 my_service_account@developer.gserviceaccount.com
    Activated service account credentials for my_service_account@developer.gserviceaccount.com.

**WARNING:** The `gcloud auth activate-service-account` will make a copy of your private key and store it in `$HOME/.config/gcloud/legacy_credentials/my_service_account@developer.gserviceaccount.com/private_key.p12` and `$HOME/.config/gcloud/credentials.db`. It will be created with `0600` permissions (read/write for your own user only), and everything stored in `$HOME/.config/gcloud` should be considered a secret already. To reliably and confidently delete any authentication data stored by the gcloud CLI, one only has to delete `$HOME/.config/gcloud`. Secure management of the key file downloaded from the Google Cloud console is left to the user. When in doubt, revoke the key in the Google Cloud console. 

Now that the service account has been activated, it can be seen in the credentials list. 
    
    
    gcloud auth list
            Credentialed Accounts
    ACTIVE    ACCOUNT
    *         my_service_account@developer.gserviceaccount.com
    
    To set the active account, run:
        $ gcloud config set account my_service_account@developer.gserviceaccount.com

Back to top

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
