---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in/
title: Sign in \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:37.740765+00:00
---

# Sign in  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Sign in Stay organized with collections  Save and categorize content based on your preferences. 

This page covers how to access and manage your workloads and resources within Google Distributed Cloud (GDC) air-gapped. It describes how to authenticate, generate kubeconfig files for zonal and global resources, and manage session inactivity. Understanding these processes ensures secure and reliable access to your projects and workloads.

This page is for audiences within the platform administrator group (such as IT admins) or the application operator group (such as application developers) who want to use GDC resources. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

You can access workloads using the GDC console, gdcloud CLI, or kubectl CLI.

## Authenticate your account for access

To sign in to the GDC console or a cluster, work through the following steps:

###  Console 

Open the following URL in a new browser tab to access the Distributed Cloud user interface (UI):
    
    
    https://GDC_URL
    

Replace `GDC_URL` with the domain name you use to access Distributed Cloud that the Infrastructure Operator (IO) provides. When opening any URL for the first time, Distributed Cloud redirects you to your identity provider login page if the Infrastructure Operator (IO) configured the page.

For example, the following image signs in to the console UI for an organization named `org-1`:

![Console UI showing welcome screen for org-1 project.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/images/login.png)

###  gdcloud 

When you sign in to the gdcloud CLI, use the [`gdcloud auth login` command](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#sign-in-with-idp) to authenticate a principal to the gdcloud CLI. The gdcloud CLI uses that principal for authentication and authorization to manage Google Cloud resources and services.

Before you sign in, ensure you do the following:

  * Download the gdcloud CLI binary and install it in your system. For more information, see [Download the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download).
  * Set up and initialize the gdcloud CLI default configuration. Make sure to set the correct organization URL, which is used to fetch the login config endpoint. For more information, see [gdcloud CLI installation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).
  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).
  * Install the authentication plugin `gdcloud-k8s-auth-plugin`. For more information, see [gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#before-you-begin).

**Important:** Run the next steps on your system with your user account and _not_ with the root account. The gdcloud CLI doesn't automatically open a browser while in root mode.

To sign in to a Management API server or Kubernetes cluster, complete the following steps:

  * **Management API server** :


  1. Export the path on where you want to store the Management API server kubeconfig file:
         
         export KUBECONFIG=MANAGEMENT_API_SERVER
         

Replace MANAGEMENT_API_SERVER with the path to the directory of where to store the kubeconfig file.

  2. Authenticate your gdcloud CLI instance to sign in. There are two ways to authenticate:

     * **Standard browser login:** Use this authentication flow when logging in from a browser.
           
           gdcloud auth login
           

     * **Secondary device login:** Use this authentication flow if your primary device does not have a browser available. This flow starts the login on the primary device with no browser access and continues the login with the secondary device that has browser access.

Initiate the login on your primary device with no browser:
           
           gdcloud auth login --no-browser
           

The `KUBECONFIG` environment variable updates with the kubeconfig files for all API servers and clusters in the organization. If the `KUBECONFIG` variable isn't set, the kubectl CLI uses the default kubeconfig file stored in `$HOME/.kube/config`.

To skip editing the kubeconfig files, add the `--skip-kubeconfig-update` flag to your command. For example:
           
           gdcloud auth login --no-browser --skip-kubeconfig-update
           

Copy the gdcloud CLI command output that is printed out, and run it on a machine with browser access.

  3. Follow the instructions on the web page to complete the login process.

On successful login completion, the browser displays the message **Authentication successful. Please close this window**.

  4. Follow the instructions on the terminal. On successful login, the terminal displays the message: **You are now logged in**.

**Note:** If you see an error `x509: certificate signed by unknown authority`, your workstation does not trust the CA certificate used in GDC. Follow your organization's procedure to check the trusted certification store for your workstation.**Warning:** Using `--login-config-cert` with an unverified certificate makes you vulnerable to man-in-the-middle attacks. Ensure that you rely only on your workstation's trust store instead of trusting a CA certificate from unknown sources.


  * **Kubernetes cluster** :


  1. Authenticate your gdcloud CLI instance to sign in. There are two ways to authenticate:

     * **Standard browser login:** Use this authentication flow when logging in from a browser.
           
           gdcloud auth login
           

     * **Secondary device login:** Use this authentication flow if your primary device does not have a browser available. This flow starts the login on the primary device with no browser access and continues the login with the secondary device that has browser access.

       1. Initiate the login on your primary device with no browser:
              
              gdcloud auth login --no-browser
              

The command in the primary device prints another `gdcloud` command that you must run on the secondary device in step c.

       2. Repeat step 1 to download the certificate on the secondary device.

       3. Complete the login on the secondary device by entering the command printed on the primary device in step a.

This action opens a browser to sign in to the configured identity provider (IdP). Provide the user and password that you set during the initial gdcloud CLI setup to sign in.

**Note:** If you see an error `x509: certificate signed by unknown authority`, your workstation does not trust the CA certificate used in GDC. Follow your organization's procedure to check the trusted certification store for your workstation.**Warning:** Using `--login-config-cert` with an unverified certificate makes you vulnerable to man-in-the-middle attacks. Ensure that you rely only on your workstation's trust store instead of trusting a CA certificate from unknown sources.
  2. Export your user identity kubeconfig file as a variable:
         
         export KUBECONFIG=/tmp/CLUSTER_NAME-ZONE-kubeconfig-with-user-identity.yaml
         

  3. Generate a kubeconfig file for a zonal cluster with your user identity:
         
         gdcloud clusters get-credentials CLUSTER_NAME --zone ZONE
         

Replace `ZONE` with the zone name.

**Important:** The global apiserver is not bound to any zone, so run this command without the `zone` flag instead to generate the kubeconfig for the global apiserver: `gdcloud clusters get-credentials global-api`.**Note:** The list of available cluster names is available in the login config URL:   
`https://GDC_URL/.well-known/login-config`.

A kubeconfig file is generated with your user identity. The following YAML file shows an example:
         
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
         

  4. To verify that you can access the cluster, sign in with the generated kubeconfig file with a user identity:
         
         kubectl --kubeconfig /tmp/admin-kubeconfig-with-user-identity.yaml version
         




## Sign out

To sign out of the GDC console, do the following:

###  Console 

Click logout **Logout** in the menu bar.

![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/pa_logout.png)

###  gdcloud 

Log out from the CLI:
    
    
    gdcloud auth revoke
    

**Note:** Any page that relies on Kubernetes resources doesn't work. Chrome debug console shows "forbidden" errors in responses. This error occurs because the user has no permissions granted and is not bound to any roles. See [Grant access to resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings) for instructions to grant permissions.

## Manually generate kubeconfig file

If you're managing resources with the kubectl CLI by calling KRM APIs directly, you must generate the kubeconfig file for the cluster or API server that hosts your resource, depending on the resource type you're managing.

You must also be aware of your GDC universe configuration to determine the zones to which you intend to deploy your zonal resources, or the global API server for global resources. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).

