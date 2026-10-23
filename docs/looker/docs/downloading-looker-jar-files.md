---
url: https://docs.cloud.google.com/looker/docs/downloading-looker-jar-files/
title: Downloading the Looker JAR files \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:10.965530+00:00
---

# Downloading the Looker JAR files  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/downloading-looker-jar-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Downloading the Looker JAR files Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** We recommend that you [create a backup of your Looker instance](https://docs.cloud.google.com/looker/docs/creating-backups) before updating Looker.

To install or update the Looker application for a customer-hosted deployment, you must download the Looker JAR files. This page describes two methods for downloading the Looker JAR files:

  1. Using the **Download Looker JAR file** web page
  2. Calling the API



Before you can download the JAR files, you must accept an End User License Agreement (EULA), which is available on the **Download Looker JAR file** web page using the specifications on this page. Each user downloading the JAR files must accept this EULA only once. (If the EULA is updated in the future, each user will also have to accept the newer version.)

## Using the **Download Looker JAR file** web page

You can access the **Download Looker JAR file** web page at this link: <https://download.looker.com/validate>. To download the Looker JAR files, follow these steps:

  1. Enter your Looker license number.
  2. Enter your email address. This must be a privately hosted email domain.
  3. Select the Looker version to download.

If you select **Latest Version** , you will download the latest version of the Looker JAR files for the current Looker release. If you select **Specific Version** , you need to enter the Looker core JAR filename exactly.

**Note:** The naming convention of JAR files for each release includes the period (`.`) in the version number and follows a set pattern. For example, the JAR filenames for Looker 22.2 are `looker-22.2.jar` and `looker-dependencies-22.2.jar`.
  4. Click **Get Download**.

If you have not already accepted the EULA, a **EULA Acceptance** form appears. Select **Read Terms and Conditions** to view the EULA in its entirety. Next, enter your **First Name** and **Last Name** and select the checkbox next to **I agree to the Terms and Conditions**. Finally, click **Get Download**.

  5. Click **Download 1 of 2** to download the Looker core JAR file. Then, click **Download 2 of 2** to download the Looker dependencies JAR file. This link expires after 10 minutes. If the link expires, you can restart the download process.




## Calling the API

Before you can download the JAR files by calling the API, you must first accept the EULA through the **Download Looker JAR file** web page.

You can then make the necessary API call by making a POST request to the HTTPS endpoint with any desired method — JavaScript, Java, Ruby, shell command, etc. For any of these requests to work, you must use the POST method to send the API payload to https://apidownload.looker.com/download. The API payload must contain values for `lic`, `email`, and `latest`.

The `latest` property denotes the version of the Looker JAR. To download the latest version of the JAR files for the current Looker release (`looker-latest.jar`), specifying `"latest"` is sufficient. To download a specific version, set `latest` to `"specific"` and include another key-value pair within the API payload called `specific` with the core JAR filename as the value.

You only need to call the API once; the initial response will contain both download links and will be available for a 10 minute period. You will need to download both JAR files separately.

Here are two examples of making a request written in ES6 (JavaScript). To request the latest version:
    
    
        axios({
            url: "https://apidownload.looker.com/download",
            method: "post",
            data: {
                lic: "YOUR-LOOK-ERLI-CENS-EKEY",
                email: "contact@email.com",
                latest: "latest"
            }
        }).then(function (response) {
            console.log(response.data);
        })
    

To request a specific JAR version (for example, Looker 22.2): `none data: { lic: "YOUR-LOOK-ERLI-CENS-EKEY", email: "contact@email.com", latest: "specific", specific: "looker-22.2-latest.jar" }`

Here are two example shell commands for making POST requests to the HTTPS endpoint.

To request a specific version of JAR files using the `wget` command (for example, Looker 22.2):
    
    
    wget -O- --header=Content-Type:application/json\
    --post-data='{"lic": "YOURLOOKERLICENSE", "email": "contact@email.com", "latest":"specific",\
    "specific":"looker-22.2-latest.jar"}'\
    "https://apidownload.looker.com/download"
    
    
    
    wget -O- --header=Content-Type:application/json\
    --post-data='{"lic": "YOURLOOKERLICENSE", "email": "contact@email.com", "latest":"specific",\
    "specific":"looker-dependencies-22.2-latest.jar"}'\
    "https://apidownload.looker.com/download"
    

To request the latest JAR files using a series of `curl` and `wget` commands to download and save the files locally:
    
    
    curl -X POST -H 'Content-Type: application/json' -d '{"lic": "YOURLOOKERLICENSE", "email": "contact@email.com", "latest":"latest"}'
    https://apidownload.looker.com/download > api_response.json
    sed -i 1,12d api_response.json
    
    
    
    wget -O "looker-latest.jar" "$(cat api_response.json | jq -r '.url')"
    
    
    
    wget -O "looker-dependencies-latest.jar" "$(cat api_response.json | jq -r '.depUrl')"
    

Alternatively, if you have [jq](https://stedolan.github.io/jq/) and `wget` installed, you can use the following shell command examples.

To request the latest JAR files using a series of `wget` commands:
    
    
    wget -O "looker-latest.jar" "$(shell curl -s -X POST -H 'Content-Type: application/json'\
    -d "{\"lic\": \"$(YOURLOOKERLICENSE)\", \"email\": \"$(contact@email.com)\",\"latest\":\"latest\"}\
    "https://apidownload.looker.com/download | jq .url -r)"
    
    
    
    wget -O "looker-dependencies-latest.jar" "$(shell curl -s -X POST -H 'Content-Type: application/json'\
    -d "{\"lic\": \"$(YOURLOOKERLICENSE)\", \"email\": \"$(contact@email.com)\",\"latest\":\"latest\"}\
    "https://apidownload.looker.com/download | jq .depUrl -r)"
    

You can also download other versions of the JAR by setting `LOOKER_VERSION` to `latest`, `22.2-latest`, or another [supported version](https://docs.cloud.google.com/looker/docs/officially-supported-releases) in the following series of command examples. For example, to request the core and dependencies files for Looker 22.2:
    
    
    export LOOKER_VERSION="22.2-latest"
    
    
    
    wget -O "looker$(LOOKER_VERSION).jar" "$(shell curl -s -X POST -H 'Content-Type: application/json'\
    -d "{\"lic\": \"$(YOURLOOKERLICENSE)\", \"email\": \"$(contact@email.com)\",\"latest\":\"specific\",\
    \"specific\":\"looker-$(LOOKER_VERSION).jar\"} "https://apidownload.looker.com/download | jq .url -r)"
    
    
    
    wget -O "looker-dependencies$(LOOKER_VERSION).jar" "$(shell curl -s -X POST -H\
    'Content-Type: application/json' -d "{\"lic\": \"$(YOURLOOKERLICENSE)\", \"email\":\
    \"$(contact@email.com)\",\"latest\":\"specific\", \"specific\":\"looker-dependencies-$(LOOKER_VERSION).jar\"}\
    "https://apidownload.looker.com/download | jq .depUrl -r)"
    

**Note:** A successful response will contain both URLs of the downloads and SHA-256 hashes of the JAR files.

API payload errors, such as missing or mistyped input parameters, result in an "Invalid request body" response. Providing an incorrect license key or omitting a `specific` value when requesting a `specific` version will result in an "Invalid request" response.

Issues with downloading both JAR files may result in a message in the `splitJarMessage` field.

If you have not previously accepted the latest EULA, the response will contain three fields: `eulaMessage`, `eulaText`, and `eulaNeeded`. The `eulaMessage` will indicate that you must first accept the EULA via the **Download Looker JAR file** web page before the API will return a download URL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
