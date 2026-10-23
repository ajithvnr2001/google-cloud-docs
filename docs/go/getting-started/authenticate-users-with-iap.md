---
url: https://docs.cloud.google.com/go/getting-started/authenticate-users-with-iap/
title: Authenticating users with Go \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:38.080932+00:00
---

# Authenticating users with Go  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/getting-started/authenticate-users-with-iap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Guides ](https://docs.cloud.google.com/go/docs/setup)



Send feedback 

#  Authenticating users with Go Stay organized with collections  Save and categorize content based on your preferences. 

Apps running on Google Cloud managed platforms such as [App Engine](https://docs.cloud.google.com/appengine/docs) can avoid managing user authentication and session management by using [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap) to control access to them. IAP can not only control access to the app, but it also provides information about the authenticated users, including the email address and a persistent identifier to the app in the form of new HTTP headers. 

## Objectives

  * Require users of your App Engine app to authenticate themselves by using IAP.

  * Access users' identities in the app to display the current user's authenticated email address.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [App Engine](https://docs.cloud.google.com/appengine/pricing)
  * [IAP](https://docs.cloud.google.com/iap/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  4. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  5. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Prepare your development environment](https://docs.cloud.google.com/go/docs/setup). 



## Setting up the project

  1. In your terminal window, clone the sample app repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git

  2. Change to the directory that contains the sample code:
         
         cd golang-samples/getting-started/authenticating-users




## Background

This tutorial uses IAP to authenticate users. This is only one of several possible approaches. To learn more about the various methods to authenticate users, see the Authentication concepts section. 

## The Hello `user-email-address` app

The app for this tutorial is a minimal Hello world App Engine app, with one non-typical feature: instead of "Hello world" it displays "Hello `user-email-address`", where `user-email-address` is the authenticated user's email address.

This functionality is possible by examining the authenticated information that IAP adds to each web request it passes through to your app. There are three new request headers added to each web request that reaches your app. The first two headers are plain text strings that you can use to identify the user. The third header is a cryptographically signed object with that same information.

  * `X-Goog-Authenticated-User-Email`: A user's email address identifies them. Don't store personal information if your app can avoid it. This app doesn't store any data; it just echoes it back to the user.

  * `X-Goog-Authenticated-User-Id`: This user ID assigned by Google doesn't show information about the user, but it does allow an app to know that a logged-in user is the same one that was previously seen before.

  * `X-Goog-Iap-Jwt-Assertion`: You can configure Google Cloud apps to accept web requests from other cloud apps, bypassing IAP, in addition to internet web requests. If an app is so configured, it's possible for such requests to have forged headers. Instead of using either of the plain text headers previously mentioned, you can use and verify this cryptographically signed header to check that the information was provided by Google. Both the user's email address and a persistent user ID are available as part of this signed header.




If you are certain that the app is configured so that only internet web requests can reach it, and that no one can disable the IAP service for the app, then retrieving a unique user ID takes only a single line of code:

`userID := r.Header.Get("X-Goog-Authenticated-User-ID")`

However, a resilient app should expect things to go wrong, including unexpected configuration or environmental issues, so we instead recommend creating a function that uses and verifies the cryptographically signed header. That header's signature cannot be forged, and when verified, can be used to return the identification. 

### Understanding the code

This section explains how the code works. If you want to run the app, you can skip ahead to the Deploy the app section.

  * The `go.mod` file defines a [Go module](https://blog.golang.org/using-go-modules) and the modules it depends on.
        
        module github.com/GoogleCloudPlatform/golang-samples/getting-started/authenticating-users
        
        go 1.25.0
        
        require (
        	cloud.google.com/go/compute/metadata v0.9.0
        	github.com/golang-jwt/jwt/v4 v4.5.2
        )
        
        require golang.org/x/sys v0.47.0 // indirect
        

  * The `app.yaml` file tells App Engine which language environment your code requires.
        
        runtime: go112

  * The app starts by importing packages and defining a `main` function. The `main` function registers an index handler and starts an HTTP server.
        
        // The authenticating-users program is a sample web server application that
        // extracts and verifies user identity data passed to it via Identity-Aware
        // Proxy.
        package main
        
        import (
        	"encoding/json"
        	"fmt"
        	"log"
        	"net/http"
        	"os"
        	"time"
        
        	"cloud.google.com/go/compute/metadata"
        	jwt "github.com/golang-jwt/jwt/v4"
        )
        
        // app holds the Cloud IAP certificates and audience field for this app, which
        // are needed to verify authentication headers set by Cloud IAP.
        type app struct {
        	certs map[string]string
        	aud   string
        }
        
        func main() {
        	a, err := newApp()
        	if err != nil {
        		log.Fatal(err)
        	}
        
        	http.HandleFunc("/", a.index)
        
        	port := os.Getenv("PORT")
        	if port == "" {
        		port = "8080"
        		log.Printf("Defaulting to port %s", port)
        	}
        
        	log.Printf("Listening on port %s", port)
        	if err := http.ListenAndServe(":"+port, nil); err != nil {
        		log.Fatal(err)
        	}
        }
        
        // newApp creates a new app, returning an error if either the Cloud IAP
        // certificates or the app's audience field cannot be obtained.
        func newApp() (*app, error) {
        	certs, err := certificates()
        	if err != nil {
        		return nil, err
        	}
        
        	aud, err := audience()
        	if err != nil {
        		return nil, err
        	}
        
        	a := &app{
        		certs: certs,
        		aud:   aud,
        	}
        	return a, nil
        }
        

  * The `index` function gets the JWT assertion header value that IAP added from the incoming request and calls the `validateAssertion` function to validate the cryptographically signed value. The email address is then used in a minimal web response.
        
        // index responds to requests with our greeting.
        func (a *app) index(w http.ResponseWriter, r *http.Request) {
        	if r.URL.Path != "/" {
        		http.NotFound(w, r)
        		return
        	}
        
        	assertion := r.Header.Get("X-Goog-IAP-JWT-Assertion")
        	if assertion == "" {
        		fmt.Fprintln(w, "No Cloud IAP header found.")
        		return
        	}
        	email, _, err := validateAssertion(assertion, a.certs, a.aud)
        	if err != nil {
        		log.Println(err)
        		fmt.Fprintln(w, "Could not validate assertion. Check app logs.")
        		return
        	}
        
        	fmt.Fprintf(w, "Hello %s\n", email)
        }
        

  * The `validateAssertion` function validates the assertion was properly signed and returns the associated email address and user ID.

Validating a JWT assertion requires knowing the public key certificates of the entity that signed the assertion (Google in this case), and the audience the assertion is intended for. For an App Engine app, the audience is a string with Google Cloud project identification information in it. The `validateAssertion` function gets those certificates from the `certs` function and the audience string from the `audience` function.
        
        // validateAssertion validates assertion was signed by Google and returns the
        // associated email and userID.
        func validateAssertion(assertion string, certs map[string]string, aud string) (email string, userID string, err error) {
        	token, err := jwt.Parse(assertion, func(token *jwt.Token) (interface{}, error) {
        		keyID := token.Header["kid"].(string)
        
        		_, ok := token.Method.(*jwt.SigningMethodECDSA)
        		if !ok {
        			return nil, fmt.Errorf("unexpected signing method: %q", token.Header["alg"])
        		}
        
        		cert := certs[keyID]
        		return jwt.ParseECPublicKeyFromPEM([]byte(cert))
        	})
        
        	if err != nil {
        		return "", "", err
        	}
        
        	claims, ok := token.Claims.(jwt.MapClaims)
        	if !ok {
        		return "", "", fmt.Errorf("could not extract claims (%T): %+v", token.Claims, token.Claims)
        	}
        
        	if claims["aud"].(string) != aud {
        		return "", "", fmt.Errorf("mismatched audience. aud field %q does not match %q", claims["aud"], aud)
        	}
        	return claims["email"].(string), claims["sub"].(string), nil
        }
        

  * You can look up the Google Cloud project's numeric ID and name and put them in the source code yourself, but the `audience` function does that for you by querying the standard metadata service made available to every App Engine app. Because the metadata service is external to the app code, that result is saved in a global variable that is returned without having to look metadata up in subsequent calls.

The App Engine metadata service (and similar metadata services for other Google Cloud computing services) looks like a web site and is queried by standard web queries. However, the metadata service isn't actually an external site, but an internal feature that returns requested information about the running app, so it is safe to use `http` instead of `https` requests. The metadata service is used to get the current Google Cloud identifiers needed to define the JWT assertion's intended audience.
        
        // audience returns the expected audience value for this service.
        func audience() (string, error) {
        	projectNumber, err := metadata.NumericProjectID()
        	if err != nil {
        		return "", fmt.Errorf("metadata.NumericProjectID: %w", err)
        	}
        
        	projectID, err := metadata.ProjectID()
        	if err != nil {
        		return "", fmt.Errorf("metadata.ProjectID: %w", err)
        	}
        
        	return "/projects/" + projectNumber + "/apps/" + projectID, nil
        }
        

  * Verification of a digital signature requires the public key certificate of the signer. Google provides a web site that returns all of the currently used public key certificates. These results are cached in case they're needed again in the same app instance.
        
        // certificates returns Cloud IAP's cryptographic public keys.
        func certificates() (map[string]string, error) {
        	const url = "https://www.gstatic.com/iap/verify/public_key"
        	client := http.Client{
        		Timeout: 5 * time.Second,
        	}
        	resp, err := client.Get(url)
        	if err != nil {
        		return nil, fmt.Errorf("Get: %w", err)
        	}
        
        	var certs map[string]string
        	dec := json.NewDecoder(resp.Body)
        	if err := dec.Decode(&certs); err != nil {
        		return nil, fmt.Errorf("Decode: %w", err)
        	}
        
        	return certs, nil
        }
        




## Deploying the app

Now you can deploy the app and then enable IAP to require users to authenticate before they can access the app.

  1. In your terminal window, go to the directory containing the `app.yaml` file, and deploy the app to App Engine:
         
         gcloud app deploy
         

  2. When prompted, select a nearby region.

  3. When asked if you want to continue with the deployment operation, enter `Y`.

Within a few minutes, your app is live on the internet.

  4. View the app:
         
         gcloud app browse
         

In the output, copy `web-site-url`, the web address for the app.

  5. In a browser window, paste `web-site-url` to open the app.

No email is displayed because you're not yet using IAP so no user information is sent to the app.




### Enable IAP

Now that an App Engine instance exists, you can protect it with IAP:

  1. In the Google Cloud console, go to the **Identity-Aware Proxy** page.

[Go to Identity-Aware Proxy page](https://console.cloud.google.com/security/iap)

  2. Because this is the first time you've enabled an authentication option for this project, you see a message that you must configure your OAuth consent screen before you can use IAP.

Click **Configure Consent Screen**.

  3. On the **OAuth Consent Screen** tab of the **Credentials** page, complete the following fields:

     * If your account is in a Google Workspace organization, select **External** and click **Create**. To start, the app will only be available to users you explicitly allow.

     * In the **Application name** field, enter `IAP Example`.

     * In the **Support email** field, enter your email address.

     * In the **Authorized domain** field, enter the hostname portion of the app's URL, for example, `iap-example-999999.uc.r.appspot.com`. Press the `Enter` key after entering the hostname in the field.

     * In the **Application homepage link** field, enter the URL for your app, for example, `https://iap-example-999999.uc.r.appspot.com/`.

     * In the **Application privacy policy line** field, use the same URL as the homepage link for testing purposes.

  4. Click **Save**. When prompted to create credentials, you can close the window.

  5. In the Google Cloud console, go to the **Identity-Aware Proxy** page.

[Go to Identity-Aware Proxy page](https://console.cloud.google.com/security/iap)

  6. To refresh the page, click **Refresh** _refresh_. The page displays a list of resources you can protect.

  7. In the **IAP** column, click to turn on IAP for the app.

  8. In your browser, go to `web-site-url` again.

  9. Instead of the web page, there is a login screen to authenticate yourself. When you log in, you're denied access because IAP doesn't have a list of users to allow through to the app.




### Add authorized users to the app

  1. In the Google Cloud console, go to the Identity-Aware Proxy page.

[Go to Identity-Aware Proxy page](https://console.cloud.google.com/security/iap)

  2. Select the checkbox for the App Engine app, and then click **Add Principal**.

  3. Enter `allAuthenticatedUsers`, and then select the **Cloud IAP/IAP-Secured Web App User** role.

  4. Click **Save**.




Now any user that Google can authenticate can access the app. If you want, you can restrict access further by only adding one or more people or groups as principals:

  * Any Gmail or Google Workspace email address

  * A Google Group email address

  * A Google Workspace domain name




### Access the app

  1. In your browser, go to `web-site-url`.

  2. To refresh the page, click **Refresh** _refresh_.

  3. On the login screen, log in with your Google credentials.

The page displays a "Hello `user-email-address`" page with your email address.

If you still see the same page as before, there might be an issue with the browser not fully updating new requests now that you enabled IAP. Close all browser windows, reopen them, and try again.




## Authentication concepts

There are several ways an app can authenticate its users and restrict access to only authorized users. Common authentication methods, in decreasing level of effort for the app, are listed in the following sections.

Option | Advantages | Disadvantages  
---|---|---  
App authentication | 

  * App can run on any platform, with or without an internet connection 
  * Users don't need to use any other service to manage authentication 

| 

  * App must manage user credentials securely, guard against disclosure 
  * App must maintain session data for logged-in users 
  * App must provide user registration, password changes, password recovery 

  
OAuth2 | 

  * App can run on any internet-connected platform, including a developer workstation 
  * App doesn't need user registration, password changes, or password recovery functions. 
  * Risk of user information disclosure is delegated to other service 
  * New login security measures handled outside the app 

| 

  * Users must register with the identity service 
  * App must maintain session data for logged-in users 

  
IAP | 

  * App doesn't need to have any code to manage users, authentication, or session state 
  * App has no user credentials that might be breached 

| 

  * App can only run on platforms supported by the service. Specifically, certain Google Cloud services that support IAP, such as App Engine. 

  
  
### App-managed authentication

With this method, the app manages every aspect of user authentication on its own. The app must maintain its own database of user credentials and manage user sessions, and it needs to provide functions to manage user accounts and passwords, check user credentials, as well as issue, check, and update user sessions with each authenticated login. The following diagram illustrates the app-managed authentication method.

![Application managed flow](https://docs.cloud.google.com/static/languages/images/auth-app.svg)

As shown in the diagram, after the user logs in, the app creates and maintains information about the user's session. When the user makes a request to the app, the request must include session information that the app is responsible for verifying.

The main advantage of this approach is that it is self-contained and under the control of the app. The app doesn't even need to be available on the internet. The main disadvantage is that the app is now responsible for providing all account management functionality and protecting all sensitive credential data.

### External authentication with OAuth2

A good alternative to handling everything within the app is to use an external identity service, such as Google, that handles all user account information and functionality and is responsible for safeguarding sensitive credentials. When a user tries to log in to the app the request is redirected to the identity service, which authenticates the user and then redirect the request back to the app with necessary authentication information provided. For more information, see [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server).

The following diagram illustrates the external authentication with the OAuth2 method.

![OAuth2 flow](https://docs.cloud.google.com/static/languages/images/auth-oauth2.svg)

The flow in the diagram begins when the user sends a request to access the app. Instead of responding directly, the app redirects the user's browser to Google's identity platform, which displays a page to log in to Google. After successfully logging in, the user's browser is directed back to the app. This request includes information that the app can use to look up information about the now authenticated user, and the app now responds to the user.

This method has many advantages for the app. It delegates all account management functionality and risks to the external service, which can improve login and account security without the app having to change. However, as is shown in the preceding diagram, the app must have access to the internet to use this method. The app is also responsible for managing sessions after the user is authenticated.

### Identity-Aware Proxy

The third approach, which this tutorial covers, is to use IAP to handle all authentication and session management with any changes to the app. IAP intercepts all web requests to your app, blocks any that haven't been authenticated, and passes others through with user identity data added to each request.

The request handling is shown in the following diagram.

![IAP flow](https://docs.cloud.google.com/static/languages/images/auth-iap.svg)

Requests from users are intercepted by IAP, which blocks unauthenticated requests. Authenticated requests are passed on to the app, provided that the authenticated user is in the list of allowed users. Requests passed through IAP have headers added to them identifying the user who made the request.

The app no longer needs to handle any user account or session information. Any operation that needs to know a unique identifier for the user can get that directly from each incoming web request. However, this can only be used for computing services that support IAP, such as App Engine and load balancers. You cannot use IAP on a local development machine. 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
