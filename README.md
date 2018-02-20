![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)

[![Travis Badge](https://travis-ci.org/thinkingserious/sendgrid-ibm-index-open-source-workshop.svg?branch=master)](https://travis-ci.org/thinkingserious/sendgrid-ibm-index-open-source-workshop)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

**This project allows you to quickly and easily deploy a SendGrid email service utilizing IBM's Cloud Functions.**

This repo is a companion to a [workshop given at IBM Index 2018](http://send.gd/2EwBh2M). The companion slides can be found [here](https://docs.google.com/presentation/d/1VL29sFM3nq2JUYou9wotaorIksA18JUuqg3MJxJPq1w/edit#slide=id.g31f03beec4_0_50).

# Table of Contents

* [Prerequisites & Dependencies](#prequisites_dependencies)
* [Installation](#installation)
* [Quick Start](#quick-start)
* [Usage](#usage)
* [Use Cases](#use-cases)
* [Announcements](#announcements)
* [Roadmap](#roadmap)
* [How to Contribute](#contribute)
* [Troubleshooting](#troubleshooting)
* [About](#about)

<a name="prequisites_dependencies"></a>
# Prerequisites & Dependencies

* [IBM Cloud Account](http://bit.ly/ibm_cloud_gep)
* [IBM CLI](https://console.bluemix.net/docs/cli/reference/bluemix_cli/download_cli.html#shell_install)
* [SendGrid Account](https://sendgrid.com/free/?source=ibm-index)
* [SendGrid API Key](https://app.sendgrid.com/settings/api_keys)
* [GitHub Account](https://github.com/join)
* [Docker](https://docs.docker.com/install)

<a name="installation"></a>
# Installation

Update the email addresses in `app.py`.

```bash
bx plugin install Cloud-Functions -r Bluemix
bx login -a api.ng.bluemix.net -o <YOUR IBM CLOUD USERNAME> -s dev
docker run --rm -v "$PWD:/tmp" ibmfunctions/action-python-v3 \
   bash  -c "cd tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"
zip -r helloSendGrid.zip virtualenv __main__.py app.py
bx wsk action create helloSendGrid --kind python-jessie:3 helloSendGrid.zip
```

The following is the procedure for updating your IBM Cloud Function after making a code change:

```bash
zip -r helloSendGrid.zip virtualenv __main__.py app.py
bx wsk action update helloSendGrid --kind python-jessie:3 helloSendGrid.zip
```

<a name="quick-start"></a>
# Quick Start

Go to the [IBM Cloud Functions Actions page](https://console.bluemix.net/openwhisk/actions).

Click the "helloSendGrid" link.

Click the "Parameters" link.

"Add" a parameter with the "Parameter Name" SENDGRID_API_KEY and the "Parameter Value" is your [SendGrid API Key](https://app.sendgrid.com/settings/api_keys). 

```bash
bx wsk action invoke --result helloSendGrid
```

<a name="usage"></a>
# Usage

In addition the [Quick Start](#quick-start), you can access your IBM Cloud Function using CURL.

```bash
cp .env_sample .env
```

Replace YOUR IBM CLOUD API KEY with your IBM Cloud [API Key](https://console.bluemix.net/openwhisk/api-key).

```bash
source .env
```

Go to the [IBM Cloud Functions Actions page](https://console.bluemix.net/openwhisk/actions).

Click the "helloSendGrid" link.

Click the "Endpoints" link.

Copy the commands under "CURL" and replace API-KEY with $IBM_CLOUD_API_KEY.

<a name="use-cases"></a>
# Use Cases

Send an email using the command line.

<a name="announcements"></a>
# Announcements

Come join me at [IBM Index 2018](http://send.gd/2EwBh2M) on 2/2/18.

<a name="roadmap"></a>
# Roadmap

Add the ability to pass in various paramaters such as to email, from email, subject and body.

Add Web Action and Gateway support.

Add tests.

Update documentation.

<a name="contribute"></a>
# How to Contribute

I encourage contribution to this project, please see our [CONTRIBUTING](https://github.com/thinkingserious/sendgrid-ibm-index-open-source-workshop/blob/master/CONTRIBUTING.md) guide for details.

<a name="troubleshooting"></a>
# Troubleshooting

Please see the [troubleshooting guide](https://github.com/thinkingserious/sendgrid-ibm-index-open-source-workshop/blob/master/TROUBLESHOOTING.md) for common library issues.

<a name="about"></a>
# About

sendgrid-ibm-index-open-source-workshop is supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

sendgrid-ibm-index-open-source-workshop is maintained and funded by SendGrid, Inc. The names and logos for sendgrid-ibm-index-open-source-workshop are trademarks of SendGrid, Inc.
