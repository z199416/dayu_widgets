"""Test MPushButton"""

import pytest
from dayu_widgets.push_button import MPushButton
from dayu_widgets import dayu_theme

MPUSHBUTTON_TYPE_LIST = (
    MPushButton.DefaultType,
    MPushButton.PrimaryType,
    MPushButton.SuccessType,
    MPushButton.WarningType,
    MPushButton.DangerType
)
@pytest.mark.parametrize('dayu_type', MPUSHBUTTON_TYPE_LIST)
@pytest.mark.parametrize('dayu_size', (
    dayu_theme.huge, dayu_theme.large, dayu_theme.medium, dayu_theme.small, dayu_theme.tiny
))
def test_mpushbutton_init(qtbot, dayu_type, dayu_size):
    """Test MPushButton set_dayu_size and set_dayu_type."""
    widget = MPushButton()
    widget.set_dayu_size(dayu_size)
    widget.set_dayu_type(dayu_type)
    qtbot.addWidget(widget)

    assert widget.property('dayu_type') == dayu_type
    assert widget.property('dayu_size') == dayu_size

@pytest.mark.parametrize('cls', (
    MPushButton,
    MPushButton.primary,
    MPushButton.success,
    MPushButton.warning,
    MPushButton.danger,))
@pytest.mark.parametrize('dayu_type', MPUSHBUTTON_TYPE_LIST)
def test_class_method(qtbot, cls, dayu_type):
    """Test MPushButton class methods."""
    widget = cls()
    widget.set_dayu_type(dayu_type)
    qtbot.addWidget(widget)
    assert widget.property('dayu_type') == dayu_type
    assert widget.property('dayu_size') == dayu_theme.default_size


@pytest.mark.parametrize('input_type', ('infos', 3, None, {'name': 'test'}))
def test_with_wrong_type(qtbot, input_type):
    """Test MPushButton set_dayu_type method with wrong arg. raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        widget = MPushButton()
        widget.set_dayu_type(input_type)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be one of " \
                            "default/primary/success/warning/danger string."