---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in/
title: Sign in \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:40.059293+00:00
---

# Sign in  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Sign in Stay organized with collections  Save and categorize content based on your preferences. 

This page covers how to access and manage your workloads and resources within Google Distributed Cloud (GDC) air-gapped appliance. It describes how to authenticate, generate kubeconfig files for both a Management API server and a Kubernetes cluster, and manage session inactivity. Understanding these processes ensures secure and reliable access to your projects and workloads.

Access your workloads through the GDC console or the gdcloud CLI.

## Sign in

To sign in to the GDC console or a cluster, work through the following steps:

### Console

Open the following URL in a new browser tab to access the GDC air-gapped appliance user interface (UI):
    
    
    https://GDC_URL
    

Replace `GDC_URL` with the domain name you use to access GDC that the Infrastructure Operator (IO) provides. When opening any URL for the first time, GDC redirects you to your identity provider login page if the Infrastructure Operator (IO) configured the page.

For example, the following page displays after signing in to the Console for an organization named `org-1: ![Console showing welcome screen for org-1 project.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/images/login.png)

### CLI

You can sign in to any cluster that you have permission to access. The CLI login process for all clusters is the same. You must only provide the cluster name and its related `kubeconfig` file, and log in separately to each cluster.

Before you sign in, ensure you do the following:

  * Download the gdcloud CLI binary and install it in your system. For more information, see [Download the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download).
  * Set up and initialize the gdcloud CLI default configuration. Make sure to set the correct organization URL, which is used to fetch the login config endpoint. For more information, see [gdcloud CLI installation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install).
  * Install the `kubectl` CLI, as described in [Install components](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install#install-components).
  * Install the authentication plugin `gdcloud-k8s-auth-plugin`. For more information, see [gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#before-you-begin).

**Important:** Run the next steps on your system with your user account and _not_ with the root account. The gdcloud CLI doesn't automatically open a browser while in root mode.

To sign in to a cluster, complete the following steps:

  1. Authenticate your gdcloud CLI instance to log in. There are two ways to authenticate:

     * **Standard browser login:** Use this authentication flow when logging in from a browser.
           
           gdcloud auth login
           

     * **Secondary device login:** Use this authentication flow if your primary device does not have a browser available. This flow starts the login on the primary device with no browser access and continues the login with the secondary device that has browser access.

       1. Initiate the login on your primary device with no browser:
              
              gdcloud auth login --no-browser
              

The command in the primary device prints another `gdcloud` command that you must run on the secondary device in step c.

       2. Repeat step 1 of Log in to a cluster to download the certificate on the secondary device.

       3. Complete the login on the secondary device by entering the command printed on the primary device in step a.

This action opens a browser to log in to the configured identity provider (IdP). Provide the user and password that you set during the initial gdcloud CLI setup to log in.

**Note:** If you see an error `x509: certificate signed by unknown authority`, your workstation does not trust the CA certificate used in GDC. Follow your organization's procedure to check the trusted certification store for your workstation.
  2. Export your user identity `kubeconfig` file as a variable:
         
         export KUBECONFIG=/tmp/admin-kubeconfig-with-user-identity.yaml
         

  3. Generate a `kubeconfig` file with your user identity:
         
         gdcloud clusters get-credentials CLUSTER_NAME
         

**Note:** The list of available cluster names is available in the login config URL:   
`https://GDC_URL/.well-known/login-config`

A `kubeconfig` file is generated with your user identity. The following YAML file shows an example:
         
         apiVersion: v1
         clusters:
         - cluster:
             certificate-authority-data: <REDACTED>
             server: https://10.200.0.32:443
           name: cluster-name
         contexts:
         - context:
             cluster: cluster-name
             user: cluster-name-anthos-default-user
           name: cluster-name-cluster-name-anthos-default-user
         current-context: cluster-name-cluster-name-anthos-default-user
         kind: Config
         preferences: {}
         users:
         - name: cluster-name-anthos-default-user
           user:
             exec:
                 apiVersion: client.authentication.k8s.io/v1
                 args:
                 - --audience=root-admin
                 command: gdcloud-k8s-auth-plugin
                 env: null
                 installHint: Run 'gdcloud components install gdcloud-k8s-auth-plugin' to use plugin
                 interactiveMode: Never
                 provideClusterInfo: false
         

  4. To verify that you can access the cluster, log in with the generated `kubeconfig` file with a user identity:
         
         kubectl --kubeconfig /tmp/admin-kubeconfig-with-user-identity.yaml version
         




