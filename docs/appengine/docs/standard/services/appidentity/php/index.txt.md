---
url: https://docs.cloud.google.com/appengine/docs/standard/services/appidentity/php/index.txt
title: https://docs.cloud.google.com/appengine/docs/standard/services/appidentity/php/index.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:53:38.262075+00:00
---

# https://docs.cloud.google.com/appengine/docs/standard/services/appidentity/php/index.txt

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/appidentity/php/index.txt

// [START asserting_identity_to_Google_APIs] // Retrieves Google Calendar contacts using OAuth use Google\AppEngine\Api\AppIdentity\AppIdentityService; function setAuthHeader() { $access_token = AppIdentityService::getAccessToken('https://www.google.com/m8/feeds'); return [sprintf('Authorization: OAuth %s', $access_token['access_token'])]; } $get_contacts_url = 'https://www.google.com/m8/feeds/contacts/default/full'; $headers = setAuthHeader(); $opts = [ 'http' => [ 'header' => implode("\r\n", $headers), ], ]; $context = stream_context_create($opts); $response = file_get_contents($get_contacts_url, false, $context); $xml = simplexml_load_string($response); $email = $xml->author->email; $service_account = AppIdentityService::getServiceAccountName(); if (strcmp($email, $service_account) != 0) { die(sprintf('%s does not match the service account name %s.', $email, $service_account)); } // [END asserting_identity_to_Google_APIs] 
