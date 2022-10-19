# Unified Middleware Distribution (UMD)

[![Docker Repository on Quay](https://quay.io/repository/egi/umd4/status "Docker Repository on Quay")](https://quay.io/repository/egi/umd4)

The role deploys the repository files needed to access the products distributed
by [UMD](https://go.egi.eu/umd), currently supported for Scientific Linux 6 and
CentOS7. This role optionally deploys the Interoperable Global Trust Federation
(IGTF) repository file.

Information on available UMD release is available on the
[EGI repository](https://repository.egi.eu/).

## Using

If you wish to use this role, install the role from
[Ansible Galaxy](https://galaxy.ansible.com/EGI-Foundation/umd):

```
ansible-galaxy install egi-foundation.umd
```

## Requirements

This role requires Ansible 2.0 or higher. The only dependency is EPEL, included
in the metadata file.

## Role Variables

Brief description of the variables used in the role:

- `release` (int) UMD release version (no default)
  - _e.g._ `release: 4`
- `enable_candidate_repo` (bool) Enable the candidate repository, commonly used
  in the release candidate (defaults to `false`)
  - _e.g._ `enable_candidate_repo: false`
- `enable_testing_repo` (bool) : Enables the testing repository (defaults to
  'false')
  - _e.g._ `enable_testing_repo: false`
- `enable_untested_repo: false` : Enables the untested repository (defaults to
  'false')
- `ca_verification: false` - Enables the IGTF repository for trusted CAs
  (defaults to `false`)
- `ca_version: 1` : CA version (defaults to '1', only if
  `ca_verification: true`)
- `ca_branch: production` : CA branch (defaults to 'production', only if
  `ca_verification: true`)
- `ca_verification: true`: - CA servers (defaults to 'repository.egi.eu', only
  if `ca_verification: true`)
  - _e.g._ `ca_server: repository.egi.eu`
- `crl_deploy: false` : Installs 'fetch-crl' package if enabled (defaults to
  `false`)
  - _e.g._ : `crl_deploy: false`

## Dependencies

A previous dependency on
[`geerlingguy.repo-epel`](https://galaxy.ansible.com/geerlingguy/repo-epel) has
been removed. EPEL is now taken care of in this role directly.

## Example Playbook

This role can be used in several scenarios, depending on your environment. These
are some examples of how to use this role.

### Just install UMD repository files (if current OS is supported)

```yaml
- hosts: all
  roles:
    - { role: ansible-umd, release: 4 }
```

### Install UMD repository files together with the trusted CAs and fetch-crl

```yaml
- hosts: all
  roles:
    - { role: ansible-umd, release: 4, ca_verification: true, crl_deploy: true }
```

### Install UMD repository files, enabling the candidate repository

```yaml
- hosts: all
  roles:
    - { role: ansible-umd, release: 4, enable_candidate_repo: true }
```

## License

Apache 2.0

## Author Information

Original author Pablo Orviz <orviz@ifca.unican.es>

For contributions see [AUTHORS.md](AUTHORS.md).
