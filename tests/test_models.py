import pytest
import importlib
import os
import sys

# ensure package root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.parametrize('module_name', ['daite.models'])
def test_import(module_name):
    module = importlib.import_module(module_name)
    assert hasattr(module, 'User')
    assert hasattr(module, 'Profile')
    assert hasattr(module, 'Preference')
    assert hasattr(module, 'MatchQueue')
    assert hasattr(module, 'ChatSession')

    ChatSession = module.ChatSession
    assert hasattr(ChatSession, 'last_message')
    assert hasattr(ChatSession, 'status')
