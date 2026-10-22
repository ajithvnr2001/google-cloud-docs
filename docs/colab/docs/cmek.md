---
url: https://docs.cloud.google.com/colab/docs/cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:25.398436+00:00
---

# Use customer-managed encryption keys (CMEK)  |  Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use customer-managed encryption keys (CMEK)

By default, Colab Enterprise encrypts customer content at rest. Colab Enterprise handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Colab Enterprise. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Colab Enterprise resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

This guide describes how to use CMEK for Colab Enterprise.

For more information about how to use CMEK for Gemini Enterprise Agent Platform, see the [Agent Platform CMEK page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/cmek).

## CMEK for Colab Enterprise

You can use CMEK to encrypt Colab Enterprise runtimes, notebook files (notebooks), and Data Science Agent data.

### Runtimes

When you run code in a Colab Enterprise notebook, a runtime runs the code on one or more virtual machine (VM) instances managed by Colab Enterprise. When you enable CMEK for your Colab Enterprise runtimes, the key that you designate, rather than a key managed by Google, is used to encrypt data on these VMs. The CMEK key encrypts the following kinds of data:

  * The copy of your code on the VMs.
  * Any data that gets loaded by your code.
  * Any temporary data that gets saved to the local disk by your code.



You can start, stop, and upgrade your runtime without affecting its CMEK encryption.

In general, the CMEK key does _not_ encrypt metadata associated with your operation, like the runtime's name or your notebook's name and region. This metadata is always encrypted using Google's default encryption mechanism.

### Notebooks

Colab Enterprise notebooks are stored in Dataform repositories. When you create a notebook, Colab Enterprise automatically creates a hidden Dataform repository where the notebook is stored. Because the repository is hidden, you can't modify its encryption settings as you would with other Dataform repositories.

To use CMEK for your notebooks, you must set a default Dataform CMEK key for the Google Cloud project that will contain your notebooks. After you set a default Dataform CMEK key, Dataform applies the key to all new repositories created in the Google Cloud project by default, including any hidden repositories created for storing your notebooks.

The default Dataform CMEK key isn't applied to existing repositories. Therefore, if you already have notebooks in that project, they won't be encrypted by the default Dataform CMEK key. To use CMEK with a notebook that was created before you set your project's default Dataform CMEK key, you can save the notebook file as a new Colab Enterprise notebook.

