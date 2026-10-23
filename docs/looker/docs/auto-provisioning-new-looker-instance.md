---
url: https://docs.cloud.google.com/looker/docs/auto-provisioning-new-looker-instance/
title: Auto-provisioning a new instance \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:14.960116+00:00
---

# Auto-provisioning a new instance  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/auto-provisioning-new-looker-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Auto-provisioning a new instance Stay organized with collections  Save and categorize content based on your preferences. 

Optionally, at the startup of a new Looker customer-hosted instance, you can automatically provision the instance with a license key, a host URL, and an initial user account.

## Automatically provisioning a new instance with an email user

On initial startup, Looker scans the `looker` directory, where the JAR file resides, for a file that has the name `provision.yml`. The format for this file is as follows:
    
    
    license_key: "1234-5678-ABCD-EFGH-IJKL"
    host_url: "https://looker.mycompany.com"
    user:
      first_name: "Ariel"
      last_name: "Q"
      email: "arielq@altostrat.com"
      password: "password123"
    

If the Looker instance is brand new and has not been set up yet, it will be provisioned with the given license key and a user account with the provided information.

If the Looker has already been provisioned, the license key and host URL values will override whatever license key and host URL are set in the instance. The user info will be ignored. This approach is useful for updating a staging instance of Looker with a fresh copy of a production instance's internal database, while still maintaining a separate license key and URL for the staging server.

## Automatically provisioning a new instance with an API user

At the startup of a new Looker instance, you can provision an initial API user programmatically. You can provision an API user _or_ an email user, but Looker does not support provisioning both an API user and an email user at the same time.

### Generating API credentials

To provision an API user, generate a client ID and a client secret that Looker will read and save to the database. The requirements for these credentials are as follows:

  * The client ID must be 20 characters in length.
  * The client secret must be 24 characters in length.
  * Both strings must be able to be included in the body of a `POST` request; for this reason, we recommend that you use only alphanumeric characters for the client ID and client secret.



For example, Looker uses the following code to programmatically generate these credentials:
    
    
    require 'securerandom'
    
    TOKEN_SYMBOLS = "bcdfghjkmnpqrstvwxyzBCDFGHJKMNPQRSTVWXYZ23456789".freeze
    
    def generate_token(size)
      Array.new(size).map { TOKEN_SYMBOLS[SecureRandom.random_number(TOKEN_SYMBOLS.size)] }.join
    end
    

This code avoids ambiguous characters to make the strings less error-prone.

You can also use the `openssl` command to generate suitable strings:
    
    
    openssl rand -hex 10
    

The number at the end of the `openssl` command is the number of bytes in the string, so use `10` for the client ID and `12` for the client secret.

### Provisioning the API user

To provision an API user at startup, ensure you have a `provision.yml` file that includes your license key and host URL in the `looker` directory. For example:
    
    
    license_key: "1234-5678-ABCD-EFGH-IJKL"
    host_url: "https://looker.mycompany.com"
    

Create a file called `api-provision.yml` with the permissions `0600` in the `looker` directory that includes the API user information. For example:
    
    
    user:
      first_name: "Ariel"
      last_name: "Q"
      client_id: "M9hZb8vRh9bSZzdPxw42"
      client_secret: "NMnqBVbHqPsPzTvbZk6xZfV3"
    

> We recommend that you store these credentials in a secret manager outside of this file, as this file will be removed on startup once the Looker instance has processed and created the user in the database.

At startup, if the instance has no users, Looker creates a Looker admin API user with these credentials and removes the `api-provision.yml` file from the disk.

Once you've signed in as the new user, you should create at least one additional admin user, since the provisioned API user will be automatically deleted by Looker.

## Automatic deletion of provisioned credentials

The provisioned API user is intended only for provisioning a new instance; it isn't intended to remain on your instance indefinitely.

Looker automatically deletes the provisioned API user after one of the following conditions has been met:

  * An admin user other than the provisioned API user has logged in to the instance.
  * 50 minutes have passed since the provisioned API user first logged in.



Therefore, it's important that you create at least one additional admin user immediately after you sign in as the provisioned user for the first time.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
