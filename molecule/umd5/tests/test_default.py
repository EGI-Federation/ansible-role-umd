"""Role testing files using testinfra."""

import re
from distutils.version import LooseVersion

import pytest


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_ca_package(host):
    p = host.package("ca-policy-egi-core")
    assert p.is_installed
    assert LooseVersion(p.version) >= "1.132"


def test_umd_release(host):
    release_package = host.package("umd-release")
    epel_package = host.package("epel-release")

    assert release_package.is_installed
    assert LooseVersion(release_package.version) >= "5"
    assert epel_package.is_installed


@pytest.mark.parametrize(
    "repo_file",
    [
        ("UMD-5.repo"),
        ("UMD-5-contrib.repo"),
        ("UMD-5-testing.repo"),
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
        ("UMD-5.repo"),
    ],
)
def test_repositories_enabled(host, repo_file):
    content = host.file("/etc/yum.repos.d/" + repo_file).content.decode("utf8")
    enabled_regex = re.compile(r"enabled\s*=\s*1")
    assert enabled_regex.search(content) is not None