## Sign out

To sign out of the GDC console, do the following:

### Console

Click logout **Logout** in the menu bar.

![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/images/pa_logout.png)

### CLI

Log out from the CLI:
    
    
    gdcloud auth revoke
    

## Manually generate kubeconfig file

If you're managing resources with the kubectl CLI by calling KRM APIs directly, you must generate the kubeconfig file for the cluster that hosts your resource, depending on the resource type you're managing. Visit the resource's documentation to determine the kubeconfig file you need.

Complete the applicable setup based on your resource type.

### Management API server resources

Complete the following steps to generate your kubeconfig file for the Management API server:

  1. Set the `MANAGEMENT_API_SERVER` environment variable:
         
         export MANAGEMENT_API_SERVER="root-admin"
         

  2. Generate the Management API server kubeconfig file, and validate the credentials:
         
         export KUBECONFIG=${HOME}/${MANAGEMENT_API_SERVER:?}-kubeconfig.yaml
         rm ${KUBECONFIG:?}
         gdcloud clusters get-credentials ${MANAGEMENT_API_SERVER:?}
         [[ $(kubectl config current-context) == *${MANAGEMENT_API_SERVER:?}* ]] && echo "Success. Your kubeconfig is at $KUBECONFIG" || echo "Failure"
         

The command `rm ${KUBECONFIG:?}` removes the existing kubeconfig file in the home directory. When you generate a new kubeconfig file, it overwrites the existing one. If you don't want to overwrite or remove the existing file, back it up in another safe location.




### Kubernetes cluster resources

Complete the following steps to generate your kubeconfig file for the bare metal Kubernetes cluster:

  1. Set the `KUBERNETES_CLUSTER` environment variable:
         
         export KUBERNETES_CLUSTER="root-infra"
         

  2. Generate the Kubernetes cluster kubeconfig file, and validate the credentials:
         
         export KUBECONFIG=${HOME}/${KUBERNETES_CLUSTER:?}-kubeconfig.yaml
         rm ${KUBECONFIG:?}
         gdcloud clusters get-credentials ${KUBERNETES_CLUSTER:?}
         [[ $(kubectl config current-context) == *${KUBERNETES_CLUSTER:?}* ]] && echo "Success. Your kubeconfig is at $KUBECONFIG" || echo "Failure"
         

The command `rm ${KUBECONFIG:?}` removes the existing kubeconfig file in the home directory. When you generate a new kubeconfig file, it overwrites the existing one. If you don't want to overwrite or remove the existing file, back it up in another safe location.




## Session inactivity logout

After fifteen or more minutes of inactivity in a session, the GDC console and gdcloud CLI logs you out. GDC considers session inactivity as a period during an open session with no active engagement from you, such as no cursor or keyboard movement. An active session lasts up to twelve hours with user activity.

### Console

For session inactivity, the GDC console logs you out. Two minutes before the GDC console logs you out for inactivity, you receive a dialog that cautions you of the logout:

![Console UI showing dialog with a timer of 99 seconds before logging out user for inactivity.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/iam-inactivity-warning-dialog.png)

After logging you out for inactivity, you see the following screen:

![Console UI showing login screen with a banner containing text on the session log out: 'You have been logged out of the system because your session was inactive for too long. Please log in again or reach out to your administrator for assistance.'](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/iam-session-inactivity-console-ui.png)

To log back in to the GDC console, select your identity provider and add your login credentials. If you use a service, such as the monitoring dashboard, and the GDC console logs you out for inactivity, log back in to gain access.

### CLI

For session inactivity, the gdcloud CLI logs you out. After the gdcloud CLI logs you out, and you attempt to run a command, you receive an authorization error:
    
    
    Error: error when creating kube client: unable to create k8sclient: Unauthorized
    

To log back in to the gdcloud CLI, follow the CLI steps in [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#cli).

**Note:** Commands that do not make API requests, such as `gdcloud init` and `gdcloud config`, are not counted towards your activity. When using these commands, the gdcloud CLI logs you out regardless.

### kubectl

The gdcloud CLI expires your kubeconfig files after session inactivity. If you attempt to run a `kubectl` command after inactivity, you receive an authorization error:
    
    
    error: You must be logged in to the server (Unauthorized)
    

To log back in and use your kubeconfig file, follow the CLI steps in [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#cli). For every session timeout, you must regenerate your kubeconfig files.

## Monitor sign in and new user activities

Activities such as signing in are exported as audit logs. For more information about viewing audit logs, see [Audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
