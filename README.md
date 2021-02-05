OMERO LogMonitor
================

[![Actions Status](https://github.com/ome/ansible-role-omero-logmonitor/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-omero-logmonitor/actions)
[![Ansible Role](https://img.shields.io/ansible/role/41334.svg)](https://galaxy.ansible.com/ome/omero_logmonitor/)

Install OmeroFenton for error notifications in Jabber


Requirements
------------

The user account that the bot is run as (default `omero`) must already exist, it will not be created automatically in case the account requires special configuration.
The default configuration assumes OMERO.server has been installed into its default location using the `omero-server` role.


Role Variables
--------------

Required variables:

- `omero_logmonitor_slack_name`: Slack bot name
- `omero_logmonitor_slack_token`: Slack secret token
- `omero_logmonitor_slack_channel`: Slack #channel for notifications

Recommended variables:

- `omero_logmonitor_server_name`: String used to identify alerts from this server

Optional variables:

- `omero_logmonitor_email_oom`: Whether to enable email notifications of out-of-memory errors, if `True` the `omero_logmonitor_email_*` properties must be defined, default `False`.
- `omero_logmonitor_email_smtp`: SMTP server
- `omero_logmonitor_email_from`: From address for email alerts
- `omero_logmonitor_email_to`: To address for email alerts@example.org
- `omero_logmonitor_logs_dir_server`: Base directory of the OMERO.server logs, set to `""` to disable monitoring
- `omero_logmonitor_logs_dir_web`: Base directory of the OMERO.web logs, set to `""` to disable monitoring
- `omero_logmonitor_logfiles`: Dictionaries of log file monitoring parameters

See `defaults/main.yml` for the full list of optional variables.
This is particularly important if you are using a modified OMERO configuration with log files in a different location, or with non-standard logfiles.


Example Playbook
----------------

    - hosts: localhost
      roles:
      - role: ome.omero_logmonitor
        omero_logmonitor_slack_name: omero-logmonitor
        omero_logmonitor_slack_token: SLACK-TOKEN
        omero_logmonitor_slack_channel: "#alerts"
        omero_logmonitor_server_name: omero test instance
        # Include the follow variables to setup email OOM alerts
        omero_logmonitor_email_oom: True
        omero_logmonitor_email_smtp: smtp.example.org
        omero_logmonitor_email_from: omero-logmonitor@example.org
        omero_logmonitor_email_to: sysadmin-alerts@example.org


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