To learn more about default Dataform CMEK keys, see [Use Dataform default CMEK keys](https://docs.cloud.google.com/dataform/docs/cmek#default-keys).

To use CMEK for your notebooks, see [Set a default Dataform CMEK key](https://docs.cloud.google.com/dataform/docs/cmek#set-default-key).

### Data Science Agent

The Data Science Agent automatically uses the Cloud KMS key configured on your default runtime template to encrypt session data at rest, such as conversation history. You don't need to configure CMEK separately for the Data Science Agent.

#### Key changes and removals for the Data Science Agent

When you change or remove the CMEK key on your default runtime template (or delete a CMEK-configured default runtime template), the encryption settings are applied to the Data Science Agent when you start a new session. The impact on your Data Science Agent data and session depends on the type of change:

  * **Changing the key** : Data from previous sessions is deleted, and new sessions are encrypted with the updated key.
  * **Removing the key** : Data from previous sessions is deleted, and subsequent sessions use Google default encryption (unless restricted by organization policy).
  * **Key unavailability** : If the Cloud KMS key is disabled, deleted, or permissions are revoked, the Data Science Agent cannot process requests until key access is restored.
  * **Organization policy** : If your organization enforces the `constraints/gcp.restrictNonCmekServices` constraint for `aiplatform.googleapis.com`, you must configure a Cloud KMS key on your default runtime template before you can use the Data Science Agent.

**Note:** Before modifying or removing the CMEK key on a default runtime template, ensure users have saved any code or analysis they want to keep from their Data Science Agent chat sessions into their notebooks, as previous session data is permanently deleted upon key changes.

## Supported keys

Colab Enterprise supports the following types of CMEK keys:

  * [Cloud KMS software keys](https://docs.cloud.google.com/kms/docs/protection-levels#software)
  * [Cloud Hardware Security Module (HSM) keys](https://docs.cloud.google.com/kms/docs/hsm)



Key availability varies by key type and region. For more information about the geographical availability of CMEK keys, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## Restrictions and limitations

Colab Enterprise supports CMEK with the following restrictions and limitations:

  * **Encryption key quota** : The default quota in Agent Platform is one encryption key per project and region. If you need to register more than one key for a region in your project, contact your Google account team to request a quota increase for CMEK configurations, providing a justification for why you need more than one key.
  * **Data Science Agent configuration** : The Data Science Agent doesn't have a separate CMEK configuration. It only inherits CMEK settings from the **default runtime template** for your project and region. Custom non-default runtime templates don't apply to the Data Science Agent.
  * **Data Science Agent session updates** : Changes to the CMEK configuration on the default runtime template (such as updating or removing the key) take effect when a new session is initiated with the Data Science Agent. Previous session data is deleted and the updated encryption setting is applied upon starting the next session.



### Cloud KMS quotas and Colab Enterprise

When you use CMEK in Colab Enterprise, your projects can consume Cloud KMS cryptographic requests quotas. Encryption and decryption operations using CMEK keys affect Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

## Configure CMEK for your runtimes

The following sections describe how to create a key ring and key in Cloud Key Management Service, grant Colab Enterprise encrypter and decrypter permissions for your key, and create a runtime template configured to use CMEK. Any runtime that Colab Enterprise generates from this runtime template uses CMEK encryption.

### Before you begin

This guide assumes that you use two separate Google Cloud projects to configure CMEK for Colab Enterprise runtimes:

  * A project for managing your encryption key (referred to as the "Cloud KMS project").
  * A project for accessing your Colab Enterprise resources and interacting with any other Google Cloud products that you need (referred to as the "Notebook project").



This recommended setup supports a [_separation of duties_](https://docs.cloud.google.com/kms/docs/separation-of-duties).

Alternatively, you can use a single Google Cloud project for the whole guide. To do so, use the same project for all of the following tasks that refer to the Cloud KMS project and the tasks that refer to the Notebook project.

#### Set up the Cloud KMS project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud KMS API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud KMS API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)




#### Set up the Notebook project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=ml.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=ml.googleapis.com)




#### Set up the Google Cloud CLI

The gcloud CLI is required for some steps in this guide and optional for others. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

### Create a key ring and key

Follow the [Cloud KMS guide to creating symmetric keys](https://docs.cloud.google.com/kms/docs/creating-keys) to create a key ring and a key. When you create your key ring, specify [a region that supports Colab Enterprise operations](https://docs.cloud.google.com/colab/docs/locations) as [the key ring's location](https://docs.cloud.google.com/kms/docs/locations). Colab Enterprise only supports CMEK when your runtime (or Data Science Agent) and key use the same region. You must not specify a dual-regional, multi-regional, or global location for your key ring.

Make sure to create your key ring and key in your Cloud KMS project.

### Grant Colab Enterprise permissions

To use CMEK for your resources, you must grant Colab Enterprise permission to encrypt and decrypt data using your key. Colab Enterprise uses a [Google-managed service agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#service-agents) to run operations using your resources. This service account is identified by an email address with the following format: `service-PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com`.

To find the appropriate service account for your Notebook project, go to the **IAM** page in the Google Cloud console and find the member that matches this email address format, with the [project number](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) for your Notebook project replacing the NOTEBOOK_PROJECT_NUMBER variable. The service account also has the name `Vertex AI Service Agent`.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

Make note of the email address for this service account, and use it in the following steps to grant it permission to encrypt and decrypt data using your key. You can grant permission by using the Google Cloud console or by using the Google Cloud CLI:

###  Google Cloud console 

  1. In the Google Cloud console, **Click Security** and select **Key Management**. This will take you to **Cryptographic Keys** page and select your Cloud KMS project.

[Go to the Cryptographic Keys page](https://console.cloud.google.com/security/kms?project=_)

  2. Click the name of the key ring that you created in a preceding section of this guide to go to the **Key ring details** page.

  3. Select the checkbox for the key that you created in a preceding section of this guide. If an info panel labeled with the name of your key is not already open, click **Show info panel**.

  4. In the info panel, click **person_add Add member** to open the **Add members to " KEY_NAME"** dialog. In this dialog, do the following:

     1. In the **New members** box, enter the service account email address that you made a note of in the preceding section: `service-NOTEBOOK_PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com`

     2. In the **Select a role** drop-down list, click **Cloud KMS** and then select the **Cloud KMS CryptoKey Encrypter/Decrypter** role.

     3. Click **Save**.




###  gcloud 

Run the following command:
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
      --keyring=KEY_RING_NAME \
      --location=REGION \
      --project=KMS_PROJECT_ID \
      --member=serviceAccount:service-NOTEBOOK_PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com \
      --role=roles/cloudkms.cryptoKeyEncrypterDecrypter

In this command, replace the following placeholders:

  * KEY_NAME: The name of the key that you created in a preceding section of this guide.
  * KEY_RING_NAME: The key ring that you created in a preceding section of this guide.
  * REGION: The region where you created your key ring.
  * KMS_PROJECT_ID: The ID of your Cloud KMS project.
  * NOTEBOOK_PROJECT_NUMBER: The project number of your Notebook project, which you noted in the preceding section as part of a service account email address.



### Configure a runtime template with the KMS key

When you create a new CMEK-supported resource you can specify your key as one of the create parameters. To create a Colab Enterprise runtime, you create a runtime template with your CMEK key specified as a parameter. Any runtime that Colab Enterprise generates from this runtime template uses CMEK encryption.

To create a runtime template by using the Google Cloud console, you specify the key in the **Create new runtime template** dialog. Do the following:

  1. In the Google Cloud console, go to the Colab Enterprise **Runtime templates** page. 

[Go to Runtime templates](https://console.cloud.google.com/agent-platform/colab/runtime-templates)

  2. Click add_box **New template**. 

The **Create new runtime template** dialog appears.

  3. In the **Configure compute** section, in **Encryption** , select **Cloud KMS key**. 

  4. For **Key type** , select **Cloud KMS** , and then, in the next field, select your customer-managed encryption key. 

  5. Complete the rest of the instance creation dialog, and then click **Create**. 

Your runtime template appears in the list on the **Runtime templates** tab. 




### Configure CMEK for the Data Science Agent

To enable CMEK for the Data Science Agent, configure your Cloud KMS key on the **default runtime template** for your project and region. The Data Science Agent only inherits encryption configurations from the default runtime template, not from custom non-default templates.

To configure CMEK for the Data Science Agent, follow the steps in Configure a runtime template with the KMS key when creating or editing the default runtime template for your region.

## What's next

  * To use CMEK for your notebooks, see [Set a default Dataform CMEK key](https://docs.cloud.google.com/dataform/docs/cmek#set-default-key).
  * Learn how to [use the Data Science Agent](https://docs.cloud.google.com/colab/docs/use-data-science-agent).
  * Learn more about [CMEK on Google Cloud](https://docs.cloud.google.com/kms/docs/cmek).
  * Learn [how to use CMEK with other Google Cloud products](https://docs.cloud.google.com/kms/docs/use-keys-google-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
