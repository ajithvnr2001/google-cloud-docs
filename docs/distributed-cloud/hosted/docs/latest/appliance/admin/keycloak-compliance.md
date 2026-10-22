---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/keycloak-compliance/
title: Manage Keycloak compliance \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:39.879901+00:00
---

# Manage Keycloak compliance  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/keycloak-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage Keycloak compliance Stay organized with collections  Save and categorize content based on your preferences. 

## Set password policies

By default, Keycloak has no policy on passwords, but this identity provider provides different password policies available through the Keycloak Admin Console, such as password expiration, minimum length, or special characters.

To set password policies, complete the following steps in the Keycloak Admin Console:

  1. In the navigation menu, click **Authentication**.
  2. Click the **Password Policy** tab.
  3. In the **Add policy** list, select the policy that you want to apply.
  4. Enter a **Policy value** corresponding to the policy that you selected.
  5. Click **Save**.



After saving the policy, Keycloak enforces the policy for new users and sets an update password action for existing users to ensure that they change their password the next time they log in.

## Configure two-factor authentication

Keycloak supports using [Yubikeys](https://www.yubico.com/products/) as 2nd factor authentication (2FA) devices through the FIDO2/WebAuthn protocol.

### Enable two-factor authentication

  1. Add **Webauthn Register** as a **Required Action** :

     1. Open to the `gdch` realm admin page using the local administrator credential.

     2. Open the **Authentication** page from the navigation menu and then open the **Required Actions** tab.

     3. Enable the **Webauthn Register** item:

![keycloak-webauthn-register.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/webauthn-register.png)

  2. Add **Webauthn Authentication** to the browser flow:

     1. Switch to the **Flows** tab and use the **Duplicate** button corresponding to **browser** flow name to copy the existing **browser** flow as a **Browser Yubikey** flow.

     2. Switch to the **Browser Yubikey** flow.

     3. Delete the **Browser Yubikey Browser - Conditional OTP** step.

     4. Click the **Add step** button corresponding to **Browser Yubikey forms** step and add **WebAuthn Authenticator**.

     5. Set the **WebAuthn Authenticator** item to **Required** :

![keycloak-yubikey-required.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/yubikey-required.png)

  3. Use the **Bind flow** button corresponding to **Browser Yubikey** flow and select **Browser Flow** :

![keycloak-yubikey-binding.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/yubikey-binding.png)

  4. Click **Save**.




### Register a Yubikey

  1. Open the GDC console to sign in.

  2. Use any user you created before in the `gdch` realm and enter the password.

  3. Click **Register** button:

![keycloak-yubikey-registration-1.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/yubikey-registration-1.png)

  4. Select the **USB security key** option:

![keycloak-yubikey-registration-2.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/yubikey-registration-2.png)

  5. Tap your inserted Yubikey:

![keycloak-yubikey-registration-3.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/yubikey-registration-3.png)

  6. Type in any name for your new security key:

![yubikey-label.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/yubikey-label.png)

  7. If you want to switch to another key or try this flow again, use the local administrator account to open the admin console and delete the Yubikey from the **Credential** tab of the user:

![yubikey-delete.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/yubikey-delete.png)




### Sign in with a Yubikey

  1. Sign out from the GDC console and open it again.

  2. Use the user that you have registered a Yubikey.

  3. After typing the password, select the Yubikey device:

![yubikey-login.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/yubikey-login.png)

  4. Tap your Yubikey device:

![yubikey-login-select.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak-yubikey/yubikey-login-select.png)




## Set login attempt threshold

Keycloak has brute force detection capabilities and can temporarily disable a user account if the number of login failures exceeds a specified threshold. This threshold can be configured to block an account from login either temporarily or permanently.

To set up the brute force detection, complete the following steps in the Keycloak Admin Console:

  1. In the navigation menu, click **Realm Settings.**
  2. Click the **Security Defenses** tab.
  3. Click the **Brute Force Detection** tab.
  4. Turn **Enabled** to on.
  5. Set values in the fields to match compliance requirements, such as the following:

     * **Max Login Failures**
     * **Wait Increment**
     * **Quick Login check**
     * **Max Wait**
     * **Failure Reset time**

![keycloak_brute_force.png](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/keycloak_brute_force.png)




## Connect to the GDC air-gapped appliance audit logging system

### Enable audit logging in Keycloak

To enable audit logging, use the Keycloak Admin Console to complete the following steps:

  1. In the navigation menu, click **Events.**
  2. Click the **Config** tab.
  3. In the **Login Events Settings** and the **Admin Events Settings** sections, set the **Save Events** toggle to **ON.**
  4. In the **Expiration** field, specify how long you want to keep events stored.
  5. In the **Saved Types** field, specify the different actions that you consider important for auditing.
  6. Click **Save**.
  7. Click the **Login Events** tab to see audit logs about user account operations.
  8. Click the **Admin Events** tab to see audit logs about any action that an admin performs within the admin console.



### Connect Keycloak audit logs to GDC air-gapped appliance

Keycloak provides built-in Service Provider Interfaces (SPIs) to enable audit logging. Audit logging export is configured in Keycloak to store a duplicate of the audit logs as files in the Pod. By default the logs are stored in the database). The GDC air-gapped appliance logging system uses the volume mount to pick up the log and parse the logs automatically.

### Change the Keycloak theme

A theme provides one or more types to customize different aspects of Keycloak. The types available are:

  * Account - Account management
  * Admin - Admin Console
  * Email - Emails
  * Login - Login forms
  * Welcome - Welcome page



To change the Keycloak theme, follow these steps:

  1. Log into the Keycloak Admin Console.
  2. Select your realm from the drop-down list.
  3. Click **Realm Settings**.
  4. Click the **Themes** tab.
  5. To set the theme for the master Admin Console, set the Admin Console theme for the master realm.
  6. To see the changes to the Admin Console, refresh the page.



## Root admin account management

Keycloak is bootstrapped with an initial root admin account with a trivial username and password of `admin/admin`. To ensure the protection and security of this root account, complete the following manual steps as soon as the bootstrapping is completed:

  * Set up a strong password for the root admin account
  * Set up 2FA for the root admin account



We recommend that you escrow the credential to the root admin account to a secure place.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
