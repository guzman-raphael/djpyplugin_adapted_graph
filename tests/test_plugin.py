from datajoint.plugin import type_plugins


def test_check_plugin_status():
    assert(type_plugins['graph']['verified'])
