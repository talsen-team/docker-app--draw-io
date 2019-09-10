import pytest
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    '/bash-commands/docker-compose--compose--down.sh',
    '/bash-util/elevate.sh',
    '/bash-util/functions.sh',
    '/docker/server--draw-io/default.docker',
    '/docker-compose/server--draw-io/default.docker-compose',
    '/host.env',
])
def test_that_required_files_are_existing(host, name):
    test_dir = os.environ['TESTS_DIRECTORY'] + '/test--docker-compose--compose--down'  # noqa: #501

    f = host.file(test_dir + name)

    assert f.exists


def test_that_required_docker_container_is_existing(host):
    c = host.docker.get_containers(name='server--draw-io')

    assert len(c) == 0


def test_that_mapped_port_is_reserved(host):
    s = host.socket('tcp://127.0.0.1:80')

    assert not s.is_listening


def test_that_mapped_port_is_responding(host):
    r = host.run('wget --output-document=/dev/null http://127.0.0.1')

    assert r.rc != 0