Determine whether the resource you're manipulating is a global or zonal resource. Visit the resource's dedicated documentation for help if you're unsure.

Complete the applicable setup based on your resource type.

### Zonal Management API server resources

Complete the following steps to generate your kubeconfig file for the zonal Management API server:

  1. View all available zones:
         
         gdcloud zones list
         

Note the name of the zone that hosts your custom resource.

  2. Set the `ZONE` environment variable to the zone that hosts your zonal resources:
         
         export ZONE="ZONE"
         

Replace `ZONE` with the zone name.

  3. Set the `MANAGEMENT_API_SERVER` environment variable:
         
         export MANAGEMENT_API_SERVER="ORG_NAME-admin"
         

Replace `ORG_NAME` with the name of your organization, such as `org-1`.

  4. Generate the Management API server kubeconfig file for the targeted zone, and validate the credentials:
         
         export KUBECONFIG=${HOME}/${MANAGEMENT_API_SERVER:?}-kubeconfig.yaml
         rm ${KUBECONFIG:?}
         gdcloud clusters get-credentials ${MANAGEMENT_API_SERVER:?} --zone ${ZONE:?}
         [[ $(kubectl config current-context) == *${MANAGEMENT_API_SERVER:?}* ]] && echo "Success. Your kubeconfig is at $KUBECONFIG" || echo "Failure"
         

The command `rm ${KUBECONFIG:?}` removes the existing kubeconfig file in the home directory. When you generate a new kubeconfig file, it overwrites the existing one. If you don't want to overwrite or remove the existing file, back it up in another safe location.




### Zonal Kubernetes cluster resources

Complete the following steps to generate your kubeconfig file for the zonal Kubernetes cluster:

  1. View all available zones:
         
         gdcloud zones list
         

