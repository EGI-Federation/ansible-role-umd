"""Role testing files using testinfra."""

import re
import urllib.request
from xml.dom import minidom

import pytest


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


# Test that UMD release is there
def test_umd_version(host):
    umd_package = host.package("umd-release")
    assert umd_package.is_installed


@pytest.mark.parametrize(
    "repo_file",
    [
        ("EGI-trustanchors.repo"),
        ("epel.repo"),
    ],
)
# Test that repositories are present
def test_repositories_present(host, repo_file):
    f = host.file("/etc/yum.repos.d/" + repo_file)
    assert f.exists
    assert f.uid == 0
    assert f.group == "root"


@pytest.mark.parametrize(
    "repo_file",
    [
        ("EGI-trustanchors.repo"),
    ],
)
def test_repositories_enabled(host, repo_file):
    content = host.file("/etc/yum.repos.d/" + repo_file).content.decode("utf8")
    enabled_regex = re.compile(r"enabled\s*=\s*1")
    assert enabled_regex.search(content) is not None


@pytest.mark.parametrize(
    "systemd_file",
    [
        ("fetch-crl.service"),
        ("fetch-crl.timer"),
    ],
)
def test_crl_renewal_task(host, systemd_file):
    crl_renewal = host.file("/usr/lib/systemd/system/" + systemd_file)
    assert crl_renewal.exists
    assert crl_renewal.is_file


# def test_crl_freshness(host):


def test_egi_policy(host):
    ca_package_name = "ca-policy-egi-core"
    ca_package_version_url = (
        "https://repository.egi.eu/sw/production/cas/1/current/release.xml"
    )
    _doc = minidom.parse(urllib.request.urlopen(ca_package_version_url))
    _version = _doc.getElementsByTagName("Version")[0].firstChild.data
    ca_package_version = _version.split("-")[0]

    pkg = host.package(ca_package_name)
    assert pkg.is_installed
    assert pkg.version.startswith(ca_package_version)
