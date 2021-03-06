import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('http01')


def test_certificate_file_exists(host):
    cert = host.file('/etc/dehydrated/certs/le2.wtf/cert.pem')
    chain = host.file('/etc/dehydrated/certs/le2.wtf/chain.pem')
    fullchain = host.file('/etc/dehydrated/certs/le2.wtf/fullchain.pem')
    privkey = host.file('/etc/dehydrated/certs/le2.wtf/privkey.pem')

    assert cert.exists
    assert chain.exists
    assert fullchain.exists
    assert privkey.exists