Note the name of the zone that hosts your custom resource.

  2. Set the `ZONE` environment variable to the zone that hosts your Kubernetes cluster:
         
         export ZONE="ZONE"
         

Replace `ZONE` with the zone name.

  3. Set the `KUBERNETES_CLUSTER` environment variable:
         
         export KUBERNETES_CLUSTER="KUBERNETES_CLUSTER_NAME"
         

Replace `KUBERNETES_CLUSTER_NAME` with the name of your Kubernetes cluster.

  4. Generate the Kubernetes cluster kubeconfig file for the targeted zone variable, and validate the credentials:
         
         export KUBECONFIG=${HOME}/${KUBERNETES_CLUSTER:?}-kubeconfig.yaml
         rm ${KUBECONFIG:?}
         gdcloud clusters get-credentials ${KUBERNETES_CLUSTER:?} --zone ${ZONE:?}
         [[ $(kubectl config current-context) == *${KUBERNETES_CLUSTER:?}* ]] && echo "Success. Your kubeconfig is at $KUBECONFIG" || echo "Failure"
         

The command `rm ${KUBECONFIG:?}` removes the existing kubeconfig file in the home directory. When you generate a new kubeconfig file, it overwrites the existing one. If you don't want to overwrite or remove the existing file, back it up in another safe location.




### Global API server resources

Complete the following steps to generate your kubeconfig file for the global API server:

  1. Set the `GLOBAL_API_SERVER` environment variable:
         
         export GLOBAL_API_SERVER="global-api"
         

  2. Generate the global API server kubeconfig file, and validate the credentials:
         
         export KUBECONFIG=${HOME}/${GLOBAL_API_SERVER:?}-kubeconfig.yaml
         rm ${KUBECONFIG:?}
         gdcloud clusters get-credentials ${GLOBAL_API_SERVER:?}
         [[ $(kubectl config current-context) == *${GLOBAL_API_SERVER:?}* ]] && echo "Success. Your kubeconfig is at $KUBECONFIG" || echo "Failure"
         

The command `rm ${KUBECONFIG:?}` removes the existing kubeconfig file in the home directory. When you generate a new kubeconfig file, it overwrites the existing one. If you don't want to overwrite or remove the existing file, back it up in another safe location.




## Session inactivity logout

After fifteen or more minutes of inactivity in a session, the GDC console and gdcloud CLI logs you out. Distributed Cloud considers session inactivity as a period during an open session with no active engagement from you, such as no cursor or keyboard movement. An active session lasts up to twelve hours with user activity.

### Console

For session inactivity, the GDC console logs you out. Two minutes before the GDC console logs you out for inactivity, you receive a dialog that cautions you of the logout:

![Console UI showing dialog with a timer of 99 seconds before logging out user for inactivity.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/images/iam-inactivity-warning-dialog.png)

After logging you out for inactivity, you see the following screen:

![Console UI showing login screen with a banner containing text on the session log out: 'You have been logged out of the system because your session was inactive for too long. Please log in again or reach out to your administrator for assistance.'](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/images/iam-session-inactivity-console-ui.png)

To log back in to the GDC console, select your identity provider and add your login credentials. If you use a service, such as the monitoring dashboard, and the GDC console logs you out for inactivity, log back in to gain access.

###  gdcloud 

For session inactivity, the gdcloud CLI logs you out. After the gdcloud CLI logs you out, and you attempt to run a command, you receive an authorization error:
    
    
    Error: error when creating kube client: unable to create k8sclient: Unauthorized
    

To log back in to GDC, follow the CLI steps in [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli).

If you log back in to GDC through a Management API server, your kubeconfig file automatically updates. To avoid your kubeconfig file updating, use the `--skip-kubeconfig-update` flag in the `gdcloud auth login` command.

**Note:** Commands that don't make API requests, such as `gdcloud init` and `gdcloud config`, are not counted towards your activity. When using these commands, the gdcloud CLI logs you out regardless.

### kubectl

The gdcloud CLI expires your kubeconfig files after session inactivity. If you attempt to run a `kubectl` command after inactivity, you receive an authorization error:
    
    
    error: You must be logged in to the server (Unauthorized)
    

To log back in and use your kubeconfig file, follow the CLI steps in [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli). For every session timeout, you must regenerate your kubeconfig files.

## Monitor sign in and new user activities

Activities such as signing in are exported as audit logs. For more information about viewing audit logs, see [Audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/audit-iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
