# Unified Middleware Distribution (UMD)

[![Docker Repository on Quay](https://quay.io/repository/egi/umd5/status "Docker Repository on Quay")](https://quay.io/repository/egi/umd5)

The role deploys the repository files needed to access the products distributed
by [UMD](https://go.egi.eu/umd), currently supported for AlmaLinux 9 (and
compatible). This role optionally deploys the Interoperable Global Trust
Federation (IGTF) repository file.

Information on available UMD release is available on the
[EGI repository](https://repository.egi.eu/).

## Using

If you wish to use this role, install the role from
[Ansible Galaxy](https://galaxy.ansible.com/EGI-Foundation/umd):

```shell
# Install ansible module from Ansible Galaxy
$ ansible-galaxy install egi-foundation.umd
```

## Requirements

This role requires Ansible 2.0 or higher. The only dependency is EPEL, included
in the metadata file.

## Role Variables

Brief description of the variables used in the role:

- `release` (int) UMD release version (no default)
  - _e.g.,_ `release: 5`
- `enable_candidate_repo: false`: Enable the candidate repository, commonly used
  in the release candidate (defaults to `false`)
  - _e.g.,_ `enable_candidate_repo: false`
- `enable_testing_repo: false`: Enables the testing repository (defaults to
  'false')
  - _e.g.,_ `enable_testing_repo: false`
- `ca_verification: false`: Enables the IGTF repository for trusted CAs
  (defaults to `false`)
- `ca_version: 1`: CA version (defaults to '1', only if `ca_verification: true`)
- `ca_branch: production`: CA branch (defaults to 'production', only if
  `ca_verification: true`)
- `ca_verification: true`: CA servers (defaults to 'repository.egi.eu', only if
  `ca_verification: true`)
  - _e.g.,_ `ca_server: repository.egi.eu`
- `crl_deploy: false`: Installs 'fetch-crl' package if enabled (defaults to
  `false`)
  - _e.g.,_ : `crl_deploy: false`

## Dependencies

A previous dependency on
[`geerlingguy.repo-epel`](https://galaxy.ansible.com/geerlingguy/repo-epel) has
been removed. EPEL is now taken care of in this role directly.

## Example Playbook

This role can be used in several scenarios, depending on your environment. These
are some examples of how to use this role.

### Install UMD repository files on supported OS

```yaml
- hosts: all
  roles:
    - { role: ansible-umd, release: 5 }
```

### Install UMD repository files together with the trusted CAs and fetch-crl

```yaml
- hosts: all
  roles:
    - { role: ansible-umd, release: 5, ca_verification: true, crl_deploy: true }
```

### Install UMD repository files, enabling the candidate repository

```yaml
- hosts: all
  roles:
    - { role: ansible-umd, release: 5, enable_candidate_repo: true }
```

## Running molecule locally

Prepare a virtual env for testing using
[molecule](https://molecule.readthedocs.io), as documented in the
[EGI Ansible style guide](https://docs.egi.eu/ansible-style-guide/).

```shell
# Create a folder for virtual environments
$ mkdir -p ~/.virtualenvs
# Create a python3 virtualenv
$ python3 -m venv ~/.virtualenvs/molecule
# Activate virtual env
$ source ~/.virtualenvs/ui-deployment/bin/activate
# Install dependencies
$ pip install -r requirements.txt
```

Run molecule

```shell
# Lint
$ molecule lint
# Run the complete test suite
$ molecule test
```

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in `CHANGELOG`
- Once the PR has been merged, publish a new release using GitHub web interface
  - Suffix the tag name to be created with `v`, like `v1.0.0`
  - Packages will be built using GitHub Actions and attached to the release page

## License

Apache 2.0

## Author Information

Original author [Pablo Orviz](https://github.com/orviz).

For contributions see [AUTHORS.md](AUTHORS.md).
