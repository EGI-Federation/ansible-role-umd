import os
from distutils.version import LooseVersion  # , StrictVersion

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ca_package(host):
    p = host.package('ca-policy-egi-core')
    assert p.is_installed
    assert LooseVersion(p.version) >= '1.93'


def test_umd_release(host):
    release_package = host.package('umd-release')
    epel_package = host.package('epel-release')

    assert release_package.is_installed
    assert LooseVersion(release_package.version) >= '4'
    assert epel_package.is_installed
