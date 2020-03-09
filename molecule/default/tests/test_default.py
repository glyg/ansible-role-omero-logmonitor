import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_running_and_enabled(host):
    service = host.service('omero-logmonitor')
    assert service.is_running
    assert service.is_enabled


def test_config_file(host):
    f = host.file('/opt/omero/logmonitor/omero-fenton/omero-fenton.cfg')
    assert f.contains('/opt/omero/server/OMERO.server/var/log/Blitz-0.log')
    assert f.contains('/opt/omero/web/OMERO.web/var/log/OMEROweb.log')
